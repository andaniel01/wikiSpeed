from TreeNode import TreeNode
from bs4 import BeautifulSoup
import requests

try:
    from urllib.parse import unquote
except ImportError:
    from urlparse import unquote


def get_url(url):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        # storing all the urls
        urls_string = []
        """
        not using it for now
        urls = []
        urls_name = []
        wiki_dict = {}
        """
        # gets all the relevant links
        urls = soup.select('p a')

        # changing to click-able links
        # also adds the string version to the urls_string
        # also checks for the type of the inputs
        for url in urls:
            suf = url.get('href')

            if suf is None:
                break
            else:
                suf = suf.encode('ascii', 'ignore')

            url = "https://en.wikipedia.org" + str(suf)
            urls_string.append(url)

        # identifies the faulty urls
        for n in range(len(urls_string)):
            if ("/wiki/" not in urls_string[n]) or ("wiktionary.org" in urls_string[n]) or \
                    (".jpg" in urls_string[n]) or (".png" in urls_string[n]) or ("BookSources" in urls_string[n]) or \
                    (".svg" in urls_string[n]) or ("ISBN" in urls_string[n]) or ("(" in urls_string[n]) or \
                    ("Category" in urls_string[n]) or ("wikidata.org" in urls_string[n]) or \
                    ("Verifiability" in urls_string[n]) or ("Portal" in urls_string[n]) or \
                    ("Citation" in urls_string[n]) or ("wikisource" in urls_string[n]) or \
                    ("File" in urls_string[n]) or ("Help" in urls_string[n]) or ("#cite" in urls_string[n]):
                urls_string[n] = "temp"

        # gets rid of all faulty urls
        for n in range(len(urls_string) - 1, 0, -1):
            if urls_string[n] == "temp":
                urls_string.remove("temp")

        # gets the "name" of the urls

        """
        for n in range(len(urls_string) - 1):
        urls_name.append(urls_string[n].replace("https://en.wikipedia.org/wiki/", "").replace("_", " "))

        creates the dictionary
        for n in range(len(urls_string) - 1):
        wiki_dict[urls_name[n]] = urls_string[n]

        for url in urls_string:
        print(url)
        print(len(urls_string))
        """
        return urls_string

    except requests.exceptions.ConnectionError:
        print("Wikipedia Overload")
    return ""


def find_shortest_path(start_node, goal_node):
    # queue initially starts with the starting point
    # queue is the array with all possible paths
    #
    visited = []
    start_node.add_links(get_url(start_node.page_link))
    queue = [[start_node]]

    if not start_node.page_link == goal_node.page_link:
        i = 0
        j = 0
        while queue:
            print(i)
            # path is the starting node
            path = queue.pop(0)
            # node checks the last path
            node = path[-1]
            if node not in visited:
                links = node.child_links
                for link in links:
                    j = j + 1
                    print(j)
                    if link != goal_node.page_link:
                        new_node = TreeNode(
                            unquote(link.replace("https://en.wikipedia.org/wiki/", "").replace("_", " ")), link)
                        new_node.add_links(get_url(new_node.page_link))

                        new_path = list(path)
                        new_path.append(new_node)

                        print(new_path[0].title)
                        queue.append(new_path)

                        if len(new_path) == 1:
                            print(new_path[0].title)
                        if len(new_path) == 2:
                            print(new_path[0].title + "->" + new_path[1].title)
                        if len(new_path) == 3:
                            print(new_path[0].title + "->" + new_path[1].title + "->" + new_path[2].title)
                    else:
                        return "done"

                visited.append(node)
            i = i + 1


def main():
    # test cases
    node1 = TreeNode("Acoustic Kitty", "https://en.wikipedia.org/wiki/Acoustic_Kitty")
    node2 = TreeNode("Population control", "https://en.wikipedia.org/wiki/Animal_population_control")
    print(find_shortest_path(node1, node2))


if __name__ == "__main__":
    main()
