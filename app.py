from flask import Flask, request, jsonify, redirect
from profanityfilter import ProfanityFilter


#function to censor text
def censor(text):
    '''censor all offensive words with *'''
    pf= ProfanityFilter()
    pf.set_censor("*")
    censored = pf.censor(text)
    return censored

app = Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
   return redirect("https://documenter.getpostman.com/view/9431330/SW18wvPf?version=latest#overview")


@app.route('/', methods=['POST'])
def censortext():
    ''' Returns censored text '''
    text = request.form['text']
    censored_text = censor(text)
    return jsonify(censored_text=censored_text)

if __name__ == '__main__':
    app.run(debug=True)