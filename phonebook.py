# ایجاد یک دیکشنری خالی برای ذخیره‌سازی مخاطبین
contacts = {}

# یک حلقه بی‌نهایت برای اجرای مداوم برنامه
while True:
    # نمایش منو به کاربر
    print("\n--- Phonebook ---")
    print("1. افزودن مخاطب")
    print("2. جستجوی مخاطب")
    print("3. نمایش همه مخاطبین")
    print("4. خروج")

    # گرفتن انتخاب کاربر
    choice = input("انتخاب کنید: ")

    # اگر کاربر گزینه 1 را انتخاب کند → افزودن مخاطب
    if choice == "1":
        name = input("نام مخاطب را وارد کنید: ")
        phone = input("شماره مخاطب را وارد کنید: ")
        contacts[name] = phone
        print(f"✅ مخاطب {name} با شماره {phone} اضافه شد.")

    # اگر کاربر گزینه 2 را انتخاب کند → جستجو
    elif choice == "2":
        name = input("نام مخاطب مورد نظر را وارد کنید: ")
        if name in contacts:
            print(f"📞 شماره {name}: {contacts[name]}")
        else:
            print("❌ مخاطب پیدا نشد.")

    # اگر کاربر گزینه 3 را انتخاب کند → نمایش همه
    elif choice == "3":
        if contacts:
            print("\n--- همه مخاطبین ---")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("📂 دفترچه تلفن خالی است.")

    # اگر کاربر گزینه 4 را انتخاب کند → خروج
    elif choice == "4":
        print("👋 خداحافظ!")
        break

    # اگر ورودی اشتباه باشد
    else:
        print("❌ گزینه نامعتبر است. دوباره تلاش کنید.")