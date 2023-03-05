from Crypto.Util.number import *

from tools.factor import *
from tools.fermat import *
from tools.lowe import *
from tools.mod import *
from tools.pollard import *
from tools.get_args import *

'''
mod: 0, 4
factor: 1, 18
lowe:3, 8, 12, 16, 20
fermat: 10
pol_attack:2, 6, 19
sorry I can't: 7, 9, 11, 13, 14, 15, 17
'''

mod_attack_list = [0, 4]
factor_list = [1, 18]
lowe_list = [3, 8, 12, 16, 20]
fermat_list = [10]
pol_attack_list = [2, 6, 19]

data = get_data()

# result of mod_attack
result = mod_attack([data[i] for i in mod_attack_list])
for i in range(len(result)):
    print(f'Frame{mod_attack_list} :', long_to_bytes(result[i][:256]).decode())

# result of factor
result = factor([data[i] for i in factor_list])
for i in range(len(result)):
    print(f'Frame{factor_list} :', long_to_bytes(result[i][:256]).decode())

# result of lowe
result = lowe([data[i] for i in lowe_list])
for i in range(len(result)):
    print(f'Frame{lowe_list} :', long_to_bytes(result[i][:256]).decode())

# result of fermat
result = fermat([data[i] for i in fermat_list])
for i in range(len(result)):
    print(f'Frame{fermat_list} :', long_to_bytes(result[i][:256]).decode())

# result of pol
result = pol_attack([data[i] for i in pol_attack_list])
for i in range(len(result)):
    print(f'Frame{pol_attack_list} :', long_to_bytes(result[i][:256]).decode())
