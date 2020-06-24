# frozen_string_literal: true

require 'pycall/import'
include PyCall::Import

sys = PyCall.import_module('sys')

puts sys.stdout.encoding

pyimport :datetime
puts datetime.date.today

pyimport :datetime
puts datetime.datetime.now.strftime('%Y/%m/%d %H:%M:%S')

pyimport :calendar
puts calendar.month(2017, 12)

plt = PyCall.import_module('matplotlib.pyplot')

plt.plot([1, 5, 3, 4])
plt.show
