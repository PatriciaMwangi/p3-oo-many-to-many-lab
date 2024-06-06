class Author:
    def __init__(self,name):
        self.name=name
    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]
    def books(self):
        return [book.book for book in self.contracts()]
    def sign_contract(self,book,date,royalties):
       contract= Contract(self,book,date,royalties)
       return contract
    def total_royalties(self):
        return sum(royalty.royalties for royalty in self.contracts() )
        

class Book:
    def __init__(self,title):
        self.title=title
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [author.author for author in self.contracts()]


class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
        Contract.all.append(self)
        if not isinstance(author,Author):
            raise TypeError("Author must be an instance of class Author")
        if not isinstance(book,Book):
            raise TypeError("Book must be an instance of class Book.")
        if not isinstance(date,str):
            raise ValueError("Must be a string.")
        if not isinstance(royalties,int):
            raise ValueError("Must be an integer.")
    @classmethod   
    def contracts_by_date(cls,date):
        
        return sorted([contract for contract in cls.all if contract.date==date],key=lambda contract:contract.author.name)
        
    
#key lambda function
  ## key part
    #This key function is used to extract a comparison key from each element
    #key=... specifies that the sorted function should use the result of the lambda function as the comparison key.
    #Without this key function, sorted would attempt to compare Contract objects directly, which raises an error because Python doesn't know how to compare these objects by default.
  ##lambda part      
    #lambda contract: contract.author.name is a small anonymous function (lambda) that takes a single parameter contract and returns the name attribute of the author associated with the contract.
    #In this context, contract is each individual Contract object in the list.
