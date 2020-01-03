#!/usr/bin/env python3
# Fridosleigh.com CAPTEHA API - Made by Krampus Hollyfeld
import time
import queue
import threading
import numpy as np
import tensorflow as tf
import requests
import json
import sys
import base64
import os
import datetime as dt
from pathlib import Path
import shutil
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.logging.set_verbosity(tf.logging.ERROR)


def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label


def predict_image(q, sess, graph, image_bytes, img_full_path, labels, input_operation, output_operation):
    image = read_tensor_from_image_bytes(image_bytes)
    results = sess.run(output_operation.outputs[0], {
        input_operation.outputs[0]: image
    })
    results = np.squeeze(results)
    prediction = results.argsort()[-5:][::-1][0]
    q.put({'img_full_path': img_full_path, 'prediction': labels[prediction].title(
    ), 'percent': results[prediction]})


def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()
    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)
    return graph


def read_tensor_from_image_bytes(imagebytes, input_height=299, input_width=299, input_mean=0, input_std=255):
    image_reader = tf.image.decode_png(
        imagebytes, channels=3, name="png_reader")
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(
        dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.compat.v1.Session()
    result = sess.run(normalized)
    return result


def main():
    yourREALemailAddress = "cybergoof@gmail.com"
    # Prepare the ML part
    # Loading the Trained Machine Learning Model created from running retrain.py on the training_images directory
    graph = load_graph('/tmp/retrain_tmp/output_graph.pb')
    labels = load_labels("/tmp/retrain_tmp/output_labels.txt")

    # Load up our session
    input_operation = graph.get_operation_by_name("import/Placeholder")
    output_operation = graph.get_operation_by_name("import/final_result")
    sess = tf.compat.v1.Session(graph=graph)
    q = queue.Queue()

    # Creating a session to handle cookies
    for numThreads in range(10, 50, 4):
        print("Run number "+str(numThreads))
        s = requests.Session()
        url = "https://fridosleigh.com/"

        json_resp = json.loads(s.get("{}api/capteha/request".format(url)).text)
        # A list of dictionaries eaching containing the keys 'base64' and 'uuid'
        b64_images = json_resp['images']
        # The Image types the CAPTEHA Challenge is looking for.
        challenge_image_type = json_resp['select_type'].split(',')
        challenge_image_types = [
            challenge_image_type[0].strip().lower(),
            challenge_image_type[1].strip().lower(),
            challenge_image_type[2].replace(' and ', '').strip().lower()
        ]  # cleaning and formatting
        '''
        MISSING IMAGE PROCESSING AND ML IMAGE PREDICTION CODE GOES HERE
        '''
        current = time.time()

        for image in b64_images:
            image_bytes = base64.b64decode(str(image['base64']))
#            Path('./hhfiles/input/').mkdir(parents=True, exist_ok=True)
#            f = open('./hhfiles/input/' +
#                     image['uuid'], 'w+b')
#            f.write(image_bytes)
#            f.close()

            while len(threading.enumerate()) > numThreads:
                time.sleep(0.0001)

            threading.Thread(target=predict_image,
                             args=(q, sess, graph, image_bytes,
                                   image['uuid'],
                                   labels,
                                   input_operation, output_operation)).start()

        print('Waiting For Threads to Finish...')
        while q.qsize() < len(b64_images):
            time.sleep(0.001)

        # getting a list of all threads returned results
        prediction_results = [q.get() for x in range(q.qsize())]

        # do something with our results... Like print them to the screen.
        final_answer = []
        for prediction in prediction_results:
            #            Path('./hhfiles/' + prediction['prediction']
            #                 ).mkdir(parents=True, exist_ok=True)
            #            shutil.copy('./hhfiles/input/'+prediction['img_full_path'], './hhfiles/' +
            #                        prediction['prediction']+'/'+prediction['img_full_path'])
            if prediction['prediction'].lower() in challenge_image_types:
                final_answer.append(prediction['img_full_path'])
    #        print('TensorFlow Predicted {img_full_path} is a {prediction} with {percent:.2%} Accuracy'.format(
    #           **prediction))
        mlTime = time.time() - current
        # This should be JUST a csv list image uuids ML predicted to match the challenge_image_type .
        # final_answer = ','.join([img['uuid'] for img in b64_images])

        json_resp = json.loads(
            s.post("{}api/capteha/submit".format(url), data={'answer': ','.join(final_answer)}).text)
        if not json_resp['request']:
            # If it fails just run again. ML might get one wrong occasionally
            print('FAILED MACHINE LEARNING GUESS')
            print(
                '--------------------\nOur ML Guess:\n--------------------\n{}'.format(final_answer))
            print(
                '--------------------\nServer Response:\n--------------------\n{}'.format(json_resp['data']))
            print("Failed.  Threads: "+str(numThreads)+" time " + str(mlTime))
        else:
            print('CAPTEHA Solved!')
            # If we get to here, we are successful and can submit a bunch of entries till we win
            userinfo = {
                'name': 'Krampus Hollyfeld',
                'email': yourREALemailAddress,
                'age': 180,
                'about': "Cause they're so flippin yummy!",
                'favorites': 'thickmints'
            }
            # If we win the once-per minute drawing, it will tell us we were emailed.
            # Should be no more than 200 times before we win. If more, somethings wrong.
            entry_response = ''
            entry_count = 1
            while yourREALemailAddress not in entry_response and entry_count < 200:
                print('Submitting lots of entries until we win the contest! Entry #{}'.format(
                    entry_count))
                entry_response = s.post(
                    "{}api/entry".format(url), data=userinfo).text
                entry_count += 1
            print(entry_response)
            break


if __name__ == "__main__":
    main()
