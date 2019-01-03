# import json
# import os
# import redis
# import time
# import datetime
# import collections
# from collections import Counter
# from os.path import join, getsize
# # from filesize import size
#
# fr
#
# ts=time.time()
#
# start=time.time()
# print start
# """Creating timestamp"""
# c = collections.Counter()
# timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# """Sample data into the format"""
# res1={'root': {'username': 'File1', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res2={'root': {'username': 'File2', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew1', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res3={'root': {'username': 'File3', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew2', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res4={'root': {'username': 'File4', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew3', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res5={'root': {'username': 'File5', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew4', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res6={'root': {'username': 'File6', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew4', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res7={'root': {'username': 'File7', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew5', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# res8={'root': {'username': 'File8', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWcvgggggggggggggggggggwgdmxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzfdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'newnewnew6', 'file_size': 10000000, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
#
#
# for res in(res1,res2,res3,res4,res5,res6,res7,res8):
#     """setting attributes for redis"""
#     file_name=res['root']['transaction_uuid']
#     file_size=res['root']['file_size']
#     file_counter_size= Counter([file_size])
#
#
#     """ Storing data to the on file system as a text file with unique filename,
#     this file will be deleted once the tranmission is successful
#     """
#     save_path = '/home/EFM/Incomming_data'
#
#     f=open('{}.txt'.format('atxt'), 'w+')
#     json.dump(res, f,ensure_ascii=False)
#     f.close()
#     suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
#
#     """
#     at this function the file aer converted to the appropriate sizes
#     so its readiblity is improved(optional)
#     """
#
#     def humansize(nbytes):
#         i = 0
#         while nbytes >= 1024 and i < len(suffixes) - 1:
#             nbytes /= 1024.
#             i += 1
#         f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
#         return '%s %s' % (f, suffixes[i])
#
#
#
#
#
# """
# while transfering the files at this point i will be storing some values per transaction such as
# last completed completed time | Size of the file | total limit configured by the from the config file.
# """
#     totalsize=0
#     count = 0
#     path='C:\Users\siaher\PycharmProjects\practise\python with redis'
#     for root, dirs, files in os.walk(path):
#         totalsize += sum(getsize(join(root, name)) for name in files if name.endswith('.txt'))
#
#         count += sum(1 for name in files if name.endswith('.txt'))
#         overall_size=humansize(totalsize)
#         print ('totalsize {}'.format(totalsize))
#         b=int(totalsize)
#         print type(b)
#         print type(totalsize)
#
#     """ Getting filesizes in all format"""
#
#
#
#     """Creating redis connection
#
#      """
#     redisClient = redis.StrictRedis(host='localhost',
#
#                                      port=6379,
#
#                                  db=0)
#     """
#      storing the following as a hash -table.
#      for every entry it will stored with the file name as the unique key.
#     other attributes associated to it are  Filename, timestamp, size of the file
#
#      """
#
#     FileName = {"file_name": file_name, "timestamp": timestamp, "totalsize": totalsize}
#     print redisClient.hmset(file_name, FileName)
#     print redisClient.hgetall(file_name)
#     print redisClient.keys(file_name)
#     print(redisClient.hget(file_name, 'timestamp'), redisClient.hget(file_name, 'file_name'))
#     #
# """command to get all the keys"""
#     # print redisClient.hgetall(file_name)
#     # print redisClient.hkeys(filename)
#     # """Getting all keys as wells as individual data with in key"""
#     # print redisClient.hgetall('filename')
#     print ('uique name')
#     print redisClient.keys()
#     # print(redisClient.hgetall(file_name))
#     # redisClient.sadd ('transaction_uuid. xxx)
#     # os.remove("data.text")
#     # redisClient.flushall()
#     end=time.time()
#     timeinterval= str(float(end-start)/1000)
#     print ('total time taken for the whole process {}'.format(timeinterval))
#
#     print end
#     print ('about to sleep')
#
# """ in cofigconnector file i will taking the values for following attributes, and using them for sleeping the process
#     sleeping the process as size is more then the limit"""
#
#
# """before sleeping i will be saving follwoing information into the disk with text file, which will store the total size transfered , time taken to trasfer the limit set form config.json file"""
#     if b>10000:
#         print ('total size before making it zero{}'.format(b))
#         b=0
#
#         time.sleep(10)
#         print ('awake{}'.format(b))
#     print ('awake after making size equal to zero{}'.format(b))
#
#     print ('i am awake')


self.bandwidth = []
