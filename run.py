from backend.App import createApp

app = createApp()

if __name__ == "__main__":
    app.run(debug=True)  # 'debug=True' might be redundant if debug is already set in 'createApp'