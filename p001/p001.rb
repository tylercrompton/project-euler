#!/usr/bin/env ruby

def p001(max)
	i = 0
	total = 0

	while i < max
		if i + 15 < max
			total += i * 7 + 60
		elsif i + 12 < max
			total += i * 6 + 45
		elsif i + 10 < max
			total += i * 5 + 33
		elsif i + 9 < max
			total += i * 4 + 23
		elsif i + 6 < max
			total += i * 3 + 14
		elsif i + 5 < max
			total += i * 2 + 8
		elsif i + 3 < max
			return total + i + 3
		end
		i += 15
	end

	total
end

if __FILE__ == $0
	if ARGV.length == 1
		puts p001 ARGV[0].to_i
	else
		puts 'Usage: p001 <integer>'
		exit 1
	end
end
