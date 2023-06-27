import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def proxy_list():
    # Read the proxy file
    output_dir = "output"
    output_file = "proxies.txt"
    filepath = os.path.join(output_dir, output_file)
    with open(filepath, "r") as file:
        proxies = file.read().splitlines()

    return render_template('proxy_list.html', proxies=proxies)

if __name__ == '__main__':
    app.run()
