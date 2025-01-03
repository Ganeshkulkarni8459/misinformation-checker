from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))  # Default to 8000 if no PORT is set
    app.run(debug=True, host='0.0.0.0', port=port)

