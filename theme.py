import json
from pathlib import Path
from typing import Dict


CONFIG_PATH = Path(__file__).with_name("config.json")
DEFAULT_THEME = "dark"

# Paletas centralizadas para mantener modo oscuro/claro sin tocar la logica de la app.
PALETTES: Dict[str, Dict[str, str]] = {
    "dark": {
        "background": "#0F1117",
        "surface": "#1A1D27",
        "surface_soft": "#202434",
        "border": "#2A2D3E",
        "accent": "#F97316",
        "accent_hover": "#FB923C",
        "accent_secondary": "#3B82F6",
        "text": "#F1F5F9",
        "muted": "#94A3B8",
        "input": "#252836",
        "input_alt": "#111827",
        "neutral": "#1E293B",
        "neutral_border": "#334155",
        "destructive": "#374151",
        "destructive_hover": "#EF4444",
        "warning_bg": "#1F2937",
        "warning_border": "#F97316",
        "warning_text": "#FED7AA",
        "badge_text": "#FFFFFF",
        "selection_text": "#FFFFFF",
        "mp": "#009EE3",
        "mp_hover": "#0284C7",
        "scroll": "#475569",
        "scroll_bg": "#151927",
    },
    "light": {
        "background": "#FFFFFF",
        "surface": "#F8FAFC",
        "surface_soft": "#FFFFFF",
        "border": "#E2E8F0",
        "accent": "#EA580C",
        "accent_hover": "#F97316",
        "accent_secondary": "#2563EB",
        "text": "#0F172A",
        "muted": "#64748B",
        "input": "#F1F5F9",
        "input_alt": "#FFFFFF",
        "neutral": "#F8FAFC",
        "neutral_border": "#CBD5E1",
        "destructive": "#E2E8F0",
        "destructive_hover": "#EF4444",
        "warning_bg": "#FFF7ED",
        "warning_border": "#FDBA74",
        "warning_text": "#9A3412",
        "badge_text": "#FFFFFF",
        "selection_text": "#FFFFFF",
        "mp": "#009EE3",
        "mp_hover": "#0284C7",
        "scroll": "#CBD5E1",
        "scroll_bg": "#F1F5F9",
    },
}


def load_theme_name() -> str:
    try:
        payload = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return DEFAULT_THEME
    theme_name = str(payload.get("theme", DEFAULT_THEME)).lower()
    return theme_name if theme_name in PALETTES else DEFAULT_THEME


def save_theme_name(theme_name: str) -> None:
    if theme_name not in PALETTES:
        theme_name = DEFAULT_THEME
    try:
        CONFIG_PATH.write_text(json.dumps({"theme": theme_name}, indent=2), encoding="utf-8")
    except OSError:
        pass


def theme_toggle_text(theme_name: str) -> str:
    return "\u2600\ufe0f" if theme_name == "dark" else "\U0001F319"


def build_stylesheet(theme_name: str) -> str:
    p = PALETTES.get(theme_name, PALETTES[DEFAULT_THEME])
    return f"""
        QMainWindow, QWidget {{
            background: {p["background"]};
            color: {p["text"]};
            font-family: Inter, Segoe UI, Arial, sans-serif;
            font-size: 11px;
        }}
        QLabel#title {{
            color: {p["text"]};
            font-size: 21px;
            font-weight: 850;
            letter-spacing: 1px;
        }}
        QLabel#subtitle, QLabel#footer, QLabel#dropFormats {{
            color: {p["muted"]};
            font-size: 12px;
        }}
        QLabel#miniHelp {{
            color: {p["muted"]};
            font-size: 11px;
        }}
        QLabel#badge {{
            color: {p["badge_text"]};
            background: {p["accent"]};
            border-radius: 12px;
            padding: 5px 11px;
            font-size: 10px;
            font-weight: 900;
        }}
        QLabel#sectionTitle, QLabel#performanceTitle {{
            color: {p["text"]};
            font-size: 14px;
            font-weight: 800;
            padding-bottom: 2px;
        }}
        QLabel#performanceTitle {{
            font-size: 16px;
        }}
        QLabel#status {{
            color: {p["text"]};
            font-size: 12px;
            font-weight: 750;
        }}
        QLabel#progressMeta {{
            color: {p["muted"]};
            font-size: 11px;
            font-weight: 850;
            padding-left: 8px;
        }}
        QLabel#warning {{
            color: {p["warning_text"]};
            background: {p["warning_bg"]};
            border: 1px solid {p["warning_border"]};
            border-radius: 8px;
            padding: 6px 9px;
            font-size: 11px;
            font-weight: 650;
        }}
        QLabel#controlLabel {{
            color: {p["muted"]};
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        QLabel#exportLabel {{
            color: {p["muted"]};
            font-weight: 800;
            padding-left: 8px;
            padding-right: 2px;
        }}
        QDialog#prEditDialog, QDialog#settingsDialog,
        QFrame#card, QFrame#actionsCard, QFrame#progressCard, QFrame#performancePanel, QFrame#prPanel {{
            background: {p["surface"]};
            border: 1px solid {p["border"]};
            border-radius: 8px;
        }}
        QFrame#performancePanel {{
            min-height: 110px;
        }}
        QFrame#fileLoadPanel, QFrame#performanceGrid, QFrame#modalGrid,
        QFrame#actionsRow, QFrame#prLabelPanel, QFrame#prActions, QFrame#modalActions {{
            background: transparent;
            border: none;
        }}
        QFrame#exportBar {{
            background: {p["surface_soft"]};
            border: 1px solid {p["border"]};
            border-radius: 8px;
            padding: 6px;
        }}
        QFrame#actionsRow, QFrame#exportBar, QFrame#prActions {{
            min-height: 36px;
        }}
        QFrame#headerSeparator {{
            background: {p["border"]};
            border: none;
            min-height: 1px;
            max-height: 1px;
        }}
        QFrame#fieldGroup {{
            background: transparent;
            border: none;
        }}
        QFrame#dropFrame {{
            background: {p["input_alt"]};
            border: 2px dashed {p["border"]};
            border-radius: 8px;
            min-height: 70px;
        }}
        QFrame#dropFrame:hover {{
            border-color: {p["accent"]};
            background: {p["surface_soft"]};
        }}
        QLabel#dropIcon {{
            color: {p["accent"]};
            font-size: 24px;
        }}
        QLabel#dropTitle {{
            color: {p["text"]};
            font-size: 13px;
            font-weight: 850;
        }}
        QLabel#dropSubtitle {{
            color: {p["muted"]};
            font-size: 12px;
        }}
        QCheckBox {{
            color: {p["text"]};
            font-size: 12px;
            font-weight: 650;
            spacing: 8px;
        }}
        QCheckBox::indicator {{
            width: 14px;
            height: 14px;
            border-radius: 4px;
            border: 1px solid {p["neutral_border"]};
            background: {p["input"]};
        }}
        QCheckBox::indicator:checked {{
            background: {p["accent"]};
            border: 1px solid {p["accent"]};
        }}
        QPushButton {{
            background: {p["neutral"]};
            color: {p["text"]};
            border: 1px solid {p["neutral_border"]};
            border-radius: 8px;
            padding: 6px 10px;
            font-weight: 750;
            min-height: 22px;
        }}
        QPushButton:hover {{
            border-color: {p["accent"]};
            background: {p["surface_soft"]};
        }}
        QPushButton:pressed {{
            background: {p["input"]};
        }}
        QPushButton:disabled {{
            color: {p["muted"]};
            background: {p["surface"]};
            border-color: {p["border"]};
        }}
        QPushButton#primaryButton {{
            background: {p["accent"]};
            color: #FFFFFF;
            border: 1px solid {p["accent"]};
            font-weight: 900;
        }}
        QPushButton#primaryButton:hover {{
            background: {p["accent_hover"]};
        }}
        QPushButton#performanceButton {{
            background: {p["surface_soft"]};
            color: {p["text"]};
            border: 1px solid {p["accent"]};
            border-radius: 8px;
            padding: 9px 12px;
            font-size: 14px;
            font-weight: 900;
            text-align: left;
        }}
        QPushButton#performanceButton:hover {{
            background: {p["input"]};
            border-color: {p["accent_hover"]};
        }}
        QPushButton#secondaryButton, QPushButton#cancelButton {{
            background: {p["neutral"]};
            border-color: {p["neutral_border"]};
        }}
        QPushButton#destructiveButton {{
            background: {p["destructive"]};
            border-color: {p["neutral_border"]};
        }}
        QPushButton#destructiveButton:hover {{
            color: #FFFFFF;
            background: {p["destructive_hover"]};
            border-color: {p["destructive_hover"]};
        }}
        QPushButton#chipButton {{
            border-radius: 12px;
            padding: 6px 10px;
            min-height: 22px;
            font-size: 12px;
        }}
        QPushButton#chipButton:hover {{
            color: #FFFFFF;
            background: {p["accent_secondary"]};
            border-color: {p["accent_secondary"]};
        }}
        QPushButton#themeToggle {{
            border-radius: 14px;
            min-width: 34px;
            max-width: 34px;
            padding: 6px 0;
            font-size: 15px;
        }}
        QPushButton#donateButton {{
            background: {p["mp"]};
            color: #FFFFFF;
            border-color: {p["mp"]};
            border-radius: 14px;
            padding: 6px 12px;
            font-size: 12px;
            font-weight: 850;
        }}
        QPushButton#donateButton:hover {{
            background: {p["mp_hover"]};
            border-color: {p["mp_hover"]};
        }}
        QLineEdit#filePath, QLineEdit#smallInput, QComboBox, QTextEdit, QListWidget {{
            background: {p["input"]};
            color: {p["text"]};
            border: 1px solid {p["border"]};
            border-radius: 8px;
            padding: 6px;
            selection-background-color: {p["accent"]};
            selection-color: {p["selection_text"]};
        }}
        QLineEdit#filePath {{
            font-family: Consolas, 'Courier New', monospace;
            font-size: 11px;
            font-weight: 700;
        }}
        QLineEdit#smallInput {{
            font-size: 12px;
            font-weight: 850;
            min-height: 22px;
        }}
        QLineEdit#smallInput:hover, QLineEdit#smallInput:focus {{
            border: 1px solid {p["accent"]};
        }}
        QComboBox {{
            min-height: 22px;
        }}
        QComboBox::drop-down {{
            border: none;
            width: 24px;
        }}
        QTextEdit {{
            font-family: Consolas, 'Courier New', monospace;
            font-size: 12px;
            line-height: 1.2em;
            padding: 10px;
        }}
        QTextEdit#modalTextEdit {{
            min-height: 220px;
            line-height: 1.45em;
        }}
        QListWidget {{
            font-family: Consolas, 'Courier New', monospace;
            font-size: 11px;
            padding: 6px;
        }}
        QListWidget#prBlockList {{
            min-height: 55px;
            padding: 5px;
        }}
        QListWidget#modalBlockList {{
            min-height: 105px;
            max-height: 160px;
            padding: 6px;
        }}
        QListWidget::item {{
            border-radius: 6px;
            padding: 5px;
        }}
        QListWidget::item:selected {{
            color: #FFFFFF;
            background: {p["accent_secondary"]};
        }}
        QProgressBar {{
            background: {p["input"]};
            border: 1px solid {p["border"]};
            border-radius: 5px;
            min-height: 7px;
            max-height: 7px;
            text-align: center;
            color: transparent;
        }}
        QProgressBar::chunk {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {p["accent"]}, stop:1 {p["accent_secondary"]});
            border-radius: 4px;
        }}
        QScrollBar:vertical {{
            background: {p["scroll_bg"]};
            width: 10px;
            margin: 0;
            border-radius: 5px;
        }}
        QScrollBar::handle:vertical {{
            background: {p["scroll"]};
            min-height: 32px;
            border-radius: 5px;
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 1px;
            background: transparent;
        }}
        QSplitter::handle {{
            background: {p["background"]};
            width: 8px;
        }}
    """
