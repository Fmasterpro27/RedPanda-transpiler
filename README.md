# 🐼 RedPanda Transpiler

<p align="center">
  <img src="https://raw.githubusercontent.com/Fmasterpro27/RedPanda-transpiler/main/assets/redpanda.png" 
       alt="RedPanda Transpiler logo"
       width="250; height:auto;">
</p>

> A Python → Mandarin Chinese transpiler.

RedPanda is an experimental transpiler that converts standard Python syntax into readable Mandarin Chinese syntax while preserving the program's structure. It is designed for educational purposes, language learning, and experimentation with localized programming syntax.

> **Project Status:** 🚧 Alpha (v0.1.0)

---

## Features

- Translate Python keywords into Mandarin Chinese
- Translate built-in functions
- Translate Python constants
- Simple command-line interface
- Lightweight with no external dependencies
- Compatible with Python 3.11+

---

## Example

### Python

```python
print("Hello, World!")

if True:
    print(len([1, 2, 3]))

for i in range(5):
    print(i)
```

### Output

```python
打印("Hello, World!")

如果 真:
    打印(长度([1, 2, 3]))

对于 i 于 范围(5):
    打印(i)
```

---

## Installation

Install RedPanda Transpiler from PyPI:

```bash
pip install redpanda-transpiler
```

---

## Usage

Transpile a file:

```bash
redpanda-tr input.py
```

Write the output to another file:

```bash
redpanda-tr input.py -o output.py
```

---

## Project Structure

```
RedPanda-transpiler/
│
├── redpanda/
│   ├── cli.py
│   ├── loader.py
│   ├── transpiler.py
│   ├── __main__.py
│   ├── __init__.py
│   └── data/
│       ├── keywords.json
│       ├── builtins.json
│       └── constants.json
│
├── pyproject.toml
├── README.md
├── LICENSE
└── setup.py
```

---

## Supported Translations

### Keywords

| Python  | Mandarin |
| ------- | -------- |
| if      | 如果     |
| else    | 否则     |
| elif    | 否则如果 |
| for     | 对于     |
| while   | 当       |
| def     | 定义     |
| class   | 类       |
| return  | 返回     |
| import  | 导入     |
| from    | 从       |
| as      | 作为     |
| try     | 尝试     |
| except  | 异常     |
| finally | 最后     |

### Built-ins

| Python | Mandarin |
| ------ | -------- |
| print  | 打印     |
| input  | 输入     |
| len    | 长度     |
| range  | 范围     |
| list   | 列表     |
| dict   | 字典     |
| tuple  | 元组     |
| set    | 集合     |

### Constants

| Python | Mandarin |
| ------ | -------- |
| True   | 真       |
| False  | 假       |
| None   | 空       |

---

## Roadmap

- [x] Command-line interface
- [x] Keyword translation
- [x] Built-in translation
- [x] Constant translation
- [x] Tokenizer-based transpiler
- [ ] AST-based transpiler
- [ ] Reverse transpiler (Mandarin → Python)
- [ ] Comment translation
- [ ] Docstring translation
- [ ] F-string support
- [ ] Package import translation
- [ ] Comprehensive unit tests
- [ ] CI/CD with GitHub Actions

---

## License

This project is licensed under the Apache License 2.0.

See the `LICENSE` file for details.

---

## Disclaimer

RedPanda is an experimental project intended for education and research. The generated Mandarin syntax is **not executable by the standard Python interpreter**. It must be converted back to standard Python or interpreted by a compatible tool.

---

## Author

**fmasterpro27**

GitHub: https://github.com/Fmasterpro27

---

If you find this project useful, consider giving it a ⭐ on GitHub!
