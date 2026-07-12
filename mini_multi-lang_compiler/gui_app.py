#!/usr/bin/env python3
"""
GUI Dashboard Orchestration Core Engine Engine powered by Streamlit components frameworks.
"""
import streamlit as st
# Dynamic reference import binding from core compiler architecture base
from compiler import MultiLanguageCompilerSystem, get_sample_test_suites

st.set_page_config(page_title="Multi-Language Compiler System", layout="wide")

st.title("🎓 Design and Implementation of a Mini Multi-Language Educational Compiler Engine")
st.markdown("---")

# Sidebar Configuration Control Room
st.sidebar.header("🛠️ Compiler Control System Panel")
language_selection = st.sidebar.selectbox("Select Target Language Mode Specification", ["Mini-C", "Mini-Python", "Mini-Java"])
lang_key = "c" if language_selection == "Mini-C" else ("python" if language_selection == "Mini-Python" else "java")

# Load Sample Tests Utilities maps indices configurations matrices
test_suites = get_sample_test_suites()
sample_options = [t[0] for t in test_suites[lang_key]]
selected_sample_name = st.sidebar.selectbox("Load Standard Benchmark Programs Matrix", sample_options)

# Retrieve raw body contents payload mapped matches
source_payload = ""
for t in test_suites[lang_key]:
    if t[0] == selected_sample_name:
        source_payload = t[1]

# User Entry Interface Layout Containers
st.subheader("📝 Target Program Input Terminal Canvas")
code_input = st.text_area("Source Code Workspace Editor Framework", value=source_payload, height=250)

if st.button("🚀 Execute Comprehensive Compilation Pipeline Phases"):
    st.markdown("---")
    st.header("🔍 Compilation Execution Diagnostics Dashboard Results")
    
    # Run the core platform orchestration sequence steps
    res = MultiLanguageCompilerSystem.compile_source(code_input, lang_key)
    
    if not res["success"]:
        st.error("❌ Compilation Execution Failure Context Errors Identified.")
        for error in res["errors"]:
            st.warning(error)
            
        # Display structural intermediate code components available up to breakdown phase points
        if res["tokens"]:
            with st.expander("Show Partially Extracted Lexer Tokens List", expanded=False):
                st.write(res["tokens"])
    else:
        st.success("🎉 Target Source Program Processed successfully across all compiler phases.")
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🪙 Lexer Tokens Stream", 
            "🌲 AST Hierarchy Representation", 
            "📋 Scope Symbol Table", 
            "⚙️ TAC Intermediate Representations", 
            "📟 Assembler Target Code Architecture"
        ])
        
        with tab1:
            st.subheader("Lexical Tokens Collection List Manifest Data Table")
            token_data = [{"Index": i, "Type": tok.type, "Value": tok.value, "Line": tok.line, "Column": tok.column} for i, tok in enumerate(res["tokens"])]
            st.table(token_data)
            
        with tab2:
            st.subheader("ASCII Hierarchical Syntax Evaluation Abstract Structural Tree (AST)")
            st.text(res["ast_string"])
            
        with tab3:
            st.subheader("Variable Declarations Identifiers Scopes Context Map Table Grid")
            st.text(res["symbol_table_str"])
            
        with tab4:
            st.subheader("Three-Address Intermediary Instruction Code Architecture Framework Stages")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Raw Form Intermediate Code Base (TAC)**")
                st.text(res["tac_raw"])
            with c2:
                st.markdown("**Constant-Folded Optimized Pipeline Execution Code Base**")
                st.text(res["tac_optimized"])
                
        with tab5:
            st.subheader("Target Pseudo-Assembly Registers Architecture Machine Level Mappings instructions")
            st.text(res["assembly_code"])