import enum

from colors import base


class MaterialDesign(enum.Enum, metaclass=base.ColorEnumMeta):
    Red_50   = base.RGBColor(255, 235, 238)
    Red_100  = base.RGBColor(255, 205, 210)
    Red_200  = base.RGBColor(239, 154, 154)
    Red_300  = base.RGBColor(229, 115, 115)
    Red_400  = base.RGBColor(239,  83,  80)
    Red_500  = base.RGBColor(244,  67,  54)
    Red_600  = base.RGBColor(229,  57,  53)
    Red_700  = base.RGBColor(211,  47,  47)
    Red_800  = base.RGBColor(198,  40,  40)
    Red_900  = base.RGBColor(183,  28,  28)
    Red_A100 = base.RGBColor(255, 138, 128)
    Red_A200 = base.RGBColor(255,  82,  82)
    Red_A400 = base.RGBColor(255,  23,  68)
    Red_A700 = base.RGBColor(213,   0,   0)

    Pink_50   = base.RGBColor(252, 228, 236)
    Pink_100  = base.RGBColor(248, 187, 208)
    Pink_200  = base.RGBColor(244, 143, 177)
    Pink_300  = base.RGBColor(240,  98, 146)
    Pink_400  = base.RGBColor(236,  64, 122)
    Pink_500  = base.RGBColor(233,  30,  99)
    Pink_600  = base.RGBColor(216,  27,  96)
    Pink_700  = base.RGBColor(194,  24,  91)
    Pink_800  = base.RGBColor(173,  20,  87)
    Pink_900  = base.RGBColor(136,  14,  79)
    Pink_A100 = base.RGBColor(255, 128, 171)
    Pink_A200 = base.RGBColor(255,  64, 129)
    Pink_A400 = base.RGBColor(245,   0,  87)
    Pink_A700 = base.RGBColor(197,  17,  98)

    Purple_50   = base.RGBColor(243, 229, 245)
    Purple_100  = base.RGBColor(225, 190, 231)
    Purple_200  = base.RGBColor(206, 147, 216)
    Purple_300  = base.RGBColor(186, 104, 200)
    Purple_400  = base.RGBColor(171,  71, 188)
    Purple_500  = base.RGBColor(156,  39, 176)
    Purple_600  = base.RGBColor(142,  36, 170)
    Purple_700  = base.RGBColor(123,  31, 162)
    Purple_800  = base.RGBColor(106,  27, 154)
    Purple_900  = base.RGBColor( 74,  20, 140)
    Purple_A100 = base.RGBColor(234, 128, 252)
    Purple_A200 = base.RGBColor(224,  64, 251)
    Purple_A400 = base.RGBColor(213,   0, 249)
    Purple_A700 = base.RGBColor(170,   0, 255)

    DeepPurple_50   = base.RGBColor(237, 231, 246)
    DeepPurple_100  = base.RGBColor(209, 196, 233)
    DeepPurple_200  = base.RGBColor(179, 157, 219)
    DeepPurple_300  = base.RGBColor(149, 117, 205)
    DeepPurple_400  = base.RGBColor(126,  87, 194)
    DeepPurple_500  = base.RGBColor(103,  58, 183)
    DeepPurple_600  = base.RGBColor( 94,  53, 177)
    DeepPurple_700  = base.RGBColor( 81,  45, 168)
    DeepPurple_800  = base.RGBColor( 69,  39, 160)
    DeepPurple_900  = base.RGBColor( 49,  27, 146)
    DeepPurple_A100 = base.RGBColor(179, 136, 255)
    DeepPurple_A200 = base.RGBColor(124,  77, 255)
    DeepPurple_A400 = base.RGBColor(101,  31, 255)
    DeepPurple_A700 = base.RGBColor( 98,   0, 234)

    Indigo_50   = base.RGBColor(232, 234, 246)
    Indigo_100  = base.RGBColor(197, 202, 233)
    Indigo_200  = base.RGBColor(159, 168, 218)
    Indigo_300  = base.RGBColor(121, 134, 203)
    Indigo_400  = base.RGBColor( 92, 107, 192)
    Indigo_500  = base.RGBColor( 63,  81, 181)
    Indigo_600  = base.RGBColor( 57,  73, 171)
    Indigo_700  = base.RGBColor( 48,  63, 159)
    Indigo_800  = base.RGBColor( 40,  53, 147)
    Indigo_900  = base.RGBColor( 26,  35, 126)
    Indigo_A100 = base.RGBColor(140, 158, 255)
    Indigo_A200 = base.RGBColor( 83, 109, 254)
    Indigo_A400 = base.RGBColor( 61,  90, 254)
    Indigo_A700 = base.RGBColor( 48,  79, 254)

    Blue_50   = base.RGBColor(227, 242, 253)
    Blue_100  = base.RGBColor(187, 222, 251)
    Blue_200  = base.RGBColor(144, 202, 249)
    Blue_300  = base.RGBColor(100, 181, 246)
    Blue_400  = base.RGBColor( 66, 165, 245)
    Blue_500  = base.RGBColor( 33, 150, 243)
    Blue_600  = base.RGBColor( 30, 136, 229)
    Blue_700  = base.RGBColor( 25, 118, 210)
    Blue_800  = base.RGBColor( 21, 101, 192)
    Blue_900  = base.RGBColor( 13,  71, 161)
    Blue_A100 = base.RGBColor(130, 177, 255)
    Blue_A200 = base.RGBColor( 68, 138, 255)
    Blue_A400 = base.RGBColor( 41, 121, 255)
    Blue_A700 = base.RGBColor( 41,  98, 255)

    LightBlue_50   = base.RGBColor(225, 245, 254)
    LightBlue_100  = base.RGBColor(179, 229, 252)
    LightBlue_200  = base.RGBColor(129, 212, 250)
    LightBlue_300  = base.RGBColor( 79, 195, 247)
    LightBlue_400  = base.RGBColor( 41, 182, 246)
    LightBlue_500  = base.RGBColor(  3, 169, 244)
    LightBlue_600  = base.RGBColor(  3, 155, 229)
    LightBlue_700  = base.RGBColor(  2, 136, 209)
    LightBlue_800  = base.RGBColor(  2, 119, 189)
    LightBlue_900  = base.RGBColor(  1,  87, 155)
    LightBlue_A100 = base.RGBColor(128, 216, 255)
    LightBlue_A200 = base.RGBColor( 64, 196, 255)
    LightBlue_A400 = base.RGBColor(  0, 176, 255)
    LightBlue_A700 = base.RGBColor(  0, 145, 234)

    Cyan_50   = base.RGBColor(224, 247, 250)
    Cyan_100  = base.RGBColor(178, 235, 242)
    Cyan_200  = base.RGBColor(128, 222, 234)
    Cyan_300  = base.RGBColor( 77, 208, 225)
    Cyan_400  = base.RGBColor( 38, 198, 218)
    Cyan_500  = base.RGBColor(  0, 188, 212)
    Cyan_600  = base.RGBColor(  0, 172, 193)
    Cyan_700  = base.RGBColor(  0, 151, 167)
    Cyan_800  = base.RGBColor(  0, 131, 143)
    Cyan_900  = base.RGBColor(  0,  96, 100)
    Cyan_A100 = base.RGBColor(132, 255, 255)
    Cyan_A200 = base.RGBColor( 24, 255, 255)
    Cyan_A400 = base.RGBColor(  0, 229, 255)
    Cyan_A700 = base.RGBColor(  0, 184, 212)

    Teal_50   = base.RGBColor(224, 242, 241)
    Teal_100  = base.RGBColor(178, 223, 219)
    Teal_200  = base.RGBColor(128, 203, 196)
    Teal_300  = base.RGBColor( 77, 182, 172)
    Teal_400  = base.RGBColor( 38, 166, 154)
    Teal_500  = base.RGBColor(  0, 150, 136)
    Teal_600  = base.RGBColor(  0, 137, 123)
    Teal_700  = base.RGBColor(  0, 121, 107)
    Teal_800  = base.RGBColor(  0, 105,  92)
    Teal_900  = base.RGBColor(  0,  77,  64)
    Teal_A100 = base.RGBColor(167, 255, 235)
    Teal_A200 = base.RGBColor(100, 255, 218)
    Teal_A400 = base.RGBColor( 29, 233, 182)
    Teal_A700 = base.RGBColor(  0, 191, 165)

    Green_50   = base.RGBColor(232, 245, 233)
    Green_100  = base.RGBColor(200, 230, 201)
    Green_200  = base.RGBColor(165, 214, 167)
    Green_300  = base.RGBColor(129, 199, 132)
    Green_400  = base.RGBColor(102, 187, 106)
    Green_500  = base.RGBColor( 76, 175,  80)
    Green_600  = base.RGBColor( 67, 160,  71)
    Green_700  = base.RGBColor( 56, 142,  60)
    Green_800  = base.RGBColor( 46, 125,  50)
    Green_900  = base.RGBColor( 27,  94,  32)
    Green_A100 = base.RGBColor(185, 246, 202)
    Green_A200 = base.RGBColor(105, 240, 174)
    Green_A400 = base.RGBColor(  0, 230, 118)
    Green_A700 = base.RGBColor(  0, 200,  83)

    LightGreen_50   = base.RGBColor(241, 248, 233)
    LightGreen_100  = base.RGBColor(220, 237, 200)
    LightGreen_200  = base.RGBColor(197, 225, 165)
    LightGreen_300  = base.RGBColor(174, 213, 129)
    LightGreen_400  = base.RGBColor(156, 204, 101)
    LightGreen_500  = base.RGBColor(139, 195,  74)
    LightGreen_600  = base.RGBColor(124, 179,  66)
    LightGreen_700  = base.RGBColor(104, 159,  56)
    LightGreen_800  = base.RGBColor( 85, 139,  47)
    LightGreen_900  = base.RGBColor( 51, 105,  30)
    LightGreen_A100 = base.RGBColor(204, 255, 144)
    LightGreen_A200 = base.RGBColor(178, 255,  89)
    LightGreen_A400 = base.RGBColor(118, 255,   3)
    LightGreen_A700 = base.RGBColor(100, 221,  23)

    Lime_50   = base.RGBColor(249, 251, 231)
    Lime_100  = base.RGBColor(240, 244, 195)
    Lime_200  = base.RGBColor(230, 238, 156)
    Lime_300  = base.RGBColor(220, 231, 117)
    Lime_400  = base.RGBColor(212, 225,  87)
    Lime_500  = base.RGBColor(205, 220,  57)
    Lime_600  = base.RGBColor(192, 202,  51)
    Lime_700  = base.RGBColor(175, 180,  43)
    Lime_800  = base.RGBColor(158, 157,  36)
    Lime_900  = base.RGBColor(130, 119,  23)
    Lime_A100 = base.RGBColor(244, 255, 129)
    Lime_A200 = base.RGBColor(238, 255,  65)
    Lime_A400 = base.RGBColor(198, 255,   0)
    Lime_A700 = base.RGBColor(174, 234,   0)

    Yellow_50   = base.RGBColor(255, 253, 231)
    Yellow_100  = base.RGBColor(255, 249, 196)
    Yellow_200  = base.RGBColor(255, 245, 157)
    Yellow_300  = base.RGBColor(255, 241, 118)
    Yellow_400  = base.RGBColor(255, 238,  88)
    Yellow_500  = base.RGBColor(255, 235,  59)
    Yellow_600  = base.RGBColor(253, 216,  53)
    Yellow_700  = base.RGBColor(251, 192,  45)
    Yellow_800  = base.RGBColor(249, 168,  37)
    Yellow_900  = base.RGBColor(245, 127,  23)
    Yellow_A100 = base.RGBColor(255, 255, 141)
    Yellow_A200 = base.RGBColor(255, 255,   0)
    Yellow_A400 = base.RGBColor(255, 234,   0)
    Yellow_A700 = base.RGBColor(255, 214,   0)

    Amber_50   = base.RGBColor(255, 248, 225)
    Amber_100  = base.RGBColor(255, 236, 179)
    Amber_200  = base.RGBColor(255, 224, 130)
    Amber_300  = base.RGBColor(255, 213,  79)
    Amber_400  = base.RGBColor(255, 202,  40)
    Amber_500  = base.RGBColor(255, 193,   7)
    Amber_600  = base.RGBColor(255, 179,   0)
    Amber_700  = base.RGBColor(255, 160,   0)
    Amber_800  = base.RGBColor(255, 143,   0)
    Amber_900  = base.RGBColor(255, 111,   0)
    Amber_A100 = base.RGBColor(255, 229, 127)
    Amber_A200 = base.RGBColor(255, 215,  64)
    Amber_A400 = base.RGBColor(255, 196,   0)
    Amber_A700 = base.RGBColor(255, 171,   0)

    Orange_50   = base.RGBColor(255, 243, 224)
    Orange_100  = base.RGBColor(255, 224, 178)
    Orange_200  = base.RGBColor(255, 204, 128)
    Orange_300  = base.RGBColor(255, 183,  77)
    Orange_400  = base.RGBColor(255, 167,  38)
    Orange_500  = base.RGBColor(255, 152,   0)
    Orange_600  = base.RGBColor(251, 140,   0)
    Orange_700  = base.RGBColor(245, 124,   0)
    Orange_800  = base.RGBColor(239, 108,   0)
    Orange_900  = base.RGBColor(230,  81,   0)
    Orange_A100 = base.RGBColor(255, 209, 128)
    Orange_A200 = base.RGBColor(255, 171,  64)
    Orange_A400 = base.RGBColor(255, 145,   0)
    Orange_A700 = base.RGBColor(255, 109,   0)

    DeepOrange_50   = base.RGBColor(251, 233, 231)
    DeepOrange_100  = base.RGBColor(255, 204, 188)
    DeepOrange_200  = base.RGBColor(255, 171, 145)
    DeepOrange_300  = base.RGBColor(255, 138, 101)
    DeepOrange_400  = base.RGBColor(255, 112,  67)
    DeepOrange_500  = base.RGBColor(255,  87,  34)
    DeepOrange_600  = base.RGBColor(244,  81,  30)
    DeepOrange_700  = base.RGBColor(230,  74,  25)
    DeepOrange_800  = base.RGBColor(216,  67,  21)
    DeepOrange_900  = base.RGBColor(191,  54,  12)
    DeepOrange_A100 = base.RGBColor(255, 158, 128)
    DeepOrange_A200 = base.RGBColor(255, 110,  64)
    DeepOrange_A400 = base.RGBColor(255,  61,   0)
    DeepOrange_A700 = base.RGBColor(221,  44,   0)

    Brown_50  = base.RGBColor(239, 235, 233)
    Brown_100 = base.RGBColor(215, 204, 200)
    Brown_200 = base.RGBColor(188, 170, 164)
    Brown_300 = base.RGBColor(161, 136, 127)
    Brown_400 = base.RGBColor(141, 110,  99)
    Brown_500 = base.RGBColor(121,  85,  72)
    Brown_600 = base.RGBColor(109,  76,  65)
    Brown_700 = base.RGBColor( 93,  64,  55)
    Brown_800 = base.RGBColor( 78,  52,  46)
    Brown_900 = base.RGBColor( 62,  39,  35)

    Grey_50  = base.RGBColor(250, 250, 250)
    Grey_100 = base.RGBColor(245, 245, 245)
    Grey_200 = base.RGBColor(238, 238, 238)
    Grey_300 = base.RGBColor(224, 224, 224)
    Grey_400 = base.RGBColor(189, 189, 189)
    Grey_500 = base.RGBColor(158, 158, 158)
    Grey_600 = base.RGBColor(117, 117, 117)
    Grey_700 = base.RGBColor( 97,  97,  97)
    Grey_800 = base.RGBColor( 66,  66,  66)
    Grey_900 = base.RGBColor( 33,  33,  33)

    BlueGrey_50  = base.RGBColor(236, 239, 241)
    BlueGrey_100 = base.RGBColor(207, 216, 220)
    BlueGrey_200 = base.RGBColor(176, 190, 197)
    BlueGrey_300 = base.RGBColor(144, 164, 174)
    BlueGrey_400 = base.RGBColor(120, 144, 156)
    BlueGrey_500 = base.RGBColor( 96, 125, 139)
    BlueGrey_600 = base.RGBColor( 84, 110, 122)
    BlueGrey_700 = base.RGBColor( 69,  90, 100)
    BlueGrey_800 = base.RGBColor( 55,  71,  79)
    BlueGrey_900 = base.RGBColor( 38,  50,  56)

    Black = base.RGBColor(  0,   0,   0)
    White = base.RGBColor(255, 255, 255)
