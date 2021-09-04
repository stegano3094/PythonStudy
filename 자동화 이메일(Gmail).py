#! python3


'''
구글 이메일 자동화를 하기 위해서 몇 가지 세팅이 필요하다

먼저 Gmail에 접속하여 메일 설정 > 모든 설정 보기 > 전달 및 POP/IMAP >
IMAP 액세스 부분에 IMAP 사용으로 한 뒤 변경사항 저장 버튼을 누른다.

두 번째로 https://myaccount.google.com/lesssecureapps에 들어가서 액세스를
허용해야 한다. (단, 2단계 보안 계정이라면 사용할 수 없음)

세 번째로 중요 보안 메일이 날라오는데 본인 활동 확인임을 확인하면 된다.



동일한 폴더에 메모장을 열고 아래 코드 2줄을 입력한다.
GMAIL_ID = "이메일@gmail.com"
GMAIL_PW = "비밀번호"

저장할 때 settings.py 로 확장자까지 변경하여 저장하여 import 가능하도록 한다.

정상적으로 파일을 작성했는지 확인하는 코드
import settings
print(settings.GMAIL_ID, settings.GMAIL_PW)



우리가 사용할 코드는 아래와 같음
from_users : 자신의 이메일 주소 (자기 자신이 아니라면 전송 안 됌)
to_users : 송신할 이메일 주소 (여러명일 경우 리스트로 작성 ['a.~', 'b.~']
cc_users : 참조로 송신할 이메일, to_users와 동일한 포멧
subject : 이메일 제목
attachment : 첨부파일 (동일한 디렉터리에 있는게 좋음, ex:'test.csv')
text : 이메일 본문
text_format : 포멧으로 html, plain을 선택할 수 있음. plain은 일반 텍스트

email_temp(from_user, to_users, cc_users, subject, attachment, text, text_format="html", smtp_server="smtp.gmail.com", smtp_port=587)
'''


# http://pythonstudy.xyz/python/article/508-%EB%A9%94%EC%9D%BC-%EB%B3%B4%EB%82%B4%EA%B8%B0-SMTP

# 자동화로 이메일 주고 받기
import smtplib
from email.header import Header
from email.mime.base import MIMEBase  # MIME 프로토콜 활용
from email.mime.text import MIMEText  # MIME 프로토콜 활용
from email.mime.multipart import MIMEMultipart  # MIME 프로토콜 활용
from email import utils
from email import encoders
from email.utils import COMMASPACE
import os

import settings

def email_temp(from_user, to_users, cc_users, subject, attachment, text, text_format="html", smtp_server="smtp.gmail.com", smtp_port=587):
    msg = MIMEMultipart('multipart')
    msg['FROM'] = from_user
    msg['To'] = COMMASPACE.join(to_users)
    msg['Cc'] = COMMASPACE.join(cc_users)
    msg['Subject'] = Header(s=subject, charset='utf-8')
    msg['Date'] = utils.formatdate(localtime=1)

    part = MIMEText(text, text_format)
    msg.attach(part)

    if attachment:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(os.path.basename(attachment), "rb").read())
        encoders.encode_base64(part)

        part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(attachment)
        msg.attach(part)

    print(msg.as_string())
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)  # SMTP 연결
        try:
            server.ehlo()  # 설정된 SMTP가 정상 동작하는지 확인하기 위해 Hello 메세지를 송신함
            server.starttls()  # TLS 프로토콜(=SSL)로 송신할 데이터를 암호
            server.login(settings.GMAIL_ID, settings.GMAIL_PW)  # Gmail에 로그인
            server.sendmail(msg['FROM'], [msg['To'], msg['Cc']], msg.as_string())  # 메일 전송
            print("[OK] send mail")
        except:
            print("[Error] Fail to send mail")
        finally:
            server.quit()  # smtp 연결 종료
    except:
        print("[Error] Fail to connect")
        return False


from_user = settings.GMAIL_ID
to_users = [settings.GMAIL_ID]
cc_users = [settings.GMAIL_ID]
subject = "테스트입니다."
attachment = 'test1.xlsx'
text = '안녕하세요.'
email_temp(from_user, to_users, cc_users, subject, attachment, text, 'plain')


'''
MIME (Multi-purpose Internet Mail Extensions)
SMTP 프로토콜은 ASCII 코드로만 전송이 가능하다.
MIME에 정보(한글, 첨부파일 등)를 넣어 ASCII로 변환하여 SMTP로 전송함
'''
