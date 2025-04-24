CURRENT_YEAR = 2025

class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def is_recent(self, n):
        return (CURRENT_YEAR - self.year) <= n

class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages  = pages

    def __str__(self):
        return f"Book -> {super().__str__()}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi     = doi

    def __str__(self):
        return f"Article -> {super().__str__()}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host     = host
        self.duration = duration

    def __str__(self):
        return f"Podcast -> {super().__str__()}, Host: {self.host}, Duration: {self.duration} mins"

def save_to_file(items, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in items:
            if isinstance(item, Book):
                line = f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n"
            elif isinstance(item, Article):
                line = f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n"
            elif isinstance(item, Podcast):
                line = f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n"
            else:
                continue
            f.write(line)

def load_from_file(filename):
    items = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            typ = parts[0]
            if typ == "Book":
                _, uid, title, year, author, pages = parts
                items.append(Book(uid, title, int(year), author, int(pages)))
            elif typ == "Article":
                _, uid, title, year, journal, doi = parts
                items.append(Article(uid, title, int(year), journal, doi))
            elif typ == "Podcast":
                _, uid, title, year, host, duration = parts
                items.append(Podcast(uid, title, int(year), host, int(duration)))
    return items

if __name__ == "__main__":
    items = [
        Book("B001", "Deep Learning",       2018, "Ian Goodfellow", 775),
        Book("B002", "Python Tricks",       2021, "Dan Bader",      302),
        Article("A101", "Quantum Computing",2022, "Nature",         "10.1234/qc567"),
        Article("A102", "AI Ethics",        2020, "Science",        "10.5678/ai890"),
        Podcast("P301", "TechTalk AI",      2023, "Jane Doe",        45),
        Podcast("P302", "History Hour",     2019, "John Smith",      60),
    ]

    save_to_file(items, "archive.txt")
    loaded = load_from_file("archive.txt")

    for it in loaded:
        print(it)
    print()

    print("Recent Items:")
    for it in loaded:
        if it.is_recent(5):
            print(it)
    print()

    print("Articles with DOI starting '10.1234':")
    for it in loaded:
        if isinstance(it, Article) and it.doi.startswith("10.1234"):
            print(it)
