var woeid = null;
var trendslinks = null;
var trendarray= null;
var sD= null;
var int;
function change(ltweets,k,ldiv)
	{
	var x = document.getElementById(ldiv);
	var y= x.childNodes[0];
	if(y!= null){
	var mytext=document.createTextNode(ltweets[k]);
	x.replaceChild(mytext,y);
	}
	else
	{var mytext=document.createTextNode(ltweets[k]);
	x.appendChild(mytext);
	}

	k++;

	int = self.setTimeout(function() {
    	change(ltweets,k,ldiv);
	}, 2000);



	}
function setWoeid(id){

	window.woeid = id;
	getTrendsLink();


}

function ReplaceContentInContainer(id,content) {
var container = document.getElementById(id);
container.innerHTML = content;
}

function getTrendData(){
jQuery.ajaxSetup({async:false});
trends = new Array();

$.get("php/demo.php?woeid="+woeid, function(data){
trends = JSON.parse(data);

});
}
function getTrendsLink(){

	getTrendData();
	var x = document.getElementById("tabcontent");
	var newlink = document.createElement('div');





for(i=0;i<trends.length;i++){

	var a = document.createElement('a');
	a.title = trends[i][0];
	a.innerHTML = "<br>"+a.title;
	a.href = "#";
	a.className = "show_hide";
	a.rel = "#slidingDiv_"+i;

	newlink.appendChild(a);

	var slide = document.createElement('div');
	slide.id = "slidingDiv_"+i;
	//slide.className = "toggleDiv";
	newlink.appendChild(slide);

	/*a.onclick = function() { return function() {
	alert(a.rel);
	var k =0;
	$.get("getTweets.php",{value:a.title}, function(data){
	tweets = JSON.parse(data);
	});
	//int=window.clearInterval(int)
	//change(tweets,k);



	 }; }(i);*/

}
	$('#tabcontent').empty().append(newlink);
	$(document).ready(function(){
		jQuery('a').click(function() {

			var val = this.title;
			var ldiv = this.rel;
			ldiv = ldiv.replace('#','');
			$.get("php/getTweets.php?value="+val, function(data){
	ltweets = JSON.parse(data);
	var k =0;
	int=window.clearInterval(int)
	change(ltweets,k,ldiv);
	});
                });

   $('.show_hide').showHide({
        speed: 1000,  // speed you want the toggle to happen
        easing: '',  // the animation effect you want. Remove this line if you dont want an effect and if you haven't included jQuery UI
        changeText: 1, // if you dont want the button text to change, set this to 0
        //showText: ,// the button text to show when a div is closed
       // hideText: ;  // the button text to show when a div is open

    });
});

}



google.load("visualization", "1", {packages:["corechart"]});
      //google.setOnLoadCallback(drawChart);
	var trends;
	var freq;



	//jQuery.ajaxSetup({async:false});

	//rendarray = new Array();
	// $.get("graph.php",{woeid:12586571}, function(data){
	//trendarray = JSON.parse(data);



//})


function drawChart() {


       // var data = google.visualization.arrayToDataTable(trendarray);

        var options = {
          title: 'Trends vs Frequency'
        };

	var jsonData = $.ajax({
        url: "php/graph.php?woeid="+woeid,
        dataType:"json",
        async: false,
	method:"POST"
    	}).responseText;


	trendarray = JSON.parse(jsonData);

	var data = google.visualization.arrayToDataTable(trendarray);

	//var x = document.getElementById("tabcontent");
	$('#tabcontent').empty().append('<div id="chart_div" style="width: 650px; height: 500px;"></div>');

	//<div id="chart_div" style="width: 650px; height: 500px;"></div>
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);

}

