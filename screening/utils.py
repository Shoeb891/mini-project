from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calculate_similarity(job_description, resume_text):
    job_embedding = model.encode(job_description)
    resume_embedding = model.encode(resume_text)
    cosine_score = util.cos_sim(job_embedding, resume_embedding)
    return cosine_score.item()
