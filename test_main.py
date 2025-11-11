from main import *

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)

        assert len(align_S) == len(align_T)

        distance = sum(
            1 for a, b in zip(align_S, align_T) if a != b
        )

        assert distance == fast_MED(S, T)

