var dropdown = document.querySelector('#dropdown_1');
dropdown_1.addEventListener('click', function(event) {
  event.stopPropagation();
  dropdown.classList.toggle('is-active');
});

$( function() {
  $( document ).tooltip();
} );

var colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
		  '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];

const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Distribution of Sentiment',
        color: 'rgba(255, 255, 255, 1)',
        font: {
          size: 40
        }
      }
    },
    scales: {
      x: {
        ticks: {
          fontSize: 15,
          color: 'rgba(255, 255, 255, 1)',
          font: {
            size: 15
          }
        },
        title: {
          display: true,
          text: 'Sentiment',
          color: 'white',
          font: {
            size: 20,
          }
        },
        display: true,
        grid:{
          color: 'rgba(255, 255, 255, 0.3)',    
        }
      },
      y: {
        ticks: {
          color: 'rgba(255, 255, 255, 1)',
          font: {
            size: 15
          }
        },
        title: {
          display: true,
          text: 'Frequency',
          color: 'white',
          font: {
            size: 20,
          }
        },
        display: true,
        grid: {
          color: 'rgba(255, 255, 255, 0.3)',    
     
        },
      },
      
    },
    
  },
};

var myChart = new Chart(
  document.getElementById('myChart'),
  config,
);

const config2 = {
  type: 'doughnut',
  data: data2,
  responsive: true,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Composition of Behaviors',
        color: 'rgba(255, 255, 255, 1)',
        font: {
          size: 40
        }
      }
    }
  }
}

var myChart2 = new Chart(
  document.getElementById('myPie'),
  config2,
);

const config3 = {
  type: 'doughnut',
  data: data3,
  responsive: true,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Composition of Emotions',
        color: 'rgba(255, 255, 255, 1)',
        font: {
          size: 40
        }
      }
    }
  }
}

var myChart3 = new Chart(
  document.getElementById('myPie2'),
  config3,
);