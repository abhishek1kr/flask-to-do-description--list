import flask


def Flask(__name__):
    pass


app = Flask(__name__)

listA = []
listB = []

@app.route('/')
def text_list():
    return render_template_string('''
    <!doctype html>
    <html>
    <head>
        <style>
            :root {
                --bg-color: #f9f9f9;
                --text-color: #000;
                --task-bg-color: #fff;
            }
            body.dark-mode {
                --bg-color: #333;
                --text-color: #f9f9f9;
                --task-bg-color: #444;
            }
            body {
                background-color: var(--bg-color);
                color: var(--text-color);
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
                background-color: var(--task-bg-color);
                margin-bottom: 20px;
            }
            #userInput, #userInput2 {
                width: 100%;
                margin-bottom: 15px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
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
                max-width: 800px;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: var(--task-bg-color);
                overflow: hidden;
            }
            .task-container {
                display: flex;
                align-items: flex-start;
            }
            .task-title-container {
                flex: 1;
                display: flex;
                justify-content: flex-end;
                margin-right: 10px;
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
                word-wrap: break-word;
                max-width: 300px;
                overflow-wrap: break-word;
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
                max-height: 100px;
                overflow-y: auto;
                word-wrap: break-word;
            }
            .share-button {
                margin-top: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .share-button:hover {
                background-color: #218838;
            }
            #darkModeToggle {
                position: fixed;
                top: 10px;
                right: 10px;
                padding: 10px;
                border-radius: 50%;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <button id="darkModeToggle" onclick="toggleDarkMode()">🌙</button>
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
                            <button class="share-button" onclick="shareTask('{{ task }}', '{{ description }}')">Share</button>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
        <script>
            function toggleDarkMode() {
                document.body.classList.toggle('dark-mode');
            }

            function shareTask(task, description) {
                if (navigator.share) {
                    navigator.share({
                        title: task,
                        text: description
                    }).then(() => {
                        console.log('Task shared successfully');
                    }).catch((error) => {
                        console.error('Error sharing task', error);
                    });
                } else {
                    alert('Sharing not supported on this browser');
                }
            }
        </script>
    </body>
    </html>
    ''', listA=listA, listB=listB)

@app.route('/', methods=['POST'])
def view():
    text = request.form['userInput']
    listA.append(text)
    text2 = request.form['userInput2']
    listB.append(text2)
    return render_template_string(text_list(), listA=listA, listB=listB)

if __name__ == "__main__":
    app.jinja_env.globals.update(zip=zip)
    app.run(debug=True)
