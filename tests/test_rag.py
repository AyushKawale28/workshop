from agentic_chat.rag.embeddings import OpenRouterEmbeddingsClient
from agentic_chat.rag.pipeline import RAGContext, RAGPipeline, build_rag_message


def test_chunk_text_preserves_fenced_code_formatting(tmp_path) -> None:
    pipeline = RAGPipeline(
        embeddings_client=OpenRouterEmbeddingsClient(
            api_key="test-key",
            model="test-model",
            timeout=1.0,
        ),
        data_dir=str(tmp_path),
    )
    content = (
        "# Example\n\n"
        "```java\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        '        System.out.println("Hello");\n'
        "    }\n"
        "}\n"
        "```\n\n"
        "```output\nHello\n```"
    )

    assert pipeline._chunk_text(content) == [content]


def test_build_rag_message_uses_real_newlines() -> None:
    context = RAGContext(
        text='# Example\n```java\nSystem.out.println("Hello");\n```',
        hits=1,
        sources=("rag/data/example.md",),
    )

    message = build_rag_message(context)

    assert "RAG CONTEXT:\n# Example" in message["content"]
    assert '```java\nSystem.out.println("Hello");\n```' in message["content"]
