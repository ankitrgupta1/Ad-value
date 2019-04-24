import io
import os
import glob
import json
from google.cloud import videointelligence

def get_details(result):
    
    result_json = {}
    result_json['labels'] = []
    j = 0
    # first result is retrieved because a single video was processed
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        label = {}         
        label['description'] = segment_label.entity.description
        
        if len(segment_label.category_entities) > 0:
            label['categories'] = []
            for category_entity in segment_label.category_entities:
                label['categories'].append(category_entity.description)

        if len(segment_label.segments) > 0:
            label['segments'] = []
            
            for i, segment in enumerate(segment_label.segments):
                segment_details = {}
                start_time = (segment.segment.start_time_offset.seconds +
                              segment.segment.start_time_offset.nanos / 1e9)
                end_time = (segment.segment.end_time_offset.seconds +
                            segment.segment.end_time_offset.nanos / 1e9)
                positions = '{}s to {}s'.format(start_time, end_time)
                confidence = segment.confidence
                segment_details['start_time'] =  start_time
                segment_details['end_time'] = end_time
                segment_details[confidence] = confidence
                label['segments'].append(segment_details)
            
            
        result_json['labels'].append(label)
        
    return result_json
        
        
def run_quickstart(file_dir):
    # [START video_quickstart]
    
    i = 0
    j = 0
    k = 0
    l = 0
    errors = {}
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]
    
    for direc in os.listdir(file_dir):
        print(direc)
        loc=os.path.join(file_dir,direc)
        os.chdir(loc)
        try:
            
            if glob.glob('*.mp4'):
                
                file = glob.glob('*.mp4')[0]

                file_name = os.path.join(file_dir,direc,file)
                print("file name = " ,file_name)
                with io.open(file_name, 'rb') as movie:
                    input_content = movie.read()
                    
                operation = video_client.annotate_video(input_content=input_content, features=features)
                print('\nProcessing video for label annotations:')

                result = operation.result(timeout=120)
                print('\nFinished processing.')

                result_json = {}
                result_json = get_details(result)
                with open(os.path.join(file_dir,direc,'data.json'), 'w') as outfile:
                    json.dump(result_json, outfile)
                

                i = i+1
                
            elif glob.glob('*.webm'):
                
                l = l+1
                                    
                
        except Exception as o:
            print(o)
            j = j+1
            errors[loc]=str(o)
        
        k = k + 1
        
    print("Out of total {}, processed {} mp4 videos successfully, while {} files errored out, and left {} webm files out!".format(k,i,j, l))
    with open(os.path.join(file_dir,'error/error.json'), 'w') as outfile:
        json.dump(errors, outfile)
    
    # [END video_quickstart]


if __name__ == '__main__':
    
    file_dir = 'file directory'
    
    run_quickstart(file_dir)