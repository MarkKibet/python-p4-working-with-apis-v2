import requests
import json


class Search:
    def get_user_search_results(self):
        
        search_term = input("Enter a book title to search: ")

    
        search_term_formatted = search_term.replace(" ", "+")

        
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 5  

        
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        
        response = requests.get(URL)
        return response.json()



if __name__ == "__main__":
    search = Search()
    user_results = search.get_user_search_results()

    
    print(json.dumps(user_results, indent=2))
