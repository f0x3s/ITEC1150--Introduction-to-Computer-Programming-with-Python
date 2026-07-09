# module 7 lab part 2
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/9/26 - foxes
# modified 7/9/26 - foxes
#
# description: Book Collection

library = set()

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

    return False

def addBook(collection, title, author, genre, isbn, tags) :

    if isbnConflict(collection, isbn):
        print("ISBN is already taken.")
        return
    
    book = {}
    book["title"] = title
    book["author"] = author
    book["genre"] = genre
    book["tags"] = tupleToSet(tags)
    
    return collection.append(book)

