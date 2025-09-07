class Encryption:
    @staticmethod
    def encrypt(data,key):
        result = ""
        i = 0
        while len(data) > i:
            for char in key:
                if i < len(data):
                    result += chr(ord(data[i]) ^ ord(char))
                    i += 1
                else:
                    break
        return result

        # return "".join(chr(ord(c) ^ key) for c in data)
    def decrypt(data,key):
        return Encrption.encrypt(data,key)
    
a = Encrption.encrypt("gavriel","sdf")
print(a)
b = Encrption.encrypt(a,"sdf")
print(b)       


