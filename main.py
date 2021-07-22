import newspaper
import csv
import datetime 

url = "https://www.bloomberg.co.jp"
website = newspaper.build(url, memoize_articles = False, MAX_SUMMARY = 300)

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = 'bloomberg_' + csv_date + '.csv'
f = open(csv_file_name, 'w', encoding='cp932')
for article in website.articles:
  print(article.url)
  print(article.title)

for item in range(len(website.articles)):
    
    csvlist = []
    website_article = website.articles[item]
    try:
        website_article.download()
        website_article.parse()
        website_article.nlp()
        print("記事[" + str(item) + "]: "
                + website_article_url +" : " 
                + website_article_summary + "\n") 
        csvlist.append(str(item))
        csvlist.append(website_article_url)
        csvlist.append(website_article_summary)
        writer.writerow(csvlist)
        writer = csv.writer(f, lineterminator='\n') 
        csv_header = ["記事番号","URL","サマリー"]
        print(csvlist)
        writer.writerow(csv_header)
        
    except:
        print("記事[" + str(item) + "]: "
                + website_article.url +" : " 
                + "取得エラー" + "\n")
        continue
    f.close()