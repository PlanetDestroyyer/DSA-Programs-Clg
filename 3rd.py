class Subsection:
    def __init__(self, name):
        self.name = name
        self.subsections = []

class Section:
    def __init__(self, name):
        self.name = name
        self.subsections = []

class Chapter:
    def __init__(self, name):
        self.name = name
        self.sections = []

class Book:
    def __init__(self, name):
        self.name = name
        self.chapters = []

def create_books(num_books):
    books = []
    for i in range(num_books):
        book_name = input(f"Enter the name of Book {i+1}: ")
        book = Book(book_name)
        books.append(book)
    return books

def create_chapters(num_chapters):
    chapters = []
    for i in range(num_chapters):
        chapter_name = input(f"Enter the name of Chapter {i+1}: ")
        chapter = Chapter(chapter_name)
        chapters.append(chapter)
    return chapters

def create_sections(num_sections):
    sections = []
    for i in range(num_sections):
        section_name = input(f"Enter the name of section {i+1}: ")
        section = Section(section_name)
        sections.append(section)
    return sections

def create_subsections(num_subsections):
    subsections = []
    for i in range(num_subsections):
        subsection_name = input(f"Enter the name of subsection {i+1}: ")
        subsection = Subsection(subsection_name)
        subsections.append(subsection)
    return subsections

def construct_tree(book, num_chapters, num_sections, num_subsections):
    for chapter in create_chapters(num_chapters):
        chapter.sections.extend(create_sections(num_sections))
        for section in chapter.sections:
            section.subsections.extend(create_subsections(num_subsections))
        book.chapters.append(chapter)

def print_subsection(subsection, depth=3):
    print(" " * depth + subsection.name)

def print_section(section, depth=2):
    print(" " * depth + section.name)
    for subsection in section.subsections:
        print_subsection(subsection, depth + 1)

def print_chapter(chapter, depth=1):
    print(" " * depth + chapter.name)
    for section in chapter.sections:
        print_section(section, depth + 1)

def print_tree(book):
    print(book.name)
    for chapter in book.chapters:
        print_chapter(chapter)

num_books = int(input("How many books do you want? "))
num_chapters = int(input("How many chapters do you want to create for each book? "))
num_sections = int(input("How many sections do you want to create for each chapter? "))
num_subsections = int(input("How many subsections do you want to create for each section? "))

books = create_books(num_books)
for book in books:
    construct_tree(book, num_chapters, num_sections, num_subsections)

for book in books:
    print_tree(book)
