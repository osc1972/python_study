# import travel.thailand
# # import travel.thailand.ThailandPackage # 이렇게는 사용 불가. 틀린 방법
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *

# __init__.py 파일 (__all__)
# 외부에서 모듈 호출
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 파일 위치 찾기
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))