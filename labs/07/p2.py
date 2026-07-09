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

def isbnConflict(collection, testISBN) :

    seenFlag = False

    for book in collection :
        if "isbn" in book :
            if book["isbn"] == testISBN :
                seenFlag = True
                break

    return seenFlag

def addBook(collection, title, author, genre, isbn, tags) :

    if isbnConflict(collection, isbn):
        print(f"\033[91mError: Attempted to add {title[0:10]}(...) but ISBN is already taken.\033[0m") # using ansi color escape codes for compatibility
        return collection
    
    book = {}
    book["title"] = title
    book["author"] = author
    book["genre"] = genre
    book["isbn"] = isbn
    book["tags"] = tupleToSet(tags)

    collection.append(book)

    return collection

# ai used exclusively to generate tags for each book so I could quickly create a large library to test later functions
# other book information sourced from https://isbnsearch.org/isbn/9781199370785
# books from my personal library

library = addBook(library, "Aye, and Gomorrah", "Samuel R. Delany", SCIFI, 9780375706714, 
                  {"New Wave science fiction", 
                    "speculative fiction", 
                    "queer science fiction", 
                    "queer futurism", 
                    "Afrofuturism",})

library = addBook(library, "Myth and Guilt: The Crime and Punishment of Mankind", "Theodor Reik", CRIT, 9781199370785, 
                  {"film studies",                                                                                                             
                    "mora; psychology", 
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
print(library)