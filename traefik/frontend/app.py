from flask import Flask, request
import os
import requests

app = Flask(__name__)

# 🔥 CSS-template så vi kan återanvända samma synthwave-style
def synthwave_page(content: str) -> str:
    return f"""
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Press+Start+2P&display=swap" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style>
            :root {{
                --neon-pink: #ff00ff;
                --neon-cyan: #00ffff;
                --deep1: #1a1a2e;
                --deep2: #16213e;
                --deep3: #0f3460;
            }}
            body {{
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 24px;
                background:
                    radial-gradient(1200px 600px at 50% -200px, rgba(255,0,255,0.25), transparent 60%),
                    linear-gradient(135deg, var(--deep1), var(--deep2), var(--deep3));
                color: #fff;
                font-family: "Orbitron", sans-serif;
            }}
            .grid {{
                position: fixed;
                inset: 0;
                background:
                    repeating-linear-gradient(to right, rgba(255,255,255,0.08) 0 1px, transparent 1px 80px),
                    repeating-linear-gradient(to top, rgba(255,255,255,0.08) 0 1px, transparent 1px 80px);
                transform: perspective(700px) rotateX(60deg) translateY(40vh);
                filter: drop-shadow(0 0 10px rgba(255,0,255,0.35));
                pointer-events: none;
            }}
            .card {{
                max-width: 500px;
                background: rgba(10, 10, 25, 0.6);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 14px;
                padding: 24px;
                backdrop-filter: blur(6px);
                text-align: center;
                box-shadow: 0 0 15px rgba(255,0,255,0.35), inset 0 0 20px rgba(0,255,255,0.1);
            }}
            h1 {{
                font-family: "Press Start 2P", monospace;
                color: var(--neon-pink);
                font-size: 22px;
                text-shadow: 0 0 6px var(--neon-pink), 0 0 14px var(--neon-cyan);
                margin-bottom: 16px;
            }}
            p {{
                margin: 0 0 20px 0;
                font-size: 14px;
                color: #ddd;
            }}
            a {{
                display: inline-block;
                background: linear-gradient(90deg, var(--neon-pink), var(--neon-cyan));
                padding: 10px 18px;
                border-radius: 8px;
                color: white;
                font-weight: 700;
                font-size: 14px;
                text-transform: uppercase;
                text-decoration: none;
                box-shadow: 0 0 8px var(--neon-pink), 0 0 16px var(--neon-cyan);
                transition: transform 0.12s ease, filter 0.12s ease;
            }}
            a:hover {{ transform: translateY(-1px); filter: brightness(1.1); }}
            a:active {{ transform: translateY(0); filter: brightness(0.95); }}
        </style>
    </head>
    <body>
        <div class="grid"></div>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """

@app.route("/", methods=["GET"])
def form():
    hostname = os.environ.get("HOSTNAME", "unknown")
    try:
        res = requests.get("http://127.0.0.1:5001/messages", timeout=2)
        messages = res.json()
        message_list = "<ul>" + "".join(f"<li>{m}</li>" for m in messages) + "</ul>"
    except Exception as e:
        message_list = f"<p>Could not load messages: {e}</p>"

    return f"""
        <html>
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Press+Start+2P&display=swap" rel="stylesheet">
            <style>
                body {{
                    background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
                    color: #fff;
                    font-family: 'Orbitron', sans-serif;
                    text-align: center;
                    padding: 20px;
                }}
                h1 {{
                    font-family: 'Press Start 2P', monospace;
                    font-size: 2em;
                    color: #ff00ff;
                    text-shadow: 0 0 5px #ff00ff, 0 0 20px #00ffff;
                }}
                h2 {{
                    color: #00ffff;
                    text-shadow: 0 0 5px #00ffff, 0 0 15px #ff00ff;
                }}
                input {{
                    padding: 10px;
                    border-radius: 5px;
                    background: #222;
                    color: #fff;
                    border: none;
                }}
                button {{
                    background: linear-gradient(90deg, #ff00ff, #00ffff);
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                    box-shadow: 0 0 10px #ff00ff, 0 0 20px #00ffff;
                }}
                button:hover {{
                    background: linear-gradient(90deg, #00ffff, #ff00ff);
                }}
                ul {{ list-style: none; padding: 0; }}
                li {{ margin: 5px 0; background: rgba(255,255,255,0.1); padding: 8px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>DevOps tag wall</h1>
            <h2>Submit a message</h2>
            <form action="/send" method="post">
                <input name="message" placeholder="Type your message..." />
                <button type="submit">Send</button>
            </form>
            <form action="/clear" method="post" style="margin-top: 10px;">
                <button type="submit">Clear messages</button>
            </form>
            <h2>Latest Messages</h2>
            {message_list}
            <p>Container: <strong>{hostname}</strong></p>
        </body>
        </html>
    """

@app.route("/send", methods=["POST"])
def send():
    message = request.form.get("message", "")
    try:
        res = requests.post("http://127.0.0.1:5001/submit", json={"message": message}, timeout=2)
        if res.ok:
            return synthwave_page("<h1>✅ Sent successfully!</h1><p>Your message is glowing on the wall.</p><a href='/'>Back</a>")
        else:
            return synthwave_page("<h1>❌ Failed to send!</h1><p>Please try again.</p><a href='/'>Back</a>")
    except Exception as e:
        return synthwave_page(f"<h1>⚠️ Error</h1><p>{e}</p><a href='/'>Back</a>")

@app.route("/clear", methods=["POST"])
def clear():
    try:
        res = requests.post("http://127.0.0.1:5001/clear", timeout=2)
        if res.ok:
            return synthwave_page("<h1>🧹 Messages cleared!</h1><p>The wall is clean and shiny again.</p><a href='/'>Back</a>")
        else:
            return synthwave_page("<h1>❌ Failed to clear!</h1><p>Something went wrong.</p><a href='/'>Back</a>")
    except Exception as e:
        return synthwave_page(f"<h1>⚠️ Error</h1><p>{e}</p><a href='/'>Back</a>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
