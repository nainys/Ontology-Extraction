import re
import os
import xml.etree.ElementTree as et
from gensim.summarization.summarizer import summarize

# TIPSTER dataset
data_dir = './Datasets/cmplg-xml'
files = os.listdir(data_dir)

summary_directory = os.path.join(data_dir,"Summaries")
# Summaries Directory
if not os.path.exists(summary_directory):
    os.makedirs(summary_directory)

# Create corresponding summary files
for file in files:
	f = open(os.path.join(summary_directory, file[:-3]+"txt"),"w")
	text = ""

	tree = et.parse(os.path.join(data_dir, file))
	root = tree.getroot()

	for elem in root.iter('P'):		# Paragraph tag content extraction
		text += ''.join(elem.itertext())

	f.write(summarize(text))