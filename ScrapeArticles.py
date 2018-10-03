import json,urllib,Browser

class Scrape_Articles():
    
    def __init__(self,browser):
        
        with open('Websites.json','r') as json_file:
            self.all_websites = json.load(json_file)
        
        self.browser = browser
            
        
    def dump_to_json(self,hyperlinks):
        
        with open('search_hyperlinks.json','w') as outfile:
            json.dump(hyperlinks,outfile)
        
    def read_article_names(self,filename):
        
        self.article_names = []
        
        with open(filename,'r') as f:
            for line in f:
                self.article_names.append(line)
                
        return self.article_names
    
    def google_search_results(self,query):
        
        self.search_hyperlinks = {}
        query_copy = query
        
        
        for key in self.all_websites:
            
            self.search_hyperlinks[key] = []
            for website in self.all_websites[key]:
                
                query = query + ' site: '+str(website)
                try:
                    for result in self.browser.search(query):
                        self.search_hyperlinks[key].append(result)
                except urllib.error.HTTPError as httperr:
                    print(httperr.headers)  
                    print(httperr.read())
                
                query = query_copy
                
        self.dump_to_json(self.search_hyperlinks)
        
    def read_article_content(self):
        
        
        
browser_object = Browser.Browser()
obj = Scrape_Articles(browser_object)
name = obj.read_article_names('ArticleNames.txt')

obj.google_search_results(name[0])
print(obj.search_hyperlinks['Left'])