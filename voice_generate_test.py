from pathlib import Path
from src.utils.kokoro_voiceover import KokoroService


# 使用 Path 对象创建缓存目录
cache_dir = Path("cache")
cache_dir.mkdir(exist_ok=True)

service = KokoroService(cache_dir=cache_dir)
text = "Hello, this is a test synthesis using Kokoro voiceover service."
result = service.generate_from_text(text, cache_dir=cache_dir)
print("Generated audio file:", result["original_audio"])