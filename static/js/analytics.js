const neonCyan = '#0ff';
const neonPink = '#f0f';
const cyberDark = '#0a0a12';
const cyberGradient = 'linear-gradient(45deg, #f0f, #0ff)';


document.addEventListener('DOMContentLoaded', function() {
    // Función para generar datos aleatorios
    const generateRandomData = (points, min, max) => {
        return Array.from({length: points}, () => 
            Math.floor(Math.random() * (max - min + 1)) + min);
    };

    // Configuración inicial
    const timeRange = document.getElementById('timeRange');
    let currentData = {
        labels: [],
        visits: [],
        leads: []
    };

    // Función para inicializar datos según el rango
    const initializeData = (days) => {
        if(days === '7') {
            currentData.labels = Array.from({length: 7}, (_, i) => `Day ${i + 1}`);
            currentData.visits = generateRandomData(7, 50, 200);
            currentData.leads = generateRandomData(7, 20, 100);
        } 
        else if(days === '30') {
            currentData.labels = Array.from({length: 30}, (_, i) => `Day ${i + 1}`);
            currentData.visits = generateRandomData(30, 50, 200);
            currentData.leads = generateRandomData(30, 20, 100);
        }
        else { // Yearly
            currentData.labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            currentData.visits = generateRandomData(12, 500, 2000);
            currentData.leads = generateRandomData(12, 200, 1000);
        }
    };

    // Crear gráfico combinado
    const combinedCtx = document.getElementById('combinedChart').getContext('2d');
    const combinedChart = new Chart(combinedCtx, {
        type: 'line',
        data: {
            labels: currentData.labels,
            datasets: [{
                label: 'Google Ads Visits',
                data: currentData.visits,
                borderColor: neonPink,
                backgroundColor: 'rgba(255, 0, 255, 0.1)',
                tension: 0.4
            },
            {
                label: 'Leads Generated',
                data: currentData.leads,
                borderColor: neonCyan,
                backgroundColor: 'rgba(0, 255, 255, 0.1)',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {color: '#fff'}
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {color: 'rgba(255,255,255,0.1)'},
                    ticks: {color: '#fff'}
                },
                x: {
                    grid: {color: 'rgba(255,255,255,0.1)'},
                    ticks: {color: '#fff'}
                }
            }
        }
    });

    // Función para actualizar gráfico
    const updateChart = (days) => {
        initializeData(days);
        combinedChart.data.labels = currentData.labels;
        combinedChart.data.datasets[0].data = currentData.visits;
        combinedChart.data.datasets[1].data = currentData.leads;
        combinedChart.update();
        updateMetrics();
    };

    // Event listener para el selector de tiempo
    timeRange.addEventListener('change', function() {
        updateChart(this.value);
    });

    // Inicializar con 7 días
    updateChart('7');
});