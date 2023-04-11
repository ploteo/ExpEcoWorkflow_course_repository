function draw_graph(history_contrib){
  $('#container').highcharts({
      chart: {
          type: 'line'
      },
      title: {
          text: 'Group contributions to the project'
      },
      xAxis: {
        allowDecimals: false,
           title: {
              text: 'Round'
          },
         accessibility: {
            rangeDescription: 'Range: 1 to 20'
        }
      },
      yAxis: {
          title: {
              text: 'Points'
          }
      },
        plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
      series: [{
          name: 'Group contributions',
          color: '#79dcb4',
          data: history_contrib
      }]
  });
}

