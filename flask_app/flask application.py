from flask import Flask, request
from time import strftime
from socket import gethostname, gethostbyname
from random import choice
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <html>
            <head>
                <title>HOME</title>
            </head>
            <body>
                <a href="/whoami/"><h2><center>Whoami</center></h2></a><br />
                <a href="/source_code/"><h2><center>Source Code</center></a></h2><br />
                <a href="/random/"><h2><center>Random</center></h2></a>
            </body>
        </html>
    """

@app.route("/whoami/", methods=['GET', 'POST'])
def hello_world():
    user_agent = request.headers.get('User-Agent')
    remote_name = gethostname()
    remote_ip = gethostbyname(remote_name)
    time_server = strftime("%c")
    return f"""
        <html>
            <head>
                <title>whomai</title>
            </head>
            <body>
                <a href="/">Home</a> <a href="/source_code/">Source code</a> <a href="/random/">Random</a>
                <h3>Your User-Agent is: {user_agent}</h3>
                <br />
                <h3>Your name:{remote_name}</h3> 
                <h3>Your IP:{remote_ip}</h3>
                <br />
                <h3>Server time is:</h3>
                <h3>{time_server}</h3>
            </body>
        </html>
    """
    
@app.route("/source_code/")
def source_code():
    dir_path = Path.cwd()
    path = Path(dir_path)
    text = str()
    with open(f"{path}\\flask application.py", "r") as flask_file:
        flask_file = flask_file.readlines()
    for i in flask_file:
        text += i + "<br />"
    return f"""
        <html>
            <head>
                <title>source_code</title>
            </head>
            <body>
                <a href="/whoami/">Whoami</a> <a href="/random/">random</a><br />
                {text}
            </body>
        </html>
        """

@app.route("/random/")
def rando():
    length = request.values.get("length")
    specials = request.values.get("specials")
    digits = request.values.get("digits")
    if length == None or specials == None or digits == None or not 0 <= int(length) <= 100 or not 0 <= int(specials) <= 1 and not 0 <= int(digits) <= 1:
        warning_list = list()
        if length == None or not 0 <= int(length) <= 100:
            warning_list.append("Length must be from 0 to 100 and you enter")
            warning_list.append(request.values.get("length"))
        if specials == None or not 0 <= int(specials) <= 1:
            warning_list.append("Specials must be 0 or 1 and you enter")
            warning_list.append(request.values.get("specials"))
        if digits == None or not 0 <= int(digits) <= 1:
            warning_list.append("Digits must be 0 or 1 and you enter")
            warning_list.append(request.values.get("digits"))
        title = """
            <html>
                <head>
                    <title>Warning!!</title>
                </head>
            """
        caption = """
            <body>
                <a href="/">Home</a> <a href="/whoami/">Whomai</a> <a href="/source_code/">Source code</a><br />
                <h2 style="color:red"><center>one more time pls!!</center></h2>
            """
        body = str()
        for items in range(0, len(warning_list) - 1, 2):
            body += f"<h3><center>{warning_list[items]} {warning_list[items + 1]}</center></h3>"
        form = """
                <form><center>
                        Length: <input length = "length" /><br /><br />
                        Specials: <input specials = "specials" /><br /><br />
                        Disigts: <input digits = "digits" /><br /><br />
                        <input type="submit" />
                </center></form>
                </body>
            </html>
            """
        warning_html = "".join((title, caption, body, form))
        return warning_html

    else:
        specials_list = ["!", "№", ";", "%", ":", "?", "*", "(", ")", "_", "+"]
        digits_list = [str(num) for num in range(10)]
        full_list = list()
        for char in range(65, 123):
            if 57 < char < 97:
                continue
            else:
                full_list.append(chr(char))
        if specials == "1":
            for item in specials_list:
                full_list.append(item)
        if digits == "1":
            for item in digits_list:
                full_list.append(item)
        output_random = str()
        for _ in range(int(length)):
            output_random += choice(full_list)
        return f"""
            <html>
                <head>
                    <title>random</title>
                </head>
                <body>
                    <a href="/">Home</a> <a href="/whoami/">Whomai</a> <a href="/source_code/">Source code</a><br />
                    <h3><center>{output_random}</center></h3>
                    <form><center>
                        Length: <input length = "length" /><br /><br />
                        Specials: <input specials = "specials" /><br /><br />
                        Digits: <input digits = "digits" /><br /><br />
                        <input type="submit" />
                    </center></form>
                </body>
            </html>
                """       
                
if __name__ == "__main__":
    app.run(debug=True)