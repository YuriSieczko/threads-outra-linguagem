import threading
import urllib.request

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

def run_worker(urls, results):
    for url in urls:
        result = get_wiki_page_existence(url)
        results.append(result)

def main():
    print("Executando com Threads:")

    NUM_WORKERS = 4
    wiki_page_urls = [f"https://en.wikipedia.org/wiki/{i + 1}" for i in range(50)]

    chunk_size = len(wiki_page_urls) // NUM_WORKERS
    chunks = [wiki_page_urls[i:i+chunk_size] for i in range(0, len(wiki_page_urls), chunk_size)]

    results = []

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=run_worker, args=(chunk, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
