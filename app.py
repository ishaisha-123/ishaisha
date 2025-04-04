from flask import Flask
import os
import subprocess
from datetime import datetime
app= Flask(__name__)
@app.route('/htop')
def htop_info():
    name="Your Full Name"
    username=os.getenv("USER","codespace")
    server_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output=subprocess.getoutput("top -b -n 1")
    return f"""
    <h1>Name:{name}</h1>
    <h2>Username:{username}</h2>
    <h2>Server Time:{server_time}</h2>
    <pre>{top_output}</pre>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
