# EEGClassification
Introduction
An electroencephalogram (EEG) is a test that detects electrical activity in your brain using small, flat metal discs (electrodes) attached to your scalp. Your brain cells communicate via electrical impulses and are active all the time, even when you're asleep. This activity shows up as wavy lines on an EEG recording. [Mayo Clinic]

The goal of this project is to classify brain states from EEG data. A joint CU Anschutz/ULN project has collected EEG data on subjects during sessions in which the subjects were instructed to visualize performing a motor-based task. Each subject performed one session visualizing a very familiar task, and another session visualizing an unfamiliar task. The primary goal is to develop a classifier that can correctly identify whether a subject is visualizing a task that is familiar or unfamiliar.

Secondary goals include providing insight into which brain regions and frequency bands associate with each of the respective classes. If a deep learning approach is found to be viable, these insights may correspond to latent features found within the neural network. Other insights may be obtained from more traditional data processing and machine learning techniques.


EEG-Datasets
A list of all public EEG-datasets. This list of EEG-resources is not exhaustive. If you find something new, or have explored any unfiltered link in depth, please update the repository.

Motor-Imagery

Left/Right Hand MI: Includes 52 subjects (38 validated subjects with discriminative features), results of physiological and psychological questionnares, EMG Datasets, location of 3D EEG electrodes, and EEGs for non-task related states
Motor Movement/Imagery Dataset: Includes 109 volunteers, 64 electrodes, 2 baseline tasks (eye-open and eye-closed), motor movement, and motor imagery (both fists or both feet)
Grasp and Lift EEG Challenge: 12 subjects, 32channels@500Hz, for 6 grasp and lift events, namely a). HandStart b). FirstDigitTouch c). BothStartLoadPhase d). LiftOff e). Replace f). BothReleased
The largest SCP data of Motor-Imagery: The dataset contains 60 hours of EEG BCI recordings across 75 recording sessions of 13 participants, 60,000 mental imageries, and 4 BCI interaction paradigms, with multiple recording sessions and paradigms of the same individuals. BCI interactions involving up to 6 mental imagery states are considered. [Article]
BCI Competition IV-1: 64 EEG channels at 1000Hz sampling rate for 2 classes of left hand, right hand, foot (+ idle state) for 7 subjects. Evaluation data is continuous EEG which contains also periods of idle state.
BCI Competition IV-2a: 22-electrode EEG motor-imagery dataset, with 9 subjects and 2 sessions, each with 288 four-second trials of imagined movements per subject. Includes movements of the left hand,the right hand, the feet and the tongue. [Dataset Description]
BCI Competition IV-2b: 3-electrode EEG motor-imagery dataset with 9 subjects and 5 sessions of imagined movements of the left or the right hand, the latest 3 sessions include online feedback. [Dataset Description]
High-Gamma Dataset: 128-electrode dataset obtained from 14 healthy subjects with roughly 1000 four-second trials of executed movements divided into 13 runs per subject. The four classes of movements were movements of either the left hand, the right hand, both feet, and rest.
Left/Right Hand 1D/2D movements: 19-electrode data of one subject with various combinations of 1D and 2D hand movements (actual execution).
Imagination of Right-hand Thumb Movement: In every trial, subjects were asked to rest and rest data was recorded for 5 mins. Further, 5 second epoch data was also recorded when subjects were asked to imagine right hand thumb movement. 5 of such imagined motor movement, and rest state was recorded for each trial. Single subject, 8 electrodes at 256Hz.
Emotion-Recognition

DEAP: Includes 32 subjects, each watchine 1-min long excerpts of music-videos, rated by users in terms of arousal/valence/like-dislike/dominanace/famaliarity, and frontal face recording of 22/32 subejcts.
Enterface'06: Enterface'06 Project 07: EEG(64 Channels) + fNIRS + face video, Includes 16 subjects, where emotions were elicited through selected subset of IAPS dataset.
Imagined Emotion: 31 subjects, subjects listen to voice recordings that suggest an emotional feeling and ask subjects to imagine an emotional scenario or to recall an experience in which they have felt that emotion before.
NeuroMarketing: 25 subjects, 14 electrodes, Like/Dislike on commercial e-commerce products over 14 categories with 3 images each. Article for the dataset: Analysis of EEG signals and its application to neuromarketing. [Article]
SEED: 15 subjects were shown video clips eliciting positive/negative/neutral emotion and EEG was recorded over 62 channels.
SEED-IV: 15 subjects were shown video clips ellicity happy/sad/neutral/fear emotions and EEG was recorded over 62 channels (with eye-tracking) for 3 sessions per subject (24 trials per session).
SEED-VIG: Vigilance labels with EEG data in a simulated driving task. 18 electrodes and eye-tracking included.
HCI-Tagging: Subjetcs were shown video clips (fragments of movies) and they were asked to annotate the emotional state on the scale of valence and arousal. During the whole experiment, audio, video, gaze data and physiological data were recorded simultaneously with accurate synchronisation between sensors.
Error-Related Potentials (ErrP)

BCI-NER Challenge: 26 subjects, 56 EEG Channels for a P300 Speller task, and labeled dataset for the response elicited when P300 decodes a correct or incorrect letter.

Monitoring ErrP in a target selection task: 6 subjects with 64 EEG electrodes, watching a cursor move towards a target square, and elicited responses are labeled based on whether the cursor moves in right or wrong direction. [Dataset Description]

ErrPs during continuous feedback: 10 subjects with 28 EEG electrodes, playing a video game to study execution and outcome error. [Dataset Part-1] [Dataset Part-2]

HCI-Tagging: Subjetcs were shown images or movie fragments with a tag at the bottom of the screen. In some cases, the tag correctly described something about the situation. However, in other cases the tag did not actually apply to the media item. After each item, a participant was asked to press a green button if they agreed with the tag being applicable to the media item, or press a red button if not. During the whole experiment, audio, video, gaze data and physiological data were recorded simultaneously with accurate synchronisation between sensors.

Visually Evoked Potentials (VEPs)

c-VEP BCI: 9 subjects, 32 EEG Channels for a VEP BCI speller (32 characters) task, and labeled dataset for the response elicited for the label associated with the speller. [Dataset description] [Published article]

c-VEP BCI with dry electrodes: 9 subjects, 15 dry-EEG Channels for a VEP BCI speller (32 characters) task, and labeled dataset for the response elicited for the label associated with the speller. [Article]

SSVEP - Visual Search/Discrimination and Handshake: Includes 3 different tests, (i) Five Box visual test: attnded and unattended disc and square based stimuli, (ii) visual search within natural images: search of a yellow dot stimuli in B&W natural images, (iii) hand shake test: showing left/right hand closed/open images. 30 subjects, 14 electrodes. [Article 1] [Article 2] [More Dataset: Dataset 2]

Event Related Potentials [ERPs]

Pattern Visual Evoked Potentials: Dataset#5, 2 subjects for checkboard light pattern (oddball paradigm) recorded at O1 position.
Resting State

Resting State EEG Data: 22 subjects, 72 EEG Channels for a resting task of 8 mins with 4 mins of eyes closed and 4 mins of eyes open. [Article]
EID-M, EID-S: 8 subjects in rest state (with eyes closed) recorded from 14 electrodes using EPOC+ for 54s at 128 Hz (7000 samples each). EID-M has three trials and EID-S is a signle trial dataset. The dataset was used to develop a person identification system through brainwaves. [Article]
Music and EEG

Music Imagery Information Retrieval: 10 subjects, 64 EEG Channels for a music imagery task of 12 different pieces w/ different meter, length and tempo. [Article]
Eye-blinks/movements

Involuntary Eye Movements during Face Perception: Dataset 1, 26 electrodes, 500Hz sampling rate, and 120 trials. Eye movements and pupil diameter record, EEG and EOG data is present when subject is presented a happy/sad/angry face on the screen. [Article] [P.S: Dataset available on request only]
Voluntary-Involuntary Eye-Blinks: Voluntary eye-blinks (subject were asked to blink voluntarily within 1s of audio stimulus) and involuntary eye-blinks (natural) was recorded for 20 subjects on 14 electrodes using g.tec. For each subject, 3 sessions with 20 trials each are present in .mat format. [Article]
EEG-eye state: Eye-state labeled data for one continuous recording of EEG of 117 seconds with eye-closed and eye-open labels. The dataset was recorded from Emotiv headset.
Miscellaneous

MNIST Brain Digits: EEG data when a digit(0-9) is shown to the subject, recorded 2s for a single subject using Minwave, EPOC, Muse, Insight. Includes over 1.2M samples.
Imagenet Brain: A random image is shown (out of 14k images from the Imagenet ILSVRC2013 train dataset) and EEG signals are recorded for 3s for one subject. Includes over 70k samples.
Working Memory: Participants briefly observe an array containing multiple English characters SET (500ms) and maintain the information for three seconds. A TEST character is then presented and participants respond by press of a button if TEST charter matches one of the characters in the SET. 15 students, 64 electrodes and 500Hz sampling rate. Only a small subset of data is available publicly. [Original Paper] [Further Analysis in ICLR]
Deep Sleep Slow Osciallation: 10 seconds of recording starting 10 seconds before the end of a slow oscillation. Data is recorded with a goal to predict whether or not a slow oscillation will be followed by another one in sham condition, i.e. without any stimulation.
Genetic Predisposition to Alcoholism: 120 trials for 120 subjects recorded from 64 electrides at 256Hz. Two groups of subjects were considered, alcoholic and control. Stimuli details are given in the paper.
Clinical EEG

TUH EEG Resources: Massive amount of data for (i) Abnormal EEG and (ii) EEG Seizures
Others [Unfiltered]
https://sccn.ucsd.edu/~arno/fam2data/publicly_available_EEG_data.html - http://headit.ucsd.edu/studies
https://www2.le.ac.uk/departments/engineering/research/bioengineering/neuroengineering-lab/software
https://github.com/pbashivan/EEGLearn/tree/master/Sample%20data
Section 2: https://arxiv.org/pdf/1611.08024.pdf
EEG Databases for Emotion Recognition, NTU
https://engineuring.wordpress.com/2009/07/08/downloadable-eeg-data/
http://www.brainsignals.de/
http://www.fil.ion.ucl.ac.uk/spm/data/
http://www.brainliner.jp/search/showall/1
http://bnci-horizon-2020.eu/database/data-sets
http://archive.ics.uci.edu/ml/datasets/EEG+Database
https://www.physionet.org/physiobank/database/#neuro
http://www.physionet.org/pn6/chbmit/
https://sites.google.com/site/iitrcsepradeep7/resume
http://memory.psych.upenn.edu/RAM
http://fcon_1000.projects.nitrc.org/indi/cmi_eeg/
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8616018
https://arxiv.org/pdf/1805.06427.pdf
http://www.gtec.at/Research/Biosignal-Data-Sets/content/Biosignal-Data-Sets
http://studycatalog.org/
http://predict.cs.unm.edu/
https://datadryad.org/resource/doi:10.5061/dryad.070jc
https://ieee-dataport.org/data-competitions
