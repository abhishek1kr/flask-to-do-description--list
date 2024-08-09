from flask import Flask, render_template_string, request

app = Flask(__name__)
# open a file in append mode
# if the file is empty then initialize listA and listB
listA = []
listB = []
# if the file is not empty
# load listA and listB from the file
@app.route('/')
def text_list():
    return render_template_string('''
    <!doctype html>
    <html>
    <head>
        <style>
            body {
                overflow-y: scroll;
                overflow-x: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
                height: 100vh;
                margin: 0;
                padding-top: 50px;
                font-family: Arial, sans-serif;
            }
            #form {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 70%;
                max-width: 400px;
                border: 1px solid #ccc;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: #f9f9f9;
                margin-bottom: 20px;
            }
            #userInput, #userInput2 {
                width: 100%;
                margin-bottom: 15px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box; /* Ensures padding and border are included in width */
            }
            #userInput {
                height: 40px;
            }
            #userInput2 {
                height: 80px;
            }
            #subButton {
                width: 50%;
                padding: 10px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            #subButton:hover {
                background-color: #0056b3;
            }
            .task-box {
                width: 70%;
                max-width: 800px; /* Adjusted to allow more space for content */
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: #fff;
                overflow: hidden; /* Ensures content does not overflow */
            }
            .task-container {
                display: flex;
                align-items: flex-start; /* Align items to the top */
            }
            .task-title-container {
                flex: 1;
                display: flex;
                justify-content: flex-end;
                margin-right: 10px; /* Space between task and description */
            }
            .task-title {
                font-weight: bold;
                font-size: 18px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: right;
                word-wrap: break-word; /* Breaks long words to fit within box */
                max-width: 300px; /* Set a maximum width */
                overflow-wrap: break-word; /* Breaks long words */
            }
            .task-desc-container {
                flex: 2;
                display: flex;
                flex-direction: column;
            }
            .task-desc {
                font-size: 16px;
                color: #555;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-height: 100px; /* Set a maximum height */
                overflow-y: auto; /* Scrollbar for overflow content */
                word-wrap: break-word; /* Breaks long words to fit within box */
            }
        </style>
    </head>
    <body>
        <form id="form" method="POST">
            <label for="task">Task:</label>
            <input type="text" id="userInput" name="userInput" placeholder="Enter your task here">
            <label for="description">Description:</label>
            <textarea id="userInput2" name="userInput2" placeholder="Enter the description here"></textarea>
            <button type="submit" id="subButton">Add</button>
        </form>
        <div id="taskList">
            {% for task, description in zip(listA, listB) %}
                <div class="task-box">
                    <div class="task-container">
                        <div class="task-title-container">
                            <div class="task-title">{{ task }}</div>
                        </div>
                        <div class="task-desc-container">
                            <div class="task-desc">{{ description }}</div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </body>
    </html>
    ''')

@app.route('/', methods=['POST'])
def view():
    text = request.form['userInput']
    listA.append(text)
    text2 = request.form['userInput2']
    listB.append(text2)
    # append lists in file
    strTemp = """
    <!doctype html>
    <html>
    <head>
        <style>
            body {
                overflow-y: scroll;
                overflow-x: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
                height: 100vh;
                margin: 0;
                padding-top: 50px;
                font-family: Arial, sans-serif;
            }
            #form {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 70%;
                max-width: 400px;
                border: 1px solid #ccc;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: #f9f9f9;
                margin-bottom: 20px;
            }
            #userInput, #userInput2 {
                width: 100%;
                margin-bottom: 15px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box; /* Ensures padding and border are included in width */
            }
            #userInput {
                height: 40px;
            }
            #userInput2 {
                height: 80px;
            }
            #subButton {
                width: 50%;
                padding: 10px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            #subButton:hover {
                background-color: #0056b3;
            }
            .task-box {
                width: 70%;
                max-width: 800px; /* Adjusted to allow more space for content */
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: #fff;
                overflow: hidden; /* Ensures content does not overflow */
            }
            .task-container {
                display: flex;
                align-items: flex-start; /* Align items to the top */
            }
            .task-title-container {
                flex: 1;
                display: flex;
                justify-content: flex-end;
                margin-right: 10px; /* Space between task and description */
            }
            .task-title {
                font-weight: bold;
                font-size: 18px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: right;
                word-wrap: break-word; /* Breaks long words to fit within box */
                max-width: 300px; /* Set a maximum width */
                overflow-wrap: break-word; /* Breaks long words */
            }
            .task-desc-container {
                flex: 2;
                display: flex;
                flex-direction: column;
            }
            .task-desc {
                font-size: 16px;
                color: #555;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-height: 100px; /* Set a maximum height */
                overflow-y: auto; /* Scrollbar for overflow content */
                word-wrap: break-word; /* Breaks long words to fit within box */
            }
        </style>
    </head>
    <body>
        <form id="form" method="POST">
            <label for="task">Task:</label>
            <input type="text" id="userInput" name="userInput" placeholder="Enter your task here">
            <label for="description">Description:</label>
            <textarea id="userInput2" name="userInput2" placeholder="Enter the description here"></textarea>
            <button type="submit" id="subButton">Add</button>
        </form>
        <div id="taskList">
            {% for task, description in zip(listA, listB) %}
                <div class="task-box">
                    <div class="task-container">
                        <div class="task-title-container">
                            <div class="task-title">{{ task }}</div>
                        </div>
                        <div class="task-desc-container">
                            <div class="task-desc">{{ description }}</div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(strTemp, listA=listA, listB=listB)

if __name__ == "__main__":
    app.jinja_env.globals.update(zip=zip)
    app.run(debug=True)
