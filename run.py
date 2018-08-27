from app import create_app

app = create_app()

@app.route('/')
def hello():
    return "<h1>Hello world~<h1>"

if __name__ == '__main__':
    app.run()
