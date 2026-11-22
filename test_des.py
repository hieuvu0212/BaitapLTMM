# test_des.py - test thuat toan des

import unittest
from des import (
    hoan_vi,
    dich_vong_trai,
    sinh_16_khoa_con,
    ma_hoa_khoi_des,
    giai_ma_khoi_des
)


class TestDES(unittest.TestCase):

    def test_dich_vong_trai(self):
        # Dịch vòng trái chuỗi [1, 2, 3, 4] 1 bước -> [2, 3, 4, 1]
        bits = [1, 2, 3, 4]
        self.assertEqual(dich_vong_trai(bits, 1), [2, 3, 4, 1])
        self.assertEqual(dich_vong_trai(bits, 2), [3, 4, 1, 2])

    def test_sinh_16_khoa_con(self):
        # Kiểm tra sinh đủ 16 khóa con, mỗi khóa có đúng 48 bit
        khoa_bits = [0] * 64
        cac_khoa = sinh_16_khoa_con(khoa_bits)
        self.assertEqual(len(cac_khoa), 16)
        for k in cac_khoa:
            self.assertEqual(len(k), 48)

    def test_vector_chuan_nist_fips_46_3(self):
        """
        Test Vector chính thức của NIST FIPS 46-3:
        Khóa:       0x133457799BBCDFF1
        Bản rõ:     0x0123456789ABCDEF
        Bản mã:     0x85E813540F0AB405
        """
        khoa = "133457799BBCDFF1"
        ban_ro = "0123456789ABCDEF"
        ban_ma_mong_doi = "85E813540F0AB405"

        # 1. Kiểm tra mã hóa
        ban_ma_thuc_te = ma_hoa_khoi_des(ban_ro, khoa)
        self.assertEqual(ban_ma_thuc_te, ban_ma_mong_doi)
        print("\n[DES] Ma hoa khop 100% test vector NIST:")
        print(f"  Ban ro:     {ban_ro}")
        print(f"  Khoa:       {khoa}")
        print(f"  Ban ma:     {ban_ma_thuc_te}")

        # 2. Kiểm tra giải mã
        ban_ro_giai_ma = giai_ma_khoi_des(ban_ma_thuc_te, khoa)
        self.assertEqual(ban_ro_giai_ma, ban_ro)
        print(f"  Giai ma lai ra dung: {ban_ro_giai_ma}")

    def test_tinh_thuan_nghich_voi_nhieu_khoi(self):
        # Kiểm tra giải mã(mã hóa(P)) == P với nhiều khối ngẫu nhiên
        khoa = "AABBCCDDEEFF0011"
        cac_ban_ro = [
            "0000000000000000",
            "FFFFFFFFFFFFFFFF",
            "123456789ABCDEF0"
        ]
        for p in cac_ban_ro:
            with self.subTest(ban_ro=p):
                c = ma_hoa_khoi_des(p, khoa)
                p_khoi_phuc = giai_ma_khoi_des(c, khoa)
                self.assertEqual(p_khoi_phuc, p)


if __name__ == "__main__":
    unittest.main()
