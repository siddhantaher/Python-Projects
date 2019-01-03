#
# ------------------------------------
# # # # import redis
# # # # r= redis.Redis(port=6379)
# # # #
# # # # # r.set('Foo','bar')
# # # # # r.set('sid','dude')
# # # # # r.delete('sid')
# # # # # r.set('sid','sssup')
# # # # r.expire('sid',5)
# # # # # r.setex('name',10,34)
# # # # # print(r.get('Foo'))
# # # # # print r.get('Foo')
# # # # # print(r.get('sid'))
# # # # # print r.get('name')
# # # # # print ('ttl','name')
# # # # # r.rpush('dafdsf','heyyyutrtrtrtrtrtr')
# # # # # print r.llen('dafdsf')
# # # # # int r.memory_usage('Foo')
# # # # # print r.lpop('dafdsf')
# # # # # print r.llen('dafdsf')
# # # # # print r.keys()
# # # # # r.flushall()
# # # import time
# # # import datetime
# # # ts = time.time()
# # # # #
# # # # #
# # # st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# # # # user = {"Name":"siddhnat", "Company":"cisco", "Address":"Mumbai", "Location":st}
# # # # #
# # # # # print st
# # # # # # r.hmset("pythonDictonary", user)
# # # # #
# # # # # print r.hgetall("pythonDict")
# # # # # print r.hgetall('pythonDictonary')
# # # # # r.expire('pythonDict',10)
# # # # # print r.ttl('pythonDict')
# # # # #
# # # # # r.hset("NumberVsString", "name", "One")
# # # # #
# # # # # r.hset("NumberVsString", "age", "Two")
# # # # #
# # # # # r.hset("NumberVsString", "sex", "Three")
# # # #
# # # # # # print r.llen('NumberVsString')
# # # # # hashName = "Dessert"
# # # # # #
# # # # # r.hmset('info', user)
# # # # # # r.delete(hashName,'1')
# # # # # # r.hset(hashName, 'timestamp', st)
# # # # # r.hmset('timestamp', ts)
# # # # #
# # # # # print(r.hgetall(hashName))
# # # # import json
# # # # # dataaa=user['timestamp']
# # # # # print dataaa
# # # # result={1,2,34}
# # # user = {"timestamp":ts, "Location":"MP"}
# # # print user
# # #
# # # print type(user)
# # # import json
# # # d=json.dumps(user)
# # #
# # # # data = json.dumps(user)
# # # # new=json.loads(data)
# # # # print new
# # # # dataa= new['timestamp']
# # # # print dataa
# # # # sammm = {"timestamp":ts,'hello':user, "Location":"MP"}
# # # # r.hmset("pythonDict", sammm)
# # # #
# # # # # print  r.llen("pythonDict")
# # # # # print r.hgetall('pythonDict')
# # # # # print r.keys()
# # #
# # # import redis
# # #
# # # # Create a redis client
# # #
# # # redisClient = redis.StrictRedis(host='localhost',
# # #
# # #                                 port=6379,
# # #
# # #                                 db=0)
# # #
# # # # Add key value pairs to the Redis hash
# # #
# # # # redisClient.hset("NumberVsString", "1", "One")
# # # #
# # # # redisClient.hset("NumberVsString", "2", "Two")
# # # #
# # # # redisClient.hset("NumberVsString", "4", d)
# # #
# # # # Retrieve the value for a specific key
# # #
# # # # print("Value for the key 3 is")
# # # #
# # # # print(redisClient.hget("NumberVsString", "3"))
# # # #
# # # print("The keys present in the Redis hash:");
# # # #
# # # # print(redisClient.hkeys("NumberVsString"))
# # # #
# # # print("The values present in the Redis hash:");
# # # #
# # # # print(redisClient.hvals("NumberVsString"))
# # # #
# # # # print("The keys and values present in the Redis hash are:")
# # # #
# # # print(redisClient.hgetall("NumberVsString"))
# # # # print type(user)
# # #
# # # # d=json.loads(user)
# # #
# # # res={'root': {'username': 'sam', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'sidd', 'file_size': 255, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# # # print type(res)
# # # filesize=res['root']['file_size']
# # #
# # #
# # # new=json.dumps(res)
# # # # print type(new)
# # # # print new['timestamp']
# # #
# # # # print type(new)
# # # transaction_uuid=res['root']['transaction_uuid']
# # # # redisClient.hset("NumberVsString", "transaction_uuid", transaction_uuid)
# # # # redisClient.hset(,'name',new)
# # # a=redisClient.hgetall('NumberVsString')
# # # print type (a)
# # # # print redisClient.keys()
# # # # redisClient.hdel('NumberVsString','age')
# # # # redisClient.hset(transaction_uuid, "data",new )
# # # b= redisClient.hgetall(transaction_uuid)
# # #
# # # print type(a)
# # # print ('this is b {}'.format(a))
# # # c =json.dumps(b)
# # # print type(c)
# # #
# # # print c
# #
# # import redis
# # r = redis.Redis()
# # # r.flushall()
# # import time
# # import datetime
# # import json
# # ts = time.time()
# # res={'root': {'username': 'sid', 'timestamp':ts, 'file_attributes': '-rw-r-r-', 'file_contents': '77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxCb2FyZERldGFpbHM+\nDQogIDxEYXRlVGltZT4yMDE4LTAyLTA2IDE1OjI5OjU1PC9EYXRlVGltZT4NCiAgPFNlcmlhbE51\nbWJlcj5KQUUyMjA2MDBZSDwvU2VyaWFsTnVtYmVyPg0KICA8QXNzZW1ibHlNb2RlbD43My0xMDA5\nOTUtMDEtUjYtTlc8L0Fzc2VtYmx5TW9kZWw+DQogIDxTdGF0aW9uTmFtZT5NRVNfQmlydGg8L1N0\nYXRpb25OYW1lPg0KPC9Cb2FyZERldGFpbHM+\n', 'transaction_uuid': 'sammmmmmm', 'file_size': 255, 'file_encode': 'base64', 'smt_node_ip_address': '10.152.173.27', 'file_format': 'XML', 'raw_file_name': 'smt.xml', 'smt_node_name': 'smtanalytics'}}
# #
# # data=json.dumps(res)
# #
# # timestamp=ts
# #
# # file_size= res['root']['file_size']
# # transaction_id= res['root']['transaction_uuid']
# # # print file_size
# # # print transaction_id
# #
# # st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# # # user = {"Name":"siddhnat", "Company":"cisco", "Address":"Mumbai", "Location":st}
# # # r.hset("NumberVsString", "transaction_uuid", transaction_id)
# # # r.hset('NumberVsString','file_size',file_size)
# # # r.hset('NumberVsString','data',data)
# # # r.hset('NumberVsString','timestamp',ts)
# # l1=json.dumps(r.hgetall('NumberVsString'))
# #
# # # list= r.lpush('mylist',l1)
# # # print r.lrange('mylist',0,2)
# # # print r.llen('mylist')
# # # r.flushall()
# # # final_list=r.hgetall('NumberVsString')
# # # print final_list
# # # final=json.dumps(final_list)
# # # print final
# # # print r.lpush('mylist',final)
# # # r.sadd('smt',l1)
# # # print r.smembers('smt')
# # # print r.scard('smt')
# #
# # # print r.sismember('smt')
# # # list= r.lrange('mylist',0,3)
# # # print list
# # # new_list= json.dumps(list)
# # # print new_list
# # # print r.llen('mylist')
# #
# # # print r.keys()
# #
# # # print r.srandmember('smt',3)
# #
# # # r.set('mykey','hello')
# # print r.get('mykey')
# # r.expire('mykey',10)
# # # print r.persist('mykey')
# # print r.ttl('mykey')
#
#
# import pickle
# import redis
#
# r = redis.StrictRedis('localhost')
# import time
# import datetime
# ts = time.time()
# st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# user = {"Name":"siddhnat", "Company":"cisco", "Address":"Mumbai", "Location":st}
#
# mydict = {'sid':'2','information':user,'3':'4'}
#
# p_mydict = pickle.dumps(mydict)
# r.set('mydict',p_mydict)
#
# read_dict = r.get('mydict')
# # print read_dict
# yourdict = pickle.loads(read_dict)
# print yourdict
# print yourdict['information']
# print type(yourdict)
#
#
