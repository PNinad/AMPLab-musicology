from compmusic import dunya
from compmusic.dunya import hindustani
from compmusic.dunya import docserver
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def hz2cents(pitch_hz, tonic=440):
    return 1200 * np.log2(pitch_hz / float(tonic))

# SET YOUR DUNYA API KEY HERE '5523db6f2169631449c4a5b9642233f03b5792a8'
API_KEY =''
dunya.set_token(API_KEY)

concerts = hindustani.get_recordings()
recording = list(filter(lambda recording: '158ecd08-3751-46bc-bd48-e74c8b85dda8' in recording['mbid'], concerts))

mbid = recording[0]['mbid']

document_details = docserver.document(recording[0]['mbid'])

for document_type, data in document_details['derivedfiles'].items():    
    for subtype, metadata in data.items():        
        if metadata['mimetype'] == 'application/json':            \
            print('{},{}'.format(document_type, subtype), metadata['versions'])

pitch_data = docserver.get_document_as_json(mbid, 'pitch' ,'pitch')
pitch_data = np.array(pitch_data)

#histogram_data = docserver.get_document_as_json(mbid, 'hindustaninormalisedpitch','drawhistogram')



np.savetxt("raga_husaini_pitch_data.csv", pitch_data, delimiter=",")
#np.savetxt("raga_husaini_histogram_data.csv", histogram_data, delimiter=",")
