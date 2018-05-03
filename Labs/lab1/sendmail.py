# from gmail import GMail, Message
# gmail = GMail('Ducdz <duchn09.sic@gmail.com>','ngochoang123')
# msg = Message('Fuck u',to='<c4e.201708@gmail.com>',text='Hello')
# gmail.send(msg)
from random import choice
html_template='''<p>Em Ch&agrave;o Sếp ạ</p>
<p>H&ocirc;m nay trời đẹp, nắng l&ecirc;n cao. Em thức dậy thấy m&igrave;nh đau đầu qu&aacute;, đi kh&aacute;m b&aacute;c sĩ bảo em bị {{sickness}}, cho em nghỉ kh&ocirc;ng em l&acirc;y đấy.</p>
<p>Nh&acirc;n vi&ecirc;n y&ecirc;u qu&yacute; của sếp, ahihi :D</p>'''


sickness_list = ["HIV","EBOLA","H5N1","Quai bi"]
sickness = choice(sickness_list)
html_content = html_template.replace("{{sickness}}",sickness)
#
#
from gmail import GMail, Message
mail = GMail('duchn09.sic@gmail.com','ngochoang123')
msg = Message('Xin Nghi',to="c4e.201708@gmail.com",html=html_content)
mail.send(msg)
