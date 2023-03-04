from flask import Flask, request, abort
import subprocess

# import json

app = Flask(__name__)

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        data=request.json
        print(data["name"])
        return 'success', 200
    else:
        abort(400)

@app.route('/work', methods=['POST'])
def work():
    if request.method == 'POST':
        data=request.json
        #check for what program to run
        if (data["name"]=="freshdesk-auth-tool"):
            print("testing")
    elif (data["name"]=="create VM"):
    
        print(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()



# Run another Python script and capture the output
result = subprocess.run(['python', 'path/to/other_script.py'], capture_output=True)

# Print the output
print(result.stdout)
