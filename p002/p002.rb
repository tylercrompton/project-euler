def p002(upper_bound)
	if upper_bound <= 2
		return 0
	end

	buffer = [0, 2]

	sum = 2
	temp = 8
	while temp < upper_bound
		buffer[0], buffer[1] = buffer[1], temp
		sum += temp
		temp = 4 * buffer[1] + buffer[0]
	end

	return sum
end

if __FILE__ == $0
	if ARGV.length == 1
		puts p002 ARGV[0].to_i
	else
		puts 'Usage: p002 <integer>'
		exit 1
	end
end
