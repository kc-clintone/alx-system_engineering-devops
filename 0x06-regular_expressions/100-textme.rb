#!/usr/bin/env ruby
# A regular expression that matches anything
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
