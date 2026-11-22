# Cài đặt DES và AES

- Tác giả: Vũ Trung Hiếu

### Các file trong thư mục:
- `des_tables.py`, `aes_tables.py`: Các bảng tạo dựng sẵn để dùng (sinh bằng vòng lặp và công thức).
- `des.py`, `aes.py`: File cài đặt thuật toán mã hóa và giải mã.
- `test_des.py`, `test_aes.py`: File test xem thuật toán chạy đúng không.

### Cách chạy test:
```bash
python -m unittest test_des.py -v
python -m unittest test_aes.py -v
```
