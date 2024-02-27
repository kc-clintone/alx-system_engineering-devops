#!/usr/bin/env ruby
#This script creates a regex that matches strings starting with h, ending n
puts ARGV[0].scan(/h.n/).join
