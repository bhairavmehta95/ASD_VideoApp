import re

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

	return ms

def read_subtitles(file):
	# opens subtitle file
	srt = open(file, 'r')
	lines = srt.readlines()
	i = 0
	#print i, len(lines)
	timestamps = []
	count = 1
	lines = iter(lines)
	dialogues = []

	old_start_timestamp = 0
	added_question = False
	# gets timestamp ending times for lines with questions
	for line in lines:
		target = str(count) + '\n'
		if (line == target):
			count += 1
			timestamp = lines.next()
			start_timestamp = timestamp.split()[0]
			start_timestamp = process_ts(start_timestamp)
			if added_question and not abs(start_timestamp - old_start_timestamp) >= 4000:
				timestamps.pop()
				dialogues.pop()

			dialogue = ''
			read = lines.next()
			while read != '\n':
				dialogue += read
				read = lines.next()

			last_dash = dialogue.rfind('-')
			if last_dash == dialogue.find('-'):
				last_dash = dialogue.find('?')

			if dialogue.find('?') != -1 and dialogue.find('?') <= last_dash:
				added_question = True
				old_start_timestamp = timestamp.split()[0]
				old_start_timestamp = process_ts(old_start_timestamp)
				timestamp = timestamp.split()[2]
				# returns in milliseconds
				timestamp = process_ts(timestamp)
				timestamps.append(timestamp)
				dialogues.append(dialogue)

	print dialogues
	return {'timestamps' : timestamps, 'dialogues' : dialogues} 


if __name__ == '__main__':
	read_subtitles('dora.srt')
