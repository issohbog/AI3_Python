# input() : 입력 함수 
A = input("A : ")
B = input("B : ")

# input 함수는 값을 입력받아 문자열(str)로 가져온다 

print("A + B : " + (A + B))


A = int(A)
B = int(B)
# sep의 기본값은 " " 한칸 띄어쓰기 
# 문자열을 나열할 시 한칸 자동으로 띄어써지는데 
# sep=""로 하면 두 문자의 구분자를 띄어쓰기를 제거해준다. 

print("A + B : ", (A + B), sep="")
