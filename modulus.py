def Sum_modulus(a,b,c):
    res=((a%c)+(b%c))%c
    return res
    
print(Sum_modulus(27,15,4))
print(Sum_modulus(277,86,381))

import time
start_time = time.time()
print(powerOfNByExponentialMethod(7,105))
end_time=time.time()
print(f"Time taken to find the result thru exponential method:{enf_time-start_time}seconds")
start_time=time.time()
print(powerOfNByExponentialMethod(7,105))
end_time=time.time()
print(f"Time taken to find the result thru exponential method:{enf_time-start_time}seconds")
print("_"*100)                                                                  