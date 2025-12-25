from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    original_text = None
    char_count = 0

    if request.method == 'POST':
        original_text = request.form.get('user_input')
        if original_text:
            result = original_text.upper()
            char_count = len(original_text)

    return render_template('index.html', 
                           result=result, 
                           original=original_text, 
                           count=char_count)

if __name__ == '__main__':
    app.run(debug=True)