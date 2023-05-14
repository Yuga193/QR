import qrcode
import cv2
import json
import matplotlib.pyplot as plt
from urllib.parse import unquote

# 利用者が自分のプロフィールを入力
print("Please enter your profile information.")
name = input("名前を入力してね:")
age = input("年齢を教えて: ")
city = input("出陳地はどこ？: ")

# 入力された情報からプロフィールを作成
user_profile = {
    "name": name,
    "age": age,
    "city": city,
    # その他の項目...
}

# プロフィール情報を整形して作成
formatted_profile = f"{user_profile['name']} {user_profile['age']} {user_profile['city']}"

# QRコードを生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(formatted_profile)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

# QRコードを画面に表示
plt.imshow(img, cmap='gray')
plt.show()

# 別のQRコードを読み取るためのプロフィール情報を入力
other_profile_data = input("Enter the profile information from the other QR code: ")

# QRコードから読み取ったプロフィール情報を表示
print("Other Profile Information: ", other_profile_data)

# プロフィール情報をURLデコード
other_profile_json = unquote(other_profile_data)

# JSON文字列を辞書に変換
other_profile = json.loads(other_profile_json)

# プロフィール情報を整形して表示
formatted_other_profile = f"{other_profile['name']} {other_profile['age']} {other_profile['city']}"
print("Formatted Other Profile Information: ", formatted_other_profile)

matching_items = {k: user_profile[k] for k in user_profile if user_profile.get(k) == other_profile.get(k)}

print("Matching items: ", matching_items)