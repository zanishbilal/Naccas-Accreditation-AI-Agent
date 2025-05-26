# pipelines/phase1_pipeline.py
from utils.file_utils import read_pdfs_from_folder
from utils.text_preprocessing import clean_text, chunk_text

def run_phase1_policy_ingestion(folder_path):
    raw_text = read_pdfs_from_folder(folder_path)
    clean = clean_text(raw_text)
    chunks = chunk_text(clean)
    return chunks
