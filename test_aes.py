# test_aes.py - test thuat toan aes-128

import unittest
from aes_tables import S_BOX, INV_S_BOX, RCON, nhandathuc
from aes import (
    ma_hoa_aes_128,
    giai_ma_aes_128,
    mix_columns,
    inv_mix_columns,
    bytes_sang_state,
    state_sang_bytes
)


class TestAES128(unittest.TestCase):

    def test_0_nhandathuc_gf(self):
        """Kiem tra lai ham nhandathuc tren truong GF(2^8) tu bai tap truoc."""
        # 0x57 * 0x83 = 0xC1 trong GF(2^8) voi m = 0x1B
        self.assertEqual(nhandathuc(0x57, 0x83, 8, 0x1B), 0xC1)
        # 0xA6 * 0x3D = 0xC6
        self.assertEqual(nhandathuc(0xA6, 0x3D, 8, 0x1B), 0xC6)

    def test_1_sinh_bang_s_box(self):
        """Kiem tra cac gia tri S_BOX sinh ra co khop voi chuan FIPS 197 khong."""
        self.assertEqual(S_BOX[0x00], 0x63)
        self.assertEqual(S_BOX[0x01], 0x7c)
        self.assertEqual(S_BOX[0x02], 0x77)
        self.assertEqual(S_BOX[0x53], 0xed)
        self.assertEqual(S_BOX[0xff], 0x16)
        
        # Kiem tra tinh nghich dao: INV_S_BOX[S_BOX[x]] == x voi moi x
        for x in range(256):
            self.assertEqual(INV_S_BOX[S_BOX[x]], x)

    def test_2_hang_so_vong_rcon(self):
        """Kiem tra gia tri RCON sinh ra cho 10 vong."""
        self.assertEqual(RCON[1][0], 0x01)
        self.assertEqual(RCON[2][0], 0x02)
        self.assertEqual(RCON[8][0], 0x80)
        self.assertEqual(RCON[9][0], 0x1b)
        self.assertEqual(RCON[10][0], 0x36)

    def test_3_mix_columns(self):
        """Kiem tra MixColumns theo vi du muc 5.1.3 cua tai lieu FIPS 197."""
        # Cot dau vao: [0xd4, 0xbf, 0x5d, 0x30]
        # Sau mix_columns phai ra: [0x04, 0x66, 0x81, 0xe5]
        state = [
            [0xd4, 0, 0, 0],
            [0xbf, 0, 0, 0],
            [0x5d, 0, 0, 0],
            [0x30, 0, 0, 0]
        ]
        mix_columns(state)
        self.assertEqual(state[0][0], 0x04)
        self.assertEqual(state[1][0], 0x66)
        self.assertEqual(state[2][0], 0x81)
        self.assertEqual(state[3][0], 0xe5)
        
        # Kiem tra inv_mix_columns phuc hoi lai dung
        inv_mix_columns(state)
        self.assertEqual(state[0][0], 0xd4)
        self.assertEqual(state[1][0], 0xbf)
        self.assertEqual(state[2][0], 0x5d)
        self.assertEqual(state[3][0], 0x30)

    def test_4_nist_fips_197_appendix_b(self):
        """Test vector mau Appendix B cua FIPS 197."""
        khoa = "2b7e151628aed2a6abf7158809cf4f3c"
        ban_ro = "3243f6a8885a308d313198a2e0370734"
        ban_ma_chuan = "3925841d02dc09fbdc118597196a0b32"
        
        ban_ma = ma_hoa_aes_128(ban_ro, khoa)
        self.assertEqual(ban_ma.lower(), ban_ma_chuan.lower())
        
        ban_ro_giai_ma = giai_ma_aes_128(ban_ma, khoa)
        self.assertEqual(ban_ro_giai_ma.lower(), ban_ro.lower())

    def test_5_nist_fips_197_appendix_c1_all_zeros(self):
        """Test vector Appendix C.1 (khoa toan 0 va ban ro toan 0)."""
        khoa = "00" * 16
        ban_ro = "00" * 16
        ban_ma_chuan = "66e94bd4ef8a2c3b884cfa59ca342b2e"
        
        ban_ma = ma_hoa_aes_128(ban_ro, khoa)
        self.assertEqual(ban_ma.lower(), ban_ma_chuan.lower())
        
        ban_ro_giai_ma = giai_ma_aes_128(ban_ma, khoa)
        self.assertEqual(ban_ro_giai_ma.lower(), ban_ro.lower())


if __name__ == "__main__":
    unittest.main()
