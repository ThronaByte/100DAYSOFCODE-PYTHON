from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/blog')
def blog():
    blog_response = requests.get('https://api.npoint.io/267632ac854a79713c11')
    blog_data = blog_response.json()

    return render_template('blog.html', blog=blog_data)


if __name__ == '__main__':
    app.run(debug=True)