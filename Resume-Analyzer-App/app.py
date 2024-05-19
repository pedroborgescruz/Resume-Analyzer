from flask import Flask, render_template, request
import spacy
from spacy.pipeline import EntityRuler
import jsonlines
from spacy import displacy

app = Flask(__name__)

# Load the spaCy model and entity ruler
nlp = spacy.load("en_core_web_lg")
ruler = nlp.add_pipe("entity_ruler")
skill_pattern_path = "jz_skill_patterns.jsonl"
ruler.from_disk(skill_pattern_path)

# Define colors and options for visualization
colors = {
    "Job-Category": "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
    "SKILL": "linear-gradient(90deg, #9BE15D, #00E3AE)",
    "ORG": "#ffd966",
    "PERSON": "#e06666",
    "GPE": "#9fc5e8",
    "DATE": "#c27ba0",
    "ORDINAL": "#674ea7",
    "PRODUCT": "#f9cb9c",
}

options = {
    "ents": ["Job-Category", "SKILL", "ORG", "PERSON", "GPE", "DATE", "ORDINAL", "PRODUCT"],
    "colors": colors,
}

# Function to extract and visualize entities
def visualize_entities(text):
    doc = nlp(text)
    html = displacy.render(doc, style="ent", options=options)
    return html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        resume_text = request.form['resume']
        visualization = visualize_entities(resume_text)
        return render_template('result.html', resume_text=resume_text, visualization=visualization)

if __name__ == '__main__':
    app.run(debug=True)
