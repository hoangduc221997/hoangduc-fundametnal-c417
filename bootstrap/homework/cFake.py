from random import choice,randint
def male_name():
    h=['Nguyễn','Trần','Lê','Phạm','Hoàng','Huỳnh','Phan','Vũ','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Hà','Đào','Phùng','Trương','Nông','Phương','Cao','Mai','Đinh','Lương','Trịnh','Đoàn']
    d=['Anh','Tuấn','Hoàng','Phúc','Khải','Phương','Bá','Tuấn','Hữu','Hải','Nhân','Đức','Trọng','Phú','Minh','Xuân','Trung','Tuấn','Đinh','Khôi','Phước','Hoàng','Bảo','Thành','Lâm','Việt','Đức','Đăng','Nhật','Vinh','','']
    t=['Anh','Tuấn','Hoàng','Phúc','Khải','Phương','Nam','Dũng','Hữu','Hải','Nhân','Đức','Trọng','Phú','Minh','Dương','Trung','Tuấn','Nghĩa','Khôi','Phước','Hoàng','Bảo','Thành','Lâm','Việt','Đức','Nguyên','Nhật','Vinh','Phong','Chung','Quân','Quang','Quốc','Tuấn','Thành','Thiên','Thịnh','Sơn','Việt','Bách','Cường','Đạt','Hiếu','Huy','Hùng','Tuấn Anh']
    while True:
        ho = choice(h)
        dem = choice(d)
        ten = choice(t)
        if ho==dem or dem==ten:
            continue
        else:
            name= ho+' '+dem+' '+ten
            break
    return(name)
def female_name():
    h=['Nguyễn','Trần','Lê','Phạm','Hoàng','Huỳnh','Phan','Vũ','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Hà','Đào','Phùng','Trương','Nông','Phương','Cao','Mai','Đinh','Lương','Trịnh','Đoàn']
    d=['Mỹ','Khánh','Kiều','Phúc','Thùy','Mai','Hoa','Ngọc','Diễm','Hải','Bích','Nhã','Thúy','Minh','Xuân','Hoàng','Bảo','','Nhật','']
    t=['Anh','Ngọc','Châu','Uyên','Linh','Phương','Chi','Nhi','Thư','Hải','Thùy','Mai','Hoa','Ngọc','Minh','Dương','Hiền','Thủy','Quyên','Hà','Phước','Bích','Trâm','Khuê','Tú','Ngân','Trang','Thúy','Tuyết','Ngà','Oanh','Vân Anh','Quỳnh Anh','Phương Anh','Bảo Anh','Tâm','Bình','Ngọc Ánh']
    while True:
        ho = choice(h)
        dem = choice(d)
        ten = choice(t)
        if ho==dem or dem==ten:
            continue
        else:
            name= ho+' '+dem+' '+ten
            break
    return(name)
def tp():
    tps=['An Giang','Bà Rịa-Vũng Tàu','Bạc Liêu','Bắc Kạn','Bắc Giang','Bắc Ninh','Bến Tre','Bình Dương','Bình Định','Bình Phước','Bình Thuận','Cà Mau','Cao Bằng','Cần Thơ (TP)','Đà Nẵng (TP)','Đắk Lắk','Đắk Nông','Điện Biên','Đồng Nai','Đồng Tháp','Gia Lai','Hà Giang','Hà Nam','Hà Nội (TP)','Hà Tĩnh','Hải Dương','Hải Phòng (TP)','Hòa Bình','Hồ Chí Minh (TP)','Hậu Giang','Hưng Yên','Khánh Hòa','Kiên Giang','Kon Tum','Lai Châu','Lào Cai','Lạng Sơn','Lâm Đồng','Long An','Nam Định','Nghệ An','Ninh Bình','Ninh Thuận','Phú Thọ','Phú Yên','Quảng Bình','Quảng Nam','Quảng Ngãi','Quảng Ninh','Quảng Trị','Sóc Trăng','Sơn La','Tây Ninh','Thái Bình','Thái Nguyên','Thanh Hóa','Thừa Thiên - Huế','Tiền Giang','Trà Vinh','Tuyên Quang','Vĩnh Long','Vĩnh Phúc','Yên Bái']
    tp = choice(tps)
    return(tp)
def sdt():
    s=['096','097','098','086', '0162','0163', '0164', '0165', '0166', '0167', '0168', '0169','091', '094', '088', '0123', '0124', '0125', '0127', '0129','090', '093', '089', '0120', '0121', '0122', '0126', '0128']
    d=['0','1','2','3','4','5','6','7','8','9']
    sdt=choice(s)
    for i in range(7):
        t=choice(d)
        sdt=sdt+t
    return(sdt)

def cty():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url="http://s.cafef.vn/danh-sach-tap-doan-doanh-nghiep-lon.chn"
    conn = urlopen(url)
    raw_data=conn.read()
    text = raw_data.decode("utf8")

    soup = BeautifulSoup(text,"html.parser")

    table=soup.find("table",id='table_list')
    tr_list = table.find_all("tr")
    data=[]
    for tr in tr_list:
        list=[]
        td_list=tr.find_all("td")
        for td in td_list:
            a=td.a
            i=a.string
            list.append(i)
        if list:
            d=list[1].strip()
            data.append(d)
    cty=choice(data)
    return(cty)
def job():
    jobs=['Giám đốc','Phó Giám đốc','Chủ tịch Hội đồng quản trị','Trưởng phòng','Phó phòng','Kế toán','Nhân viên','Tạp vụ','Lao công','Bảo vệ','Chủ tịch Công đoàn','Thực tập','Quản lý','Thu ngân','Thư kí']
    job = choice(jobs)
    return(job)
def description():
    descriptions=['hút cỏ thay cơm','hút cần đụ nhau','nói không với chơi ma tuý, nói có với hút cỏ','Yêu màu tím, và thíc màu xanh','Nghiện bú trà sữa',' bú ku','hút cần thâm niên','Thành viên hội Cấn Thành']
    description = choice(descriptions)
    return(description)
def measurements():
    v1=randint(70,110)
    v2=randint(58,80)
    v3=randint(80,120)
    measurements=[v1,v2,v3]
    return(measurements)
def male_image():
    images=["https://image-ticketfly.imgix.net/00/02/54/05/34-og.jpg?w=500&h=500","https://i.ytimg.com/vi/KlUdCSJj7ow/hqdefault.jpg","https://i.ytimg.com/vi/J7DcZSGWrUc/maxresdefault.jpg","https://terrifictop10.files.wordpress.com/2015/06/morgan-freeman-marijuana-101.jpg","http://cdn.ebaumsworld.com/thumbs/2012/06/28/082753/82627716/bong.jpg"]
    image = choice(images)
    return(image)
def female_image():
    images=["http://clutchmagonline.com/wp-content/uploads/2013/11/tumblr_mhcifvyO2O1s03hsho1_5001.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDsgqHoib5D0IPmBMTj5yi8pFXiKBp0MlmxmIrxMb0Dya4kJUB","https://i.pinimg.com/236x/35/e5/b6/35e5b62b4904f2f40772204382f6fe88--bad-habits-cannabis.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTySfF28BYSAJlPS5mZ-vT7AdOg6R-kUGu6NoBOpUy3x6Vl00am","http://www.reactiongifs.com/r/gmatok.gif","http://www.thesmokersclub.com/blog/wp-content/uploads/2016/04/Screen-Shot-2016-04-26-at-8.14.27-AM-750x420.png"]
    image = choice(images)
    return(image)
