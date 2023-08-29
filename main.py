from src import app
from src.config.database import database_setup

# @app.get("/", tags=[home_tag])
# def home():
#     """
#     Redirects to /openapi, showing API documentation style selection
#     """
#     return redirect("/openapi", code=302)


if __name__ == "__main__":
    with app.app_context():
        database_setup()
        print("Database setup completed...")
        print("Starting API server...")
        app.run(debug=True, host="localhost", port=4200, use_reloader=True)
