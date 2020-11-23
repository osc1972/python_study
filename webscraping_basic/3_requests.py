import requests
res = requests.get("http://naver.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
print("응답코드 : ", res.status_code) # 200 이면 정상

# 방법 1
# if res.status_code == requests.codes.ok: # requests.codes.ok = 200
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# 방법 2 - 문제가 생기면 바로 오류로 표현됨.
# res.raise_for_status()
# print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)