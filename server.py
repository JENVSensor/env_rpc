# 데이터 전송값 디버깅 테스트용
from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    # 여기에서 데이터를 처리합니다 (예: 출력, 저장 등)
    print(data)
    return "Data received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)