#!/usr/bin/env ruby
#  prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe.
# output: [SENDER],[RECEIVER],[FLAGS]
# sender phone number or name (country code if present)
# receiver phone number or name (country code if present)
# The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
