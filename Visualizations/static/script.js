$(document).ready(function(e) {

});

var lab2id = {};

console.log(nodes);
console.log(links);

for (var i = 0; i < Object.keys(nodes).length; i++) {
    lab2id[nodes[i].label] = i;
    nodes[i].id = i;
}

for (var i = 0; i < Object.keys(links).length; i++) {
    links[i].source = lab2id[links[i].source];
    links[i].target = lab2id[links[i].target];
}

var width = 1000,
    height = 800;

var svg = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height)

var force = d3.layout.force()
    .size([width, height])
    .nodes(d3.values(nodes))
    .links(links)
    .on('tick', tick)
    .linkDistance(100)
    .gravity(.15)
    .friction(.8)
    .linkStrength(1)
    .charge(-425)
    .chargeDistance(600)
    .start();

var link = svg.selectAll('.link')
    .data(links)
    .enter().append('line')
    .attr('class', 'link')
    .style("stroke", "black")           // colour the line
    .style("stroke-width", 8)          // adjust line width
    .style("stroke-linecap", "square")  // stroke-linecap type;

var node = svg.selectAll('.node')
    .data(force.nodes())
    .enter().append('circle')
    .attr('class', 'node')
    .attr('r', width * 0.01)

function tick(e) {

    node.attr('cx', function(d) { return d.x; })
        .attr('cy', function(d) { return d.y; })
        .call(force.drag);

    link.attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; });

};