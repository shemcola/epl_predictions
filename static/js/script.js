function fetchPredictions(endpoint) {
    fetch(`/${endpoint}`)
        .then(response => response.json())
        .then(data => {
            const predictionList = document.getElementById('prediction-list');
            predictionList.innerHTML = '';  // Clear existing predictions
            
            data.forEach(prediction => {
                const listItem = document.createElement('li');
                listItem.innerHTML = `${prediction.home} vs ${prediction.away} - Prediction: ${prediction.prediction}`;
                predictionList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching predictions:', error);
        });
}
 
