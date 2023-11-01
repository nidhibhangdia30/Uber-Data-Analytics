{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Oblique;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue0;\red193\green152\blue86;
\red255\green255\blue255;\red125\green141\blue87;\red212\green212\blue212;\red70\green137\blue204;\red76\green72\blue77;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\csgray\c0\c0;\cssrgb\c80392\c65882\c41176;
\cssrgb\c100000\c100000\c100000;\cssrgb\c56078\c61569\c41569;\cssrgb\c86275\c86275\c86275;\cssrgb\c33725\c61176\c83922;\cssrgb\c37255\c35294\c37647;
}
\margl1440\margr1440\vieww16620\viewh11620\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 from\strokec5  mage_ai.settings.repo \strokec4 import\strokec5  get_repo_path\
\strokec4 from\strokec5  mage_ai.io.bigquery \strokec4 import\strokec5  BigQuery\
\strokec4 from\strokec5  mage_ai.io.config \strokec4 import\strokec5  ConfigFileLoader\
\strokec4 from\strokec5  pandas \strokec4 import\strokec5  DataFrame\
\strokec4 from\strokec5  os \strokec4 import\strokec5  path\
\
\strokec4 if\strokec5  \strokec6 'data_exporter'\strokec5  \strokec4 not\strokec5  \strokec4 in\strokec5  \strokec4 globals\strokec7 ():\strokec5 \
    \strokec4 from\strokec5  mage_ai.data_preparation.decorators \strokec4 import\strokec5  data_exporter\
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec8 @data_exporter\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec4 def\strokec5  export_data_to_big_query\strokec7 (\strokec5 data\strokec7 ,\strokec5  **kwargs\strokec7 )\strokec5  -> \strokec4 None\strokec7 :\strokec5 \
    \strokec6 """\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec6     Template for exporting data to a BigQuery warehouse.\strokec5 \
\strokec6     Specify your configuration settings in 'io_config.yaml'.\strokec5 \
\
\strokec6     Docs: https://docs.mage.ai/design/data-loading#bigquery\strokec5 \
\strokec6     """\strokec5 \
\
    config_path = path.join\strokec7 (\strokec5 get_repo_path\strokec7 (),\strokec5  \strokec6 'io_config.yaml'\strokec7 )\strokec5 \
    config_profile = \strokec6 'default'\strokec5 \
\
    \strokec4 for\strokec5  key\strokec7 ,\strokec5  value \strokec4 in\strokec5  data.items\strokec7 ():\strokec5 \
        table_id = \strokec6 'uber-test-project-403622.uber_dataengineering_project.\{\}'\strokec5 .\strokec4 format\strokec7 (\strokec5 key\strokec7 )\strokec5 \
        BigQuery.with_config\strokec7 (\strokec5 ConfigFileLoader\strokec7 (\strokec5 config_path\strokec7 ,\strokec5  config_profile\strokec7 ))\strokec5 .export\strokec7 (\strokec5 \
            DataFrame\strokec7 (\strokec5 value\strokec7 ),\strokec5 \
            table_id\strokec7 ,\strokec5 \
            if_exists=\strokec6 'replace'\strokec7 ,\strokec5   
\f1\i \strokec9 # Specify resolution policy if table name already exists
\f0\i0 \strokec5 \
        \strokec7 )\strokec5 \
\
}