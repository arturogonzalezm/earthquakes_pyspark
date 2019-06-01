# Earthquakes PySpark #
Extract the earthquakes from Geo JSON url using Apache Spark Python API.

> ### Instructions:
- Read the JSON URL and return the coordinates, shape type, place and magnitude, where magnitude is greater 
than 1.0 using PySpark.
- Build an ETL/ELT tool.
- Visualise output data.

> ### Technical Specs:
- IDE - PyCharm 2019.1
- Python 3.6.1
- Apache Spark 2.4.3 (running locally on macOS Mojave)
- Apache Hive 3.1.1

> ### High architecture level design:

The proposed ETL/ELT high level architecture design(data lake approach):

1. JSON URL.
2. The script in this case Python Script will load the RAW JSON data into the local environment.
3. Apache Spark will load into HDFS.
4. Hive will be the metastore engine on top of HDFS to query the master data.
5. Apache Spark will perform the transformation according to the business requirements and load it into our data warehouse.
6. The data warehouse(DWH) will have the data ready to be consumed by the BI's or analytics team, in this case we are using PostgreSQL as it supports GeoSpatial data.
7. The data visualisation tool will consume the data from our DWH ready to build sexy dashboards and reports.

 
![bi](https://github.com/arturosolutions/earthquakes_pyspark/blob/master/images/bi.png)

Note: This approach can be implemented on the cloud or on-prem.

> ### Run program:

Assuming your local environment is properly set up, proceed by typing the following input on your terminal.

Input:

```commandline
$SPARK_HOME/bin/spark-submit ~/path/earthquakes_pyspark/src/main.py
```

PostgreSQL Output:

![postgresql](https://github.com/arturosolutions/earthquakes_pyspark/blob/master/images/output.png)

Map Output:

![map](https://github.com/arturosolutions/earthquakes_pyspark/blob/master/images/earthquakes_30-05-2019.png)

> ### How to set up your PySpark local environment:

Refer to the following link:
[How to set up your local PySpark environment using PyCharm IDE](https://medium.com/@arturogonzalezm/how-to-set-up-your-local-pyspark-environment-using-pycharm-ide-935a75b0211)

----

MIT License

Copyright (c) 2019 Arturo Gonzalez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
