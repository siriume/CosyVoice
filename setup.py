import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cosyvoice",
    version="0.1.0",
    author="Alibaba Inc.",
    author_email="",
    description="CosyVoice: A speech synthesis model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FunAudioLLM/CosyVoice",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "torch>=1.10.0",
        "torchaudio>=0.10.0",
        "numpy",
        "pyworld",
        "tqdm",
        # extra
        "conformer",
        "deepspeed; sys_platform == 'linux'",
        "diffusers",
        "grpcio",
        "grpcio-tools",
        "hydra-core",
        "HyperPyYAML",
        "inflect",
        "librosa",
        "lightning",
        "matplotlib",
        "modelscope",
        "networkx",
        "omegaconf",
        "onnxruntime-gpu; sys_platform == 'linux'",
        "onnxruntime; sys_platform == 'darwin' or sys_platform == 'win32'",
        "openai-whisper",
        "protobuf",
        "pydantic",
        "rich",
        "soundfile",
        "tensorboard",
        "wget",
        "gdown",
        "pyarrow",
        "jieba",
        "pypinyin",
        "pydub",
        "audiosegment",
        "srt",
        "ffmpeg-python",
        # "ttsfrd",
        "gradio",
        # "WeTextProcessing", # pynini is a problem
        "matcha-tts @ git+https://github.com/rsxdalv/Matcha-TTS@better-matcha",
        "transformers",
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
        ],
        "runtime": [
            "fastapi",
            "uvicorn",
            "grpcio",
            "grpcio-tools",
        ],
    },
    entry_points={
        "console_scripts": [
            "cosyvoice-webui=cosyvoice.bin.webui:main",
            "cosyvoice-train=cosyvoice.bin.train:main",
            "cosyvoice-inference=cosyvoice.bin.inference:main",
            "cosyvoice-export-jit=cosyvoice.bin.export_jit:main",
            "cosyvoice-export-onnx=cosyvoice.bin.export_onnx:main",
        ],
    },
    include_package_data=True,
    package_data={
        "cosyvoice": ["**/*.yaml", "**/*.json"],
    },
)
