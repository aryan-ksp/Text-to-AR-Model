from flask import Flask, render_template, request, send_file
import os
from text_to_depth import generate_depth_map
from depth_to_3d import depth_to_3d

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        generate_depth_map(prompt)
        depth_to_3d("static/depth_map.png")
        return render_template("index.html", model_generated=True)
    
    return render_template("index.html", model_generated=False)

@app.route("/download")
def download():
    return send_file("static/model.obj", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
