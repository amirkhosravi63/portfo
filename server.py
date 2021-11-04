# set FLASK_APP=server
# set FLASK_ENV=development: This line enables debug mode (it is not necessary, whenever any changes is made on these files, it restarts the server)
# flask run (it starts the server)


from flask import Flask, render_template, url_for, request, redirect
import csv


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


app = Flask(__name__)
print(__name__)  # It is main file, so: __name__ = __main__
print(app)


@app.route('/')
def my_home():
    return render_template('index.html')

# Instead of adding Links manually, they are added dynamically.


@app.route('/<string:page_name>')
def my_home2(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/contact_thankyou.html')
    else:
        return 'Sth went wrong'
    # return render_template('login.html', error=error)


# @app.route("/index.html")
# def my_home2():
#     return render_template('index.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# @app.route("/components.html")
# def components():
#     return render_template('components.html')
