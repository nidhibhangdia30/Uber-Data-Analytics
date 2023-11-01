{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Oblique;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue0;\red193\green152\blue86;
\red255\green255\blue255;\red125\green141\blue87;\red212\green212\blue212;\red70\green137\blue204;\red76\green72\blue77;
\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\csgray\c0\c0;\cssrgb\c80392\c65882\c41176;
\cssrgb\c100000\c100000\c100000;\cssrgb\c56078\c61569\c41569;\cssrgb\c86275\c86275\c86275;\cssrgb\c33725\c61176\c83922;\cssrgb\c37255\c35294\c37647;
\cssrgb\c70980\c80784\c65882;}
\margl1440\margr1440\vieww22120\viewh11000\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 import\strokec5  pandas \strokec4 as\strokec5  pd\
\strokec4 if\strokec5  \strokec6 'transformer'\strokec5  \strokec4 not\strokec5  \strokec4 in\strokec5  \strokec4 globals\strokec7 ():\strokec5 \
    \strokec4 from\strokec5  mage_ai.data_preparation.decorators \strokec4 import\strokec5  transformer\
\strokec4 if\strokec5  \strokec6 'test'\strokec5  \strokec4 not\strokec5  \strokec4 in\strokec5  \strokec4 globals\strokec7 ():\strokec5 \
    \strokec4 from\strokec5  mage_ai.data_preparation.decorators \strokec4 import\strokec5  test\
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec8 @transformer\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec4 def\strokec5  transform\strokec7 (\strokec5 df\strokec7 ,\strokec5  *args\strokec7 ,\strokec5  **kwargs\strokec7 ):\strokec5 \
    \strokec6 """\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec6     Template code for a transformer block.\strokec5 \
\
\strokec6     Add more parameters to this function if this block has multiple parent blocks.\strokec5 \
\strokec6     There should be one parameter for each output variable from each parent block.\strokec5 \
\
\strokec6     Args:\strokec5 \
\strokec6         data: The output from the upstream parent block\strokec5 \
\strokec6         args: The output from any additional upstream blocks (if applicable)\strokec5 \
\
\strokec6     Returns:\strokec5 \
\strokec6         Anything (e.g. data frame, dictionary, array, int, str, etc.)\strokec5 \
\strokec6     """\strokec5 \
    
\f1\i \strokec9 # Specify your transformation logic here
\f0\i0 \strokec5 \
    df\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5  = pd.to_datetime\strokec7 (\strokec5 df\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ])\strokec5 \
    df\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5  = pd.to_datetime\strokec7 (\strokec5 df\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ])\strokec5 \
\
    df = df.drop_duplicates\strokec7 ()\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    df\strokec7 [\strokec6 'trip_id'\strokec7 ]\strokec5  = df.index\
\
    datetime_dim = df\strokec7 [[\strokec6 'tpep_pickup_datetime'\strokec7 ,\strokec6 'tpep_dropoff_datetime'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5 \
    datetime_dim\strokec7 [\strokec6 'pick_hour'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5 .dt.hour\
    datetime_dim\strokec7 [\strokec6 'pick_day'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5 .dt.day\
    datetime_dim\strokec7 [\strokec6 'pick_month'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5 .dt.month\
    datetime_dim\strokec7 [\strokec6 'pick_year'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5 .dt.year\
    datetime_dim\strokec7 [\strokec6 'pick_weekday'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_pickup_datetime'\strokec7 ]\strokec5 .dt.weekday\
\
    datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5 \
    datetime_dim\strokec7 [\strokec6 'drop_hour'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5 .dt.hour\
    datetime_dim\strokec7 [\strokec6 'drop_day'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5 .dt.day\
    datetime_dim\strokec7 [\strokec6 'drop_month'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5 .dt.month\
    datetime_dim\strokec7 [\strokec6 'drop_year'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5 .dt.year\
    datetime_dim\strokec7 [\strokec6 'drop_weekday'\strokec7 ]\strokec5  = datetime_dim\strokec7 [\strokec6 'tpep_dropoff_datetime'\strokec7 ]\strokec5 .dt.weekday\
\
    datetime_dim\strokec7 [\strokec6 'datetime_id'\strokec7 ]\strokec5  = datetime_dim.index\
\
    datetime_dim = datetime_dim\strokec7 [[\strokec6 'datetime_id'\strokec7 ,\strokec5  \strokec6 'tpep_pickup_datetime'\strokec7 ,\strokec5  \strokec6 'pick_hour'\strokec7 ,\strokec5  \strokec6 'pick_day'\strokec7 ,\strokec5  \strokec6 'pick_month'\strokec7 ,\strokec5  \strokec6 'pick_year'\strokec7 ,\strokec5  \strokec6 'pick_weekday'\strokec7 ,\strokec5 \
                             \strokec6 'tpep_dropoff_datetime'\strokec7 ,\strokec5  \strokec6 'drop_hour'\strokec7 ,\strokec5  \strokec6 'drop_day'\strokec7 ,\strokec5  \strokec6 'drop_month'\strokec7 ,\strokec5  \strokec6 'drop_year'\strokec7 ,\strokec5  \strokec6 'drop_weekday'\strokec7 ]]\strokec5 \
\
    passenger_count_dim = df\strokec7 [[\strokec6 'passenger_count'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    passenger_count_dim\strokec7 [\strokec6 'passenger_count_id'\strokec7 ]\strokec5  = passenger_count_dim.index\
    passenger_count_dim = passenger_count_dim\strokec7 [[\strokec6 'passenger_count_id'\strokec7 ,\strokec6 'passenger_count'\strokec7 ]]\strokec5 \
\
    trip_distance_dim = df\strokec7 [[\strokec6 'trip_distance'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    trip_distance_dim\strokec7 [\strokec6 'trip_distance_id'\strokec7 ]\strokec5  = trip_distance_dim.index\
    trip_distance_dim = trip_distance_dim\strokec7 [[\strokec6 'trip_distance_id'\strokec7 ,\strokec6 'trip_distance'\strokec7 ]]\strokec5 \
\
    rate_code_type = \strokec7 \{\strokec5 \
    \strokec10 1\strokec7 :\strokec6 "Standard rate"\strokec7 ,\strokec5 \
    \strokec10 2\strokec7 :\strokec6 "JFK"\strokec7 ,\strokec5 \
    \strokec10 3\strokec7 :\strokec6 "Newark"\strokec7 ,\strokec5 \
    \strokec10 4\strokec7 :\strokec6 "Nassau or Westchester"\strokec7 ,\strokec5 \
    \strokec10 5\strokec7 :\strokec6 "Negotiated fare"\strokec7 ,\strokec5 \
    \strokec10 6\strokec7 :\strokec6 "Group ride"\strokec5 \
    \strokec7 \}\strokec5 \
\
    rate_code_dim = df\strokec7 [[\strokec6 'RatecodeID'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    rate_code_dim\strokec7 [\strokec6 'rate_code_id'\strokec7 ]\strokec5  = rate_code_dim.index\
    rate_code_dim\strokec7 [\strokec6 'rate_code_name'\strokec7 ]\strokec5  = rate_code_dim\strokec7 [\strokec6 'RatecodeID'\strokec7 ]\strokec5 .\strokec4 map\strokec7 (\strokec5 rate_code_type\strokec7 )\strokec5 \
    rate_code_dim = rate_code_dim\strokec7 [[\strokec6 'rate_code_id'\strokec7 ,\strokec6 'RatecodeID'\strokec7 ,\strokec6 'rate_code_name'\strokec7 ]]\strokec5 \
\
    pickup_location_dim = df\strokec7 [[\strokec6 'pickup_longitude'\strokec7 ,\strokec5  \strokec6 'pickup_latitude'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    pickup_location_dim\strokec7 [\strokec6 'pickup_location_id'\strokec7 ]\strokec5  = pickup_location_dim.index\
    pickup_location_dim = pickup_location_dim\strokec7 [[\strokec6 'pickup_location_id'\strokec7 ,\strokec6 'pickup_latitude'\strokec7 ,\strokec6 'pickup_longitude'\strokec7 ]]\strokec5  \
\
\
    dropoff_location_dim = df\strokec7 [[\strokec6 'dropoff_longitude'\strokec7 ,\strokec5  \strokec6 'dropoff_latitude'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    dropoff_location_dim\strokec7 [\strokec6 'dropoff_location_id'\strokec7 ]\strokec5  = dropoff_location_dim.index\
    dropoff_location_dim = dropoff_location_dim\strokec7 [[\strokec6 'dropoff_location_id'\strokec7 ,\strokec6 'dropoff_latitude'\strokec7 ,\strokec6 'dropoff_longitude'\strokec7 ]]\strokec5 \
\
    payment_type_name = \strokec7 \{\strokec5 \
    \strokec10 1\strokec7 :\strokec6 "Credit card"\strokec7 ,\strokec5 \
    \strokec10 2\strokec7 :\strokec6 "Cash"\strokec7 ,\strokec5 \
    \strokec10 3\strokec7 :\strokec6 "No charge"\strokec7 ,\strokec5 \
    \strokec10 4\strokec7 :\strokec6 "Dispute"\strokec7 ,\strokec5 \
    \strokec10 5\strokec7 :\strokec6 "Unknown"\strokec7 ,\strokec5 \
    \strokec10 6\strokec7 :\strokec6 "Voided trip"\strokec5 \
    \strokec7 \}\strokec5 \
    payment_type_dim = df\strokec7 [[\strokec6 'payment_type'\strokec7 ]]\strokec5 .reset_index\strokec7 (\strokec5 drop=\strokec4 True\strokec7 )\strokec5 \
    payment_type_dim\strokec7 [\strokec6 'payment_type_id'\strokec7 ]\strokec5  = payment_type_dim.index\
    payment_type_dim\strokec7 [\strokec6 'payment_type_name'\strokec7 ]\strokec5  = payment_type_dim\strokec7 [\strokec6 'payment_type'\strokec7 ]\strokec5 .\strokec4 map\strokec7 (\strokec5 payment_type_name\strokec7 )\strokec5 \
    payment_type_dim = payment_type_dim\strokec7 [[\strokec6 'payment_type_id'\strokec7 ,\strokec6 'payment_type'\strokec7 ,\strokec6 'payment_type_name'\strokec7 ]]\strokec5 \
\
    fact_table = df.merge\strokec7 (\strokec5 passenger_count_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'passenger_count_id'\strokec7 )\strokec5  \\\
             .merge\strokec7 (\strokec5 trip_distance_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'trip_distance_id'\strokec7 )\strokec5  \\\
             .merge\strokec7 (\strokec5 rate_code_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'rate_code_id'\strokec7 )\strokec5  \\\
             .merge\strokec7 (\strokec5 pickup_location_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'pickup_location_id'\strokec7 )\strokec5  \\\
             .merge\strokec7 (\strokec5 dropoff_location_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'dropoff_location_id'\strokec7 )\strokec5 \\\
             .merge\strokec7 (\strokec5 datetime_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'datetime_id'\strokec7 )\strokec5  \\\
             .merge\strokec7 (\strokec5 payment_type_dim\strokec7 ,\strokec5  left_on=\strokec6 'trip_id'\strokec7 ,\strokec5  right_on=\strokec6 'payment_type_id'\strokec7 )\strokec5  \\\
             \strokec7 [[\strokec6 'trip_id'\strokec7 ,\strokec6 'VendorID'\strokec7 ,\strokec5  \strokec6 'datetime_id'\strokec7 ,\strokec5  \strokec6 'passenger_count_id'\strokec7 ,\strokec5 \
               \strokec6 'trip_distance_id'\strokec7 ,\strokec5  \strokec6 'rate_code_id'\strokec7 ,\strokec5  \strokec6 'store_and_fwd_flag'\strokec7 ,\strokec5  \strokec6 'pickup_location_id'\strokec7 ,\strokec5  \strokec6 'dropoff_location_id'\strokec7 ,\strokec5 \
               \strokec6 'payment_type_id'\strokec7 ,\strokec5  \strokec6 'fare_amount'\strokec7 ,\strokec5  \strokec6 'extra'\strokec7 ,\strokec5  \strokec6 'mta_tax'\strokec7 ,\strokec5  \strokec6 'tip_amount'\strokec7 ,\strokec5  \strokec6 'tolls_amount'\strokec7 ,\strokec5 \
               \strokec6 'improvement_surcharge'\strokec7 ,\strokec5  \strokec6 'total_amount'\strokec7 ]]\strokec5 \
\
    \strokec4 return\strokec5  \strokec7 \{\strokec6 "datetime_dim"\strokec5  \strokec7 :\strokec5 datetime_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "passenger_count_dim"\strokec7 :\strokec5 passenger_count_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "trip_distance_dim"\strokec5  \strokec7 :\strokec5 trip_distance_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "rate_code_dim"\strokec7 :\strokec5 rate_code_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "pickup_location_dim"\strokec5  \strokec7 :\strokec5 pickup_location_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "dropoff_location_dim"\strokec5  \strokec7 :\strokec5 dropoff_location_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "payment_type_dim"\strokec5  \strokec7 :\strokec5 payment_type_dim.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 ),\strokec5 \
    \strokec6 "fact_table"\strokec7 :\strokec5 fact_table.to_dict\strokec7 (\strokec5 orient=\strokec6 "dict"\strokec7 )\}\strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec8 @test\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec4 def\strokec5  test_output\strokec7 (\strokec5 output\strokec7 ,\strokec5  *args\strokec7 )\strokec5  -> \strokec4 None\strokec7 :\strokec5 \
    \strokec6 """\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec6     Template code for testing the output of the block.\strokec5 \
\strokec6     """\strokec5 \
    \strokec4 assert\strokec5  output \strokec4 is\strokec5  \strokec4 not\strokec5  \strokec4 None\strokec7 ,\strokec5  \strokec6 'The output is undefined'\strokec5 \
\
}