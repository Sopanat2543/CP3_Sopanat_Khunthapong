'''
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
'''
# ใส่ข้อมูล Username & Password
Username = input("Enter your username: ")
Password = input("Enter your password: ")

# Check if both username and password are correct
if Username == "Sopanat" and Password == "Ex8-CompletePython3":
    print("Login successful!")
    # แสดงรายการสินค้า
    print("ยินดีต้อนรับ คุณ", Username)
    print("แสดงรายการสินค้า")
    print("Apple ราคา 10 บาท ต่อ กิโลกรัม")
    print("Orange ราคา 20 บาท ต่อ กิโลกรัม")
    print("Mango ราคา 30 บาท ต่อ กิโลกรัม")
    
    # ระบุน้ำหนักสินค้า
    print("กรณีไม่ได้ซื้อสินค้า กรุณาใส่ 0 ")
    น้ำหนักสินค้า1 = int(input("กรุณาชั่งน้ำหนัก Apple: "))
    น้ำหนักสินค้า2 = int(input("กรุณาชั่งน้ำหนัก Orange: "))
    น้ำหนักสินค้า3 = int(input("กรุณาชั่งน้ำหนัก Mango: "))
    
    # คำนวนราคาสินค้า
    print("สรุปรายการการสั่งซื้อสินค้า")
    print("Apple:", น้ำหนักสินค้า1, "ราคาสินค้า", น้ำหนักสินค้า1 * 10, "บาท")
    print("Orange:", น้ำหนักสินค้า2, "ราคาสินค้า", น้ำหนักสินค้า2 * 20, "บาท")
    print("Mango:", น้ำหนักสินค้า3, "ราคาสินค้า", น้ำหนักสินค้า3 * 30, "บาท")
    print("สรุปราคารวมของรายการสั่งซื้อทั้งหมด", (น้ำหนักสินค้า1 * 10) + (น้ำหนักสินค้า2 * 20) + (น้ำหนักสินค้า3 * 30), "บาท")
    print("---------------------------------------------------")
    print("ขอบคุณลูกค้าทุกท่าน ที่พึงพอใจในบริการของเรา")

# Username & Password ไม่ถูกต้อง
else:
    print("กรุณาสมัครสมาชิกก่อนการใช้งานระบบ")
