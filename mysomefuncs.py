import time

class Ignore():
    """pass 대용. pass 또는 ...은 나중에 코딩하기 위해
    잠시 비워두었다는 느낌이 있어서 이와 구분하기 위해 만듦.
    이 클래스는 try-except문에서의 에러를 무시하고 다음 코드로 진행하는 등의
    상황에서 쓰면 된다."""
    pass


class TimeForFileName():
    """파일명에 넣기 위한 시간 관련 클래스"""
    def __init__(self):
        self.current_time = time.localtime(time.time())

    def currentTimeForFileName(self) -> str:
        """현재 시각을 년월일시분초 형태의 문자열로 반환."""
        strformat = '%Y%m%d%H%M%S'
        current_time_format = time.strftime(strformat, self.current_time)
        return current_time_format
    

if __name__ == '__main__':
    Ignore()