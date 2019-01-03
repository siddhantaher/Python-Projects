import multiprocessing
import os
import json
import time
from datetime import datetime
import datetime
import collections

from os.path import join, getsize

ts=time.time()

start=time.time()
print start
"""Creating timestamp"""
c = collections.Counter()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

res1={'root': {'username': 'File1', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res2={'root': {'username': 'File2', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew1', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res3={'root': {'username': 'File3', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew2', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res4={'root': {'username': 'File4', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew3', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res5={'root': {'username': 'File5', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew4', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res6={'root': {'username': 'File6', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew4', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res7={'root': {'username': 'File7', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew5', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
res8={'root': {'username': 'File8', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew6', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}




for res in(res1,res2,res3,res4,res5,res6,res7,res8):
    """setting attributes for redis"""
    file_name=res['root']['transaction_uuid']
    file_size=res['root']['file_size']
    totalsize = 0
    path='C:\Users\siaher\PycharmProjects\practise\python with redis'
    for root, dirs, files in os.walk(path):
        totalsize += sum(getsize(join(root, name)) for name in files if name.endswith('.txt'))
        # print(type(totalsize))
        b=int(totalsize)
        print(b)
        print(type(b))

    """ Storing data to the on file system as a text file with unique filename,
    this file will be deleted once the tranmission is successful
    """
    save_path = 'C:\Users\siaher\PycharmProjects\practise\Python projects\IncomingData'

    f=open('{}.txt'.format(file_name), 'w+')
    json.dump(res, f,ensure_ascii=False)
    f.close()
    print(sum([b]))


