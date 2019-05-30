# Earthquakes PySpark #
Extract the earthquakes from Geo JSON url using Apache Spark Python API.

> ### Instructions:
- Read the JSON URL and return the coordinates, shape type, place and magnitude of earthquakes greater 
than 1.0 using PySpark.
- Build an ETL tool.
- Visualise output data.

> ### Technical Specs:
- IDE - PyCharm 2019.1
- Python 3.6.1
- Apache Spark 2.4.3 (running locally on macOS Mojave)
- Apache Hive 3.1.1

> ### High architecture level design:

#### The proposed architecture approach:
 
![data_lake](https://github.com/arturosolutions/earthquakes_pyspark/blob/master/images/bi.png)

Note: This approach can be implemented on the cloud or on-prem.

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
