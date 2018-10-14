$(document).ready(function(e) {

});

var lab2id = {};

for (var i = 0; i < Object.keys(nodes).length; i++) {
    lab2id[nodes[i].label] = i;
    nodes[i].id = i;
}

for (var i = 0; i < Object.keys(links).length; i++) {
    links[i].source = lab2id[links[i].source];
    links[i].target = lab2id[links[i].target];
}

var width = window.innerWidth-20,
    height = window.innerHeight;

var svg = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height)

var force = d3.layout.force()
    .size([width, height])
    .nodes(d3.values(nodes))
    .links(links)
    .on('tick', tick)
    .linkDistance(155)
    .gravity(.15)
    .friction(.85)
    .linkStrength(1)
    .charge(-925)
    .chargeDistance(1000)
    .start();


var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return 1; })
      .style("stroke", "dimgray")
      .style("stroke-linecap", "square");

  var node = svg.append("g")
      .attr("class", "nodes")
    .selectAll("g")
    .data(nodes)
    .enter().append("g")
    .call(force.drag);
    
  var circles = node.append("circle")
      .attr('r', width * 0.0065)
    .style("fill", function (d) { return d.color; })

  var labels = node.append("text")
      .text(function(d) {
        return d.label;
      })
      .attr('x', 17)
      .attr('y', 4.5)
      .attr('font-weight',500);

  node.append("title")
      .text(function(d) { return d.label; });

function tick(e) {

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    link.attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; });

};