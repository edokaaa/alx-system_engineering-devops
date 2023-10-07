#!/usr/bin/env ruby
# This scripts scraps data from a textme log

if ARGV.length != 1
  exit(1)
end

text = ARGV[0]

pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
matches = text.match(pattern)

if matches
  sender = matches[1]
  receiver = matches[2]
  flags = matches[3]

  output = "#{sender},#{receiver},#{flags}"
  puts output
else
  exit(1)
end
