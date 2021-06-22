const data = {
labels: labels,
datasets: [{
  label: 'Distribution of Sentiments',
  backgroundColor: 'DeepSkyBlue',
  borderColor: 'rgb(0, 255, 255)',
  borderWidth: 0.5,
  data: data_values1,
}],
};   

const data2 = {
labels: labels2,
datasets: [{
  label: 'Distribution of Sentiments',
  backgroundColor: behaviorColorArray,
  borderColor: behaviorColorArray,
  data: data_values2,
}],
};

const data3 = {
labels: labels3,
datasets: [{
  label: 'Distribution of Emotions',
  backgroundColor: emotionColorArray ,
  borderColor: emotionColorArray ,
  data: data_values3,
}],
};

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