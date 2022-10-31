from Backend import app

if __name__ == '__main__':
    print("Production")
    app.run(host='0.0.0.0', port=5000, debug=True)