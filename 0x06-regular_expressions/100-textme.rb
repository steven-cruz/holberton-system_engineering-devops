#!/usr/bin/env ruby
# Ruby script to filter message for sender, receiver and flags used
puts ARGV[0].scan(/(?<=\[from:|\[to:|\[flags:)(.*?)(?=\])/).join(",")
