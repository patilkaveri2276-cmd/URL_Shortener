from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

# Dictionary to store short code and original URL
url_mapping = {}

# Function to generate random short code
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        url_mapping[short_code] = original_url
        return f"""
        <h3>Short URL created!</h3>
        <p>Short URL: <a href='/{short_code}'>http://127.0.0.1:5000/{short_code}</a></p>
        <br><a href='/'>Shorten Another URL</a>
        """
    
    return '''
        <h2>Simple URL Shortener</h2>
        <form method="post">
            Enter URL: <input type="text" name="url" required>
            <input type="submit" value="Shorten">
        </form>
    '''

# Redirect to original URL
@app.route('/<short_code>')
def redirect_to_url(short_code):
    if short_code in url_mapping:
        return redirect(url_mapping[short_code])
    return "<h3>URL not found!</h3>"

if __name__ == '__main__':
    app.run(debug=True)
