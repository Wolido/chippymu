## 一个用numpy实现的8bit音乐生成器

### 功能特性

- MIDI 音符映射：通过枚举类将 MIDI 缺陷值与音名绑定。
- 多种波形支持：包括正弦波、方波、三角波、锯齿波和白噪声。
- 基本鼓组支持：Kick、Snare、Hi-hat 等常见打击乐器模拟。
- 通道生成器：支持旋律和鼓声分别生成独立通道。
- 后处理与播放：混音、音量控制、裁剪与播放功能。
- ️参数配置系统：灵活定义采样率、BPM 和时长等音频参数。

### 安装方式

```bash
pip install chippymu
```


### 示例用法

#### 播放一段旋律

```python
from chippymu.models import Note, WaveType
from chippymu.configs import BasicParams
from chippymu.channelgen import generate_wave
from chippymu.sound import post_processing, play

params = BasicParams(sample_rate=16000, bpm=90, length=4)

melody = [(0, Note.C1, 1), (2, Note.E1, 1), (3, Note.G1, 1)]
wave = generate_wave(melody=melody, wave_type=WaveType.SINE, params=params)
mixed = post_processing([wave], volumes=[0.8])
play(mixed, params)
```

#### 播放一段鼓点

```python
from chippymu.models import DrumType
from chippymu.channelgen import generate_drums
from chippymu.sound import post_processing, play

drums = [(0, DrumType.KICK, 1), (1, DrumType.HIHAT, 0.5), (2, DrumType.SNARE, 1)]
drum_audio = generate_drums(drums=drums, params=params)
mixed = post_processing([drum_audio], volumes=[0.8])
play(mixed, params)
```

### 核心模块说明

1. `models` 模块：定义了 MIDI 音符映射、波形类型和鼓点类型。

    - WaveType：波形类型，包括 `SINE`、`SQUARE`、`SAWTOOTH` 和 `TRIANGLE`。
    - DrumType：鼓点类型，包括 `KICK`、`HIHAT`、`SNARE` 和 `PERC`。
    - Note：音符对象，包含音符的起始时间、持续时间、音高和音量等信息。

2. `configs` 模块：定义了参数配置，包括采样率、每分钟节拍数、总时长。

    - sample_rate：采样率，默认为 16000 Hz。
    - bpm：每分钟节拍数，默认为 90。
    - length：总时长(以拍数为单位)。

3. `utils` 模块：工具函数集合。

    - `note_to_freq`：将音符对象转换为频率。
    - `basic_wave_gen`：生成基本波形。
    - `basic_drum_gen`：生成基本鼓声。

4. `channelgen`模块：通道生成器。

    - `generate_wave`： 生成波形通道。
    - `generate_drum`： 生成鼓声通道。

5. `sound`模块：后处理与播放。

    - `post_processing`: 混音、裁剪、量化等。
    - `play`: 使用`sounddevice`播放音频。
