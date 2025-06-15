"""
后处理和音频播放
"""

import sounddevice as sd # type: ignore
import numpy as np

from numpy import ndarray

from chippymu.configs import BasicParams


def post_processing(channels: list[ndarray], volumes: list[float]) -> ndarray:
    """
    后处理过程，包括音量控制、混音、裁剪、量化
    """
    if len(channels) != len(volumes):
        raise ValueError("channels和volumes长度不一致")

    mix = np.zeros_like(channels[0])
    for i in range(len(channels)):
        mix += channels[i] * volumes[i]

    mix = np.clip(mix, -1, 1)

    mix_8bit = np.round(mix * 127).astype(np.int8)

    return mix_8bit


def play(data: ndarray, params: BasicParams):
    sd.play(data=data, samplerate=params.sample_rate)
    sd.wait()
    