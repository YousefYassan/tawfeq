import logging
import ast
import json
from weakref import ref
from bs4 import BeautifulSoup
#import session
import requests
import pandas as pd
import numpy as np
import re
null = None
def main(param ) :
    # req_body = json.loads(param)
    # #req.get_json()
    
    # # Extract the JSON string from the 'param' key (or based on your structure)
    # json_data = req_body.get('param')

    # # Convert JSON data back to a DataFrame
    # df = pd.read_json(json.dumps(json_data), orient='columns')
    df=pd.DataFrame(param["data"])
    logging.info("5555555555")

   
    def scrape_the_price(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        try:
            page = requests.get(url, headers=headers)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                convert_tag = soup.find('div', class_='YMlKec fxKbKc')
                convert = convert_tag.get_text(strip=True).replace('$', '')
                return float(convert)
            else:
                return None
        except Exception as e:
            logging.error(f"Error scraping {url}: {e}")
            return None

    SAR_USD = scrape_the_price("https://www.google.com/finance/quote/SAR-USD") or 0.27  # Fallback value
    EUR_USD = scrape_the_price("https://www.google.com/finance/quote/EUR-USD") or 1.1
    EGP_USD = scrape_the_price("https://www.google.com/finance/quote/EGP-USD") or 0.03

   
    def convert_price_before(value):
        value =str(value)
        if isinstance(value, str):
            try:
                value = value.upper()
                value = value.replace(',', '')
                value = value.replace('SAR','')
                value = value.replace('EUR','')
                value = value.replace('€','')
                return float(value)
            except ValueError:
                return None
        else:
            return None
    def convert_rate(value):
        value =str(value)
        if isinstance(value, str):
            try:
                value = value.lower()
                value = value.replace(',', '')
                value = value.replace('out of 5 stars','')
                return float(value)
            except ValueError:
                return None
        else:
            return None
    def convert_to_gb(value):
        value = str(value)
        if isinstance(value, str):
            value = value.replace(',', '')
            value = value.upper()
            if 'GB' in value:
                try:
                    return float(value.replace('GB', ''))
                except ValueError:
                    return np.nan
            elif 'MB' in value:
                try:
                    return float(value.replace('MB', '')) / 1024 
                except ValueError:
                    return np.nan
            elif 'TB' in value:
                try:
                    return float(value.replace('TB', '')) * 1024 
                except ValueError:
                    return np.nan
            elif 'LESS THAN' in value:
                return np.nan 
            else:
                return np.nan 
        elif isinstance(value, (int, float)):
            return float(value) 
        else:
            return np.nan
    def convert_screen_size(value):
        value = str(value)
        value = value.upper()
        if 'INCHES' in value:
            value = value.replace('INCHES','')
            return float(value)
        elif 'INCH' in value:
            value = value.replace('INCH','')
            return float(value)
        else:
            return None
    def convert_resolution(value):
        value = str(value)
        if value and isinstance(value, str):
            try:
                width, height = value.lower().split('x')
                width = float(width)
                height = float(height)
                return width, height
            except ValueError:
                return None, None
        else:
            return None, None
    def change_price_to_USD(value,convert):
        if value :
            value = value*convert
            return value
        else:
            return None
    def change_to_USD(value):
        return 'USD'
    def find_model_in_title(title, model_sizes):
        if title:
            title_lower = title.lower()
            # Check for keywords related to RAM
            
            if 'model' in title_lower  :
                for model in model_sizes:
                    if re.search(r'\b' + re.escape(model.lower()) + r'\b', title_lower, re.IGNORECASE):
                        return model
        return None
    def find_cpu_in_title(title):
        cpu_sizes=['Octa Core', 'Hexa Core', 'Quad Core', 'Deca Core']
        if title :
            title_lower = title.lower()
            if 'cpu' in title_lower  :
                for cpu in cpu_sizes:
                    if re.search(r'\b' + re.escape(cpu.lower()) + r'\b', title_lower, re.IGNORECASE):
                        return cpu
        return None
    def find_color_in_title(title):
        allcolors = [
        "Rose Gold", "Navy Blue","Light Blue","Cobalt Violet","Awesome Graphite","Titanium Black","Wave Green","Emerald Green","Titanium Silver",
        "Midnight Blue", "Forest Green", "Pink", "Purple", "Lavender","Charcoal Ink","Carbon Grey","Glamorous Green","Flowing Silver",
        "Orange", "Bronze", "Copper", "Champagne", "Beige", "Coral", "Midnight Black","Cobalt Violet",
        "Turquoise", "Teal", "Mint Green", "Burgundy", "Aqua", "Cyan", "Lime Green","Rose Red",
        "Space Gray", "Graphite", "Alpine Green", "Starlight", "Pacific Blue", "Ceramic White","Moonlight White"
        "Jet Black", "Matte Black", "Phantom Black", "Phantom Silver", "Mystic Bronze", "Awesome Navy"
        "Mystic Green", "Cosmic Gray", "Cosmic Black", "Pearl White", "Glossy White", "Awesome Lime","Silver Shadow",
        "Aura Glow", "Aurora Blue", "Prism White", "Cloud Pink", "Midnight Green", "Mint","Charcoal",
        "Sunset Gold", "Ocean Blue", "Thunder Purple", "Starry Night", "Twilight", "Clear","Navy","Chartreuse",
        "Gradient Purple", "Gradient Blue", "Gradient Red","Gradient Pink", "Marble White", "Graphite","Violet",
        "Opal White", "Crystal Blue", "Ice Blue", "Sunrise Red", "Fiery Red","Blue","Black", "White", "Gray", "Silver", "Gold", "Red","Yellow", "Green", "Brown"
    ]
        for color in allcolors:
            if color.lower() in title.lower():
                return color
        return None
    def find_strg_in_title(title):
        storage_sizes =["1TB","512GB", "256GB", "128GB", "64GB", "32GB", "16GB", "8GB"]
        if title:
            title_lower = title.lower()
            # Check for keywords related to RAM
            
            if 'storage' in title_lower  :
                for storage in storage_sizes:
                    if re.search(r'\b' + re.escape(storage.lower()) + r'\b', title_lower, re.IGNORECASE):
                        return storage
        return None
    def find_ram_in_title(title):
        ram_sizes = ["1GB","2GB", "3GB","4GB","6GB","8GB","12GB","16GB"]
        if title:
            title_lower = title.lower()
            # Check for keywords related to RAM
            if 'ram' in title_lower or 'memory' in title_lower:
                for ram in ram_sizes:
                    if re.search(r'\b' + re.escape(ram.lower()) + r'\b', title_lower, re.IGNORECASE):
                        return ram
        return None
    df_nl=df
    df_nl.columns = [col.lower() for col in df_nl.columns]
    df_nl.rename(columns={'main camera': 'camera', 'network': 'cellular technology','number of sim':'sim count',}, inplace=True)
    df_nl['CPU'] = df_nl.apply(lambda row: find_cpu_in_title(row['title']) or row['cpu'], axis=1)
    df_nl['color'] = df_nl.apply(lambda row: find_color_in_title(row['title']) or row['color'], axis=1)
    df_nl['Storage'] = df_nl.apply(lambda row: find_strg_in_title(row['title']) or row['storage'], axis=1)
    df_nl['RAM'] = df_nl.apply(lambda row: find_ram_in_title(row['title']) or row['ram'], axis=1)
    dfm = list(df_nl['model'].unique())
    df_nl['Model'] = df_nl.apply(lambda row: find_model_in_title(row['title'], dfm) or row['model'], axis=1)
    df_nl['ram'] = df_nl['ram'].fillna(df_nl['RAM'])
    df_nl['storage'] = df_nl['storage'].fillna(df_nl['Storage'])
    df_nl['model']= df_nl['model'].fillna(df_nl['Model'])
    df_nl['cpu'] = df_nl['cpu'].fillna(df_nl['CPU'])
    df_nl=df_nl.drop(['Storage','CPU','RAM','Model'], axis=1)
    df_nl['storage'] = df_nl['storage'].apply(convert_to_gb)
    df_nl['ram'] = df_nl['ram'].apply(convert_to_gb)
    df_nl['screen size'] = df_nl['screen size'].apply(convert_screen_size)
    df_nl[['width resolution', 'height resolution']] = df_nl['resolution'].apply(convert_resolution).apply(pd.Series)
    df_nl['price'] = df_nl['price'].apply(convert_price_before).apply(lambda x: change_price_to_USD(x, EUR_USD))
    df_nl['price before promotion'] = df_nl['price before promotion'].apply(convert_price_before).apply(lambda x: change_price_to_USD(x, EUR_USD))
    df_nl['rate'] = df_nl['rate'].apply(convert_rate)
    df_nl['currancy'] = df_nl['currancy'].apply(change_to_USD)
     
    df2 =pd.DataFrame(df_nl)  
    df2=df2.to_json(orient='columns')     
    return df2
    #return df_nl.to_dict(orient='list')
