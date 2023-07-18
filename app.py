from flask import Flask , render_template , url_for
from flask import request as req
import requests

app = Flask(__name__)

@app.route("/" , methods=["GET" , "POST"])
def home():
    return render_template("index.html")
@app.route("/Summarize" ,methods= ["GET" , "POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}
        maxL=int(req.form["maxL"])
        minL= maxL//4
        data = req.form["data"]
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters":{"min_length":minL , "max_length":maxL},
        })[0]
        print(output)
        return render_template("index.html" , result=output["summary_text"])
    else:
        return render_template("index.html")

