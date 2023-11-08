from GUI import MyWindow, QApplication, app
import sys

#애플리케이션의 메인 창인 MyWindow 클래스의 인스턴스를 생성합니다. 이 때, MyWindow 클래스의 생성자(__init__ 메서드)가 호출됩니다.
window = MyWindow()

#window.show(): 메인 창을 화면에 표시합니다. 이 메서드를 호출하지 않으면 창이 숨겨진 상태로 시작합니다.
window.show()

#(app.exec_()): PyQt5 애플리케이션의 이벤트 루프를 실행합니다. 이 루프는 사용자의 상호 작용(버튼 클릭, 메뉴 선택 등)을 처리하고 애플리케이션을 실행합니다. 
#app.exec_()는 애플리케이션의 실행을 시작하고, 이벤트 루프가 종료되면 sys.exit()를 사용하여 애플리케이션을 종료합니다.
sys.exit(app.exec_())
