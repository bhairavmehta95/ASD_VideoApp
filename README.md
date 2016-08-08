# ASD_VideoApp

This is a project that involves OpenCV and Google's Speech APIs to help children (especially those with Autism Spectrum Disorder) of all ages gain more out of television programs such as Dora and Blue's Clues. By pairing Facial Tracking as well as forcing the viewer to interact with the program, teachers and parents can gain better insight where the child needs help.

While this project is still an early iteration, future builds will have:

* A feedback system
* A transcript at the end of each video (Question, Child's Answer)
* A "focus score" : A score that tells the adult how long the student was looking at the screen (and therefore, how long the student was paying attention)

## What You Need To Build
* Python
* VLC Installed on Your Computer
* [SpeechRecognition 3.4.6](https://pypi.python.org/pypi/SpeechRecognition/)
* A subtitle file (I am using a Dora .srt file off the internet)
* A video file that goes along with that .srt file

### Things That Work

* Parsing subtitles
* Google Speech starts up at about the right time (more testing needed, currently using two seconds) and records answers accurately
* Printing questions and their responses (Need a way to generate reports)

### Things That Don't Work
* Still getting some incorrect questions

### Things To Still Be Implemented
* OpenCV facial tracking + focus score
* Report generation
