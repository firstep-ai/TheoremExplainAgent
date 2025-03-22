"""
Copyright (c) 2025 Xposed73
All rights reserved.
This file is part of the Manim Voiceover project.
"""

import hashlib
import json
from pathlib import Path
from manim_voiceover.services.base import SpeechService
from src.config.config import Config
from elevenlabs import ElevenLabs  # 新增：ElevenLabs 语音合成 API

class KokoroService(SpeechService):
    """Speech service class for kokoro_self using ElevenLabs API for text-to-speech synthesis."""

    def __init__(self, engine=None, 
                 voice: str = Config.ELEVENLABS_DEFAULT_VOICE,
                 **kwargs):
        # 初始化 ElevenLabs 客户端（请确保 Config 中设置了 ELEVENLABS_API_KEY）
        self.client = ElevenLabs(api_key=Config.ELEVENLABS_API_KEY)
        self.voice = voice  # 此处 voice 为 ElevenLabs 的 voice_id

        if engine is None:
            engine = self.text_to_speech  # 默认使用本类的 text_to_speech 方法

        self.engine = engine
        super().__init__(**kwargs)

    def get_data_hash(self, input_data: dict) -> str:
        """
        Generates a hash based on the input data dictionary.
        The hash is used to create a unique identifier for the input data.
        """
        data_str = json.dumps(input_data, sort_keys=True)
        return hashlib.sha256(data_str.encode('utf-8')).hexdigest()

    def text_to_speech(self, text, output_file, voice_name):
        """
        Generates speech from text using ElevenLabs API and saves the audio file.
        """
        audio_generator = self.client.text_to_speech.convert(
            voice_id=voice_name,
            output_format="mp3_44100_128",
            text=text,
            model_id="eleven_multilingual_v2",
        )
        with open(output_file, "wb") as f:
            for chunk in audio_generator:
                f.write(chunk)
        print(f"Saved at {output_file}")
        return output_file

    def generate_from_text(self, text: str, cache_dir: str = None, path: str = None) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_data = {"input_text": text, "service": "elevenlabs_self"}
        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_data_hash(input_data) + ".mp3"
        else:
            audio_path = path

        output_path = str(Path(cache_dir) / audio_path)
        self.engine(
            text=text,
            output_file=output_path,
            voice_name=self.voice,
        )

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

        return json_dict
