import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
from collections import defaultdict

def main(param ) :
    category_name_list = []
    all_phones_pages_link_list = []
    all_phones_link_list = []
    all_headphones_pages_link_list = []
    all_headphones_link_list = []
    all_covers_pages_link_list = []
    all_covers_link_list = []
    all_screens_pages_link_list = []
    all_screens_link_list = []
    all_power_banks_pages_link_list = []
    all_power_banks_link_list = []
    all_chargers_pages_link_list = []
    all_chargers_link_list = []
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}
    def scrape_proxies(url, limit=30):
        try:
            # Fetch the webpage content
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all table rows
            rows = soup.find_all('tr')
            
            # Extract IP and Port from each row and format as requested
            proxies = [
                {'http': f"{row.find_all('td')[0].text}:{row.find_all('td')[1].text}"}
                for row in rows[:limit]
                if len(row.find_all('td')) >= 2
            ]
            
            return proxies
        
        except requests.RequestException as e:
            print(f"An error occurred while fetching the webpage: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    mohamed = "https://free-proxy-list.net"  # Replace with the actual mohamed
    proxies = scrape_proxies(mohamed)

    for i in range(1,11):
        product_link = f'https://www.amazon.eg/-/en/s?i=electronics&rh=n%3A21832883031%2Cp_123%3A110955%7C1500397%7C329744%7C338933%7C339703%7C367594%7C46655%7C559198%7C568349%7C723042&s=featured-rank&dc&fs=true&page={i}&language=en&qid=1723650023&ref=sr_pg_{i}'
        all_phones_pages_link_list.append(product_link)
    proxy_failures = defaultdict(int)
    MAX_FAILURES = 25
    def get_proxy():
        working_proxies = [p for p, failures in proxy_failures.items() if failures < MAX_FAILURES]
        return random.choice(working_proxies) if working_proxies else None


    def get_text_or_none(tag, attribute_name=None):
        if tag:
            if attribute_name:
                return tag.get(attribute_name, None)
            return tag.get_text(strip=True)
        return None
    def make_request(url, max_retries=5):        
        for attempt in range(max_retries):
            proxy = get_proxy()
            if not proxy:
                print("No working proxies available. Trying without proxy.")
                try:
                    response = requests.get(url, headers=headers, timeout=30)
                    response.raise_for_status()
                    return response
                except requests.RequestException as e:
                    print(f"Attempt {attempt + 1} failed without proxy: {e}")
                    time.sleep(random.uniform(1, 3))
                    continue

            try:
                response = requests.get(url, headers=headers, proxies={'http': proxy}, timeout=30)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"Attempt {attempt + 1} failed with proxy {proxy}: {e}")
                proxy_failures[proxy] += 1
                if proxy_failures[proxy] >= MAX_FAILURES:
                    print(f"Proxy {proxy} has failed {MAX_FAILURES} times and will no longer be used.")
                time.sleep(random.uniform(1, 3))
        
        raise Exception(f"Failed to retrieve {url} after {max_retries} attempts")

    def get_all_phones_link(link, max_retries=8):
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                page = make_request(link)
                soup = BeautifulSoup(page.content, "html.parser")
                all_phones = soup.find_all("div", class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
                
                if all_phones:
                    for phone in all_phones:
                        phone_link = phone.find_all("a")[0].get("href")
                        phone_link = f"https://www.amazon.eg{phone_link}"
                        all_phones_link_list.append(phone_link)
                    
                    print(f"Found {len(all_phones)} phones on page {link}")
                    return
                
                else:
                    retry_count += 1
                    print(f"No phones found on page {link}, retrying... ({retry_count}/{max_retries})")
                    time.sleep(random.uniform(1, 3))  # Random delay before retrying

            except Exception as e:
                print(f"Error getting phone links from {link}: {e}")
                retry_count += 1
                time.sleep(random.uniform(1, 3))  # Random delay before retrying
        
        print(f"Failed to find phones on {link} after {max_retries} retries")


    # Modified scrape_product_data function
    def scrape_product_data(link, max_retries=20):
        for attempt in range(max_retries):
            time.sleep(random.uniform(1, 3))
            try:
                page = make_request(link)
                soup = BeautifulSoup(page.content, "html.parser")

            
                camera_info = None
                for li in soup.find_all('li', class_='a-spacing-mini'):
                    if 'MP' in li.text:
                        camera_info = re.search(r'(\d+MP)', li.text)
                        if camera_info:
                            camera_info = camera_info.group(1)
                            break
        
                color_row = soup.find('tr', class_='a-spacing-small po-color')
                color = None  # Initialize color
                if color_row:
                    # If the color row exists, find the span inside it and get the text
                    color = get_text_or_none(color_row.find('span', class_='a-size-base po-break-word'))
                
                elif soup.find('table', id ='productDetails_techSpec_section_1'):
                    color_row2 = soup.find('th', string='Color')
                    if color_row2:
                        color = color_row2.find_next('td').get_text(strip=True)
                
                else:
                    # Check for color in div with id='variation_color_name'
                    outerSelect = soup.find('div', id='variation_color_name')
                    if outerSelect:
                        selection_row = outerSelect.find('span', class_='selection')
                        if selection_row:
                            color = get_text_or_none(selection_row)
        
                price = get_text_or_none(soup.find('div', class_='a-section a-spacing-micro').find('span', class_='a-offscreen')
                            if soup.find('div', class_='a-section a-spacing-micro') else None)
                if not price:
                    price = get_text_or_none(soup.find('span', class_='a-price-whole'))
        
                Website = 'Amazon EG'
                Currency = 'EGP'
        
                # Extract other product data
                data = {
                    # "category": category_name_list[0] if category_name_list else "unknown-category",
                    "Title": get_text_or_none(soup.find('span', id='productTitle')),
                    "Brand": get_text_or_none(soup.find('tr', class_='a-spacing-small po-brand').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-brand') else None),
                    "OS": get_text_or_none(soup.find('tr', class_='a-spacing-small po-operating_system').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-operating_system') else None),
                    "RAM": get_text_or_none(soup.find('tr', class_='a-spacing-small po-ram_memory.installed_size').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-ram_memory.installed_size') else None),
                    "CPU": get_text_or_none(soup.find('tr', class_='a-spacing-small po-cpu_model.family').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-cpu_model.family') else None),
                    "Storage": get_text_or_none(soup.find('tr', class_='a-spacing-small po-memory_storage_capacity').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-memory_storage_capacity') else None),
                    "Screen Size": get_text_or_none(soup.find('tr', class_='a-spacing-small po-display.size').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-display.size') else None),
                    "Resolution": get_text_or_none(soup.find('tr', class_='a-spacing-small po-resolution').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-resolution') else None),
                    "CPU Speed": get_text_or_none(soup.find('tr', class_='a-spacing-small po-cpu_model.speed').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-cpu_model.speed') else None),
                    "Model": get_text_or_none(soup.find('tr', class_='a-spacing-small po-model_name').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-model_name') else None),
                    "Wireless Provider": get_text_or_none(soup.find('tr', class_='a-spacing-small po-wireless_provider').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-wireless_provider') else None),
                    "Cellular Technology": get_text_or_none(soup.find('tr', class_='a-spacing-small po-cellular_technology').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-cellular_technology') else None),
                    "Color": color,
                    "Refresh Rate": get_text_or_none(soup.find('tr', class_='a-spacing-small po-refresh_rate').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-refresh_rate') else None),
                    "SIM Count": get_text_or_none(soup.find('tr', class_='a-spacing-small po-sim_card_slot_count').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-sim_card_slot_count') else None),
                    "Wireless Technology": get_text_or_none(soup.find('tr', class_='a-spacing-small po-wireless_network_technology').find('span', class_='a-size-base po-break-word') if soup.find('tr', class_='a-spacing-small po-wireless_network_technology') else None),
                    "Price": price,
                    "Price Before Promotion": get_text_or_none(soup.find('span', class_='a-price a-text-price').find('span', class_='a-offscreen') if soup.find('span', class_='a-price a-text-price') else None),
                    "Rate": get_text_or_none(soup.find('span', class_='a-icon-alt')),
                    "Camera": camera_info,
                    "IMG": get_text_or_none(soup.find('img', class_='a-dynamic-image'), 'data-old-hires') or get_text_or_none(soup.find('img', class_='a-dynamic-image'), 'src'),
                    "Website" : Website,
                    'Currancy' : Currency,
                    "URL" : link
                }
        
                # Extract reviews
                reviews_from_egypt = []
                reviews_outside_egypt = []
        
                review_elements = soup.find_all("div", class_="a-section review aok-relative")
                for review in review_elements:
                    reviewer_name = get_text_or_none(review.find("span", class_="a-profile-name"))
                    rating = get_text_or_none(review.find("span", class_="a-icon-alt"))
                    review_date = get_text_or_none(review.find("span", class_="a-size-base a-color-secondary review-date"))
                    review_text = get_text_or_none(review.find("span", class_="a-size-base review-text review-text-content"))
                    
                    review_info = f"Name: {reviewer_name}, Rating: {rating}, Date: {review_date}, Review: {review_text}"
                    
                    if "Verified Purchase" in review.text:
                        reviews_from_egypt.append(review_info)
                    else:
                        reviews_outside_egypt.append(review_info)
        
                data["Reviews"] = reviews_from_egypt
                if data['Title']:
                    print(f"Successfully scraped data for {data['Title']}")
                    return data
                else:
                    print(f"No title found for {link}, retrying... (Attempt {attempt + 1}/{max_retries})")
            except Exception as e:
                print(f"Error scraping {link}: {e}. Retrying... (Attempt {attempt + 1}/{max_retries})")
        
        print(f"Failed to scrape {link} after {max_retries} attempts")
        return None


    # Main execution
        # Get all phone links with retries on individual pages
    for proxy in proxies:
        proxy_failures[proxy['http']] = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_all_phones_link, all_phones_pages_link_list)
    
    print(f"Total phone links found: {len(all_phones_link_list)}")
    
    if len(all_phones_link_list) == 0:
        print("No phone links found. Exiting...")
    else:
        # Scrape product data
        results = []
        with ThreadPoolExecutor(max_workers=25) as executor:
            future_to_url = {executor.submit(scrape_product_data, url): url for url in all_phones_link_list}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    if data:
                        results.append(data)
                except Exception as exc:
                    print(f'{url} generated an exception: {exc}')
        
        print(f"Successfully scraped data for {len(results)} phones")
        
        df1 = pd.DataFrame(results)
        
        if not df1.empty:
            print("Data scraping and saving completed.")
        else:
            print("No data was scraped. Check the logs for errors.")
    df2 =df1.to_json(orient='columns')        
    return df2