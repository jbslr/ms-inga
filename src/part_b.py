"""
Half a Log Pose reading — Ms. Semicolon's contribution. Runs standalone
once the crew has done their work.
"""

import json
from pathlib import Path


def _read_lfs_int(path):
    """Assets in this log are stashed as PREFIX:<int> once recovered."""
    return int(Path(path).read_text().split(":")[1])


def _read_config_value():
    return json.load(open("../config.json"))["seal_value"]


HEADER_VALUE_B2 = None    # the header crew's job -- resolve the header conflict
EXPECTED_INTEGRITY = 6    # HEADER_VALUE_B2 * LFS_VALUE_B2 must equal this


def checksum(a, b):
    raise NotImplementedError("lifted from an old page — go find it")


def pad_digits(n):
    raise NotImplementedError("lifted from an old page — go find it")


def main():
    config_value = _read_config_value()
    lfs_value_b1 = _read_lfs_int("../assets/note_b1.wav")
    lfs_value_b2 = _read_lfs_int("../assets/scan_b2.png")
    if HEADER_VALUE_B2 * lfs_value_b2 != EXPECTED_INTEGRITY:
        raise SystemExit("Seal doesn't hold -- one of the readings is off.")
    print(pad_digits(checksum(config_value, lfs_value_b1)))


if __name__ == "__main__":
    main()
