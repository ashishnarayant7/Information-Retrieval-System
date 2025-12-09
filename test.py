try:
    from langchain_community.text_splitter import RecursiveCharacterTextSplitter
    print("✅ SUCCESS: langchain_community is installed and working!")
except ImportError as e:
    print(f"❌ ERROR: {e}")
