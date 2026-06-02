parking_lot = []
id = 1

while True:
    print("\n==================================================")
    print("        QUẢN LÝ BÃI XE - SMART PARKING")
    print("==================================================")
    print("   1. Check-in (Đăng ký xe vào)")
    print("   2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("   3. Tìm kiếm xe (Theo biển số)")
    print("   4. Check-out (Xử lý xe ra & Tính phí)")
    print("   5. Thoát chương trình")
    print("==================================================")
    choice = input("Nhập lựa chọn của bạn (1-5): ")

    if not choice.isdigit():
        print("ERR-05 [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue
    choice = int(choice)

    if choice < 1 or choice > 5:
        print("ERR-05 [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue

    if choice == 1:
        while True:
            plate = input("Nhập biển số xe: ").strip().upper()
            if plate == "":
                print("[Lỗi]: Biển số xe không được để trống!")
            else:
                break

        is_duplicate = False
        for vehicle in parking_lot:
            if vehicle["plate"] == plate:
                is_duplicate = True
                break

        if is_duplicate:
            print(f"ERR-01 [Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
            continue

        while True:
            type_input = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if type_input.isdigit():
                vehicle_type = int(type_input)
                if vehicle_type in [1, 2]:
                    break
                else:
                    print("ERR-02 [Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
            else:
                print("ERR-02 [Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")

        while True:
            entry_input = input("Nhập giờ vào (0-24): ").strip()
            if entry_input.isdigit():
                entry_time = int(entry_input)
                if 0 <= entry_time <= 24:
                    break
                else:
                    print("[Lỗi]: Giờ vào phải nằm trong khoảng từ 0 đến 24!")
            else:
                print("[Lỗi]: Vui lòng nhập số nguyên!")

        new_vehicle = {
            "id": id,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time,
            "status": "parked"
        }
        parking_lot.append(new_vehicle)
        print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi.")
        id += 1
    elif choice == 2:
        if len(parking_lot) == 0:
            print("[Thông báo]: Bãi xe hiện đang trống!")
        else:
            print(f"{"ID":<6} | {"Biển số xe":<15} | {"Loại xe":<10} | {"Giờ vào":<8}")
            print("-" * 50)
            for vehicle in parking_lot:
                if vehicle["type"] == 1:
                    type_name = "Xe máy"
                else:
                    type_name = "Ô tô"
                print(f"{vehicle["id"]:<6} | {vehicle["plate"]:<15} | {type_name:<10} | {vehicle["entry_time"]:<8}")
    elif choice == 3:
        plate_input = input("Nhập biển số xe cần tìm: ").strip().upper()

        find = None
        for vehicle in parking_lot:
            if vehicle["plate"] == plate_input:
                find = vehicle
                break

        if find is None:
            print(f"ERR-04 [Lỗi]: Không tìm thấy biển số {plate_input} trong hệ thống!")
        else:
            print(f"Thông tin chi tiết: {find}")
    elif choice == 4:
        out_plate = input("Nhập biển số xe cần ra: ").strip().upper()
        checkout_vehicle = None
        for vehicle in parking_lot:
            if vehicle["plate"] == out_plate:
                checkout_vehicle = vehicle
                break

        if checkout_vehicle is None:
            print(f"ERR-04 [Lỗi]: Không tìm thấy biển số {out_plate} trong hệ thống!")
            continue

        while True:
            out_input = input("Nhập giờ ra: ").strip()
            if out_input.isdigit():
                out_time = int(out_input)
                if out_time < checkout_vehicle["entry_time"]:
                    print("ERR-03 [Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                elif out_time > 24 or out_time < 0:
                    print("[Lỗi]: Giờ ra phải nằm trong khoảng từ 0 đến 24!")
                else:
                    break
            else:
                print("[Lỗi]: Vui lòng nhập số nguyên!")
        
        duration = out_time - checkout_vehicle["entry_time"]
        if duration == 0:
            duration = 1

        if checkout_vehicle['type'] == 1:
            while True:
                bike_fare_input = input("Nhập đơn giá gửi xe máy (VNĐ/giờ): ").strip()
                if bike_fare_input.isdigit():
                    current_bike_fare = int(bike_fare_input)
                    break
                else:
                    print("[Lỗi]: Vui lòng nhập số nguyên!")
            total_fee = duration * current_bike_fare
        else:
            while True:
                car_fare_input = input("Nhập đơn giá gửi ô tô (VNĐ/giờ): ").strip()
                if car_fare_input.isdigit():
                    current_car_fare = int(car_fare_input)
                    break
                else:
                    print("[Lỗi]: Vui lòng nhập số nguyên!")
            total_fee = duration * current_car_fare

        print(f"Tổng phí phải trả: {total_fee} VNĐ")
        
        deleted_id = checkout_vehicle["id"]
        parking_lot.remove(checkout_vehicle)
        print(f"[Thành công]: Đã xóa xe ID {deleted_id} thành công!")
    elif choice == 5:
        print("[Thông báo]: Đã thoát chương trình. Tạm biệt!")
        break