from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Data Storage (Replace with a Database in a Real Application) ---
PORTAL_DATA = {
    'home': {
        'title': 'Welcome to Our Portal!',
        'content': 'This is the homepage of our web portal. Explore the links below to find what you need.'
    },
    'services': {
        'title': 'Our Services',
        'content': 'Here you can find a list of the services we offer.'
    },
    'products': {
        'title': 'Our Products',
        'content': 'Check out our latest products!'
    },
    'contact': {
        'title': 'Contact Us',
        'content': 'Get in touch with us using the information below.'
    }
}

LINKS = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Services', 'url': '/services'},
    {'name': 'Products', 'url': '/products'},
    {'name': 'Contact', 'url': '/contact'}
]

# --- Routes ---

@app.route('/')
def home():
    return render_template('page.html', page_data=PORTAL_DATA.get('home'), links=LINKS)

@app.route('/<page_name>')
def generic_page(page_name):
    page_data = PORTAL_DATA.get(page_name)
    if page_data:
        return render_template('page.html', page_data=page_data, links=LINKS)
    else:
        return render_template('404.html', links=LINKS), 404

# --- Optional: Example of a Form and Handling ---
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    page_data = PORTAL_DATA.get('contact')
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_text = request.form.get('message')
        # In a real application, you would process this data (e.g., send an email, save to a database)
        print(f"Received message from: {name} <{email}> - {message_text}")
        message = "Your message has been received. We will get back to you soon!"
        return render_template('contact.html', page_data=page_data, links=LINKS, message=message)
    return render_template('contact.html', page_data=page_data, links=LINKS, message=message)

# --- Error Handling ---
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', links=LINKS), 404

if __name__ == '__main__':
    app.run(debug=True)