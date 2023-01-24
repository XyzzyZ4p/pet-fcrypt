from pathlib import Path


def file_path_helper(out_path: str, ext: str) -> str:
    out = Path(out_path)
    return str(out.resolve().parent / (out.resolve().stem + ext))
    

__all__ = ('file_path_helper',)
