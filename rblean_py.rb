# frozen_string_literal: true

require 'pycall/import'
include PyCall::Import

sys = PyCall.import_module('sys')

puts sys.stdout.encoding
puts sys.version

pyimport :datetime
puts datetime.date.today

pyimport :datetime
puts datetime.datetime.now.strftime('%Y/%m/%d %H:%M:%S')

pyimport :calendar
puts calendar.month(2017, 12)
