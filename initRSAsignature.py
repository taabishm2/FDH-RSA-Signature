#Initialize RSA File Signature Scheme

import fileOp
import generatePrime

def generate_prime_pair(b=1024):   #1024 bit primes
    '''b = number of bits used for the prime generation'''
    
    p = generatePrime.gen_prime_2(b)    
    q = generatePrime.gen_prime_2(b)

    n = p*q
    
    fileOp.write_list("FprimesPQ",[p,q])
    
    fileOp.write_list("FmodulusRSA",[n]) 
    
print("Hello")