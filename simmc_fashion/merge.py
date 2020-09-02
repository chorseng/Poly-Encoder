# If I want to use this this needs to be editted

import json
with open('fashion_devtest_dials.json') as infile:
    data = json.load(infile)

with open('fashion_devtest_dials_retrieval_candidates,json') as infile:
    responses = json.load(infile)
    
for line, content in zip(infile, data):
    _, candidate_id, utterance = line.split('\t')
    content['options-for-correct-answers'] = [{'candidate-id':candidate_id, 'utterance':utterance}]

with open('test.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
