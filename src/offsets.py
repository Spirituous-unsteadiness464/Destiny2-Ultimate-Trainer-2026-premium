from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Offsets:
    GOD_MODE: int = 0x2a4b570
    UNLIMITED_AMMO: int = 0x2a4b5af
    ESP_ENABLED: int = 0x2a4b5f4
    SPEED_HACK: int = 0x2a4b6ab
    NO_RECOIL: int = 0x2a4b726
    LOOT_UNLOCKER: int = 0x2a4b80a
    BOUNTY_COMPLETE: int = 0x2a4b873
    AIMBOT_FOV: int = 0x2a4b939
    PLAYER_BASE: int = 0x1e8a3fc
    PLAYER_OFFSETS: list = field(default_factory=lambda: [0x0, 0x30, 0x8, 0x20])
    VERSION_OFFSETS: Dict[str, Dict[str,int]] = field(default_factory=lambda: {
        "2026.06.28-662": {
            "GOD_MODE": 0x2a4b570,
            "UNLIMITED_AMMO": 0x2a4b5af,
        }
    })
    def get_for_version(self, ver): return self.VERSION_OFFSETS.get(ver, {})

offsets = Offsets()
