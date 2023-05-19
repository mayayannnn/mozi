from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr

app = Flask(__name__)

@app.route("/")
def a():
    return render_template("mozi.html")

@app.route("/mozi",methods=["post"])
def mozi():
    mozi = request.files["mozi"]
    tools = pyocr.get_available_tools()
    tool = tools[0]
    img = Image.open(mozi)
    txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
    if txt == "":
        txt = "読み取れませんでした"
    return render_template("mozi.html",txt=txt)

if __name__ == '__main__':
    app.run(debug=True)
