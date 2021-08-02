# coding: UTF-8
import sys
l111_opy_ = sys.version_info [0] == 2
l11l_opy_ = 2048
l1l11l_opy_ = 7
def l1ll11_opy_ (l1ll_opy_):
    global l1ll1l_opy_
    l1lll_opy_ = ord (l1ll_opy_ [-1])
    l1l_opy_ = l1ll_opy_ [:-1]
    l1111_opy_ = l1lll_opy_ % len (l1l_opy_)
    l11l1_opy_ = l1l_opy_ [:l1111_opy_] + l1l_opy_ [l1111_opy_:]
    if l111_opy_:
        l11_opy_ = l1lll1_opy_ () .join ([l1llll_opy_ (ord (char) - l11l_opy_ - (l111l_opy_ + l1lll_opy_) % l1l11l_opy_) for l111l_opy_, char in enumerate (l11l1_opy_)])
    else:
        l11_opy_ = str () .join ([chr (ord (char) - l11l_opy_ - (l111l_opy_ + l1lll_opy_) % l1l11l_opy_) for l111l_opy_, char in enumerate (l11l1_opy_)])
    return eval (l11_opy_)
# l1ll111_opy_ l1l111_opy_ 7
# ll_opy_ is a l1l1l_opy_ l1l1l11_opy_ l11l1ll_opy_ l111l1_opy_ that l11ll1_opy_ a
# list of l1111l_opy_ l1l11ll_opy_ l1l1ll1_opy_. l11ll11_opy_ l1l1111_opy_ is l1l111l_opy_
# l1lllll1_opy_ to 4 l1llll1l_opy_ to l1ll11l_opy_ the l1l1l11_opy_. l11l111_opy_ time the user
# l1lll1l1_opy_ l111111_opy_, the number of l11ll1ll1_opy_ l11l11l11_opy_ in their
# l11ll1ll1_opy_ l11ll1l11_opy_ is l11l1l1ll_opy_ and the user is l111lll_opy_ to
# l111l1l_opy_ a new l1ll11l_opy_. l11ll11_opy_ l111l1_opy_ l1ll1l1_opy_ l11111l_opy_ the l1l1111_opy_
# l1lll11l_opy_ l1lll111_opy_ the l1l1l11_opy_ or not.
from uagame import Window
from time import sleep
from random import randint, choice
def main():
    location = [0,0]
    l1llll1l_opy_ = 4
    window = l11ll111l_opy_()
    l11ll1111_opy_(window, location, l1llll1l_opy_)
    l1l1l11_opy_ = l11l1l111_opy_(window, location)
    l1ll11l_opy_ = l11l111ll_opy_(window, l1l1l11_opy_, location, l1llll1l_opy_)
    l11l1ll11_opy_(window, l1ll11l_opy_, l1l1l11_opy_)
def l11ll111l_opy_():
    window = Window(l1ll11_opy_ (u"ࠧࡉࡣࡦ࡯࡮ࡴࡧࠨऍ"), 600, 500)
    window.set_font_name(l1ll11_opy_ (u"ࠨࡥࡲࡹࡷ࡯ࡥࡳࡰࡨࡻࠬऎ"))
    window.set_font_size(18)
    window.set_font_color(l1ll11_opy_ (u"ࠩࡪࡶࡪ࡫࡮ࠨए"))
    window.set_bg_color(l1ll11_opy_ (u"ࠪࡦࡱࡧࡣ࡬ࠩऐ"))
    return window
def l11ll1111_opy_(window, location, l1llll1l_opy_):
    l1lllll_opy_ = [l1ll11_opy_ (u"ࠫࡉࡋࡂࡖࡉࠣࡑࡔࡊࡅࠨऑ"), str(l1llll1l_opy_) + l1ll11_opy_ (u"ࠬࠦࡁࡕࡖࡈࡑࡕ࡚ࠨࡔࠫࠣࡐࡊࡌࡔࠨऒ"), l1ll11_opy_ (u"࠭ࠧओ")]
    for l1llllll_opy_ in l1lllll_opy_:
        l11l1l1l1_opy_(window, l1llllll_opy_, location)
def l11l1l111_opy_(window, location):
    l11l111l1_opy_ = 20
    l1111ll_opy_ = [l1ll11_opy_ (u"ࠧࡑࡔࡒ࡚ࡎࡊࡅࠨऔ"), l1ll11_opy_ (u"ࠨࡕࡈࡘ࡙ࡏࡎࡈࠩक"), l1ll11_opy_ (u"ࠩࡆࡅࡓ࡚ࡉࡏࡃࠪख"), l1ll11_opy_ (u"ࠪࡇ࡚࡚ࡔࡊࡐࡊࠫग"), l1ll11_opy_ (u"ࠫࡍ࡛ࡎࡕࡇࡕࡗࠬघ"), l1ll11_opy_ (u"࡙ࠬࡕࡓࡘࡌ࡚ࡊ࠭ङ"),  l1ll11_opy_ (u"࠭ࡈࡆࡃࡕࡍࡓࡍࠧच"), l1ll11_opy_ (u"ࠧࡉࡗࡑࡘࡎࡔࡇࠨछ"), l1ll11_opy_ (u"ࠨࡔࡈࡅࡑࡏ࡚ࡆࠩज"), l1ll11_opy_ (u"ࠩࡑࡓ࡙ࡎࡉࡏࡉࠪझ"), l1ll11_opy_ (u"ࠪࡓ࡛ࡋࡒࡍࡃࡓࠫञ"), l1ll11_opy_ (u"ࠫࡋࡏࡎࡅࡋࡑࡋࠬट"), l1ll11_opy_ (u"ࠬࡖࡕࡕࡖࡌࡒࡌ࠭ठ")]
    for l1l1l11_opy_ in l1111ll_opy_:
        l11ll1l1l_opy_ = l11l11l1l_opy_(l1l1l11_opy_, l11l111l1_opy_)
        l11l1l1l1_opy_(window, l11ll1l1l_opy_, location)
    l11l1l1l1_opy_(window, l1ll11_opy_ (u"࠭ࠧड"), location)
    return l1111ll_opy_[7]
def l11l11l1l_opy_(l1l1l11_opy_, size):
    #
    fill = l1ll11_opy_ (u"ࠧࠢࡂࠦࠨࠪࡤࠦࠫࠪࠬ࠱࠰ࡃࡾ࡜࡟ࡾࢁࠬढ")
    l11l1l11l_opy_ = len(l1l1l11_opy_)
    l11l1lll1_opy_ = l1ll11_opy_ (u"ࠨࠩण")
    l11l1ll1l_opy_ = randint(0, size - l11l1l11l_opy_)
    for index in range(0, l11l1ll1l_opy_):
        l11l1lll1_opy_ = l11l1lll1_opy_ + choice(fill)
    l11l1lll1_opy_ = l11l1lll1_opy_ + l1l1l11_opy_
    for index in range(l11l1ll1l_opy_ + l11l1l11l_opy_, size):
        l11l1lll1_opy_ = l11l1lll1_opy_ + choice(fill)
    return l11l1lll1_opy_
def l11l111ll_opy_(window, l1l1l11_opy_, location, l111ll1_opy_):
    prompt = l1ll11_opy_ (u"ࠩࡈࡒ࡙ࡋࡒࠡࡒࡄࡗࡘ࡝ࡏࡓࡆࠣࡂࠬत")
    l11l1llll_opy_ = [window.get_width() // 2, 0]
    l1ll11l_opy_ = l11l11ll1_opy_(window, prompt, location)
    l111ll1_opy_ = l111ll1_opy_ - 1
    while l1ll11l_opy_ != l1l1l11_opy_ and l111ll1_opy_ > 0:
        window.draw_string(str(l111ll1_opy_), 0, window.get_font_height())
        l11l11lll_opy_(window, l111ll1_opy_)
        l11ll11l1_opy_(window, l1l1l11_opy_, l1ll11l_opy_, l11l1llll_opy_)
        l1ll11l_opy_ = l11l11ll1_opy_(window, prompt, location)
        l111ll1_opy_ = l111ll1_opy_ - 1
    return l1ll11l_opy_
def l11l11lll_opy_(window, l111ll1_opy_):
    l1111l1_opy_ = l1ll11_opy_ (u"ࠪ࠮࠯࠰ࠠࡍࡑࡆࡏࡔ࡛ࡔ࡙ࠡࡄࡖࡓࡏࡎࡈࠢ࠭࠮࠯࠭थ")
    if l111ll1_opy_ == 1:
        l1llll11_opy_ = window.get_width() - window.get_string_width(l1111l1_opy_)
        l1lll1ll_opy_ = window.get_height() - window.get_font_height()
        window.draw_string(l1111l1_opy_, l1llll11_opy_, l1lll1ll_opy_)
def l11ll11l1_opy_(window, l1l1l11_opy_, l1ll11l_opy_, location):
    string = l1ll11l_opy_ + l1ll11_opy_ (u"ࠫࠥࡏࡎࡄࡑࡕࡖࡊࡉࡔࠡࠩद")
    l11l1l1l1_opy_(window, string, location)
    index = 0
    l11ll1ll1_opy_ = 0
    max = len(l1l1l11_opy_)
    for letter in l1ll11l_opy_:
        if (index < max) and (letter == l1l1l11_opy_[index]):
            l11ll1ll1_opy_ = l11ll1ll1_opy_ + 1
        index = index + 1
    string = str(l11ll1ll1_opy_) + l1ll11_opy_ (u"ࠬ࠵ࠧध") + str(max) + l1ll11_opy_ (u"࠭ࠠࡊࡐࠣࡑࡆ࡚ࡃࡉࡋࡑࡋࠥࡖࡏࡔࡋࡗࡍࡔࡔࡓࠨन")
    l11l1l1l1_opy_(window, string, location)
def l11l1ll11_opy_(window, l1ll11l_opy_, l1l1l11_opy_):
    window.clear()
    if l1ll11l_opy_ == l1l1l11_opy_:
        l11l1l_opy_ = [l1ll11l_opy_, l1ll11_opy_ (u"ࠧࠨऩ"), l1ll11_opy_ (u"ࠨࡇ࡛ࡍ࡙ࡏࡎࡈࠢࡇࡉࡇ࡛ࡇࠡࡏࡒࡈࡊ࠭प"), l1ll11_opy_ (u"ࠩࠪफ"), l1ll11_opy_ (u"ࠪࡐࡔࡍࡉࡏࠢࡖ࡙ࡈࡉࡅࡔࡕࡉ࡙ࡑ࡙ࠦ࠭ࠡࡈࡐࡈࡕࡍࡆࠢࡅࡅࡈࡑࠧब"), l1ll11_opy_ (u"ࠫࠬभ")]
        prompt = l1ll11_opy_ (u"ࠬࡖࡒࡆࡕࡖࠤࡊࡔࡔࡆࡔࠣࡘࡔࠦࡃࡐࡐࡗࡍࡓ࡛ࡅࠨम")
    else:
        l11l1l_opy_ = [l1ll11l_opy_, l1ll11_opy_ (u"࠭ࠧय"), l1ll11_opy_ (u"ࠧࡍࡑࡊࡍࡓࠦࡆࡂࡋࡏ࡙ࡗࡋࠠ࠮ࠢࡗࡉࡗࡓࡉࡏࡃࡏࠤࡑࡕࡃࡌࡇࡇࠫर"), l1ll11_opy_ (u"ࠨࠩऱ"),l1ll11_opy_ (u"ࠩࡓࡐࡊࡇࡓࡆࠢࡆࡓࡓ࡚ࡁࡄࡖࠣࡅࡓࠦࡁࡅࡏࡌࡒࡎ࡙ࡔࡓࡃࡗࡓࡗ࠭ल"), l1ll11_opy_ (u"ࠪࠫळ")]
        prompt = l1ll11_opy_ (u"ࠫࡕࡘࡅࡔࡕࠣࡉࡓ࡚ࡅࡓࠢࡗࡓࠥࡋࡘࡊࡖࠪऴ")
    location = l11ll11ll_opy_(window, l11l1l_opy_)
    location[0] = (window.get_width() - window.get_string_width(prompt)) // 2
    l11l11ll1_opy_(window, prompt, location)
    window.close()
def l11ll11ll_opy_(window, l11l1l_opy_):
    l1l1l1l_opy_ = window.get_font_height()
    l111ll_opy_ = (len(l11l1l_opy_) + 1)*l1l1l1l_opy_
    l11ll1l_opy_ = window.get_height() - l111ll_opy_
    l1llll1_opy_ = l11ll1l_opy_ // 2
    location = [0, l1llll1_opy_]
    for l11l1l1_opy_ in l11l1l_opy_:
        l11lll_opy_ = window.get_width() - window.get_string_width(l11l1l1_opy_)
        location[0] = l11lll_opy_ // 2
        l11l1l1l1_opy_(window, l11l1l1_opy_, location)
    return location
def l11l1l1l1_opy_(window, string, location):
    l111l11_opy_ = 0.3
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(l111l11_opy_)
    location[1] = location[1] + window.get_font_height()
def l11l11ll1_opy_(window, prompt, location):
    input = window.input_string(prompt, location[0], location[1])
    location[1] = location[1] + window.get_font_height()
    return input
main()