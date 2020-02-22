"""Small description of the project.

This project aims to record the keyboard keys
using the pynput library as well as pyqt5.
Most of the functions are defined in snake_case (Python)
contrary to PyQt5 which uses CamelCase (C++).

No copyright.
"""


__author__ = '{Armanta}'
__copyright__ = 'Copyright {2020}, {NoCopyright}'
__credits__ = ['{Armanta}']
__license__ = '{NoLicense}'
__version__ = '{0}.{0}.{1}'
__maintainer__ = '{Armanta}'
__email__ = '{antoine.chauvin@live.fr}'

#Local
from pynput.keyboard import Key


BOX_WIDTH = 80
BOX_HEIGHT = 80
HORIZONTAL_SPACING = 0
VERTICAL_SPACING = 0
BOTH_SPACING = 0
FADE_DURATION = 1
FONT_SIZE = 10
PATH = "PATH"

KEYS = {Key.alt:"Key.alt",
Key.alt_l:"Key.alt_l",
Key.alt_r:"Key.alt_r",
Key.backspace:"Key.backspace",
Key.caps_lock:"Key.caps_lock",
Key.cmd:"Key.cmd",
Key.cmd_r:"Key.cmd_r",
Key.ctrl:"Key.ctrl",
Key.ctrl_l:"Key.ctrl_l",
Key.ctrl_r:"Key.ctrl_r",
Key.delete:"Key.delete",
Key.down:"Key.down",
Key.end:"Key.end",
Key.enter:"Key.enter",
Key.esc:"Key.esc",
Key.f1:"Key.f1",
Key.f2:"Key.f2",
Key.f3:"Key.f3",
Key.f4:"Key.f4",
Key.f5:"Key.f5",
Key.f6:"Key.f6",
Key.f7:"Key.f7",
Key.f8:"Key.f8",
Key.f9:"Key.f9",
Key.f10:"Key.f10",
Key.f11:"Key.f11",
Key.f12:"Key.f12",
Key.f13:"Key.f13",
Key.f14:"Key.f14",
Key.f15:"Key.f15",
Key.f16:"Key.f16",
Key.f17:"Key.f17",
Key.f18:"Key.f18",
Key.f19:"Key.f19",
Key.f20:"Key.f20",
Key.home:"Key.home",
Key.left:"Key.left",
Key.page_down:"Key.page_down",
Key.page_up:"Key.page_up",
Key.right:"Key.right",
Key.shift:"Key.shift",
Key.shift_r:"Key.shift_r",
Key.space:"Key.space",
Key.tab:"Key.tab",
Key.up:"Key.up",
Key.media_play_pause:"Key.media_play_pause",
Key.media_volume_mute:"Key.media_volume_mute",
Key.media_volume_down:"Key.media_volume_down",
Key.media_volume_up:"Key.media_volume_up",
Key.media_previous:"Key.media_previous",
Key.media_next:"Key.media_next",
Key.insert:"Key.insert",
Key.menu:"Key.menu",
Key.num_lock:"Key.num_lock",
Key.pause:"Key.pause",
Key.print_screen:"Key.print_screen",
Key.scroll_lock:"Key.scroll_lock"}
