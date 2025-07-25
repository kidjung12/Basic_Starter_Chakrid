"""
people = 0
hours = 0
total = 1
general_cost_per_hour = 50
private_cost_per_hour = 60
general = {'table_1' : 0 , 'table_2' : 0 , 'table_3' : 0 , 'table_4' : 0 }
private = {'table_5' : 0 , 'table_6' : 0 , 'table_7' : 0 , 'table_8' : 0 }



def zone_select():
    global zone
    zone = input('')
    if zone == 'private':
        for i in private.items():
            print(f"{private[]}")
    elif zone == 'general':
        for i in general:
            print(f"{general[]}")

def table_select():
    table = input('')
    #เลือกkeyไหนให้เปลี่ยนค่าเป็น 1

    if #โต๊ะในเลขเป็น 1:
        print("ถูกจองแล้ว")
        return False
    else:
        print("จองสำเร็จ")
        return True
    
def check_in():
    checkin = int(input(""))
    checkout = int(input(""))
    if checkin == 0 and checkin <= 24:
        hours = checkout - checkin
        return True
    else:
        print("คุณใส่เวลาผิด")
        return False

def timecount(): #คำนวนเวลาราคาเพิ่มตาม ชั่วโมง * ราคาต่อชั่วโมง
    if zone == 'private':
        total = hours * private_cost_per_hour
    elif zone == 'general':
        total = hours * general_cost_per_hour


def main():
#เว้นไว้ก่อน
main()

print(f"จำนวนคน: {people} อยากให้แบ่งzoneด้วย{บอกว่าอยู่zoneไหน} จำนวนชั่วโมง: {hours} ราคา: {total}")
"""


people = 0
hours = 0
total = 1
zone = ""
table = ""

general_cost_per_hour = 50
private_cost_per_hour = 60

general = {'1': 0, '2': 0, '3': 0, '4': 0}
private = {'5': 0, '6': 0, '7': 0, '8': 0}


def zone_select():
    global zone
    zone = input("เลือกโซน (general/private): ")
    if zone == 'private':
        for table_name, status in private.items():
            print(f"Table_{table_name}: {'ว่าง' if status == 0 else 'ถูกจองแล้ว'}")
    elif zone == 'general':
        for table_name, status in general.items():
            print(f"Table_{table_name}: {'ว่าง' if status == 0 else 'ถูกจองแล้ว'}")
    else:
        print("กรุณาเลือก 'general' หรือ 'private'")
        zone_select()  # ถ้าใส่ผิดให้เลือกใหม่


def table_select():
    global table
    table = input("เลือกโต๊ะ (เช่นพิมพ์ 1): ")
    if zone == "general" and table in general:
        if general[table] == 1:
            print("โต๊ะนี้ถูกจองแล้ว")
            return False
        else:
            general[table] = 1
            print("จองสำเร็จ")
            return True
    elif zone == "private" and table in private:
        if private[table] == 1:
            print("โต๊ะนี้ถูกจองแล้ว")
            return False
        else:
            private[table] = 1
            print("จองสำเร็จ")
            return True
    else:
        print("ไม่พบโต๊ะนี้ในโซนที่เลือก")
        return False

from datetime import datetime


def validate_time_input(time_str):
    fmt = "%I %p"  
    try:
        datetime.strptime(time_str.upper(), fmt)
        return True
    except ValueError:
        return False

def check_in():
    global hours
    fmt = "%I %p"
    print("ให้ใส่เวลาเป็นรูปแบบ เช่น 3 PM, 11 AM")

    while True:
        start = input("เวลาเช็คอิน: ")
        if validate_time_input(start):
            break
        print("รูปแบบเวลาเช็คอินไม่ถูกต้อง กรุณาใส่ใหม่")

    while True:
        end = input("เวลาเช็คเอาท์: ")
        if not validate_time_input(end):
            print("รูปแบบเวลาเช็คเอาท์ไม่ถูกต้อง กรุณาใส่ใหม่")
            continue
        try:
            t1 = datetime.strptime(start.upper(), fmt)
            t2 = datetime.strptime(end.upper(), fmt)
            if t2 <= t1:
                t2 = t2.replace(day=t2.day + 1)

            diff = t2 - t1
            hours = int(diff.total_seconds() // 3600)
            if hours <= 0:
                print("เวลาที่เลือกไม่ถูกต้อง กรุณาใส่ใหม่")
                return check_in()
            return True
        except ValueError:
            print("เวลาที่ใส่มาไม่ถูกต้อง กรุณาใส่ใหม่")



def timecount():
    global total
    if zone == 'private':
        total = hours * private_cost_per_hour
    elif zone == 'general':
        total = hours * general_cost_per_hour


def main():
    global people
    people = int(input("จำนวนคน: "))
    zone_select()
    while not table_select():
        pass
    while not check_in():
        pass
    timecount()
    print(f"จำนวนคน: {people} | โซน: {zone} | โต๊ะ: {table} | จำนวนชั่วโมง: {hours} | ราคา: {total} บาท")


main()