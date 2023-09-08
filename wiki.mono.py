import urllib.request
import time

def get_wiki_page_existence(wiki_page_url):
    try:
        response = urllib.request.urlopen(wiki_page_url)
        page_status = "unknown"

        if response.getcode() == 200:
            page_status = "Existe"
        elif response.getcode() == 404:
            page_status = "Não existe"

        return f"{wiki_page_url} - {page_status}"
    except Exception as error:
        return f"{wiki_page_url} - error: {error}"

def main():
    print("Executando de forma sequencial:")

    def gerar_wiki_url(i):
        return f"https://en.wikipedia.org/wiki/{i + 1}"

    wiki_page_urls = [gerar_wiki_url(i) for i in range(50)]

    start_time = time.time()

    for url in wiki_page_urls:
        print(get_wiki_page_existence(url))

    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Tempo sequencial: {elapsed_time:.2f}s")

if __name__ == "__main__":
    main()
