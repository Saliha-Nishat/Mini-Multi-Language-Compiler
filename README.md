# Mini Multi-Language Educational Compiler System

### *A Modular Cross-Paradigm Compilation Infrastructure for Mini-C, Mini-Python, and Mini-Java*

---

## 📌 Project Overview

This repository contains the complete implementation of a unified, multi-mode educational compiler built entirely from scratch from first principles. Developed to address the limitations of standard compiler pedagogy, this sandbox infrastructure allows computer science students to write source code in three separate language paradigms (**Mini-C**, **Mini-Python**, and **Mini-Java**) and observe the entire sequential conversion pipeline side-by-side in real-time.

### 🎓 Academic Identity

* **Presenter / Developer:** Saliha Nishad Farid 
* **Department:** Department of Computer Science, Karakoram International University (KIU)
* **Faculty Supervisor:** Sir Shahid Malik

---

## 🎯 Problem Statement & Core Objectives

Standard compiler design tools and university projects often rely on a single target paradigm (like a standard compiler pipeline for a subset of C) using black-box automated generation utilities (`LEX`, `YACC`, `Flex`, `Bison`). This creates several structural issues for students:

1. **Pedagogical Isolation:** Hides how differing syntax rules (such as block-bounding braces `{}` vs. semantic indentation/whitespace) structurally shift front-end lexical scanning streams.
2. **Lack of Contrast:** Students cannot directly observe how abstract logic from completely different language modes scales into matching intermediate configurations.

### 🛠️ Engineering Objectives

* **Zero Third-Party Dependecies:** Implement all stages (Lexer, Parser, Analyzer) manually using clean, readable Python code to understand the underlying mathematics.
* **Cross-Paradigm Support:** Validate distinct syntax constructs across procedural, object-oriented, and whitespace-sensitive languages.
* **Complete Six-Phase Implementation:** Follow the entire standard pipeline: Lexical Analyzer $\rightarrow$ Predictive LL(1) Parser $\rightarrow$ Scope-Aware Symbol Table Analyzer $\rightarrow$ Intermediate Three-Address Code (TAC) Optimizer $\rightarrow$ Target Pseudo-Assembly Code Emitter.
* **Interactive UI Visualization:** Leverage a high-fidelity Streamlit interface to display pipeline mutations interactively.

---

## 🏗️ System Architecture & Data Flow

```
[ Source Workspace Input ]
       │ (Mini-C / Mini-Python / Mini-Java)
       ▼
[ Multi-Mode Lexer ] ──► (Generates Token Stream & Tracks Indentation Stacks)
       ▼
[ Predictive LL(1) Parser ] ──► (Eliminates Left-Recursion, Emits AST Graph)
       ▼
[ Scope-Aware Semantic Analyzer ] ──► (Type Matrix Check, Scoped Table Stack)
       ▼
[ Intermediate Code Generator ] ──► (Expression Flattening, Registers t1, t2)
       ▼
[ Constant Folding Optimizer ] ──► (Evaluates Static Arithmetic Loops)
       ▼
[ Target Pseudo-Assembly Emitter ] ──► (Outputs Structured Registers R1, R2, R3)

```

---

## 💻 Key Implementation Aspects

### 1. Front-End Multi-Mode Lexer

* **Indentation Tracking Stack:** For `Mini-Python` mode, the scanner records leading whitespaces using a Python array stack. It compares subsequent lines to automatically inject artificial `INDENT` and `DEDENT` tokens to safely isolate logical scopes without curly brackets.
* **Delimiter Toggling:** Toggles internal scanning states to cleanly distinguish statement separators (`:`, `;`, `{`, `}`) based on whether a C, Python, or Java workspace is activated.
* **Error Isolation:** Identifies structural anomalies such as malformed variable descriptors or unclosed multi-line remarks instantly, preventing subsequent component failures.

### 2. Predictive LL(1) Parsing & Abstract Syntax Tree (AST)

To ensure deterministic top-down tracking without infinite looping vectors, left-recursion is eliminated from algebraic expression production chains. For instance, the traditional math rules are rewritten as:

$$E \rightarrow T E'$$

$$E' \rightarrow + T E' \mid \epsilon$$

The system accepts the flat sequential array of generated tokens and outputs a clean, recursive Abstract Syntax Tree mapping out execution loops, conditional nesting, and operator priorities.

### 3. Scope Management & Semantic Analysis

* **Symbol Table Stack:** Manages overlapping identifier scopes using a stack of dictionaries. Variable scopes are managed dynamically according to their active block levels:

$$\text{Scope Level} \in \{0, 1, 2, \dots, n\}$$


* **Strict Type Evaluation:** Validates operational semantic rules at compile time. It flags assignments where source types conflict with destination containers, throwing readable exceptions like:
`[Semantic Error] Line 5: Type Mismatch. Cannot assign 'string' to variable of type 'int'.`

### 4. Intermediate Three-Address Code (TAC) & Optimization Pass

The AST tree nodes are flattened sequentially down to a stylized linear three-address format using tracking values (`t1`, `t2`) and jump destination tags (`L1`, `L2`).

* **Constant Folding Pass:** A linear analyzer scans the intermediate structure to compute static arithmetic logic groups at compilation time, saving runtime processing overhead:
* *Unoptimized Input:* `x = 10 * 2 + 5`
* *Optimized Output:* `x = 25`



### 5. Target Code Synthesis

Translates intermediate instruction structures into low-level virtual pseudo-assembly segments:

* Data fields are separated cleanly into standard `.data` allocations, while logic steps reside inside `.text` tags.
* Structural primitives translate directly to simulated architecture registers (`R1`, `R2`, `R3`), mapping assignment behaviors to `MOV` keys, operators to `ADD`/`SUB`/`MUL`/`DIV`, and loop vectors to standard hardware-like comparisons (`CMP`, `BEQ`).

---

## 🔬 Testing Metrics & Results

* **Rigorous Benchmark Suite:** Evaluated systematically against **30 custom-built program test files** featuring varying nested control flows, correct expressions, and syntax anomalies.
* **Streamlit Web Sandbox Dashboard:** Provides an interactive split-screen workspace where users can edit input source files on the left and see real-time, synchronized visual tabs (Token Tables, Hierarchical AST, Clean TAC, and Virtual Target Assembly) on the right.

---

## ⚠️ System Constraints & Boundaries

Because this architecture is specialized for compiler education, the following parameters define its scope:

* **Primitive Types Only:** Limited strictly to standard primitives (`int`, `float`, `char`, `string`, `bool`). It does not process pointers, array offsets, or custom class inheritance structures.
* **Panic-Mode Error Recovery:** Uses standard panic-mode tracking, which drops invalid lookahead tokens until the next structural boundary mark (like `;` or a newline) is met, rather than assembling fully resilient relational error-correction graph nodes.
* **Sequential Register Assignment:** Registers are loaded using localized linear tracking matrices instead of a thorough graph-coloring execution routine.

---

## 🚀 Future Roadmap & Conclusion

### 🗺️ Future Scope

1. **LLVM IR Backend Integration:** Upgrade the execution engine to yield formal LLVM Intermediate Representation, allowing the output to compile into operational machine binaries (`.exe` / `.out`) using standard `Clang` drivers.
2. **Advanced Code Optimization Passes:** Introduce Common Subexpression Elimination (CSE) and Dead Code Elimination (DCE) analysis.
3. **Hindley-Milner Type Inference:** Implement type inferencing mechanisms to support dynamic variable instantiations in `Mini-Python` fields without requiring upfront explicit casting headers.

### 🎓 Conclusion

This implementation demonstrates that conflicting programming syntax patterns and cross-paradigm specifications can be comfortably checked, structuralized, and translated using a clean, single unified compilation framework—providing a useful interactive testing toolbox for learning.

---

## 📁 Installation & Local Deployment

### Prerequisites

* Python 3.8 or higher installed on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/educational-compiler-system.git
cd educational-compiler-system

```

### Step 2: Install UI Interface Dependencies

```bash
pip install streamlit

```

### Step 3: Run the Dashboard

```bash
streamlit run app.py

```

Open the provided local URL (usually `http://localhost:8501`) in your browser to interact with the system workspace.
