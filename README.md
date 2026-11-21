# Bài tập nhóm - Mã dòng SOSEMANUK

Phần em làm:
- key_setup.py: nhận key từ 128 bit đến 256 bit rồi sinh ra 25 khóa con K0 đến K24
- iv_setup.py: lấy 25 khóa con vừa sinh cộng với IV 128 bit chạy 24 vòng Serpent để gán vào các thanh ghi LFSR và FSM
- folder tests:
  + test_key_setup.py: test các hàm con và check thử 2 bộ test (1 bộ tự tính tay theo vở, 1 bộ test chuẩn)
  + test_iv_setup.py: test 24 vòng và check xem gán đúng thanh ghi không
