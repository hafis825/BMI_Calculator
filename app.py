from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height']) / 100  # convert cm to m
            bmi = weight / (height * height)
            
            if bmi < 18.5:
                category = "น้ำหนักน้อย / ผอม"
            elif bmi < 23:
                category = "ปกติ"
            elif bmi < 25:
                category = "ท้วม / โรคอ้วนระดับ 1"
            elif bmi < 30:
                category = "อ้วน / โรคอ้วนระดับ 2"
            else:
                category = "อ้วนมาก / โรคอ้วนระดับ 3"
                
        except ValueError:
            return "กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น"
            
    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)