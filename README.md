# BMI Calculator Web Application

เว็บแอพพลิเคชันสำหรับคำนวณค่าดัชนีมวลกาย (BMI) พัฒนาด้วย Python และ Flask

## คุณสมบัติ
- คำนวณค่า BMI จากน้ำหนักและส่วนสูง
- แสดงผลการประเมินตามเกณฑ์มาตรฐานสำหรับคนเอเชีย
- รองรับการแสดงผลภาษาไทย
- ใช้งานง่ายผ่านหน้าเว็บ

## การติดตั้งและใช้งาน

### วิธีที่ 1: รันด้วย Python
```bash
# 1. Clone repository
git clone https://github.com/hafis825/BMI_Calculator.git
cd BMI_Calculator

# 2. สร้าง virtual environment
python -m venv venv
source venv/bin/activate  # สำหรับ Linux/Mac
# หรือ
venv\Scripts\activate  # สำหรับ Windows

# 3. ติดตั้ง dependencies
pip install -r requirements.txt

# 4. รันแอพพลิเคชัน
python app.py
```

### วิธีที่ 2: รันด้วย Docker
```bash
# 1. Build Docker image
docker build -t bmi-calculator .

# 2. รัน container
docker run -p 5000:5000 bmi-calculator
```

เข้าใช้งานที่ http://localhost:5000

## โครงสร้างโปรเจกต์
```
├── app.py              # ไฟล์หลักของแอพพลิเคชัน
├── templates/          # โฟลเดอร์เก็บไฟล์ HTML
│   └── index.html     # หน้าเว็บหลัก
├── requirements.txt    # รายการ dependencies
├── Dockerfile         # ไฟล์สำหรับสร้าง Docker image
└── README.md          # เอกสารอธิบายโปรเจกต์
```

## เทคโนโลยีที่ใช้
- Python 3.9
- Flask 2.0.1
- Docker
- Gunicorn

## License
MIT License
