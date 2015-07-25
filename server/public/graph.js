var keys = [];
var vals = [];

$.getJSON( "/data1.json", function( data ) {
    $.each(data, function(key, val) {
        if (val.key.substring(0,2) == 's2') {
            keys.push(val.key);
            vals.push(val.value);
        }
    });
    console.log(keys);
    console.log(vals);
    new Chartist.Line('.ct-chart', {
      labels: keys,
      series: [
          vals
      ]
    }, {
      fullWidth: false,
      chartPadding: {
        right: 2
      }
    });
});
