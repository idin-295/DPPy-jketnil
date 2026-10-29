category = 1
menu = 2

match category:
    case 1:
        print("อาหารคาว")
        match menu:
            case 1:
                print("ข้าวผัด")
            case 2:
                print("ผัดไทย")
            case _:
                print("ไม่มีเมนูนี้")

    case 2:
        print("ของหวาน")
        match menu:
            case 1:
                print("ไอศกรีม")
            case 2:
                print("เค้ก")
            case _:
                print("ไม่มีเมนูนี้")

    case _:
        print("ไม่มีหมวดหมู่นี้")
        