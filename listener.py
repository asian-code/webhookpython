from flask import Flask, request, abort
import os

# import json

app = Flask(__name__)

@app.route('/work/freshdesk-auth-tool', methods=['POST'])
def work():
    print('Running FD auth tool...')
    os.system('python3 /home/eric/Downloads/FreshdeskReAuthChecker.py')
    return 'success', 200

@app.route('/work', methods=['POST'])
def test():
    print("got it from /work YAY")
    data=request.json
    print(request.get_json())
    if (data["name"]=="freshdesk-auth-tool"):
        print('IT WORKS --------------------------------------------')
    return 'success', 200
if __name__ == '__main__':
    app.run()




