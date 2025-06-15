"""
基础工具
"""

import numpy as np

from chippymu.models import DrumType, WaveType
from numpy import ndarray


def note_to_freq(*, note: int) -> float:
    """
    将 MIDI 音符编号转换为频率 (Hz)

    - 参数
        - note: MIDI 音符编号

    - 返回
        - 频率 (Hz)
    """
    return 440 * 2 ** ((note - 69) / 12)


def basic_wave_gen(
    *,
    wave_type: WaveType,
    frequency: float,
    duration: float,
    amplitude: float = 1.0,
    duty_cycle: float = 0.5,
    sample_rate: int = 16000,
) -> ndarray:
    """
    生成指定类型的波形数组。

    - 参数:
        - wave_type: 波形的类型，可以是 "sine"、"square"、"triangle"、"sawtooth" 或 "noise"。
        - frequency: 波形的频率，单位为赫兹（Hz）。
        - duration: 波形的持续时间，单位为秒（s）。
        - amplitude: 波形的振幅，范围从 0 到 1。
        - duty_cycle:  Square 波形的占空比，范围从 0 到 1。
        - sample_rate: 采样率，单位为赫兹（Hz），默认为16000，使用时可能从Params中获取。

    - 返回:
        - 一个包含波形数据的 NumPy 数组。
    """
    t: ndarray = np.linspace(
        start=0, stop=duration, num=int(sample_rate * duration), endpoint=False
    )
    phase: ndarray = (t * frequency) % 1

    match wave_type:
        case WaveType.SINE:
            return amplitude * np.sin(2 * np.pi * frequency * t)
        case WaveType.SQUARE:
            return amplitude * np.where(phase < duty_cycle, 1, -1)
        case WaveType.TRIANGLE:
            return amplitude * np.where(phase < 0.5, -1 + 4 * phase, 3 - 4 * phase)
        case WaveType.SAWTOOTH:
            return amplitude * (2 * phase - 1)
        case WaveType.NOISE:
            return amplitude * (2 * np.random.rand(len(t)) - 1)
        case _:
            raise ValueError("未知波形类型")


def generate_kick(
    *,
    duration: float,
    amplitude: float = 1.0,
    sample_rate: int = 16000,
) -> ndarray:
    """
    生成底鼓声音，低频正弦波带衰减。

    - 参数：
        - duration: 持续时间，单位秒
        - frequency: 频率，单位赫兹
        - amplitude: 振幅，范围0~1
        - sample_rate: 采样率，默认16000

    - 返回：
        - 音频数据，ndarray
    """
    frequency: int = 50
    t: ndarray = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    envelope: ndarray = np.exp(-10 * t)  # 衰减
    return amplitude * envelope * np.sin(2 * np.pi * frequency * t)


def generate_snare(
    *, duration: float, amplitude: float = 1.0, sample_rate: int = 16000
) -> ndarray:
    """
    生成军鼓声音，噪声带衰减。

    - 参数：
        - duration: 持续时间，单位秒
        - amplitude: 振幅，范围0~1
        - sample_rate: 采样率，默认16000

    - 返回：
        - 音频数据，ndarray
    """
    t: ndarray = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    noise: ndarray = 2 * np.random.rand(len(t)) - 1
    envelope: ndarray = np.exp(-20 * t)
    return amplitude * envelope * noise


def generate_hihat(
    *, duration: float, amplitude: float = 1.0, sample_rate: int = 16000
) -> ndarray:
    """
    生成踩镲声音，短噪声带快速衰减。

    - 参数：
        - duration: 持续时间，单位秒
        - amplitude: 音量
        - sample_rate: 采样率，默认16000

    - 返回：
        - 噪声, ndarray
    """
    t: ndarray = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    noise: ndarray = 2 * np.random.rand(len(t)) - 1
    envelope: ndarray = np.exp(-50 * t)
    return amplitude * envelope * noise


def basic_drum_gen(
    *,
    drum_type: DrumType,
    frequency: int = 50,
    duration: float,
    amplitude: float = 1.0,
    sample_rate: int = 16000,
) -> ndarray:
    """
    生成基本鼓声

    - 参数：
        - drum_type: 鼓声类型
        - frequency: 频率，单位赫兹
        - duration: 持续时间，单位秒
        - amplitude: 振幅，范围0~1
        - sample_rate: 采样率，单位赫兹

    - 返回：
        - 音频数据，ndarray
    """
    match drum_type:
        case DrumType.KICK:
            return generate_kick(
                duration=duration,
                amplitude=amplitude,
                sample_rate=sample_rate,
            )
        case DrumType.SNARE:
            return generate_snare(
                duration=duration, amplitude=amplitude, sample_rate=sample_rate
            )
        case DrumType.HIHAT:
            return generate_hihat(
                duration=duration, amplitude=amplitude, sample_rate=sample_rate
            )
        case _:
            raise ValueError("未知鼓类型")
