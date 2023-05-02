import openai
import time
import openpyxl
# API 키

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

model = "gpt-3.5-turbo"

messages = []
# 엑셀 파일
wb = openpyxl.Workbook()
# 워크시트
ws = wb.create_sheet('문장모음')
ws['A1'] = '문장'
ws['B1'] = '정답'
k=2
for i in range(5):
    #1 보기없는 버전
    content = "To study English,make 5 TOEIC English problems using the blanks.with answer for example problem is The company's goal is to _______ market share in the next fiscal year.Answer: increase"

    messages.append({"role":"user", "content":content})
    time.sleep(20)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
# chat_response 는 str 변수이다.
    chat_response = chat_response.replace('Answer:', '.').replace('1.', '.').replace('2.', '.').replace('3.', '.').replace('4.', '.').replace('5.', '.')
    print(chat_response)
    for j in range(5):
        ws['A'+str(k)] = chat_response.split('.')[j*3+1]
        ws['B'+str(k)] = chat_response.split('.')[3*(j+1)].replace(' ', '').replace('\n', '')
        k = k + 1
    #print(chat_response.split('.')[4])
    messages.append({"role": "assistant", "content": chat_response})
    wb.save('/Users/KJH/Documents/GitHub/Capstone_6/excel/Sentence.xlsx')


