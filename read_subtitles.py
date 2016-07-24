def read_subtitles():
	# opens subtitle file
	srt = open('dora.srt', 'r')
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
				timestamps.append(timestamp)


	print timestamps


if __name__ == '__main__':
	read_subtitles()
