# module 7 lab part 2
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/9/26 - foxes
# modified 7/9/26 - foxes
#
# description: Book Collection

library = []
SCIFI = "Science Fiction"
CRIT = "Critical Theory"
ART = "Art Book"
FICT = "Fiction"


def tupleToSet(tuple) :
    # avoiding set() function call for performance
    return {*(tuple)}

# depricated 
def isbnConflict(collection, testISBN) :

    seenFlag = False

    for book in collection :
        if "isbn" in book :
            if book["isbn"] == testISBN :
                seenFlag = True
                break

    return seenFlag

def addBook(collection, title, author, genre, isbn, tags) :
    if bookWithIsbn(collection, isbn): # optional extension 
        print(f"\033[91mError: Attempted to add {title[0:10]}(...) but ISBN is already taken.\033[0m") # using ansi color escape codes for compatibility
        return collection
    
    book = {}
    book["title"] = title
    book["author"] = author
    book["genre"] = genre
    book["isbn"] = isbn
    book["tags"] = tupleToSet(tags)

    collection.append(book)
    if title != "testTitle" :
        print(f"\x1b[32mSUCCESS: Added: {title[0:10]}(...) to library\x1b[0m") # using ansi color escape codes for compatibility

    return collection

def booksWithTags(collection, tags) :
    books = []

    for book in collection :
        if tags.issubset(book["tags"]) :
            books.append(book)

    return books

def bookWithIsbn(collection, isbn):
    found = ()

    for book in collection :
        if isbn == book["isbn"] :
            found = (book["title"], book["author"]) 
    return found

# used for human-readable output
def searchByTags(collection, tags) :
    print("\nsearching for tags: " + ", ".join(tags) + "...")
    match = booksWithTags(collection, tags)

    if len(match) < 1 :
        print("Unfortunately, no books in our collecton match the tags requested.")
        return
    
    print("\nYou may enjoy: ")

    for index, book in enumerate(match):
        print(f"{index + 1}. {book["title"]} by {book["author"]}")

def searchByIsbn(collection, isbn) :
    print(f"\nSearching for ISBN: {isbn}")

    found =  bookWithIsbn(collection, isbn)
    if found :
        print("We have: ")
        print(f"{found[0]} by {found[1]} in our collection.")
    else :
        print("We do not have any books matching the ISBN requested.")
        
# tests
testCollection = []
testBook = {
    "title": "testTitle",
    "author": "testAuthor",
    "genre": "testGenre",
    "isbn": 1234,
    "tags": {"t1", "t2", "t3", "t4"}
}
try :
    assert addBook(testCollection, testBook["title"], testBook["author"], testBook["genre"], testBook["isbn"], testBook["tags"]) == [testBook], "adding book to collection function failed"
    assert tupleToSet((1,2)) == {1,2}, "tuple to set function failed"
    assert bookWithIsbn(testCollection, 1234) == (testBook["title"], testBook["author"]), "search by isbn function failed"
    assert booksWithTags(testCollection, {"t1"}) == [testBook], "search by tags function failed"
    print("All unit tests passed. Starting program...\n")

except AssertionError as e :
    print(f"\033[91m{e}\033[0m")
    quit()

# ai used exclusively to generate tags for each book so I could quickly create a large library to test later functions
# other book information sourced from https://isbnsearch.org/isbn/9781199370785
# books from my personal library
print("Adding books to library...")

library = addBook(library, "Aye, and Gomorrah", "Samuel R. Delany", SCIFI, 9780375706714, 
                  {"New Wave science fiction", 
                    "speculative fiction", 
                    "queer science fiction", 
                    "queer futurism", 
                    "Afrofuturism",})

library = addBook(library, "Myth and Guilt: The Crime and Punishment of Mankind", "Theodor Reik", CRIT, 9781199370785, 
                  {"film studies",                                                                                                             
                    "moral psychology", 
                    "German Expressionism", 
                    "Weimar cinema", 
                    "crime and guilt"})

library = addBook(library, "Cyberfeminism Index", "Mindy Seu", CRIT, 9781941753514,
                  {"cyberfeminism",
                   "feminist internet history",
                   "digital activism",
                   "net art",
                   "techno-critical theory"})

library = addBook(library, "Dyani White Hawk: Love Language", "Tarah Hogue and Siri Engberg", ART, 9781935963349,
                  {"contemporary Indigenous art",
                   "Lakota visual culture",
                   "abstraction",
                   "beadwork and quillwork",
                   "exhibition catalogue"})

library = addBook(library, "A Canticle for Leibowitz", "Walter M. Miller Jr.", SCIFI, 9780060892999,
                  {"post-apocalyptic fiction",
                   "monastic preservation",
                   "speculative fiction",
                   "nuclear war",
                   "religion and science",
                   "cyclical history"})

library = addBook(library, "God Bless You, Mr. Rosewater", "Kurt Vonnegut", FICT, 9780385333474,
                  {"satire",
                   "wealth inequality",
                   "philanthropy",
                   "American capitalism",
                   "postmodern fiction"})

library = addBook(library, "Glitch Feminism: A Manifesto", "Legacy Russell", CRIT, 9781786632661,
                  {"cyberfeminism",
                   "gender and technology",
                   "digital embodiment",
                   "queer theory",
                   "manifesto"})

library = addBook(library, "This Can't Be the Place: Alternative Theories of the Internet", "August Kaasa Sundgaard and Ruben Stoffelen", CRIT, 9789083672120,
                  {"internet culture",
                   "network theory",
                   "digital politics",
                   "platform critique",
                   "techno-critical theory"})

# intentional duplicate book to test duplicate isbn rejection
library = addBook(library, "Glitch Feminism: A Manifesto", "Legacy Russell", CRIT, 9781786632661,
                  {"cyberfeminism",
                   "gender and technology",
                   "digital embodiment",
                   "queer theory",
                   "manifesto"})

# search by tags
tagsToSearch1 = {"techno-critical theory"}
tagsToSearch2 = {"speculative fiction"}

tagsToSearch3 = {"speculative fiction", "Afrofuturism"}
tagsToSearch4 = {"cyberfeminism", "techno-critical theory"}

searchByTags(library, tagsToSearch1)
searchByTags(library, tagsToSearch2)
searchByTags(library, tagsToSearch3)
searchByTags(library, tagsToSearch4)

# search by isbn
isbn1 = 9781935963349
isbn2 = 9781945963349 # does not exist 

searchByIsbn(library, isbn1)
searchByIsbn(library, isbn2)