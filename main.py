import re

datas = [
    "1234567890",
    "(123)-456-7890",
    "9876543210",
    "(987)-654-3210",
    "not_a_number",
    "123-456-7890",  # bu regexine uymaz
    "123456789",  # eksik hane
    "(12)-3456-7890",  # yanlış format
    "0001112222",
    "(000)-111-2222",
    "abcdefghij",  # tamamen yanlış
]
mails = [
    "user123@a.com",
    "john.doe@",
    "my_email123@",
    "test.user+name@",
    "user-name@",
    "user.name+tag@",
    "invalidemail",  # içinde @ yok, eşleşmez
    "another.one@domain",  # bu regexe göre sadece 'another.one@' kısmı yakalanır
    "noatsign.com",  # eşleşmez
    "@missingusername",  # eşleşmez çünkü kullanıcı adı eksik
]

emailPattern = re.compile("[a-zA-Z0-9_.+-]+@*[a-zA-Z0-9-]+\.[a-zA-Z0-9]")
phoneNumpattern = r"\d{10}|\(\d{3}\)-\d{3}-\d{4}"
for data in datas:
    if re.match(phoneNumpattern, data):
        print(data, "basarili")
    else:
        print(data, "basarisiz")

print("_________________")

for mail in mails:
    if re.match(emailPattern, mail):
        print(mail, "suceed")
    else:
        print(mail, "fail")
