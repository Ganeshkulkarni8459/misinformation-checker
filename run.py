# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
import os
from app import create_app  # Assuming you have a factory function in __init__.py

# Create the instance folder dynamically if it doesn't exist
if not os.path.exists("instance"):
    os.makedirs("instance")

app = create_app()

if __name__ == "__main__":
    app.run()
