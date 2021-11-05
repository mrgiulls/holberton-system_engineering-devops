#!/usr/bin/env ruby
args = ARGV[0].scan(/\[from:(.{0,}?)\]|\[to:(.{0,}?)\]|\[flags:(.{0,}?)\]/)
args = args.join(' ').gsub('    ', ',')
puts(args)
