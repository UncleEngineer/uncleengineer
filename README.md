# Uncle Engineer (uncleengineer)



สวัสดีจร้าาาาทุกคน ไลบรารี่นี้เป็นโปรแกรมที่ลุงเขียนขึ้นมาเพื่อเผยแพร่เป็นวิทยาทาน
ให้ทุกคนได้ศึกษาภาษา Python แบบง่ายๆ อยากให้คนไทยเก่งเทีบยเท่าต่างชาติ ช่วย
กันพัฒนาประเทศเราให้ก้าวหน้า พึ่งตัวเองดีที่สุด ถ้ามัวแต่รอรัฐบาลสนับสนุนก็คงอีก 1000 ปี 555

เวอร์ชั่นนี้มีอะไรบ้าง

  - เช็คราคาหุ้นไทย 
  - อื่นๆ ลุงจะทยอยลงเรื่อยๆนะจ๊ะ

# เช็คราคาหุ้นไทย (thaistock())

  - เช็คราคาแบบเรียลไทม์
  - เช็คราคาเปลี่ยนกี่บาท
  - เช็คเปอร์เซ็นเปลี่ยนแปลง
  - เช็คว่าราคาอัพเดตตอนไหน





### วิธีติดตั้งแสนง่าย

ไปกดไลค์เพจ ก่อน [ลุงวิศวกร สอนคำนวณ](https://www.facebook.com/UncleEngineer)  ฮ่าาา ไม่บังคับ (กดไลค์หน่อยๆ 555)

เราจะติดตั้งผ่านเจ้า pip

```sh
pip install uncleengineer
```

ง่ายไหมล่ะ

วิธีใช้ก็ง่ายมาก
- เปิด Python แล้วพิพม์ตามนี้เลย

```sh
from uncleengineer import thaistock

#เช็คราคาหุ้นลุงเปรมหน่อย 
#55 (ขอโต้ดคับลุงเปรม ผมช่วยโปรโมทบริษัทให้)

ITD = thaistock('ITD') 
print(ITD)
# จะได้ ['ITD ', '2.16', '0.00', '0.00%', '17/05/2019 14:22:59']
# ['ชื่อหุ้น 'ราคา', 'ราคาเปลี่ยนกี่บาท', 'ราคาเปลี่ยนกี่เปอร์เซ็น', 'อัพเดตเมื่อ']
```

### Plugins

แวะเข้าไปเยี่ยมชมกันได้ แหล่งกบดานเรามีสอนหลายวิชา

| วิชาที่เปิดสอน | ลิ้งค์ |
| ------ | ------ |
| เช็คตาราง |http://uncle-engineer.com/ |
| Automated Bot with Python | http://uncle-engineer.com/python |
| Basic Ptyhon + Web Scraping | http://uncle-engineer.com/python/web|
| Basic Python GUI + Google Firebase| http://uncle-engineer.com/python/gui|
| Hacking with Python | http://uncle-engineer.com/python/hacking |
| อ่านบทความใน Medium  | https://medium.com/@UncleEngineer|
| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer] |

### เจอกันตอนถัดไป...ในเพจ "ลุงวิศวกร สอนคำนวณ"
