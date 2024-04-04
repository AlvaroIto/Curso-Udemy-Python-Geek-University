'''
Métodos mágicos são todos os métodos que utilizam dunder

__init__ -> Construtor
    def __init__(self, titulo, autor, paginas) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

__repr__ -> Representação do objeto
    def __repr__(self) -> str:
        return f'O livro {self.titulo} do autor {self.autor} contém {self.paginas} páginas'

__str__ -> Representação pro usuário final
    def __str__(self) -> str:
        return self.titulo



'''

class Livro:
    def __init__(self, titulo, autor, paginas) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self) -> str:
        return f'O livro {self.titulo} do autor {self.autor} contém {self.paginas} páginas'

    def __str__(self) -> str:
        return self.titulo
    
    def __len__(self):
        return len(self.titulo)
    
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')
    

livro1 = Livro('Python', 'Geek University', 400)
livro2 = Livro('IA', 'Geek', 350)

print(livro1)
print(livro2)
