from flask import Flask, redirect, url_for # type: ignore
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'welcome flask app page!'


@app.route('/about')
def about():
    return '<html><body><h1>welcome flask About page!</h1></body></html>'


@app.route('/passed/<int:marks>')
def passed(marks):
    return "Congratulation you have passed and your mark is: " + str(marks)


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




if __name__ == '__main__':
    app.run(debug=True)




# knockMsg = "Hi there Rakib!"
# print(knockMsg)
# print("Do code daily 10 hours!")