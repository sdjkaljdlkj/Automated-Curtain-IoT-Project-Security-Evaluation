from flask import Flask, redirect
from curtain import open_curtain, close_curtain
from motor import Stop

app = Flask(__name__)

@app.route("/")
def home_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    
    body {
        font-family: sans-serif;
        text-align: center;
        background: #1a1a2e;
        color: white;
    }
    
    .background_card {
        background: #16213e;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    
    h1 {
        font-size: 22px;
        margin-bottom: 6px;
    }

    p {
    color: #8a8aa0;
    margin-bottom: 30px;
    }
    
    button {
    width: 220px;
    background: #4b6cb7;
    color: white;
    border: none;
    padding: 16px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 10px;
    margin: 8px;
    transition: 0.3s;
    cursor: pointer;
    }

    .buttons { display: flex; flex-direction: column; gap: 14px; }
    .open { background: #2ecc71; }
    .close { background: #fdaa48; }
    .stop { background: #ff0000; }

    button:hover {
        opacity: 0.8;
    }
    button:active {
        transform: scale(0.98);
    }

    </style>
    </head>
    <body>
    
        <div class="background_card">
            <h1>Welcome to the Curtain Control Server</h1>
            <p>Click on the following buttons to control the curtains:</p>
            <div class= "buttons">
                <a href="/open"><button class="open">Open Curtain</button></a>
                <a href="/close"><button class="close">Close Curtain</button></a>
                <a href="/stop"><button class="stop">Stop Curtain</button></a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/open")
def open_curtain_route():
    open_curtain()
    return redirect("/")

@app.route("/close")
def close_curtain_route():
    close_curtain()
    return redirect("/")


@app.route("/stop")
def stop_curtain_route():
    Stop()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)

