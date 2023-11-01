{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue0;\red193\green152\blue86;
\red255\green255\blue255;\red125\green141\blue87;\red212\green212\blue212;\red70\green137\blue204;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\csgray\c0\c0;\cssrgb\c80392\c65882\c41176;
\cssrgb\c100000\c100000\c100000;\cssrgb\c56078\c61569\c41569;\cssrgb\c86275\c86275\c86275;\cssrgb\c33725\c61176\c83922;}
\margl1440\margr1440\vieww18400\viewh12940\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 import\strokec5  io\
\strokec4 import\strokec5  pandas \strokec4 as\strokec5  pd\
\strokec4 import\strokec5  requests\
\strokec4 if\strokec5  \strokec6 'data_loader'\strokec5  \strokec4 not\strokec5  \strokec4 in\strokec5  \strokec4 globals\strokec7 ():\strokec5 \
    \strokec4 from\strokec5  mage_ai.data_preparation.decorators \strokec4 import\strokec5  data_loader\
\strokec4 if\strokec5  \strokec6 'test'\strokec5  \strokec4 not\strokec5  \strokec4 in\strokec5  \strokec4 globals\strokec7 ():\strokec5 \
    \strokec4 from\strokec5  mage_ai.data_preparation.decorators \strokec4 import\strokec5  test\
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec8 @data_loader\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec4 def\strokec5  load_data_from_api\strokec7 (\strokec5 *args\strokec7 ,\strokec5  **kwargs\strokec7 ):\strokec5 \
    \strokec6 """\strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec6     Template for loading data from API\strokec5 \
\strokec6     """\strokec5 \
    url = \strokec6 'https://storage.googleapis.com/uber-data-engineering-project-niddhi/uber_data.csv'\strokec5 \
    response = requests.get\strokec7 (\strokec5 url\strokec7 )\strokec5 \
\
    \strokec4 return\strokec5  pd.read_csv\strokec7 (\strokec5 io.StringIO\strokec7 (\strokec5 response.text\strokec7 ),\strokec5  sep=\strokec6 ','\strokec7 )\strokec5 \
\
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