import sys
try:
    import langchain_community
    print("✅ SUCCESS: langchain_community found!")
    print(f"Location: {langchain_community.__file__}")
except ImportError as e:
    print("❌ ERROR: Module still not found.")
    print(f"Python is running from: {sys.executable}")
    print("Make sure you run 'pip install' using THIS python executable.")
