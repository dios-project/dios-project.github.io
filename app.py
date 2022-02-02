from flask import Flask

app=Flask("app")
@app.route("/")
def f(): return "ok"

app.run()
