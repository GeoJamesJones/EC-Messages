import os
import json
import argparse
import pprint
import requests

import xmltodict

def post_to_geoevent(json_data, geoevent_url):
    headers = {
        'Content-Type': 'application/json',
                }

    response = requests.post((geoevent_url), headers=headers, data=json_data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path of XML Documents", required=True)
    parser.add_argument("-g", "--geoevent", help="GeoEvent Server URL", required=True)
    args = parser.parse_args()

    docs = os.listdir(args.path)

    for doc in docs:
        pp = pprint.PrettyPrinter(indent=4)
        doc_path = os.path.join(args.path, doc)
        with open(doc_path) as xml_data:
            base_data = {}

            xml_doc = xmltodict.parse(xml_data.read())
            base_data['security_class'] = xml_doc["env:Envelope"]["env:Header"]["Security"]["@classification"]
            base_data['rel_to'] = xml_doc["env:Envelope"]["env:Header"]["Security"]["@releasableTo"]
            base_data['begin_position'] = xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:phenomenonTime"]["gml:TimePeriod"]["gml:beginPosition"]
            base_data['end_position'] = xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:phenomenonTime"]["gml:TimePeriod"]["gml:endPosition"]
            base_data['sr'] = xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:featureOfInterest"]["sas:SF_SpatialSamplingFeature"]["sas:shape"]["gml:Point"]["@srsName"]
            base_data['pos'] = xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:featureOfInterest"]["sas:SF_SpatialSamplingFeature"]["sas:shape"]["gml:Point"]["gml:pos"]
            base_data['x'] = float(xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:featureOfInterest"]["sas:SF_SpatialSamplingFeature"]["sas:shape"]["gml:Point"]["gml:pos"].split(" ")[0])
            base_data['y'] = float(xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:featureOfInterest"]["sas:SF_SpatialSamplingFeature"]["sas:shape"]["gml:Point"]["gml:pos"].split(" ")[1])
            base_data['observed_property'] = xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:observedProperty"]["@xlink:href"]
            for x in xml_doc["env:Envelope"]["env:Body"]["sos:InsertObservation"]["sos:observation"]["om:OM_Observation"]["om:result"]["swe:DataRecord"]["swe:field"]:
                if "swe:Category" in x:
                    base_data['DetectionCode']=x["swe:Category"]["swe:value"]

            post_to_geoevent(json.dumps(base_data), args.geoevent)

            print(base_data)
            

if __name__=="__main__":    
    main()
