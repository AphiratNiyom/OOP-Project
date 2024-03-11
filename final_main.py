import streamlit as st
import random
import string
from PIL import Image
import base64

bg_image_path = "img/Background.jpg"
with open(bg_image_path, "rb") as img_file:
    bg_image = img_file.read()
bg_image_base64 = base64.b64encode(bg_image).decode()
page_bg_img = f'''
    <style>
    
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image_base64}");
            background-size: cover;
            
        }}
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def generate_password(min_length, number=True, special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters = letters
  if number:
    characters += digits
  if special_characters:
    characters += special

  pwd = ""
  meets_criteria = False
  has_number = False
  has_special = False

  while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(characters)
    pwd += new_char

    if new_char in digits:
      has_number = True
    elif new_char in special:
      has_special = True

    meets_criteria = True
    if number:
      meets_criteria = has_number
    if special_characters:
      meets_criteria = meets_criteria and has_special

  return pwd

min_length = 12
has_number = True
has_special = True

st.title("สร้างรหัสผ่าน")

min_length = st.number_input("ความยาวขั้นต่ำ", min_value=1, max_value=100, value=min_length)
has_number = st.checkbox("ตัวเลข", value=has_number)
has_special = st.checkbox("ตัวอักษรพิเศษ", value=has_special)

if st.button("สร้างรหัสผ่าน"):
  pwd = generate_password(min_length, has_number, has_special)
  st.success(f"รหัสผ่านที่สร้าง: {pwd}")

st.markdown("""
  ### คำแนะนำ
  - รหัสผ่านที่ดีควรมีความยาวอย่างน้อย 12 ตัวอักษร
  - ควรมีตัวอักษรทั้งพิมพ์ใหญ่และพิมพ์เล็ก ตัวเลข และตัวอักษรพิเศษ
  - ไม่ควรใช้ข้อมูลส่วนตัว เช่น วันเกิด เบอร์โทรศัพท์ ในรหัสผ่าน
  - ควรเปลี่ยนรหัสผ่านเป็นประจำ
  """)
