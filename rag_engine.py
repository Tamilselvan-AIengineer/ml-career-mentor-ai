from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class CareerRAG:

    def __init__(self):

        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        self.docs = []
        self.load_docs()

        embeddings = self.model.encode(self.docs)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def load_docs(self):

        files = [
            "data/careers.txt",
            "data/skills.txt",
            "data/courses.txt"
        ]

        for f in files:
            with open(f) as file:
                self.docs += file.readlines()

    def retrieve(self, query):

        q = self.model.encode([query])
        D, I = self.index.search(np.array(q), k=3)

        context = ""
        for i in I[0]:
            context += self.docs[i]

        return context
        
