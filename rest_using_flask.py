from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    
    if(request.method == 'GET'):

        data = "Hello World!"
        return jsonify({'data':data})
    
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

    return jsonify({'data':num**2})

    

if __name__ == '__main__':
    app.run(debug=True)