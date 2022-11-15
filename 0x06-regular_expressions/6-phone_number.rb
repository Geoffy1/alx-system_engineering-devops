#!/usr/bin/env ruby
# ^ begining of string to match
puts ARGV[0].scan(/^\d{10}$/).join
