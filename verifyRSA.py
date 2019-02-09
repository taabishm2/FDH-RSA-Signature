import fileOp
import fdh

class verifier:

    def __init__(self):
        
        self.signature = fileOp.read_list_noint("Fsignature")[0]
        
        self.verify()

    def verify(self):

        ciphertext = fileOp.read_list("Fciphertext")[0]
        
        n = fileOp.read_list("FpublicKey")[0]
        
        public_key = fileOp.read_list("FpublicKey")[1]

        print("File to be checked:",end=" ")
        
        inp = input()
        
        inp = fdh.fdh(inp,(len(bin(n))-2)) #TEST
        
        signaturec = hex(pow(ciphertext,public_key,n))

        print(inp,self.signaturec)
        
        if inp == signaturec:
            
            print("VERIFIED!")
            
        else:
            
            print("FAILED!")

v = verifier()
