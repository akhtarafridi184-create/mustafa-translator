import sys
from deep_translator import GoogleTranslator

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QComboBox, QPushButton, QHBoxLayout
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Mustafa Translator")
window.resize(400, 650)

layout = QVBoxLayout()

title = QLabel("🌍 Mustafa Translator")
layout.addWidget(title)

text_box = QTextEdit()
text_box.setPlaceholderText("یہاں اپنا جملہ لکھیں...")
layout.addWidget(text_box)

languages = {
    "اردو": "ur",
    "English": "en",
    "عربی": "ar",
    "ہندی": "hi",
    "پنجابی": "pa",
    "پشتو": "ps",
    "فارسی": "fa",
    "سندھی": "sd",
    "بنگالی": "bn",
    "ترکی": "tr",
    "فرانسیسی": "fr",
    "جرمن": "de",
    "ہسپانوی": "es",
    "اطالوی": "it",
    "پرتگالی": "pt",
    "روسی": "ru",
    "چینی": "zh-CN",
    "جاپانی": "ja",
    "کوریائی": "ko",
    "تھائی": "th",
    "ویتنامی": "vi",
    "انڈونیشی": "id",
    "ملائی": "ms",
    "یونانی": "el",
    "عبرانی": "he",
    "ڈچ": "nl",
    "پولش": "pl",
    "رومانی": "ro",
    "یوکرینی": "uk",
    "سویڈش": "sv",
    "ناروے": "no",
    "ڈینش": "da",
    "فن لینڈ": "fi",
    "چیک": "cs",
    "ہنگیرین": "hu"
}

language = QComboBox()

for name in languages:
    language.addItem(name)

layout.addWidget(language)

buttons = QHBoxLayout()

translate_button = QPushButton("🔄 ترجمہ")
copy_button = QPushButton("📋 Copy")
clear_button = QPushButton("🧹 Clear")

buttons.addWidget(translate_button)
buttons.addWidget(copy_button)
buttons.addWidget(clear_button)

layout.addLayout(buttons)

result = QTextEdit()
result.setReadOnly(True)
result.setPlaceholderText("ترجمہ یہاں آئے گا...")
layout.addWidget(result)


def translate():
    text = text_box.toPlainText()

    if text:
        target = languages[language.currentText()]

        translated = GoogleTranslator(
            source="auto",
            target=target
        ).translate(text)

        result.setText(translated)


def copy_text():
    result.selectAll()
    result.copy()


def clear_text():
    text_box.clear()
    result.clear()


translate_button.clicked.connect(translate)
copy_button.clicked.connect(copy_text)
clear_button.clicked.connect(clear_text)

window.setLayout(layout)
window.show()

sys.exit(app.exec())