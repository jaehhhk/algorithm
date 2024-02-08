# 188p 사칙연산 클래스 직접 짜보기
#클래스 변수는 클래스로 만든 모든 객체에 공유됨(모두 같은 메모리 주소 -> id 함수로 확인 가능)

class FourCal:
    
    # 생성자 (Constructor) -> 객체가 생성될 때 자동으로 호출하는 메서드 
    # 객체에 초기값 설정해줘야 할 때 안전한 방법
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    # 두 숫자 받아옴
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        resut = self.first - self.second
        return resut
    
    def div(self):
        result = self.first / self.second
        return result
    
# 상속 -> 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경할 때
class MoreFourClass(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# 메서드 오버라이딩 + 상속
class SafeFourcal(FourCal):
    # 0으로 나눠주는 오류 보완하기 위해 기존 div 메서드 변경
    def div(self):
        if self.second == 0:
            return 0 
        else:
            return self.first / self.second