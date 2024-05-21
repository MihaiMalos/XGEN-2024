async function fetchDataSets() {
    const res = await fetch('http://127.0.0.1:5000/get_datasets');
    const dataSets = await res.json();

    const select = document.getElementById('dataSets');
    select.innerHTML = '';
    dataSets.forEach(dataSet => {
        const option = document.createElement('option');
        option.value = dataSet.value;
        option.text = dataSet.text;
        select.appendChild(option);
    });
}
async function sendRequest() {
    const selectedDataSet = document.getElementById('dataSets').value;
    const selectedValue = document.getElementById('selectedValue').value;

    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const siteLink = tabs[0].url;

        // Trimite cererea la server
        fetch('http://127.0.0.1:5000/submit_dataset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ selectedDataSet,selectedValue, siteLink })
        }).then(response => response.json())
        .then(result => {
            console.log(result); // Poți face ceva cu răspunsul primit
        }).catch(error => {
            console.error('Error sending request:', error);
        });
    });
}


document.addEventListener('DOMContentLoaded', (event) => {
    fetchDataSets(); // Apelează funcția pentru a popula dropdown-ul cu dataSets

    const sendRequestButton = document.getElementById('sendRequestButton');
    sendRequestButton.addEventListener('click', sendRequest);
});
