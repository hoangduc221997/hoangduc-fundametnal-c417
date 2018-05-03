from random import choice
from gmail import GMail, Message
import datetime *
template='''<p>Em Ch&agrave;o Sếp ạ</p>
<p>H&ocirc;m nay trời đẹp, nắng l&ecirc;n cao. Em thức dậy thấy m&igrave;nh đau đầu qu&aacute;, đi kh&aacute;m b&aacute;c sĩ bảo em bị {{sickness}}, cho em nghỉ kh&ocirc;ng em l&acirc;y đấy.</p>
<p>Nh&acirc;n vi&ecirc;n y&ecirc;u qu&yacute; của sếp, ahihi :D</p>'''


sick_list = ["HIV","EBOLA","H5N1","Quai bi"]
sick = choice(sick_list)
html_content = html_template.replace("{{sickness}}",sick)

gmail = Gmail("duongtom.221@gmail.com","ngochoang123")

while True:
    time = datetime.datetime.now()
    if time.hour == 7 and time.minute > 0:
        msg = Message('Don xin nghi om', to='duchn09.sic@gmail.com',html=html_content)
        mail.send(msg)
        break
