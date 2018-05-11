from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/submit')
def submit():
	return render_template('submit.html')

@app.route('/api')
def api():
	return render_template('api.html')

@app.route('/analysis')
def analysis():
	return render_template('analysis.html')

if __name__ == '__main__':
  app.run()