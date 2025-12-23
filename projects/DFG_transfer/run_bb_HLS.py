from utility import *

top_func_name = 'fn1'
dic = './'
case_name = 'dfg_0' 
#case_name = 'dfg_' + str(idx)
ret = run_HLS_synthesis(top_func_name, dic, case_name, True)
if ret == 0:
    print("test passed!")
else:
    print("test fail")
