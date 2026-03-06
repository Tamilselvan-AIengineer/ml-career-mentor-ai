"""
rag_engine.py — Retrieval-Augmented Generation pipeline
Replace the mock implementations with your real vector store + LLM calls.
"""
from pathlib import Path
import os


class RAGEngine:
    """Simple RAG engine — swap internals for FAISS/ChromaDB + OpenAI/Anthropic."""

    def __init__(self, data_dir: str = "data", top_k: int = 3):
        self.data_dir = Path(data_dir)
        self.top_k = top_k
        self.docs: dict[str, str] = {}
        self._index()

    # ── Indexing ──────────────────────────────────────────────────────────
    def _index(self):
        """Load text files into memory (replace with vector embeddings)."""
        for fname in ["courses.txt", "careers.txt", "skills.txt"]:
            p = self.data_dir / fname
            if p.exists():
                self.docs[fname] = p.read_text(encoding="utf-8")

    def refresh(self):
        self.docs.clear()
        self._index()

    # ── Retrieval ─────────────────────────────────────────────────────────
    def retrieve(self, query: str) -> list[dict]:
        """
        Keyword-based retrieval (mock).
        Replace with: embeddings = model.encode(query); FAISS.search(embeddings, k)
        """
        results = []
        q = query.lower()
        for fname, content in self.docs.items():
            score = sum(1 for word in q.split() if word in content.lower())
            if score > 0:
                # Return best chunk
                lines = content.splitlines()
                chunk = "\n".join(lines[:20])
                results.append({"source": fname, "content": chunk, "score": score})
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[: self.top_k]

    # ── Generation ────────────────────────────────────────────────────────
    def generate(self, query: str, context_docs: list[dict], llm_fn=None) -> str:
        """
        Build prompt with retrieved context and call LLM.
        llm_fn: callable(prompt: str) -> str  (your OpenAI / Anthropic wrapper)
        """
        context = "\n\n".join(
            f"[{d['source']}]\n{d['content']}" for d in context_docs
        )
        prompt = (
            f"You are an intelligent educational assistant.\n\n"
            f"Context from knowledge base:\n{context}\n\n"
            f"Student question: {query}\n\n"
            f"Answer concisely and helpfully:"
        )
        if llm_fn:
            return llm_fn(prompt)
        # Fallback: return mock answer
        return f"[RAG mock] Based on retrieved context from {[d['source'] for d in context_docs]}: {query}"

    # ── Combined query ────────────────────────────────────────────────────
    def query(self, question: str, llm_fn=None) -> dict:
        docs = self.retrieve(question)
        answer = self.generate(question, docs, llm_fn)
        return {
            "answer": answer,
            "sources": [d["source"] for d in docs],
            "context": docs,
        }
