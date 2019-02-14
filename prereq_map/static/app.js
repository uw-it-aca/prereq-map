$(document).ready(function(){
    var curric_code = getUrlParameter('curric');
    if (curric_code !== undefined){
        fetch_prereqs_for_curric(curric_code);
    }
});

window.show_graph = function(graph_data) {
    var initResult;
    var graph_div = $("<div/>", {id: "graph_div"});
    $("#graph_container").append(graph_div);
    var el = graph_div;

    var graph = $("<div/>", {id: "graph"+el.id});
    $("#graph_container").append(graph);
    // build_graph(graph_div, data.x, initResult)
    new_graph(graph_div.get(0), graph_data.x)
};


function fetch_prereqs_for_curric(curric){
    var url = "/api/curric/" + curric;
    $.ajax({
               url: url,
               dataType: "JSON",
               type: "GET",
               accepts: {html: "text/html"},
               success: function(results) {
                   window.show_graph(results);
               },
               error: function(xhr, status, error) {
                   console.log('api error fetching curric');
               }
           });
}

function px(x) {
    if (typeof(x) === "number")
        return x + "px";
    else
        return x;
}

// stab at refactor of graph
function new_graph(graph_div, data){
    var node_list = [];
    for(var i = 0; i < Object.keys(data.nodes.course_number).length; i++){
        var course_id = data.nodes.department_abbrev[i] + " " + data.nodes.course_number[i];
        node_list.push({id: course_id,
                       label: course_id})
    };


    var edge_list = [];
    Object.keys(data.edges.from).forEach(function(key){
        var from = data.edges.from[key];
        var to = data.edges.to[key];
        edge_list.push({from: from, to: to});
    });
    var nodes = new vis.DataSet(node_list);
    var edges = new vis.DataSet(edge_list);


    var data = {nodes: nodes, edges:edges};
    var options = {height: '500px', width:'100%'};
    var network = new vis.Network(graph_div, data, options);
}


function build_graph(el, x, instance) {
    if(x.nodes){

        // network
        nodes = new vis.DataSet();
        edges = new vis.DataSet();

        var tmpnodes;
        if(x.nodesToDataframe){ // data in data.frame
            tmpnodes = visNetworkdataframeToD3(x.nodes, "nodes")
        } else { // data in list
            tmpnodes = x.nodes;
        }
        // only one element
        if(tmpnodes.length === undefined){
            tmpnodes = new Array(tmpnodes);
        }

        // update coordinates if igraph
        if(x.igraphlayout !== undefined){
            // to improved
            var zoomLevel = -232.622349 / (tmpnodes.length + 91.165919)  +2.516861;
            var igclientWidth = document.getElementById("graph"+el.id).clientWidth;
            var scalex = 100;
            var scaley = 100;

            // current div visibled
            if(igclientWidth !== 0){
                var factor = igclientWidth / 1890;
                zoomLevel = zoomLevel/factor;
                var scalex = (igclientWidth / 2) * zoomLevel;
                var scaley = scalex;
                if(x.igraphlayout.type !== "square"){
                    scaley = (document.getElementById("graph"+el.id).clientHeight / 2) * zoomLevel;
                }
            } else {
                // current div not visibled....
                igclientWidth = parseInt(el_id.style.width);
                if(igclientWidth !== 0){
                    var factor = igclientWidth / 1890;
                    zoomLevel = zoomLevel/factor;
                    var scalex = (igclientWidth / 2) * zoomLevel;
                    var scaley = scalex;
                    if(x.igraphlayout.type !== "square"){
                        scaley = (parseInt(el_id.style.height) / 2) * zoomLevel;
                    }
                }
            }

            for (var nd in tmpnodes) {
                tmpnodes[nd].x = tmpnodes[nd].x * scalex;
                tmpnodes[nd].y = tmpnodes[nd].y * scaley;
            }
        }

        nodes.add(tmpnodes);

        var tmpedges;
        if(x.edgesToDataframe){ // data in data.frame
            tmpedges = visNetworkdataframeToD3(x.edges, "edges")
        } else { // data in list
            tmpedges = x.edges;
        }
        // only one element
        if(tmpedges !== null){
            if(tmpedges.length === undefined){
                tmpedges = new Array(tmpedges);
            }
            edges.add(tmpedges);
        }

        // reset tmpnodes
        tmpnodes = null;

        data = {
            nodes: nodes,
            edges: edges
        };

        //save data for re-use and update
        document.getElementById("graph"+el.id).nodes = nodes;
        document.getElementById("graph"+el.id).edges = edges;

    }else if(x.dot){
        data = {
            dot: x.dot
        };
    }else if(x.gephi){
        data = {
            gephi: x.gephi
        };
    }




    // manipulation

    // var style = document.createElement('style');
    // style.type = 'text/css';
    // style.appendChild(document.createTextNode(x.datacss));
    // document.getElementsByTagName("head")[0].appendChild(style);
    //
    // var div = document.createElement('div');
    // div.id = 'network-popUp';
    //
    // div.innerHTML = '<span id="operation">node</span> <br>\
    //   <table style="margin:auto;"><tr>\
    //   <td>id</td><td><input id="node-id" value="new value" disabled = true></td>\
    //   </tr>\
    //   <tr>\
    //   <td>label</td><td><input id="node-label" value="new value"> </td>\
    //   </tr></table>\
    //   <input type="button" value="save" id="saveButton"></button>\
    //   <input type="button" value="cancel" id="cancelButton"></button>';

    // el_id.appendChild(div);


    var options = x.options;

    options.manipulation.addNode = function(data, callback) {
        document.getElementById('operation').innerHTML = "Add Node";
        document.getElementById('node-id').value = data.id;
        document.getElementById('node-label').value = data.label;
        document.getElementById('saveButton').onclick = saveNode.bind(this, data, callback, "addNode");
        document.getElementById('cancelButton').onclick = clearPopUp.bind();
        document.getElementById('network-popUp').style.display = 'block';
    };

    options.manipulation.editNode = function(data, callback) {
        document.getElementById('operation').innerHTML = "Edit Node";
        document.getElementById('node-id').value = data.id;
        document.getElementById('node-label').value = data.label;
        document.getElementById('saveButton').onclick = saveNode.bind(this, data, callback, "editNode");
        document.getElementById('cancelButton').onclick = cancelEdit.bind(this,callback);
        document.getElementById('network-popUp').style.display = 'block';
    };

    options.manipulation.deleteNode = function(data, callback) {
        var r = confirm("Do you want to delete " + data.nodes.length + " node(s) and " + data.edges.length + " edges ?");
        if (r === true) {
            deleteSubGraph(data, callback);
        }
    };

    options.manipulation.deleteEdge = function(data, callback) {
        var r = confirm("Do you want to delete " + data.edges.length + " edges ?");
        if (r === true) {
            deleteSubGraph(data, callback);
        }
    };

    options.manipulation.addEdge = function(data, callback) {
        if (data.from == data.to) {
            var r = confirm("Do you want to connect the node to itself?");
            if (r === true) {
                saveEdge(data, callback, "addEdge");
            }
        }
        else {
            saveEdge(data, callback, "addEdge");
        }
    };

    options.manipulation.editEdge = function(data, callback) {
        if (data.from == data.to) {
            var r = confirm("Do you want to connect the node to itself?");
            if (r === true) {
                saveEdge(data, callback, "editEdge");
            }
        }
        else {
            saveEdge(data, callback, "editEdge");
        }
    };

    // create network
    new vis.Network(document.getElementById("graph"+el.id), data, options);
}

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};