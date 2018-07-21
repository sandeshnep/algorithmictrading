import os;
import urllib.request;
import pandas as pd;
import json;

# parses the website which has JSON content written on it. Reads JSON content
# then decodes it into UTF-8 format. Returns the entire string whic has JSON content of the website.
def import_web(symbl):
    """
    :param identifier: List, Takes the company name
    :return:displays companies records per minute
    """
    url = 'https://api.iextrading.com/1.0/stock/'+ symbl + '/chart/dynamic';
    fp = urllib.request.urlopen(url);
    mybytes = fp.read();
    mystr = mybytes.decode("utf8");
    fp.close();
    return mystr;

# sends the data to another funtion called partionSave.
def get_value(symbl):
    js = import_web(symbl);
    pandasObj= pd.read_json(js);

    df = pd.DataFrame(data=pandasObj, columns=['data']);

    print(df.loc[len(df)-1][0]['close']);

    # parsed_data = json.loads(js); # loads the json and converts the json string into dictionary
    # print(parsed_data);
    # ps = parsed_data['Time Series (1day)'];





def main():
    #Start Process
    company_list = ['ORCL'];
    try:
        for company in company_list:
            print("Starting with " + company)
            get_value(company)
            print("Ended Writing Data of " + company)
    except Exception as e:
        print(e)

main();
