// Gráfico aleatorio
document.addEventListener('DOMContentLoaded', function() {
    // Configurar gráfico
    const ctx = document.getElementById('conversionChart').getContext('2d');
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'];
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: months,
            datasets: [{
                label: 'Conversion Rate %',
                data: months.map(() => Math.floor(Math.random() * (80 - 40) + 40)),
                tension: 0.4,
                pointRadius: 5,
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#fff'
                    },
                    grid: {
                        color: 'rgba(255,255,255,0.1)'
                    }
                },
                x: {
                    ticks: {
                        color: '#fff'
                    },
                    grid: {
                        color: 'rgba(255,255,255,0.1)'
                    }
                }
            }
        }
    });
        
// Paginación de tabla
const table = document.getElementById('leadsTableUpdate');
const rows = table.tBodies[0].rows;
const rowsPerPage = 5;
let currentPage = 1;

function updateTable() {
    const start = (rows.length - rowsPerPage) > 0 ? rows.length - rowsPerPage : 0;
    Array.from(rows).forEach((row, index) => {
        row.style.display = (index >= start) ? '' : 'none';
    });
    document.getElementById('paginationInfo').textContent = 
        `Showing ${start + 1} to ${rows.length} of ${rows.length} entries`;
}

updateTable();
});