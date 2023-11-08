"""사용자 정의 예외 모음"""

class CurrentDirectoryNotSetted(Exception):
    def __init__(self):
        error_message = """{}: 현재 루트 폴더 경로를
        나타내는 속성과 os.getcwd()가 서로 다릅니다.
        os.chdir() 실행을 어디선가 하지 않고 놓친 것 같습니다."""

        # 클래스.__name__ => 클래스 이름을 문자열로 반환.
        error_message = error_message.format(CurrentDirectoryNotSetted.__name__)
        super().__init__(error_message)


class NotSatisfiedAllIfContiditions(Exception):
    def __init__(self):
        error_message = """{}: 
        함수 내 조건문들 중 만족되는 조건문이 없습니다.
        """.format(NotSatisfiedAllIfContiditions.__name__)
        super().__init__(error_message)


class QtWidgetNoneError(Exception):
    def __init__(self):
        error_message = """{}: 
        Qt 위젯이 설정되지 않았습니다.""".format(QtWidgetNoneError.__name__)
        super().__init__(error_message)

    def setTryExcept(
            self,
            qt_obj,
            error_method_name: str
            ):
        """qt_obj: Qt 위젯 객체
        error_method_name: 에러가 발생할 것으로 예상되는 함수 또는 메서드 이름"""
        try:
            if qt_obj is None:
                raise QtWidgetNoneError()
        except QtWidgetNoneError as e:
            print(e)
            print("에러 발생 메서드(함수): ", error_method_name)
        

if __name__ == '__main__':
    try:
        raise CurrentDirectoryNotSetted()
    except CurrentDirectoryNotSetted as e:
        print(e)