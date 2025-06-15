"""
定义一些基础类型
"""

from enum import Enum


class WaveType(str, Enum):
    """
    几种波形
    """

    SINE = "sine"
    SQUARE = "square"
    TRIANGLE = "triangle"
    SAWTOOTH = "sawtooth"
    NOISE = "noise"


class DrumType(str, Enum):
    """
    几种鼓声
    """

    KICK = "kick"
    SNARE = "snare"
    HIHAT = "hihat"


class Note(int, Enum):
    """
    音符
    """

    C0 = 48
    C0_SHARP = 49
    D0 = 50
    D0_SHARP = 51
    E0 = 52
    F0 = 53
    F0_SHARP = 54
    G0 = 55
    G0_SHARP = 56
    A0 = 57
    A0_SHARP = 58
    B0 = 59
    
    C1 = 60
    C1_SHARP = 49
    D1 = 62
    D1_SHARP = 51
    E1 = 64
    F1 = 65
    F1_SHARP = 54
    G1 = 67
    G1_SHARP = 56
    A1 = 69
    A1_SHARP = 58
    B1 = 71

    C2 = 72
    C2_SHARP = 49
    D2 = 74
    D2_SHARP = 51
    E2 = 76
    F2 = 77
    F2_SHARP = 54
    G2 = 79
    G2_SHARP = 56
    A2 = 81
    A2_SHARP = 58
    B2 = 83

    C3 = 84
    C3_SHARP = 49
    D3 = 86
    D3_SHARP = 51
    E3 = 88
    F3 = 89
    F3_SHARP = 54
    G3 = 91
    G3_SHARP = 56
    A3 = 93
    A3_SHARP = 58
    B3 = 95

    C4 = 96
    C4_SHARP = 49
    D4 = 98
    D4_SHARP = 51
    E4 = 100
    F4 = 101
    F4_SHARP = 54
    G4 = 103
    G4_SHARP = 56
    A4 = 105
    A4_SHARP = 58
    B4 = 107