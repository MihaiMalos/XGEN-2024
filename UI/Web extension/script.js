async function fetchDataSets() {
    const res = await fetch('http://127.0.0.1:5000/get_datasets');
    const dataSets = await res.json();

    const select = document.getElementById('dataSets');
    select.innerHTML = '';
    dataSets.forEach(dataSet => {
        const option = document.createElement('option');
        option.value = dataSet;
        option.text = dataSet;
        select.appendChild(option);
    });
}

async function processText() {
    const inputText = document.getElementById('inputText').value;

    const res = await fetch('http://127.0.0.1:5000/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    });

    const result = await res.json();
    document.getElementById('inputText').value = result.processedText; // Afișează răspunsul în textbox
}

async function scrapeSite() {
    const loadingMessage = document.getElementById('loadingMessage');
    loadingMessage.style.display = 'block';

    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const siteLink = tabs[0].url;
    
        fetch('http://127.0.0.1:5000/scrape_site', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ siteLink })
        }).then(response => response.json())
        .then(result => {
            articlesList = result;
            displayArticles(); // Afișează articolele în HTML
        }).catch(error => {
            console.error('Error sending request:', error);
        }).finally(() => {
            // Ascunde mesajul de încărcare
            loadingMessage.style.display = 'none';
        });
    });
}
function displayArticles() {
    const articlesContainer = document.getElementById('articlesContainer');
    const articlesListElement = document.getElementById('articlesList');
    articlesListElement.innerHTML = '';

    articlesList.forEach((article, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <div class="article-container">
                <span>${article}</span>
                <select class="articleLabel" data-title="${article}" id="label-${index}">
                    <option value="true">True</option>
                    <option value="false">False</option>
                </select>
            </div>
        `;
        articlesListElement.appendChild(listItem);
    });

    articlesContainer.style.display = 'block';
}

async function submitArticles() {
    const selectedDataSet = document.getElementById('dataSets').value;
    const articleLabels = document.querySelectorAll('.articleLabel');
    const labels = Array.from(articleLabels).map(labelInput => labelInput.value === 'true' ? 1 : 0);
    const res = await fetch('http://127.0.0.1:5000/submit_articles', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({selectedDataSet,labels })
    });

    const result = await res.json();
    console.log(result); // You can do something with the response if needed
}

document.addEventListener('DOMContentLoaded', (event) => {
    fetchDataSets(); // Apelează funcția pentru a popula dropdown-ul cu dataSets

    const sendRequestButton = document.getElementById('sendRequestButton');
    sendRequestButton.addEventListener('click', scrapeSite);
    
    const submitArticlesButton = document.getElementById('submitArticlesButton');
    submitArticlesButton.addEventListener('click', submitArticles);
    
    const processTextButton = document.getElementById('processTextButton');
    processTextButton.addEventListener('click', processText);
});
