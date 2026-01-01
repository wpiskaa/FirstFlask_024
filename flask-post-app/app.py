import os
from flask import Flask, render_template, request

# Mengatur path folder agar Flask tidak bingung mencari file index.html
template_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(template_dir, 'templates')
static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    original_text = None
    char_count = 0

    if request.method == 'POST':
        # Mengambil data dari form HTML
        original_text = request.form.get('user_input')
        if original_text:
            # Logika Python untuk memproses teks
            result = original_text.upper()
            char_count = len(original_text)

    # Menghubungkan variabel Python ke file HTML (index.html)
    return render_template('index.html', 
                           result=result, 
                           original=original_text, 
                           count=char_count)

if __name__ == '__main__':
    app.run(debug=True)