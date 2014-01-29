var map;
var box = null;
var newContent;
var trendfreq;
var toggleBtn;
var jsonArray = [];
var locations = [];
var int;
var val = null;


function change(tweets,k)
	{

	x = document.getElementById('tweetinfo');
	y= x.childNodes[0];
	var mytext=document.createTextNode(tweets[k]);
	x.replaceChild(mytext,y);
	//alert(tweets[k]);
	k++;
	//alert(tweets[k]);
	int = self.setTimeout(function() {
    	change(tweets,k);
	}, 2000);



	}

function createJson(trends,lat,lon){

	var x = 0.5;
	var y = 0.5;

	var sw = 0;
	var sh = 0;

	var count = 0;
	for (i=0;i<trends.length;i++)
	{
	count++;

	if(trends[i][1] > 400){
	sw = 100;
	sh = 40;

	}
	else if(trends[i][1] > 300 && trends[i][1] < 200){
	sw = 80;
	sh = 25;
	}
	else if(trends[i][1] > 200 && trends[i][1] < 100){
	sw = 60;
	sh = 20;
	}
	else if(trends[i][1] > 100 && trends[i][1] < 50){
	sw = 40;
	sh = 15;
	}
	else{
	sw = 20;
	sh = 10;
	}



	var latLng = new google.maps.LatLng(lat,lon);
	jsonArray.push({
      	position: latLng,
	id:i,
	value : trends[i][0],
      draggable: false,
      map: map,
      icon: new google.maps.MarkerImage(
        "http://chart.googleapis.com/chart?chst=d_text_outline&chld=FFFFFF|14|h|030303|b|".concat(trends[i][0]),
       new google.maps.Size(100, 200),null, new google.maps.Point(x, y),new google.maps.Size(sw,sh)),

    	});

	lat = lat + x;
	lon = lon + y;



	if(count==3){

	x = x;
	y = -y;
	}
	else if(count == 6){
	y= y;
	x = -x
	}
	else if(count == 9){

	x = x;
	y= -y;
	}
	}

	for (j = 0; j < jsonArray.length; j++) {
  	var data = jsonArray[j];

  	var marker = new google.maps.Marker(data);
	marker.set("id", j);



	(function(marker, data) {

  	google.maps.event.addListener(marker, 'click', function() {
     	val = marker.get("value");
		$.get("getTweets.php",{value:val}, function(data){
	tweets = JSON.parse(data);
	});
	//alert(tweets);
	//var boxheading = document.getElementById('boxheading');
	//var boxheadingchild= boxheading.childNodes[0];
	var boxheading = "<h3>People Tweeting about <i>"+val+"</i>:<h3>";
	document.getElementById("boxheading").innerHTML= boxheading;
	//var boxtext=document.createTextNode("Tweets on "+val+":");
	//boxheading.replaceChild(boxtext,boxheadingchild);
	var k =0;
	int=window.clearInterval(int)
	change(tweets,k);
	});

})(marker, data);

	}
}



function initialize() {
    var mapDiv = document.getElementById('map_canvas');
    var myOptions = {
        zoom: 5,
        center: new google.maps.LatLng(21.7679, 78.8718),
        mapTypeId: google.maps.MapTypeId.SATELLITE
    }

 map = new google.maps.Map(mapDiv, myOptions);


	locations.push([18.9765,72.8258,12586539]);
	locations.push([29.0167,77.3833,20070458]);
	locations.push([12.3024,76.6386,12586571]);
	locations.push([22.5697,88.3697,12586798]);
	for(var i=0;i<locations.length;i++){




	jQuery.ajaxSetup({async:false});
 	trends = new Array();
	 $.get("demo.php",{woeid:locations[i][2]}, function(data){
	trendfreq = JSON.parse(data);




})
		var lat = locations[i][0];
		var lon = locations[i][1];

	createJson(trendfreq,lat,lon);
	}



}

