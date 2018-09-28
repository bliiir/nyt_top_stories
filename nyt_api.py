# https://developer.nytimes.com/top_stories_v2.json
# https://api.nytimes.com/svc/topstories/v2/home.json?api-key=d4c336d4ec5c47098500255219c96a7e

import json, sys, requests, os, mysql.connector as mc

class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']

        if method == "GET" and path == "/stories":
            return json.dumps(self.get_results())

        elif method == 'GET' and path == "/load":
            return json.dumps(self.retreive_top_stories())

        return "Your request is invalid. Please try a different URL"

    def get_pic(self, article):
        width = 0
        image_url = ""
        for img in article['multimedia']:
            if img['width'] > width:
                image_url = img['url']
                width = img['width']
        return image_url

    def retreive_top_stories(self):
        mydb = self._connect()
        r = requests.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key=d4c336d4ec5c47098500255219c96a7e", json=True)
        data_dict = r.json()
        articles = data_dict["results"]
        for article in articles:
            self.data_insert(article['title'], article['abstract'], article['published_date'], article['short_url'], self.get_pic(article))

        mydb.close()
        return data_dict

    def data_insert(self, title, abstract, published_date, short_url, image_url):
        mydb = self._connect()
        mycursor = mydb.cursor()

        try:
            insert = "INSERT INTO topstories (title, abstract, published_date, short_url, image_url) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(insert, (title, abstract, published_date, short_url, image_url))
            mydb.commit()

        except Exception as exc: print(exc)
        finally: mydb.close() # mycursor.close()

    def get_results(self):
        mydb = self._connect()
        mycursor = mydb.cursor()

        try:
            mycursor.execute("SELECT * FROM topstories")
            my_result = mycursor.fetchall()

        except Exception as exc:
            print(exc)
        finally:
            mydb.close() # mycursor.close()

        #mydb.close()
        return my_result

    def _connect(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password = os.environ.get("MYSQL_PASSWORD"),
            database="ny_articles_in_classs"
            )
        return(mydb)

