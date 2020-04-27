# brute force 
def brute(cipher):
    cipher = cipher.lower()
    for key in range(0,26):
        plain = "The plaintext could be: "
        for i in range(0, len(cipher)):
            pi = (ord(cipher[i]) - 97 - key) % 26
            pc = chr(pi + 97 )
            plain = plain + pc
        print plain + '\n'

# main
def main():
    
    # call function as you need 
    cipher = "ZNKIGKYGXIOVNKXOYGXKGRREURJIOVNKXCNOINOYXKGRRECKGQOSTUZYAXKNUCURJHKIGAYKOSZUURGFEZURUUQGZZNKCOQOVGMKGZZNKSUSKTZHAZOLOMAXKOZYMUZZUHKGZRKGYZROQKLOLZEEKGXYURJUXCNGZKBKXBGPJADLIVBAYKZNUYKRGYZZKTINGXGIZKXYGYZNKYURAZOUT"
    brute(cipher)

if __name__ == "__main__":
    main()



