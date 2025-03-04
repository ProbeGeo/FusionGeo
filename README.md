# README of FusionGeo

## Published Databases
We publish a total of two types of FusionGeo IP geolocation databases, including binary geolocation geolocation database and online geolocation API. 

### Binary Database
The binary geolocation database provides the locations of all possible IPv4 and IPv6 addresses. Researchers can download as they like. For user privacy and data security, we have aggregated the geolocation database by prefix in the binary files. Therefore, its database accuracy is lower than that of the online API. 
https://cloud.tsinghua.edu.cn/f/69e3fa5b7fc441cd9ce3/

### Online API
We make our geolocation services as open as possible to the community and provide queries with the highest possible geolocation accuracy while ensuring user privacy and data security. We use an online API to provide location queries to the public. The online API limits the rate and total number of queries. The code is online-api.py and the server IP and port is provided and updated in this file. Note that if the set request rate is exceeded, we will permanently block the accessing IP. We set a limit of 10,000 IPs per minute. 
