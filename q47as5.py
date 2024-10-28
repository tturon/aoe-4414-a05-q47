# conv_ops.py
#
# Usage: conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# Figuring out the output shape and operation count of a convolution layer.

# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter width count
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides

# Output (all int):
#  c_out: output channel count
#  h_out: output height count
#  w_out: output width count
#  adds: number of additions performed
#  muls: number of multiplications performed
#  divs: number of divisions performed

# Written by Thomas Turon
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys
import math

# script arguments
c_in = ''
h_in = ''
w_in = ''
n_filt = ''
h_filt = ''
w_filt = ''
s = ''
p = ''

# checking correct argument number
if len(sys.argv) == 9:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  n_filt = float(sys.argv[4])
  h_filt = float(sys.argv[5])
  w_filt = float(sys.argv[6])
  s = float(sys.argv[7])
  p = float(sys.argv[8])

else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
  )
  exit()

# determine output channel count
c_out = n_filt

# calculate height of output map
h_out = (h_in + (2 * p) - h_filt)/s + 1

# calculate width of output map
w_out = (w_in + (2 * p) - w_filt)/s + 1

# calculate number of additions, multiplications, and divisions
adds = n_filt * h_out * w_out * c_in * h_filt * w_filt
muls = n_filt * h_out * w_out * c_in * h_filt * w_filt
divs = 0 # no divisions required

# print results
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed