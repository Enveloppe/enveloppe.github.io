from bs4 import BeautifulSoup


def on_post_page(output, page, config) -> str:
    soup = BeautifulSoup(output, "html.parser")
    for a_tag in soup.find_all("a", {"class": "ezlinks_not_found"}):
        a_tag["class"] = a_tag.get("class", []) + ["ezlinks_not_found"]
        new_tag = soup.new_tag("span")
        new_tag.string = a_tag.string or a_tag.get("href", "File not found")
        for attr in a_tag.attrs:
            if attr != "href":
                new_tag[attr] = a_tag[attr]
        new_tag["src"] = a_tag["href"]
        a_tag.replaceWith(new_tag)
    return str(soup)
