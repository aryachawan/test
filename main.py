from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    id='unknown'
    return render_template('index.html',id=id)

@app.route("/login-signup",methods=['POST','GET'])
def loginsignup():
    return render_template('login-signup.html')

@app.route("/shop/<id>",methods=['POST','GET'])
def shop(id):
    return render_template('shop.html',id=id)

@app.route("/cart/<id>",methods=['POST','GET'])
def cart(id):
    return render_template('cart.html',id=id)

@app.route("/test",methods=['POST','GET'])
def test():
    if request.method=='POST':
        data=request.form
        return jsonify(data)
    return render_template('test.html')


if __name__=="__main__":
    app.run(debug=True)