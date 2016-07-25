def process_ts(timestamp):
	# 1 hr = 3600000 ms
	# 1 min = 60000 ms
	# 1 sec = 1000 ms

	values = timestamp.split(':')
	ms = 0
	ms += 3600000 * int(values[0])
	ms += 60000 * int(values[1])
	last = values[2].split(',')
	ms += 1000 * int(last[0])
	ms += int(last[1])

	print timestamp, ms
	return ms

def read_subtitles(file):
	# opens subtitle file
	srt = open(file, 'r')
	lines = srt.readlines()
	i = 0
	print i, len(lines)
	timestamps = []
	count = 1
	lines = iter(lines)

	# gets timestamp ending times for lines with questions
	for line in lines:
		target = str(count) + '\n'
		if (line == target):
			count += 1
			timestamp = lines.next()
			dialogue = ''
			read = lines.next()
			while read != '\n':
				dialogue += read
				read = lines.next()
			if dialogue.find('?') != -1:
				timestamp = timestamp.split()[2]
				# returns in milliseconds
				timestamp = process_ts(timestamp)
				timestamps.append(timestamp)

	return timestamps


if __name__ == '__main__':
	read_subtitles('dora.srt')
