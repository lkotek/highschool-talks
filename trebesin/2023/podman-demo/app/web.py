#!/usr/bin/env python3

from bottle import route, run, default_app
from paste import httpserver
import subprocess

@route('/')
def uptime_app():
    uptime = subprocess.Popen(
        "uptime", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        ).communicate()[0]
    return f"Uptime: {uptime.decode()}"

if __name__ == "__main__":
    application = default_app()
    httpserver.serve(application, host="0.0.0.0", port=8081)
