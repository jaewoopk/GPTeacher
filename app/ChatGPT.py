import openai
import time
import openpyxl
# API 키

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

model = "gpt-3.5-turbo"

messages = []
# 엑셀 파일

fpath = '/Users/KJH/Documents/GitHub/Capstone_6/excel/Sentence.xlsx'
wb = openpyxl.load_workbook(fpath)
# 워크시트
ws = wb['문장모음']
k = 1
for i in range(10):
    #1 보기없는 버전
    content = "To study English,make 10 TOEIC problems using blank.with answer"

    messages.append({"role":"user", "content":content})
    time.sleep(10)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
# chat_response 는 str 변수이다.
    chat_response = chat_response.replace('Answer:', '.').replace('-','.')
    for N in range(10):
        chat_response = chat_response.replace(str(N+1)+'.', '.')
    print(chat_response)
    for j in range(10):
        ws['A'+str(k)] = chat_response.split('.')[j*3+1]
        ws['B'+str(k)] = chat_response.split('.')[3*(j+1)].replace(' ', '').replace('\n', '')
        k = k + 1
    #print(chat_response.split('.')[4])
    messages.append({"role": "assistant", "content": chat_response})
    wb.save('/Users/KJH/Documents/GitHub/Capstone_6/excel/Sentence2.xlsx')


