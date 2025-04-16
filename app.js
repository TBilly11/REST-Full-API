document.addEventListener("DOMContentLoaded", function() {
    fetch('/autos')
      .then(response => response.json())
      .then(data => {
        const tableBody = document.querySelector('#autoTable tbody');
        data.forEach(auto => {
          const row = document.createElement('tr');
          Object.values(auto).forEach(value => {
            const cell = document.createElement('td');
            cell.textContent = value;
            row.appendChild(cell);
          });
          tableBody.appendChild(row);
        });
      })
      .catch(error => console.error('Error:', error));
  });
  