// import the base css and js needed for the boilerplate

import "../css/base.scss";
import "../css/custom.scss";
import "../js/app.js";
import "../js/cluster.js";

$(function() {
  // handle global nav link outbound click tracking for google analytics
  $(".nav-link").click(function() {
    var href = $(this).attr("href");
    window.ga("send", "event", "outbound", "click", href);
  });

  $(".footer-links a").click(function() {
    var href = $(this).attr("href");
    window.ga("send", "event", "outbound", "click", href);
  });
});
