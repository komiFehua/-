from flask import Flask, render_template
from pyvis.network import Network
app = Flask(__name__)


def create_graph():
    net = Network(notebook=True, cdn_resources="remote")
    net.add_nodes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], #есди будешь добовлять имена то добавь тут еще одну цифру
    #можешь сама написать имена заместо этих и можешь добавть 
    # имена добовляются ,"имя"
            label=["я", "Мать", "Отец", "Бабука ","Дедушка ", "Бабука ","Дедушка ","Прадед","Прабабка","Прадед","Прабабка","Прадед","Прабабка","Прадед","Прабабка"],
    #есди будешь добовлять имена то 
            color=["#a80000", "#94A88A", "#7bd3da","#65c432","#9fb909","#00ff4c","#0051ff","#6284cf","#62cf93","#626dcf","#cf6283","#bd62cf","#2d515c","#2d5c3f","#5b5c2d"]) 
    #код цвето можешь кайти в гугле и обезптельно с хештегом

    net.add_edges([(1, 2), (1, 3), (2, 4), (2, 5), (3,6), (3,7),(4,8),(4,9),(5,10),(5,11),(6,12),(6,13),(7,14),(7,15)])


    net.show("templates/index.html")


@app.route("/")
def index():
    create_graph()
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
