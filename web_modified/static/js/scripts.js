var dropdown = document.querySelector('#dropdown_1');
dropdown_1.addEventListener('click', function(event) {
  event.stopPropagation();
  dropdown.classList.toggle('is-active');
});

$( function() {
  $( document ).tooltip();
} );

const config = {
  type: 'bar',
  data,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Prices of Bitcoin Over Time',
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
          text: 'Month',
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
          text: 'Value',
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