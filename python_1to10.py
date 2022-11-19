# print HelloWorld!
def Exam_01_helloWorld() :
    print("Hello World!")

# print ' 
## if you print Special symbols use \ 
def Exam_02_MarysCosmetics() :
    print("Mary\'s Cosmetics") 

# 신 said "도둑이야!" 
def Exam_03_Thief() :
    print("신씨가 소리쳤다 \"도둑이야!\" ")

# C:\Windows
def Exam_04_driveC() :
    print("C:\\Windows")

# 안녕하세요.\n만나서\t\t반갑습니다. \t \n 
def Exam_05_tab():
    print("안녕하세요./n 만나서/t/t반갑습니다. /t/n")

# use two arguments in print() 월요일, 일요일 
def Exam_06_printArguments():
    print("월요일", "일요일")

# use parameter print("", sep="")
# naver;kakao;sk;samsung
def Exam_07():
    print("naver", "kakao", "sk", "samsung", sep=";")

# naver/kakao/sk/samsung
def Exam_08():
    print("naver", "kakao", "sk", "samgsung", sep="/")

# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. 
# (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("", end="")
def Exam_09():
    print("first", end="11");print("second")

#5/3의 결과를 화면에 출력하세요.
def Exam_10():
    print(5/3)

Exam_01_helloWorld()
Exam_02_MarysCosmetics()
Exam_03_Thief()
Exam_04_driveC()
Exam_05_tab()
Exam_06_printArguments()
Exam_07()
Exam_08()
Exam_09()
Exam_10()