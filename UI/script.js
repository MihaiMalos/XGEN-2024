document.getElementById('csvFileInput').addEventListener('change', handleFileSelect, false);

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        Papa.parse(file, {
            header: true, // if the CSV has a header row
            dynamicTyping: true, // auto-convert types
            complete: function(results) {
                console.log("Parsed CSV Data:", results.data);
                displayCSVContent(results.data);
            },
            error: function(error) {
                console.error("Error parsing CSV:", error);
            }
        });
    }
}

function displayCSVContent(data) {
    const output = document.getElementById('csvOutput');
    output.textContent = JSON.stringify(data, null, 2); // Pretty-print JSON
}