def quote_change(text: str) -> str:
    """Replace all " symbols in text with ' and vise versa."""
    tr_map = text.maketrans({'"': "'", "'": '"'})
    return text.translate(tr_map)


if __name__ == "__main__":
    print(quote_change('"ds\'f"  df"e\'wr"'))
