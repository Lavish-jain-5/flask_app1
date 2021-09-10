from flask import Flask ,request,json,jsonify

app = Flask(__name__)

@app.route('/')

def first():
    return "Hello WOrld"

@app.route('/name/<name>')

def  second(name):
    return "Hello WOrld %s" %name

@app.route('/test',methods =['POST'] )

def third():
    data = request.get_json(force=True)
    print(data)
    print(request.headers)
    print(request.data)
    return  {
          'statusCode': 200,
          'body': json.dumps('Successful!')
      }

if __name__ =='__main__':  
    app.run(debug=True)

