### Integrate HTML with FLASK (using Jinja tool)
### HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template, request # type: ignore
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/passed/<int:marks>')
def passed(marks):
    res = ""
    if marks >= 50:
        res = "PASSED SUCCESSFULLY."
    else:
        res = "Try Again. You Failed."

    return render_template('result.html', resultd = res) 


@app.route('/failed/<int:marks>')
def failed(marks):
    return "You failed and your mark is: " + str(marks)


@app.route('/results/<int:grade>')
def results(grade):
    result = ""
    if grade < 40: 
        result = "failed"
    else:
        result = "passed"

    # return result
    
    return redirect(url_for(result,marks=grade))


### result checker (HTML)page  
@app.route('/submit',methods=['POST', 'GET'])
def submit():
    totalScore = 0
    if request.method == "POST":
        datascience = float(request.form['datascience'])
        math = float(request.form['math'])
        dsa = float(request.form['dsa'])
        cplusplus = float(request.form['cplusplus'])
        totalScore = (datascience + math + dsa + cplusplus) / 4

    # res = ""
    # if totalScore >= 50:
    #     res = "passed"

    # else:
    #     res = "failed"

    return redirect(url_for('passed',marks=totalScore))




if __name__ == '__main__':
    app.run(debug=True)

