from flask import Flask, render_template, request
import openai


app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    bot_response = generate_text(user_input)
    return {"response": bot_response}


def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003", # You can choose a different GPT model here
        prompt=prompt,
        max_tokens=12,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text.strip()
    return message

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
