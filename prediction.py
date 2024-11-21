 
import requests
from bs4 import BeautifulSoup

def fetch_predictions():
    url = 'https://www.predictz.com/predictions/english-premier-league/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    predictions = []
    matches = soup.find_all('div', class_='match')  # Adjust based on actual website structure

    for match in matches:
        home_team = match.find('span', class_='home-team').text.strip()
        away_team = match.find('span', class_='away-team').text.strip()
        prediction = match.find('span', class_='prediction').text.strip()

        predictions.append({
            'home': home_team,
            'away': away_team,
            'prediction': prediction
        })

    return predictions
