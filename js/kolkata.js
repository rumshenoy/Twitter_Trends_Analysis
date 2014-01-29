google.load("jquery", "1.3");
var id = null;
var trendslinks = null;
var trendarray= null;


function setWoeid(id){

	window.id = id;



}

function ReplaceContentInContainer(id,content) {
var container = document.getElementById(id);
container.innerHTML = content;
}

jQuery.ajaxSetup({async:false});
trends = new Array();

$.get("php/demo.php",{woeid:12586798}, function(data){
trends = JSON.parse(data);
});

function getTrendsLink(){

	var x = document.getElementById("tabcontent");
	var newlink = document.createElement('div');


for(i=0;i<trends.length;i++){


	var a = document.createElement('a');
	a.title = trends[i];
	a.innerHTML = "<br>"+a.title;
	a.href = "#";
	a.onclick = function() { return function() {
	var k =0;
	$.get("php/getTweets.php",{value:a.title}, function(data){
	tweets = JSON.parse(data);
	});
	int=window.clearInterval(int)
	change(tweets,k);
	 }; }(i);
	newlink.appendChild(a);

}
	$('#tabcontent').empty().append(newlink);
}



google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
	var trends;
	var freq;
	jQuery.ajaxSetup({async:false});

	trendarray = new Array();
	 $.get("php/graph.php",{woeid:12586798}, function(data){
	trendarray = JSON.parse(data);

});

function drawChart() {
        var data = google.visualization.arrayToDataTable(trendarray);

        var options = {
          title: 'Trends vs Frequency'
        };

	//var x = document.getElementById("tabcontent");
	$('#tabcontent').empty().append('<div id="chart_div" style="width: 650px; height: 500px;"></div>');

	//<div id="chart_div" style="width: 650px; height: 500px;"></div>
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);

};
