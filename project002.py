from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    file = open("/home/pi/iot_project/data.txt", 'r')
    data = file.readline()
    first = int(data)
    file.close()
    file005 = open("/home/pi/iot_project/data_dht.txt", 'r')
    data005 = file005.readline()
    data_dht = int(data005)
    file005.close()
    return render_template('index.html', data001 = first, data_dht=data_dht )

@app.route('/key', methods=['POST'])
def key():
    data002 = request.form['key']
    print(data002)
    file002 = open("/home/pi/iot_project/data.txt", 'w')
    file002.write(data002)
    file002.close()
        
if __name__ == "__main__":
   app.run(host="172.30.1.25", port = "8080")