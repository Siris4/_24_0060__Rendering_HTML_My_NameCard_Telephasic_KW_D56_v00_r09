from flask import Flask, render_template
import datetime as dt
import os

now = dt.datetime.now() # because it is (datetime Module, then datetime Class), to distinguish them from each other, we will rename the datetime Module as 'dt' or datetimeClass

# print(os.getcwd())

app = Flask(__name__)
# print(f"The __name__ is now: {__name__}")
# Re: The __name__ is now: __main__

@app.route("/")
def hello_world():
    return render_template("index_telephasic_NameCard_KW_09.html")    # removed: f"<p>Hello, Flask! It is currently {now} </p>", because we are rendering html from an html file, not placing a string down.

# remove below if unneeded:
if __name__ == "__main__":
    app.run(debug=True)   # can toggle this: True or False, depending on your needs
