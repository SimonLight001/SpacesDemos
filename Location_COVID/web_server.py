import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    global people
    if request.method == 'GET':
        app.logger.info(people)
        status = 'red'
        if int(people) < 580:
            status = 'green'
        return '''
        <html>
            <head>
                <title>Library</title>
            </head>
            <body style="margin: auto;width: 50%; background-color:''' + status + '''">
                <h1 style="font-size: large">Library</h1>
                <h1>''' + str(people) + '''</h1>
            </body>
        </html>'''
    elif request.method == 'POST':
        data = request.data
        people = Update(data)
        return 'Successful Update with: ' + str(people)


def Update(data):
    global people
    data = data.decode("utf-8")
    data = json.loads(data)
    people = data['users']
    app.logger.info(people)
    return people

    # forces to listen to all hosts on port 80
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
