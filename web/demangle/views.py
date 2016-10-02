from flask import Blueprint, render_template, request, Response
import json
from .demangler import demanglers

front_page = Blueprint('front_page', __name__)

@front_page.route('/')
def index():
    return render_template('index.html', demanglers=demanglers)

@front_page.route('/run', methods=['POST'])
def run():
    names = request.form['names']
    lang = request.form['lang']
    if lang not in demanglers:
        return 'Bad lang'
    else:
        result = demanglers[lang].run(names)
        return Response(result.decode('utf-8'), mimetype='text/plain')

