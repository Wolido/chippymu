"""
按通道生成音G
"""

import numpy as np

from chippymu.utils import basic_wave_gen, basic_drum_gen, note_to_freq

from numpy import ndarray
from chippymu.configs import BasicParams
from chippymu.models import DrumType, Note, WaveType


def generate_wave(
    *, melody: list[tuple[float, int | Note, float]], wave_type: WaveType, params: BasicParams
) -> ndarray:
    """
    生成指定波形和旋律的通道

    - 参数：
        - melody: 旋律列表，每个元素为 (frequency, duration, amplitude)
        - wave_type: 波形类型
        - params: 基本参数

    - 返回：
        - 通道数据
    """
    melody_beat: list[tuple[float, int | Note, float]] = [
        (start * params.beat_duration, note, dur * params.beat_duration)
        for start, note, dur in melody
    ]

    melody_audio = np.zeros(params.whole_duration)

    for start, note, dur in melody_beat:
        wave = basic_wave_gen(
            wave_type=wave_type,
            frequency=note_to_freq(note=note),
            duration=dur,
            sample_rate=params.sample_rate,
        )
        start_idx = int(start * params.sample_rate)
        end_idx = start_idx + len(wave)
        melody_audio[start_idx:end_idx] += wave

    return melody_audio


def generate_drums(
    *, drums: list[tuple[float, DrumType, float]], params: BasicParams
) -> ndarray:
    """
    生成鼓声

    - 参数：
        - drums: 鼓声列表，每个元素是一个元组，包含起始时间，鼓声类型，持续时间
        - params: 基础参数

    - 返回：
        - 通道数据
    """
    drums_beat: list[tuple[float, DrumType, float]] = [
        (start * params.beat_duration, note, dur * params.beat_duration)
        for start, note, dur in drums
    ]

    drums_audio = np.zeros(params.whole_duration)

    for start, drum_type, dur in drums_beat:
        wave = basic_drum_gen(
            drum_type=drum_type,
            duration=dur,
            amplitude=1.0,
            sample_rate=params.sample_rate,
        )
        start_idx = int(start * params.sample_rate)
        end_idx = start_idx + len(wave)
        drums_audio[start_idx:end_idx] += wave

    return drums_audio
