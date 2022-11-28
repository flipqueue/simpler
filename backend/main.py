from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/activity/2/prompt")
def activity_two_hardcoded_prompt():
    return "if x + 2 = 5, what is x?"


@app.route("/activity/2/grading_guide")
def activity_two_hardcoded_answer():
    # Future expansion ideas: 
    # partial credit, 
    # per-topic partial credit, 
    # explanations for common mistakes,
    # autograding
    return {"explanation": "The only correct answer is 3."}


@app.route("/activity/2/suggestions/topics")
def activity_two_suggested_topics():
    return ['algebra', 'prealgebra', 'simple_equations']
