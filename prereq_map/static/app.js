$(document).ready(function(){
    window.show_graph();
});

window.show_graph = function() {
    var initResult;
    var graph_div = $("<div/>", {id: "graph_div"});
    $("#graph_container").append(graph_div);
    var el = graph_div;
    var data = $("#graph_data").html();
    data = JSON.parse(data);

    var graph = $("<div/>", {id: "graph"+el.id});
    $("#graph_container").append(graph);
    build_graph(graph_div, data.x, initResult)
};

function initSizing(el) {
    var sizing = sizingPolicy(el);
    if (!sizing)
        return;

    var cel = document.getElementById("htmlwidget_container");
    if (!cel)
        return;

    if (typeof(sizing.padding) !== "undefined") {
        document.body.style.margin = "0";
        document.body.style.padding = "0";
    }

    if (sizing.fill) {
        document.body.style.overflow = "hidden";
        document.body.style.width = "100%";
        document.body.style.height = "100%";
        document.documentElement.style.width = "100%";
        document.documentElement.style.height = "100%";
        if (cel) {
            cel.style.position = "absolute";
            var pad = unpackPadding(sizing.padding);
            cel.style.top = pad.top + "px";
            cel.style.right = pad.right + "px";
            cel.style.bottom = pad.bottom + "px";
            cel.style.left = pad.left + "px";
            el.style.width = "100%";
            el.style.height = "100%";
        }

        return {
            getWidth: function() { return cel.offsetWidth; },
            getHeight: function() { return cel.offsetHeight; }
        };

    } else {
        el.style.width = px(sizing.width);
        el.style.height = px(sizing.height);

        return {
            getWidth: function() { return el.offsetWidth; },
            getHeight: function() { return el.offsetHeight; }
        };
    }
}

function sizingPolicy(el) {
    var sizingEl = document.querySelector("script[data-for='" + el.id + "'][type='application/htmlwidget-sizing']");
    if (!sizingEl)
        return null;
    var sp = JSON.parse(sizingEl.textContent || sizingEl.text || "{}");
    if (viewerMode) {
        return sp.viewer;
    } else {
        return sp.browser;
    }
}

function px(x) {
    if (typeof(x) === "number")
        return x + "px";
    else
        return x;
}

function elementData(el, name, value) {
    if (arguments.length == 2) {
        return el["htmlwidget_data_" + name];
    } else if (arguments.length == 3) {
        el["htmlwidget_data_" + name] = value;
        return el;
    } else {
        throw new Error("Wrong number of arguments for elementData: " +
                            arguments.length);
    }
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
    console.log(document.getElementById("graph"+el.id));
    new vis.Network(document.getElementById("graph"+el.id), data, options);
}