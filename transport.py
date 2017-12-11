#!/usr/bin/env python

from __future__ import print_function

import time
import json, ast

from satori.rtm.client import make_client, SubscriptionMode

endpoint = "wss://open-data.api.satori.com"
appkey = "a9DCBCDDfc7007df375eFd1aEf4745C4"
channel = "transportation"

def main():
    with make_client(endpoint=endpoint, appkey=appkey) as client:
        print('Connected to Satori RTM!')

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    message_cleaned = ast.literal_eval(json.dumps(message))
                    #print(message_cleaned['entity'][0]['id'])
                    with open("Data/"+message_cleaned['entity'][0]['id']+".json",'w') as f:
                        json.dump(message,f)



        subscription_observer = SubscriptionObserver()
        client.subscribe(
            channel,
            SubscriptionMode.SIMPLE,
            subscription_observer)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
