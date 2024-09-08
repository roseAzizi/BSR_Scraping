import pandas as pd   
import asyncio 
from playwright.async_api import async_playwright 

#put somehwere else later, dictionary to access amazon catagory types 
catagory_dict = {
    "movies": { 
        "bbn" : "917972",
        "rhn" : "3A917972" 
    }, 
    "Toys": { 
        "bbn" : "6205517011", 
        "rhn" : "3A6205517011" 
    }
}

def createDF(): 
    column_specs = { 
       'BSR Catagory': str,
       'Title': str,
       'UPC': str,  
       'ASIN': str,  
       'BSR Rank': str
    } 
    df = pd.DataFrame(columns = column_specs)  
    return df  

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()

if __name__ == "__main__": 
    asyncio.run(main()) 
