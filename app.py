from flask import Flask, render_template, request

import requests
import json




app = Flask(__name__)

@app.route('/')
def get_search():
    params = {
            "Key":"TN28u9Y7KNVS",
            "limit": 10
        }

    #params["q"] = request.args.get('gif_search')
    params["search"] = request.args.get('gif_search')
    #query = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params["search"], params["Key"], params["limit"]))

    return render_template('index.html')

@app.route('/gif')
def display_gifs():



    """
    <p>print(gif_search)</p>
    """
    return render_template('gif.html')
    # extract query term



    # make 'params' dict with query term and API key

    # API call to Tenor using a request

    # first ten results from search

    # render the html using variables, passing gifs as named parameters
