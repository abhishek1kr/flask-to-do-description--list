from flask import Flask , render_template_string, request

processed_text =str
app = Flask(__name__)
listA =[]
listB =[]
@app.route('/')
def text_list(): 
    return render_template_string('''<!doctype html>
        <html>
        <head>
        </head>
        <body> 
        <form id = "form" method="POST" action="view">
        <label for="task">task:</label>
        <input type="text" id="userInput" name="userInput">
        <label for="description">description:</label>  
        <input type="text" id="userInput2" name="userInput2">   
        <button type="submit" id ="subButton" > submit</button>        
        </form>
        </body>
        </html>
        ''')

@app.route('/view', methods=['POST'])
def view():
    text = request.form['userInput']
    listA.append(text)
    text2 = request.form['userInput2']
    listB.append(text2)
    strTemp =  """
    <html>
    <head><title>List Example</title></head>
    <body>
    <form id = "form" method="POST" action="view">
    <label for="task">task:</label>
    <input type="text" id="userInput" name="userInput">
    <label for="description">description:</label>  
    <input type="text" id="userInput2" name="userInput2">   
    <button type="submit" id ="subButton" > submit</button>        
    </form>
    <dl>
     {% for task, description in zip(listA, listB) %}
        <dt>{{ task }}</dt>
     <dd>{{ description }}</dd>
     {% endfor %}
    </dl>
    </body>
    </html>
    """


    return render_template_string(strTemp ,listA=listA , listB = listB)

if __name__ == "__main__":
   app.jinja_env.globals.update(zip=zip)
   app.run(debug=True)