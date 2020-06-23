# frozen_string_literal: true

require 'pycall/import'
include PyCall::Import

sys = PyCall.import_module('sys')
random = PyCall.import_module('random')
os = PyCall.import_module('os')

class Dice
    def saiko
      pyimport :random
      saikoro = ["⚀","⚁","⚂","⚃","⚄","⚅"]
      (0..5).each do |x|
      print ' ' + (random.choice(saikoro))
      end
      puts ''
    end
end

Dice.new.saiko