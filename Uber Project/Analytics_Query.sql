{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red39\green78\blue204;\red255\green255\blue255;\red44\green55\blue61;
\red21\green129\blue62;\red42\green55\blue62;\red0\green0\blue0;\red107\green0\blue1;}
{\*\expandedcolortbl;;\cssrgb\c20000\c40392\c83922;\cssrgb\c100000\c100000\c100000;\cssrgb\c22745\c27843\c30588;
\cssrgb\c5098\c56471\c30980;\cssrgb\c21569\c27843\c30980;\cssrgb\c0\c0\c0;\cssrgb\c50196\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 CREATE\cf4 \strokec4  \cf2 \strokec2 OR\cf4 \strokec4  \cf2 \strokec2 REPLACE\cf4 \strokec4  \cf2 \strokec2 TABLE\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.tbl_analytics`\cf4 \strokec4  \cf2 \strokec2 AS\cf4 \strokec4  \cf6 \strokec6 (\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 \
SELECT\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec7 f\strokec4 .\strokec7 VendorID\strokec4 , \cb1 \
\cb3 \strokec7 d\strokec4 .\strokec7 tpep_pickup_datetime\strokec4 ,\cb1 \
\cb3 \strokec7 d\strokec4 .\strokec7 tpep_dropoff_datetime\strokec4 ,\cb1 \
\cb3 \strokec7 p\strokec4 .\strokec7 passenger_count\strokec4 ,\cb1 \
\cb3 \strokec7 t\strokec4 .\strokec7 trip_distance\strokec4 ,\cb1 \
\cb3 \strokec7 r\strokec4 .\strokec7 rate_code_name\strokec4 ,\cb1 \
\cb3 \strokec7 pick\strokec4 .\strokec7 pickup_latitude\strokec4 ,\cb1 \
\cb3 \strokec7 pick\strokec4 .\strokec7 pickup_longitude\strokec4 ,\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 drop\cf4 \strokec4 .\strokec7 dropoff_latitude\strokec4 ,\cb1 \
\cf2 \cb3 \strokec2 drop\cf4 \strokec4 .\strokec7 dropoff_longitude\strokec4 ,\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec7 pay\strokec4 .\strokec7 payment_type_name\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 fare_amount\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 extra\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 mta_tax\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 tip_amount\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 tolls_amount\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 improvement_surcharge\strokec4 ,\cb1 \
\cb3 \strokec7 f\strokec4 .\strokec7 total_amount\cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 FROM\cf4 \strokec4  \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 `uber-test-project-403622.uber_dataengineering_project.fact_table`\cf4 \strokec4  \strokec7 f\cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.datetime_dim`\cf4 \strokec4  \strokec7 d\strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \strokec7 f\strokec4 .\cf8 \strokec8 datetime_id\cf4 \strokec4  = \strokec7 d\strokec4 .\strokec7 datetime_id\cb1 \strokec4 \
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.passenger_count_dim`\cf4 \strokec4  \strokec7 p\strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \strokec7 p\strokec4 .\cf8 \strokec8 passenger_count_id\cf4 \strokec4  = \strokec7 f\strokec4 .\strokec7 passenger_count_id\cb1 \strokec4 \
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.trip_distance_dim`\cf4 \strokec4  \strokec7 t\strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \strokec7 t\strokec4 .\cf8 \strokec8 trip_distance_id\cf4 \strokec4  = \strokec7 f\strokec4 .\strokec7 trip_distance_id\cb1 \strokec4 \
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.rate_code_dim`\cf4 \strokec4  \strokec7 r\strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \strokec7 r\strokec4 .\cf8 \strokec8 rate_code_id\cf4 \strokec4  = \strokec7 f\strokec4 .\strokec7 rate_code_id\cb1 \strokec4 \
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.pickup_location_dim`\cf4 \strokec4  \strokec7 pick\strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \strokec7 pick\strokec4 .\cf8 \strokec8 pickup_location_id\cf4 \strokec4  = \strokec7 f\strokec4 .\strokec7 pickup_location_id\cb1 \strokec4 \
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.dropoff_location_dim`\cf4 \strokec4  \cf2 \strokec2 drop\cf4 \strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \cf2 \strokec2 drop\cf4 \strokec4 .\cf8 \strokec8 dropoff_location_id\cf4 \strokec4  = \strokec7 f\strokec4 .\strokec7 dropoff_location_id\cb1 \strokec4 \
\cf2 \cb3 \strokec2 JOIN\cf4 \strokec4  \cf5 \strokec5 `uber-test-project-403622.uber_dataengineering_project.payment_type_dim`\cf4 \strokec4  \strokec7 pay\strokec4  \cf2 \strokec2 ON\cf4 \strokec4  \strokec7 pay\strokec4 .\cf8 \strokec8 payment_type_id\cf4 \strokec4  = \strokec7 f\strokec4 .\strokec7 payment_type_id\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 ; \cb1 \
}