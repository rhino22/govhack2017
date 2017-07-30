

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['treemap']});

// Set a callback to run when the Google Visualization API is loaded.
//google.charts.setOnLoadCallback(readynow);
//
//function readynow() {
//console.log("ready")
//drawChart()
//}

//get data
//function getData() {
//
//    var xhttp = new XMLHttpRequest();
//
//    // what to do on success:
//    xhttp.onreadystatechange = function() {
//
//      if (this.readyState == 4 && this.status == 200) {
//        global_lol = JSON.parse(xhttp.responseText);
//      } else {
//        console.log(this)
//      }
//    };
//    xhttp.open("POST", "/data", false) // use post if its large, false = noync
//
//    xhttp.send();
//}

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
//var b;
function drawChart() {

var data = google.visualization.arrayToDataTable(global_lol);

tree = new google.visualization.TreeMap(document.getElementById('chart_div'));


tree.draw(data, {
          minColor: '#f00',
          midColor: '#ddd',
          maxColor: '#0d0',
          headerHeight: 15,
          fontColor: 'black',
          showScale: true
        });

var data2 = google.visualization.arrayToDataTable(twenty);

tree2 = new google.visualization.TreeMap(document.getElementById('chart_div2'));

tree2.draw(data2, {
          minColor: '#f00',
          midColor: '#ddd',
          maxColor: '#0d0',
          headerHeight: 15,
          fontColor: 'black',
          showScale: true
        });

}


//https://stackoverflow.com/questions/11821261/how-to-get-all-selected-values-from-select-multiple-multiple
//function getSelectValues(select) {
//  var result = [];
//  var options = select && select.options;
//  var opt;
//
//  for (var i=0, iLen=options.length; i<iLen; i++) {
//    opt = options[i];
//
//    if (opt.selected) {
//      result.push(opt.value || opt.text);
//    }
//  }
//  return result;
//}
//
//function getRolling() {
//
//year = document.getElementById("year");
//state = document.getElementById("state");
//industry = document.getElementById("industry");
//age = document.getElementById("age");
//absyear = document.getElementById("absyear");
//
//    return getSelectValues(year)
//
//}