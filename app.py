from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from collections import defaultdict
import os

app = Flask(__name__)
CORS(app)

# Define the list of languages to track
languages_to_track = [
    'python', 'javascript', 'java', 'ruby',
    'go', 'rust', 'sql', 'react',
    'flutter', 'android'
]

# Read and process the CSV
def load_language_frequencies():
    filepath = os.path.join(os.path.dirname(__file__), 'updated_stackoverflow_questions.csv')
    df = pd.read_csv(filepath)

    if 'tags' not in df.columns or 'timestamp' not in df.columns:
        return {}

    df['year'] = pd.to_datetime(df['timestamp'], errors='coerce').dt.year

    # Count total questions per year
    total_per_year = df['year'].value_counts().to_dict()
    # print("\nTotal questions per year:", total_per_year)  # Debugging print

    # Initialize frequency dict
    freq = {year: {lang: 0 for lang in languages_to_track} for year in [2022, 2023, 2024]}

    for _, row in df.iterrows():
        year = row['year']
        if year in freq:
            tags = str(row['tags']).lower()
            for lang in languages_to_track:
                if lang in tags:
                    freq[year][lang] += 1

    # Print raw counts before normalization
    # print("\nRaw frequencies:", freq)  # Debugging print

    # Normalize frequencies
    normalized_freq = {}
    for year in freq:
        total = total_per_year.get(year, 1)  # Avoid divide-by-zero
        normalized_freq[year] = {lang: round(freq[year][lang] / total * 100, 4) for lang in languages_to_track}

    # Print normalized values to check
    # print("\nNormalized frequencies:", normalized_freq)  # Debugging print

    return normalized_freq


@app.route('/language-frequency')
def language_frequency():
    data = load_language_frequencies()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
