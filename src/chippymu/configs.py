"""
基础参数的配置文件
"""


class BasicParams:
    def __init__(self, *, sample_rate: int = 16000, bpm: int = 90, length: float):
        # 定义采样率
        self.sample_rate: int = sample_rate
        # 定义BPM
        self.bpm: int = bpm
        # 定义音频总拍数
        self.length: float = length

    @property
    def beat_duration(self) -> float:
        """
        计算每拍的时长
        """
        return 60.0 / self.bpm

    @property
    def whole_duration(self) -> int:
        """
        计算音频矩阵总长
        """
        return int(self.length * self.beat_duration * self.sample_rate)
        
