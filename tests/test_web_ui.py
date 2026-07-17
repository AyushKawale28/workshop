import streamlit as st

from agentic_chat.core.config import Settings
from agentic_chat.ui.web.streamlit_app import _render_chat_content, build_client


def test_build_client_uses_settings_values() -> None:
    settings = Settings(
        api_key="openrouter-key",
        model="openrouter/free",
        site_url="https://example.com",
        site_name="Workshop",
        timeout=30.0,
        no_effect=False,
        available_models=("openrouter/free",),
        exa_api_key="exa-key",
        exa_num_results=7,
    )

    client = build_client(settings)

    assert client.timeout == 30.0
    assert client.exa_api_key == "exa-key"
    assert client.exa_num_results == 7


def test_render_chat_content_separates_code_and_output(monkeypatch) -> None:
    markdown_blocks: list[str] = []
    code_blocks: list[tuple[str, str, bool, bool]] = []
    captions: list[str] = []

    monkeypatch.setattr(st, "markdown", markdown_blocks.append)
    monkeypatch.setattr(st, "caption", captions.append)
    monkeypatch.setattr(
        st,
        "code",
        lambda content, language, line_numbers, wrap_lines: code_blocks.append(
            (content, language, line_numbers, wrap_lines)
        ),
    )

    _render_chat_content(
        'Example:\n```java\nSystem.out.println("Hello");\n```\n'
        "Expected result:\n```output\nHello\n```"
    )

    assert markdown_blocks == ["Example:", "Expected result:"]
    assert code_blocks == [
        ('System.out.println("Hello");', "java", True, True),
        ("Hello", "text", False, True),
    ]
    assert captions == ["Output"]
