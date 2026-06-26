"""
Reusable UI Components
Productivity OS
"""

from theme import COLORS, FONT


def title(workbook):
    return workbook.add_format({
        "bold": True,
        "font_name": FONT,
        "font_size": 24,
        "font_color": COLORS["text"],
        "align": "center",
        "valign": "vcenter",
        "bg_color": COLORS["primary"]
    })


def heading(workbook):
    return workbook.add_format({
        "bold": True,
        "font_name": FONT,
        "font_size": 14,
        "font_color": COLORS["text"],
        "bg_color": COLORS["surface"],
        "border": 1,
        "border_color": COLORS["border"]
    })


def body(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "font_size": 11,
        "font_color": COLORS["text"],
        "bg_color": COLORS["background"]
    })


def card(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "font_size": 14,
        "bold": True,
        "align": "center",
        "valign": "vcenter",
        "text_wrap": True,
        "font_color": COLORS["text"],
        "bg_color": COLORS["card"],
        "border": 1,
        "border_color": COLORS["border"]
    })


def sidebar(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "font_size": 11,
        "bold": True,
        "font_color": COLORS["text"],
        "bg_color": COLORS["surface"],
        "align": "left",
        "valign": "vcenter"
    })


def success(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "bold": True,
        "font_color": "#FFFFFF",
        "bg_color": COLORS["success"],
        "align": "center"
    })


def warning(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "bold": True,
        "font_color": "#FFFFFF",
        "bg_color": COLORS["warning"],
        "align": "center"
    })


def danger(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "bold": True,
        "font_color": "#FFFFFF",
        "bg_color": COLORS["danger"],
        "align": "center"
    })


def muted(workbook):
    return workbook.add_format({
        "font_name": FONT,
        "italic": True,
        "font_color": COLORS["muted"],
        "bg_color": COLORS["background"]
    })