from src.app import create_app
import pyqrcode

if __name__ == "__main__":

    app = create_app()
    app.run(debug=True)