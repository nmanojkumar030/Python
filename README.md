# Python Learning Repository

A comprehensive collection of Python code examples, documentation, and learning resources organized for efficient learning and reference.

## 📁 Project Structure

```
Python/
├── python_concepts/          # Organized Python code examples
├── python-documents/         # Learning materials and documentation
├── python-exercise/          # Practice exercises and problems
└── README.md                 # This file
```

## 🚀 Quick Start

### For Beginners
1. Start with `python_concepts/01_data_structures/` for basic concepts
2. Use `python-documents/01_books_and_references/` for comprehensive learning
3. Practice with `python-exercise/` problems

### For Intermediate Users
1. Explore `python_concepts/04_functional_programming/` and `05_object_oriented_programming/`
2. Reference `python-documents/03_official_documentation/` for authoritative information
3. Use `python-documents/04_how_to_guides/` for specific implementation help

### For Advanced Users
1. Dive into `python_concepts/06_generators_iterators/` and advanced topics
2. Study `python-documents/05_advanced_topics/` for specialized knowledge
3. Explore design patterns in `python_concepts/10_design_patterns/`

## 📚 Python Concepts (`python_concepts/`)

Organized into 13 logical categories with 108+ code examples:

### 01_data_structures/ (15 files)
Lists, Dictionaries, Tuples, and Set operations
- List access methods, creation, searching, slicing
- Dictionary fundamentals and advanced operations
- Tuple operations and negative indexing
- Data structure demonstrations

### 02_string_operations/ (11 files)
String manipulation, formatting, and processing
- Basic and advanced string operations
- String formatting and tokenization
- String transformation and processing utilities
- Quote formatting examples

### 03_functions/ (5 files)
Function definitions, arguments, and scope
- Function fundamentals and usage examples
- Keyword arguments and variable arguments
- Variable scope demonstrations

### 04_functional_programming/ (11 files)
Lambda functions, map, filter, reduce, and functional concepts
- Lambda function basics and advanced usage
- Map, filter, and reduce function examples
- Functional programming concepts and patterns

### 05_object_oriented_programming/ (11 files)
Classes, inheritance, polymorphism, and OOP concepts
- OOP fundamentals and class basics
- Encapsulation, inheritance, and polymorphism demos
- Employee and person class examples
- Method resolution order and multiple inheritance

### 06_generators_iterators/ (7 files)
Generator functions, expressions, and iterator patterns
- Generator fundamentals and examples
- Generator expressions and functions
- Iterator patterns and parallel iteration

### 07_file_operations/ (12 files)
File I/O, directory operations, and file utilities
- File I/O operations and archiving
- Directory walking and traversal utilities
- Tail file utilities and JSON processing
- Pickle file examples

### 08_csv_processing/ (4 files)
CSV file reading, writing, and processing
- Basic and advanced CSV reading
- Pandas CSV processing
- CSV writing examples

### 09_regular_expressions/ (6 files)
Regex patterns, matching, and text processing
- Greedy vs non-greedy matching
- Pattern matching and character classes
- Quantifiers, groups, and substitution

### 10_design_patterns/ (3 files)
Singleton pattern and other design patterns
- Singleton pattern implementations (v2, v3, alternative)

### 11_testing/ (2 files)
Unit testing examples and test cases
- Unit test examples and test case demonstrations

### 12_utilities_demos/ (13 files)
Various utility programs and demonstrations
- Integer operations and I/O demos
- Loop control and greeting programs
- Countdown songs and validators
- SSH client utilities and standard library examples

### 13_vowel_counters/ (8 files)
Various approaches to counting vowels in text
- Basic, function-based, dictionary, set approaches
- Comprehension and advanced approaches
- Vowel search utilities and modules

## 📖 Python Documents (`python-documents/`)

Organized into 8 categories with 50+ learning materials:

### 01_books_and_references/ (6 documents)
Complete books and comprehensive learning materials
- Python books, academic textbooks, web development guides
- Introduction materials and comprehensive references

### 02_cheatsheets_and_quick_references/ (3 documents)
Quick reference guides and cheat sheets
- Python quick references and cheat sheets for immediate lookups

### 03_official_documentation/ (7 documents)
Official Python Software Foundation documentation
- Tutorial, reference, library documentation, installation guides

### 04_how_to_guides/ (16 documents)
Practical tutorials for specific topics
- How-to guides for argparse, logging, regex, sockets, web servers, and more

### 05_advanced_topics/ (4 documents)
Advanced Python topics and specialized documentation
- C API, distribution, extending Python, virtual environments

### 06_course_materials/ (12 documents)
Structured educational content and handouts
- Progressive learning modules from fundamentals to advanced concepts

### 07_lambda_and_functional_programming/ (2 documents)
Lambda functions and functional programming concepts
- Specialized materials for functional programming approaches

### 08_images_and_diagrams/ (1 document)
Visual learning materials and diagrams
- Python execution model and visual aids

## 💻 Python Exercises (`python-exercise/`)

Practice problems and exercises for hands-on learning:
- Programming challenges and problems
- Intermediate and advanced exercises
- Practical coding scenarios

## 🎯 Learning Paths

### Beginner Path
1. **Start Here:** `python_concepts/01_data_structures/`
2. **Learn Functions:** `python_concepts/03_functions/`
3. **String Operations:** `python_concepts/02_string_operations/`
4. **Read:** `python-documents/01_books_and_references/`
5. **Practice:** `python-exercise/`

### Intermediate Path
1. **OOP Concepts:** `python_concepts/05_object_oriented_programming/`
2. **Functional Programming:** `python_concepts/04_functional_programming/`
3. **File Operations:** `python_concepts/07_file_operations/`
4. **CSV Processing:** `python_concepts/08_csv_processing/`
5. **Reference:** `python-documents/03_official_documentation/`

### Advanced Path
1. **Generators & Iterators:** `python_concepts/06_generators_iterators/`
2. **Regular Expressions:** `python_concepts/09_regular_expressions/`
3. **Design Patterns:** `python_concepts/10_design_patterns/`
4. **Advanced Topics:** `python-documents/05_advanced_topics/`
5. **How-to Guides:** `python-documents/04_how_to_guides/`

## 🔍 Finding What You Need

### By Topic
- **Data Structures:** `python_concepts/01_data_structures/`
- **Strings:** `python_concepts/02_string_operations/`
- **Functions:** `python_concepts/03_functions/`
- **OOP:** `python_concepts/05_object_oriented_programming/`
- **File I/O:** `python_concepts/07_file_operations/`
- **Regex:** `python_concepts/09_regular_expressions/`
- **Testing:** `python_concepts/11_testing/`

### By Document Type
- **Books:** `python-documents/01_books_and_references/`
- **Quick Reference:** `python-documents/02_cheatsheets_and_quick_references/`
- **Official Docs:** `python-documents/03_official_documentation/`
- **How-to Guides:** `python-documents/04_how_to_guides/`
- **Course Materials:** `python-documents/06_course_materials/`

## 🛠️ Running the Examples

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python syntax

### Running Code Examples
```bash
# Navigate to a specific concept folder
cd python_concepts/01_data_structures/

# Run a specific example
python list_basic_operations.py

# Run all examples in a folder
for file in *.py; do
    echo "Running $file..."
    python "$file"
done
```

### Viewing Documentation
```bash
# Open documentation in your preferred PDF viewer
open python-documents/01_books_and_references/python-book.pdf

# Or use a command-line PDF viewer
# brew install mupdf  # macOS
# mupdf python-documents/01_books_and_references/python-book.pdf
```

## 📝 Contributing

This repository is organized for learning purposes. Each folder contains:
- **README.md** - Explains the contents and purpose
- **Code Examples** - Practical implementations
- **Documentation** - Learning materials and references

## 🎓 Learning Tips

1. **Start Small:** Begin with basic concepts and gradually progress
2. **Practice Regularly:** Use the exercise folder for hands-on practice
3. **Read Documentation:** Reference official docs for authoritative information
4. **Experiment:** Modify examples to understand concepts better
5. **Build Projects:** Apply concepts to real-world scenarios

## 📊 Repository Statistics

- **Total Code Examples:** 108+ Python files
- **Total Documents:** 50+ learning materials
- **Organized Categories:** 21 logical groupings
- **Learning Paths:** 3 progressive difficulty levels
- **Documentation:** Complete README files for each folder

## 🔗 Related Resources

- [Python Official Documentation](https://docs.python.org/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Real Python Tutorials](https://realpython.com/)

## 📄 License

This repository contains educational materials and examples for learning Python programming. Feel free to use these resources for educational purposes.

---

**Happy Learning! 🐍✨**

*This repository is designed to be your comprehensive Python learning companion, from basic concepts to advanced topics.*