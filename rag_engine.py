from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class CareerRAG:

    def __init__(self):

        self.embed_model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        self.documents = []
        self.load_documents()

        embeddings = self.embed_model.encode(self.documents)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

    def load_documents(self):

        files = [
            "data/careers.txt",
            "data/skills.txt",
            "data/courses.txt"
        ]

        for f in files:
            with open(f) as file:
                self.documents += file.readlines()

    def retrieve(self, query):

        q_embed = self.embed_model.encode([query])

        D, I = self.index.search(np.array(q_embed), k=3)

        context = ""

        for idx in I[0]:
            context += self.documents[idx]

        return context
