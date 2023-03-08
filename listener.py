from flask import Flask, request, abort
import subprocess

# import json

app = Flask(__name__)

@app.route('/work', methods=['POST'])
def work():
    print('WOOOHOOOOO')
    data=request.json
    print(data)
    if request.method == 'POST':#'POST':
        
        #check for what program to run
        if (data["name"]=="freshdesk-auth-tool"):
            print("Running freshdesk-auth-tool ")
            # Run another Python script and capture the output
            # result = subprocess.run(['python3', '/home/eric/Downloads/FreshdeskReAuthChecker.py'], capture_output=True)
            # print(result.stdout)

        elif (data["name"]=="create VM"):
            print("VM WOOOHOOO")
            print("data: "+request.json)
        return 'success', 200
    else:
        print(request.json)
        print('HEHEHEHEHEHEHEHEHHEEH')
        abort(400)
    print('END of function')
if __name__ == '__main__':
    app.run()




