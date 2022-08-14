from flask import Flask , render_template ,url_for , request
import json , requests
from datetime import datetime , date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
d2 = today.strftime("%B %d, %Y")

with open('config.json','r') as c:
    param = json.load(c)["param"]
    
def get_weather(city,api_key):
    api_url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)
    r=requests.get(api_url)
    return r.json()

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET'])
def home():
    return render_template("search.html")

@app.route('/result', methods=['GET','POST'])
def results():
    city = request.form['city_name']
    data=get_weather(city,param['api_key'])

    temp=(data["main"]["temp"])
    tempr=(temp)
    city_name=data["name"]
    count=data["sys"]["country"]
    time=current_time
    dat=d2
    des= (data['weather'][0]['description']).capitalize()
    return render_template('index.html',temp=temp,param=param,city_name=city_name,count=count,time=time,tempr=tempr,dat=dat,des=des)


if __name__=='__main__':
    app.run(debug=True)
   




    
