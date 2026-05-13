from app import create_app

# source venv/bin/activate
app = create_app()


if __name__ == "__main__":
    app.run(port=8000)