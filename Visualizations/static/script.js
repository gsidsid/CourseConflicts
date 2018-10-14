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
    .linkDistance(175)
    .gravity(.15)
    .friction(.85)
    .linkStrength(1)
    .charge(-925)
    .chargeDistance(1000)
    .start();

var link = svg.selectAll('.link')
    .data(links)
    .enter().append('line')
    .attr('class', 'link')
    .style("stroke", "black")           // colour the line
    .style("stroke-width", 1)          // adjust line width
    .style("stroke-linecap", "square")  // stroke-linecap type;

var node = svg.selectAll('.node')
    .data(nodes)
    .enter()
    .append("g")
    .append('circle')
    .attr('class', 'node')
    .attr('r', width * 0.006)
    .style("fill", function (d) { return d.color; })
    .call(force.drag);

node.append("text")
      .attr("dx", 12)
      .attr("dy", ".35em")
      .text(function(d) { return d.label });

function tick(e) {

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    link.attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; });

};