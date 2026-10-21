def nhandathuc(A,B,n,m):
    C = 0 # kết quả cuối
    bit_cao = 1 << (n-1) 
    quychieu = (1 <<n) - 1 # check xem cần bao nhiêu bit trong GF
    while(n!= 0):
        # bit thap nhat cua A = 1 nghĩa là có tốn tại để nhân với B nên cộng vô  
        if (A&1)!= 0:
            C = C ^B 
        A  = A >> 1
        carry = B & bit_cao
        B = (B << 1) & quychieu
        if ( carry != 0): 
            B = B ^ m  # nếu bit cao của B = 1 nghĩa là sẽ tràn so với GF nên phải XOR với m để giảm bậc
        n = n - 1
    return C

print("GF(2^4):")
print(f"A = 0xB, B = 0x6 -> C = {nhandathuc(0xB, 0x6, 4, 0x03):04b}")
print(f"A = 0x7, B = 0xD -> C = {nhandathuc(0x7, 0xD, 4, 0x03):04b}")

print("\nGF(2^8):")
print(f"A = 0x57, B = 0x83 -> C = {nhandathuc(0x57, 0x83, 8, 0x1B):08b}")
print(f"A = 0xA6, B = 0x3D -> C = {nhandathuc(0xA6, 0x3D, 8, 0x1B):08b}")