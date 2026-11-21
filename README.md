# BaitapLTMM - Bài tập Lý thuyết mật mã
Repo tổng hợp các bài tập môn Lý thuyết mật mã - Vũ Trung Hiếu.

## Cấu trúc tổng hợp:
1. **[nhandathuc/](./nhandathuc/)**: Bài tập nhân đa thức trong trường hữu hạn GF(2^n).
   - Thuật toán nhân chuyển đổi về dạng bit và giảm bậc bằng phép XOR khi có tràn.
   - Nhánh riêng: `nhandathuctrongtruongGF`

2. **[baitapnhom_sosemanuk/](./baitapnhom_sosemanuk/)**: Bài tập nhóm mô phỏng mã dòng SOSEMANUK.
   - `key_setup.py`: Đệm khóa lên 256 bit và sinh 25 khóa con K0 đến K24.
   - `iv_setup.py`: Chạy 24 vòng Serpent để gán giá trị khởi tạo cho 10 thanh ghi LFSR và 2 thanh ghi FSM.
   - Nhánh riêng: `baitapnhom`

3. **des_aes**: Thiết kế thuật toán DES và AES-128.
   - Nhánh riêng: `des_aes`
