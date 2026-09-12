#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


# ============================================================
# KleopatraKindomOS OOBE
# ============================================================

# Ubiquity отвечает за:
#   - разметку диска
#   - установку системы
#   - загрузчик
#   - базовое создание пользователя
#
# OOBE отвечает за:
#   - лицензию
#   - оформление
#   - рабочий стол
#   - активацию
#   - завершение первоначальной настройки
# ============================================================


# ------------------------------------------------------------
# Язык
# ------------------------------------------------------------

def detect_language():
    try:
        lang = locale.getlocale()[0] or ""
    except Exception:
        lang = ""

    lang = lang.lower()

    for code in [
        "ru",
        "uk",
        "en",
        "de",
        "fr",
        "es",
        "it",
        "pl",
        "cs",
        "sk",
        "nl",
        "tr",
        "sv",
        "fi",
        "da",
        "no",
        "ja",
        "ko",
        "zh",
        "ar",
        "hi"
    ]:
        if lang.startswith(code):
            return code

    return "en"


LANG = detect_language()


TEXT = {

"en": {

"app_title":
"KleopatraKindomOS — Initial Setup",

"welcome":
"Welcome",

"welcome_text":
"Welcome to KleopatraKindomOS.\n\n"
"This wizard will help you configure the system after installation.",

"license":
"System License",

"license_accept":
"I accept the KleopatraKindomOS license agreement",

"license_required":
"You must accept the license agreement to continue.",

"appearance":
"Appearance",

"theme":
"Theme",

"theme_light":
"Light",

"theme_dark":
"Dark",

"theme_auto":
"Automatic",

"panel":
"Panel position",

"panel_bottom":
"Bottom",

"panel_left":
"Left",

"panel_right":
"Right",

"animations":
"Animations",

"animations_on":
"Enable animations",

"desktop":
"Desktop",

"desktop_icons":
"Show desktop icons",

"home_icon":
"Show Home folder",

"trash_icon":
"Show Trash",

"double_click":
"Open items with double click",

"auto_trash":
"Automatically empty Trash",

"focus_hover":
"Focus windows when hovering",

"activation":
"Activation",

"activation_text":
"KleopatraKindomOS activation is required to continue.\n\n"
"Enter the activation code provided by the system developers.",

"activation_code":
"Activation code",

"activate":
"Activate",

"activation_success":
"KleopatraKindomOS has been successfully activated.",

"activation_error":
"Invalid activation code.",

"activation_required":
"You must activate the system to continue.",

"finish":
"Finish",

"finish_text":
"The initial KleopatraKindomOS setup is complete.\n\n"
"Click Finish to apply the settings and continue to the desktop.",

"back":
"Back",

"next":
"Next",

"finish_button":
"Finish",

"step":
"Step",

"of":
"of",

"system_ready":
"System is ready",

"activation_status":
"Activation status",

"activated":
"Activated"

}

}


def merge_language(base, update):
    result = base.copy()
    result.update(update)
    return result


TEXT["ru"] = merge_language(
    TEXT["en"],
    {

    "app_title":
        "KleopatraKindomOS — первоначальная настройка",

    "welcome":
        "Добро пожаловать",

    "welcome_text":
        "Добро пожаловать в KleopatraKindomOS.\n\n"
        "Этот мастер поможет выполнить первоначальную "
        "настройку системы после установки.",

    "license":
        "Лицензия системы",

    "license_accept":
        "Я принимаю условия лицензионного соглашения "
        "KleopatraKindomOS",

    "license_required":
        "Для продолжения необходимо принять "
        "лицензионное соглашение.",

    "appearance":
        "Оформление",

    "theme":
        "Тема",

    "theme_light":
        "Светлая",

    "theme_dark":
        "Тёмная",

    "theme_auto":
        "Автоматическая",

    "panel":
        "Положение панели",

    "panel_bottom":
        "Снизу",

    "panel_left":
        "Слева",

    "panel_right":
        "Справа",

    "animations":
        "Анимации",

    "animations_on":
        "Включить анимации",

    "desktop":
        "Рабочий стол",

    "desktop_icons":
        "Показывать значки на рабочем столе",

    "home_icon":
        "Показывать папку «Домашняя»",

    "trash_icon":
        "Показывать «Корзину»",

    "double_click":
        "Открывать элементы двойным щелчком",

    "auto_trash":
        "Автоматически очищать корзину",

    "focus_hover":
        "Фокусировать окна при наведении курсора",

    "activation":
        "Активация",

    "activation_text":
        "Для продолжения необходимо активировать "
        "KleopatraKindomOS.\n\n"
        "Введите код активации, предоставленный "
        "разработчиками системы.",

    "activation_code":
        "Код активации",

    "activate":
        "Активировать",

    "activation_success":
        "KleopatraKindomOS успешно активирована.",

    "activation_error":
        "Неверный код активации.",

    "activation_required":
        "Для продолжения необходимо активировать систему.",

    "activation_status":
        "Статус активации",

    "activated":
        "Активировано",

    "finish":
        "Завершение",

    "finish_text":
        "Первоначальная настройка KleopatraKindomOS завершена.\n\n"
        "Нажмите «Завершить», чтобы применить настройки "
        "и перейти к рабочему столу.",

    "back":
        "Назад",

    "next":
        "Далее",

    "finish_button":
        "Завершить",

    "step":
        "Шаг",

    "of":
        "из",

    "system_ready":
        "Система готова к работе"
    }
)


TEXT["uk"] = merge_language(
    TEXT["en"],
    {
"welcome":"Ласкаво просимо",
"license":"Ліцензія системи",
"appearance":"Оформлення",
"desktop":"Робочий стіл",
"activation":"Активація",
"finish":"Завершення",
"next":"Далі",
"back":"Назад",
"finish_button":"Завершити"
})


TEXT["de"] = merge_language(
    TEXT["en"],
    {
"welcome":"Willkommen",
"license":"Systemlizenz",
"appearance":"Darstellung",
"desktop":"Desktop",
"activation":"Aktivierung",
"finish":"Fertig",
"next":"Weiter",
"back":"Zurück",
"finish_button":"Beenden"
})


TEXT["fr"] = merge_language(
    TEXT["en"],
    {
"welcome":"Bienvenue",
"license":"Licence système",
"appearance":"Apparence",
"desktop":"Bureau",
"activation":"Activation",
"finish":"Terminer",
"next":"Suivant",
"back":"Retour",
"finish_button":"Terminer"
})


TEXT["es"] = merge_language(
    TEXT["en"],
    {
"welcome":"Bienvenido",
"license":"Licencia del sistema",
"appearance":"Apariencia",
"desktop":"Escritorio",
"activation":"Activación",
"finish":"Finalizar",
"next":"Siguiente",
"back":"Atrás",
"finish_button":"Finalizar"
})


TEXT["it"] = merge_language(
    TEXT["en"],
    {
"welcome":"Benvenuto",
"license":"Licenza di sistema",
"appearance":"Aspetto",
"desktop":"Desktop",
"activation":"Attivazione",
"finish":"Fine",
"next":"Avanti",
"back":"Indietro",
"finish_button":"Fine"
})


TEXT["pl"] = merge_language(
    TEXT["en"],
    {
"welcome":"Witamy",
"license":"Licencja systemu",
"appearance":"Wygląd",
"desktop":"Pulpit",
"activation":"Aktywacja",
"finish":"Zakończenie",
"next":"Dalej",
"back":"Wstecz",
"finish_button":"Zakończ"
})


TEXT["ja"] = merge_language(
    TEXT["en"],
    {
"welcome":"ようこそ",
"license":"システムライセンス",
"appearance":"外観",
"desktop":"デスクトップ",
"activation":"アクティベーション",
"finish":"完了",
"next":"次へ",
"back":"戻る",
"finish_button":"完了"
})


TEXT["ko"] = merge_language(
    TEXT["en"],
    {
"welcome":"환영합니다",
"license":"시스템 라이선스",
"appearance":"모양",
"desktop":"바탕 화면",
"activation":"활성화",
"finish":"완료",
"next":"다음",
"back":"뒤로",
"finish_button":"완료"
})


TEXT["zh"] = merge_language(
    TEXT["en"],
    {
"welcome":"欢迎",
"license":"系统许可证",
"appearance":"外观",
"desktop":"桌面",
"activation":"激活",
"finish":"完成",
"next":"下一步",
"back":"返回",
"finish_button":"完成"
})


TEXT["ar"] = merge_language(
    TEXT["en"],
    {
"welcome":"مرحبا",
"license":"ترخيص النظام",
"appearance":"المظهر",
"desktop":"سطح المكتب",
"activation":"التنشيط",
"finish":"إنهاء",
"next":"التالي",
"back":"رجوع",
"finish_button":"إنهاء"
})


TEXT["hi"] = merge_language(
    TEXT["en"],
    {
"welcome":"स्वागत है",
"license":"सिस्टम लाइसेंस",
"appearance":"रूप",
"desktop":"डेस्कटॉप",
"activation":"सक्रियण",
"finish":"समाप्त",
"next":"आगे",
"back":"पीछे",
"finish_button":"समाप्त"
})


T = TEXT.get(
    LANG,
    TEXT["en"]
)


# ------------------------------------------------------------
# KLICENSE
# ------------------------------------------------------------

KLICENSE_RU = """
Лицензия KleopatraKindom

Любой контрибьютор может вносить изменения в ОС,
Однако любые патчи должны быть в ПРИВАТНОМ репозитории
https://github.com/KleopatraKindom-Inc/kleopatrakindomos-tmp .

Пользователь который НЕ является участником разработки
(контрибьютором) не имеет права вносить изменений.

Стать участником группы можно на:
https://kleopatrakindom.ddns.net/become-a-contributer.html

Используя KleopatraKindomOS, вы принимаете
условия данного лицензионного соглашения.
"""


KLICENSE_EN = """
KleopatraKindom License

Any contributor may make changes to the OS.

However, all patches must be stored in the PRIVATE repository:
https://github.com/KleopatraKindom-Inc/kleopatrakindomos-tmp

A user who is NOT a member of the development group
(contributor) does not have the right to make changes.

You can become a group member at:
https://kleopatrakindom.ddns.net/become-a-contributer.html

By using KleopatraKindomOS, you accept
the terms of this license agreement.
"""


KLICENSE_UK = """
Ліцензія KleopatraKindom

Будь-який контриб'ютор може вносити зміни до ОС.

Однак усі патчі повинні зберігатися у ПРИВАТНОМУ репозиторії:
https://github.com/KleopatraKindom-Inc/kleopatrakindomos-tmp

Користувач, який НЕ є учасником розробки
(контриб'ютором), не має права вносити зміни.

Стати учасником групи можна на:
https://kleopatrakindom.ddns.net/become-a-contributer.html

Використовуючи KleopatraKindomOS, ви приймаєте
умови цієї ліцензійної угоди.
"""


KLICENSE_DE = """
KleopatraKindom Lizenz

Jeder Mitwirkende darf Änderungen am Betriebssystem vornehmen.

Alle Patches müssen jedoch im PRIVATEN Repository gespeichert werden:
https://github.com/KleopatraKindom-Inc/kleopatrakindomos-tmp

Benutzer, die KEINE Mitglieder des Entwicklerteams
(Mitwirkende) sind, dürfen keine Änderungen vornehmen.

Durch die Nutzung von KleopatraKindomOS akzeptieren Sie
diese Lizenzvereinbarung.
"""


KLICENSE_FR = """
Licence KleopatraKindom

Tout contributeur peut apporter des modifications au système.

Cependant, tous les correctifs doivent être stockés dans le dépôt PRIVÉ :
https://github.com/KleopatraKindom-Inc/kleopatrakindomos-tmp

Un utilisateur qui n'est PAS membre du groupe de développement
(contributeur) n'est pas autorisé à modifier le système.

En utilisant KleopatraKindomOS, vous acceptez
les termes de cette licence.
"""


KLICENSE_ES = """
Licencia KleopatraKindom

Cualquier colaborador puede realizar cambios en el sistema.

Sin embargo, todos los parches deben almacenarse en el repositorio PRIVADO:
https://github.com/KleopatraKindom-Inc/kleopatrakindomos-tmp

Un usuario que NO sea miembro del grupo de desarrollo
(colaborador) no tiene derecho a realizar cambios.

Al utilizar KleopatraKindomOS acepta
los términos de esta licencia.
"""


KLICENSE = {
    "ru": KLICENSE_RU,
    "uk": KLICENSE_UK,
    "en": KLICENSE_EN,
    "de": KLICENSE_DE,
    "fr": KLICENSE_FR,
    "es": KLICENSE_ES,
}.get(
    LANG,
    KLICENSE_EN
)


# ------------------------------------------------------------
# Код активации
# ------------------------------------------------------------

ACTIVATION_CODE = "$KOS:47591479754"


# ------------------------------------------------------------
# Файл завершения OOBE
# ------------------------------------------------------------

OOBE_COMPLETE_FILE = Path(
    "/etc/kleopatrakindomos-oobe-complete"
)


# ------------------------------------------------------------
# Главное окно
# ------------------------------------------------------------

class OOBEWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.current_page = 0

        # 1 Welcome
        # 2 License
        # 3 Appearance
        # 4 Desktop
        # 5 Activation
        # 6 Finish

        self.pages_count = 6

        self.activation_successful = False

        self.setWindowTitle(
            T["app_title"]
        )

        self.setMinimumSize(
            900,
            600
        )

        self.build_ui()
        self.apply_style()

        # Полноэкранный режим
        self.showFullScreen()

    # ========================================================
    # Построение интерфейса
    # ========================================================

    def build_ui(self):

        root = QWidget()

        root_layout = QHBoxLayout(root)

        root_layout.setContentsMargins(
            0, 0, 0, 0
        )

        root_layout.setSpacing(0)

        # ----------------------------------------------------
        # Левая панель
        # ----------------------------------------------------

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")

        sidebar_layout = QVBoxLayout(
            sidebar
        )

        sidebar_layout.setContentsMargins(
            36, 42, 36, 36
        )

        sidebar_layout.setSpacing(18)

        logo = QLabel("K")

        logo.setObjectName("logo")

        logo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        sidebar_layout.addWidget(logo)

        brand = QLabel(
            "KleopatraKindomOS"
        )

        brand.setObjectName("brand")

        brand.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        sidebar_layout.addWidget(brand)

        sidebar_layout.addSpacing(30)

        step_names = [
            T["welcome"],
            T["license"],
            T["appearance"],
            T["desktop"],
            T["activation"],
            T["finish"],
        ]

        self.step_labels = []

        for index, name in enumerate(
            step_names
        ):

            label = QLabel(
                f"{index + 1}.  {name}"
            )

            label.setObjectName(
                "step"
            )

            sidebar_layout.addWidget(
                label
            )

            self.step_labels.append(
                label
            )

        sidebar_layout.addStretch()

        version = QLabel(
            "KleopatraKindomOS"
        )

        version.setObjectName(
            "version"
        )

        sidebar_layout.addWidget(
            version
        )

        # ----------------------------------------------------
        # Основная область
        # ----------------------------------------------------

        main = QWidget()

        main_layout = QVBoxLayout(main)

        main_layout.setContentsMargins(
            70, 55, 70, 35
        )

        main_layout.setSpacing(20)

        self.stack = QStackedWidget()

        self.stack.setObjectName(
            "stack"
        )

        self.create_welcome_page()
        self.create_license_page()
        self.create_appearance_page()
        self.create_desktop_page()
        self.create_activation_page()
        self.create_finish_page()

        main_layout.addWidget(
            self.stack
        )

        # ----------------------------------------------------
        # Навигация
        # ----------------------------------------------------

        navigation = QHBoxLayout()

        navigation.setSpacing(12)

        self.status_label = QLabel()

        self.status_label.setObjectName(
            "status"
        )

        navigation.addWidget(
            self.status_label
        )

        navigation.addStretch()

        self.back_button = QPushButton(
            T["back"]
        )

        self.back_button.setObjectName(
            "secondaryButton"
        )

        self.back_button.clicked.connect(
            self.previous_page
        )

        self.next_button = QPushButton(
            T["next"]
        )

        self.next_button.setObjectName(
            "primaryButton"
        )

        self.next_button.clicked.connect(
            self.next_page
        )

        navigation.addWidget(
            self.back_button
        )

        navigation.addWidget(
            self.next_button
        )

        main_layout.addLayout(
            navigation
        )

        root_layout.addWidget(
            sidebar
        )

        root_layout.addWidget(
            main,
            1
        )

        self.setCentralWidget(root)

        self.update_navigation()

    # ========================================================
    # Вспомогательные элементы
    # ========================================================

    def page_title(self, text):

        label = QLabel(text)

        label.setObjectName(
            "pageTitle"
        )

        return label

    def page_text(self, text):

        label = QLabel(text)

        label.setObjectName(
            "pageText"
        )

        label.setWordWrap(True)

        return label

    def card(self):

        frame = QFrame()

        frame.setObjectName(
            "card"
        )

        layout = QVBoxLayout(frame)

        layout.setContentsMargins(
            25, 22, 25, 22
        )

        layout.setSpacing(16)

        return frame, layout

    # ========================================================
    # Страница 1 — Добро пожаловать
    # ========================================================

    def create_welcome_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(25)

        layout.addWidget(
            self.page_title(
                T["welcome"]
            )
        )

        layout.addWidget(
            self.page_text(
                T["welcome_text"]
            )
        )

        card, card_layout = self.card()

        title = QLabel(
            T["system_ready"]
        )

        title.setObjectName(
            "infoTitle"
        )

        card_layout.addWidget(
            title
        )

        text = QLabel(
            "KleopatraKindomOS"
        )

        text.setObjectName(
            "cardText"
        )

        card_layout.addWidget(
            text
        )

        layout.addWidget(card)

        layout.addStretch()

        self.stack.addWidget(page)

    # ========================================================
    # Страница 2 — Лицензия
    # ========================================================

    def create_license_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(20)

        layout.addWidget(
            self.page_title(
                T["license"]
            )
        )

        license_box = QFrame()

        license_box.setObjectName(
            "licenseBox"
        )

        license_layout = QVBoxLayout(
            license_box
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QFrame.Shape.NoFrame
        )

        container = QWidget()

        container_layout = QVBoxLayout(
            container
        )

        license_label = QLabel(
            KLICENSE
        )

        license_label.setWordWrap(
            True
        )

        license_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        license_label.setObjectName(
            "licenseText"
        )

        container_layout.addWidget(
            license_label
        )

        container_layout.addStretch()

        scroll.setWidget(
            container
        )

        license_layout.addWidget(
            scroll
        )

        layout.addWidget(
            license_box,
            1
        )

        self.license_checkbox = QCheckBox(
            T["license_accept"]
        )

        self.license_checkbox.stateChanged.connect(
            self.update_navigation
        )

        layout.addWidget(
            self.license_checkbox
        )

        self.stack.addWidget(page)

    # ========================================================
    # Страница 3 — Оформление
    # ========================================================

    def create_appearance_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(20)

        layout.addWidget(
            self.page_title(
                T["appearance"]
            )
        )

        # ----------------------------------------------------
        # Тема
        # ----------------------------------------------------

        theme_card, theme_layout = self.card()

        theme_title = QLabel(
            T["theme"]
        )

        theme_title.setObjectName(
            "settingTitle"
        )

        theme_layout.addWidget(
            theme_title
        )

        self.theme_combo = QComboBox()

        self.theme_combo.addItems([
            T["theme_light"],
            T["theme_dark"],
            T["theme_auto"],
        ])

        theme_layout.addWidget(
            self.theme_combo
        )

        layout.addWidget(
            theme_card
        )

        # ----------------------------------------------------
        # Положение панели
        # ----------------------------------------------------

        panel_card, panel_layout = self.card()

        panel_title = QLabel(
            T["panel"]
        )

        panel_title.setObjectName(
            "settingTitle"
        )

        panel_layout.addWidget(
            panel_title
        )

        self.panel_combo = QComboBox()

        self.panel_combo.addItems([
            T["panel_bottom"],
            T["panel_left"],
            T["panel_right"],
        ])

        panel_layout.addWidget(
            self.panel_combo
        )

        layout.addWidget(
            panel_card
        )

        # ----------------------------------------------------
        # Анимации
        # ----------------------------------------------------

        animation_card, animation_layout = self.card()

        animation_title = QLabel(
            T["animations"]
        )

        animation_title.setObjectName(
            "settingTitle"
        )

        animation_layout.addWidget(
            animation_title
        )

        self.animations_checkbox = QCheckBox(
            T["animations_on"]
        )

        self.animations_checkbox.setChecked(
            True
        )

        animation_layout.addWidget(
            self.animations_checkbox
        )

        layout.addWidget(
            animation_card
        )

        layout.addStretch()

        self.stack.addWidget(page)

    # ========================================================
    # Страница 4 — Рабочий стол
    # ========================================================

    def create_desktop_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(14)

        layout.addWidget(
            self.page_title(
                T["desktop"]
            )
        )

        card, card_layout = self.card()

        self.desktop_icons = QCheckBox(
            T["desktop_icons"]
        )

        self.desktop_icons.setChecked(
            True
        )

        self.home_icon = QCheckBox(
            T["home_icon"]
        )

        self.home_icon.setChecked(
            True
        )

        self.trash_icon = QCheckBox(
            T["trash_icon"]
        )

        self.trash_icon.setChecked(
            True
        )

        self.double_click = QCheckBox(
            T["double_click"]
        )

        self.double_click.setChecked(
            True
        )

        self.auto_trash = QCheckBox(
            T["auto_trash"]
        )

        self.auto_trash.setChecked(
            False
        )

        self.focus_hover = QCheckBox(
            T["focus_hover"]
        )

        self.focus_hover.setChecked(
            False
        )

        card_layout.addWidget(
            self.desktop_icons
        )

        card_layout.addWidget(
            self.home_icon
        )

        card_layout.addWidget(
            self.trash_icon
        )

        card_layout.addWidget(
            self.double_click
        )

        card_layout.addWidget(
            self.auto_trash
        )

        card_layout.addWidget(
            self.focus_hover
        )

        layout.addWidget(card)

        layout.addStretch()

        self.stack.addWidget(page)

    # ========================================================
    # Страница 5 — Активация
    # ========================================================

    def create_activation_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(22)

        layout.addWidget(
            self.page_title(
                T["activation"]
            )
        )

        layout.addWidget(
            self.page_text(
                T["activation_text"]
            )
        )

        card, card_layout = self.card()

        title = QLabel(
            T["activation_code"]
        )

        title.setObjectName(
            "settingTitle"
        )

        card_layout.addWidget(
            title
        )

        # Поле кода
        self.activation_input = QLineEdit()

        self.activation_input.setPlaceholderText(
            "$KOS:..."
        )

        self.activation_input.setMinimumHeight(
            48
        )

        self.activation_input.setClearButtonEnabled(
            True
        )

        card_layout.addWidget(
            self.activation_input
        )

        # Кнопка активации
        self.activate_button = QPushButton(
            T["activate"]
        )

        self.activate_button.setObjectName(
            "primaryButton"
        )

        self.activate_button.clicked.connect(
            self.activate_system
        )

        card_layout.addWidget(
            self.activate_button
        )

        # Статус
        self.activation_status = QLabel()

        self.activation_status.setWordWrap(
            True
        )

        self.activation_status.setObjectName(
            "activationStatus"
        )

        card_layout.addWidget(
            self.activation_status
        )

        layout.addWidget(
            card
        )

        layout.addStretch()

        self.stack.addWidget(page)

    # ========================================================
    # Страница 6 — Завершение
    # ========================================================

    def create_finish_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setSpacing(25)

        layout.addWidget(
            self.page_title(
                T["finish"]
            )
        )

        layout.addWidget(
            self.page_text(
                T["finish_text"]
            )
        )

        layout.addStretch()

        self.stack.addWidget(page)

    # ========================================================
    # Активация
    # ========================================================

    def activate_system(self):

        entered_code = (
            self.activation_input
            .text()
            .strip()
        )

        if entered_code == ACTIVATION_CODE:

            self.activation_successful = True

            self.activation_status.setText(
                "✓ " + T["activation_success"]
            )

            self.activation_status.setProperty(
                "success",
                True
            )

            self.activation_status.style().unpolish(
                self.activation_status
            )

            self.activation_status.style().polish(
                self.activation_status
            )

            self.activation_input.setReadOnly(
                True
            )

            self.activate_button.setEnabled(
                False
            )

            self.update_navigation()

        else:

            self.activation_successful = False

            self.activation_status.setText(
                "✕ " + T["activation_error"]
            )

            self.activation_status.setProperty(
                "success",
                False
            )

            self.activation_status.style().unpolish(
                self.activation_status
            )

            self.activation_status.style().polish(
                self.activation_status
            )

            self.update_navigation()

    # ========================================================
    # Навигация
    # ========================================================

    def update_navigation(self):

        self.current_page = (
            self.stack.currentIndex()
        )

        # Назад
        self.back_button.setEnabled(
            self.current_page > 0
        )

        # ----------------------------------------------------
        # Лицензия
        # ----------------------------------------------------

        if self.current_page == 1:

            self.next_button.setEnabled(
                self.license_checkbox.isChecked()
            )

        # ----------------------------------------------------
        # Активация
        # ----------------------------------------------------

        elif self.current_page == 4:

            self.next_button.setEnabled(
                self.activation_successful
            )

        else:

            self.next_button.setEnabled(
                True
            )

        # ----------------------------------------------------
        # Последняя страница
        # ----------------------------------------------------

        if (
            self.current_page
            == self.pages_count - 1
        ):

            self.next_button.setText(
                T["finish_button"]
            )

        else:

            self.next_button.setText(
                T["next"]
            )

        # ----------------------------------------------------
        # Индикатор шага
        # ----------------------------------------------------

        self.status_label.setText(
            f"{T['step']} "
            f"{self.current_page + 1} "
            f"{T['of']} "
            f"{self.pages_count}"
        )

        # ----------------------------------------------------
        # Sidebar
        # ----------------------------------------------------

        for index, label in enumerate(
            self.step_labels
        ):

            label.setProperty(
                "active",
                index == self.current_page
            )

            label.style().unpolish(
                label
            )

            label.style().polish(
                label
            )

    # ========================================================
    # Далее
    # ========================================================

    def next_page(self):

        # Лицензия
        if self.current_page == 1:

            if not self.license_checkbox.isChecked():

                self.activation_status.setText(
                    T["license_required"]
                )

                return

        # Активация
        if self.current_page == 4:

            if not self.activation_successful:

                self.activation_status.setText(
                    T["activation_required"]
                )

                return

        # Переход
        if (
            self.current_page
            < self.pages_count - 1
        ):

            self.stack.setCurrentIndex(
                self.current_page + 1
            )

            self.update_navigation()

        else:

            self.finish_oobe()

    # ========================================================
    # Назад
    # ========================================================

    def previous_page(self):

        if self.current_page > 0:

            self.stack.setCurrentIndex(
                self.current_page - 1
            )

            self.update_navigation()

    # ========================================================
    # Завершение OOBE
    # ========================================================

    def finish_oobe(self):

        self.save_settings()

        try:

            OOBE_COMPLETE_FILE.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            OOBE_COMPLETE_FILE.touch()

        except PermissionError:

            # Вариант для запуска без root
            try:

                local_file = (
                    Path.home()
                    / ".config"
                    / "kleopatrakindomos-oobe-complete"
                )

                local_file.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                local_file.touch()

            except Exception:
                pass

        except Exception:
            pass

        QApplication.quit()

    # ========================================================
    # Сохранение настроек
    # ========================================================

    def save_settings(self):

        settings = {
            "theme":
                self.theme_combo.currentText(),

            "panel":
                self.panel_combo.currentText(),

            "animations":
                self.animations_checkbox.isChecked(),

            "desktop_icons":
                self.desktop_icons.isChecked(),

            "home_icon":
                self.home_icon.isChecked(),

            "trash_icon":
                self.trash_icon.isChecked(),

            "double_click":
                self.double_click.isChecked(),

            "auto_trash":
                self.auto_trash.isChecked(),

            "focus_hover":
                self.focus_hover.isChecked(),

            "activated":
                self.activation_successful,
        }

        config_dir = (
            Path.home()
            / ".config"
            / "kleopatrakindomos"
        )

        try:

            config_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            config_file = (
                config_dir
                / "oobe.conf"
            )

            with open(
                config_file,
                "w",
                encoding="utf-8"
            ) as file:

                for key, value in settings.items():

                    file.write(
                        f"{key}={value}\n"
                    )

        except Exception:
            pass

    # ========================================================
    # Стиль
    # ========================================================

    def apply_style(self):

        self.setStyleSheet(
            """
            * {
                font-family:
                    "Noto Sans",
                    "DejaVu Sans";
            }

            QMainWindow {
                background: #f4f5f7;
            }

            #sidebar {
                background: #20232a;
                min-width: 280px;
                max-width: 320px;
            }

            #logo {
                background: #ffffff;
                color: #20232a;
                border-radius: 32px;

                min-width: 64px;
                max-width: 64px;

                min-height: 64px;
                max-height: 64px;

                font-size: 30px;
                font-weight: 800;
            }

            #brand {
                color: #ffffff;
                font-size: 20px;
                font-weight: 700;
            }

            #version {
                color: #9299a5;
                font-size: 12px;
            }

            #step {
                color: #9299a5;
                font-size: 14px;
                padding: 10px;
                border-radius: 8px;
            }

            #step[active="true"] {
                color: #ffffff;
                background: #343943;
                font-weight: 700;
            }

            #pageTitle {
                color: #20232a;
                font-size: 34px;
                font-weight: 800;
                margin-bottom: 5px;
            }

            #pageText {
                color: #606773;
                font-size: 17px;
            }

            #card {
                background: #ffffff;
                border: 1px solid #e0e3e8;
                border-radius: 14px;
            }

            #cardText {
                color: #606773;
                font-size: 15px;
            }

            #infoTitle {
                color: #20232a;
                font-size: 20px;
                font-weight: 700;
            }

            #settingTitle {
                color: #20232a;
                font-size: 17px;
                font-weight: 700;
            }

            #licenseBox {
                background: #ffffff;
                border: 1px solid #e0e3e8;
                border-radius: 12px;
            }

            #licenseText {
                color: #3e434c;
                font-size: 14px;
            }

            #activationStatus {
                color: #b13a3a;
                font-size: 14px;
                font-weight: 600;
                padding-top: 8px;
            }

            #activationStatus[success="true"] {
                color: #2f7d4a;
            }

            QCheckBox {
                color: #30343b;
                font-size: 15px;
                spacing: 10px;
            }

            QCheckBox::indicator {
                width: 19px;
                height: 19px;
            }

            QLineEdit {
                background: #ffffff;
                border: 1px solid #cfd4dc;
                border-radius: 8px;
                padding: 11px 13px;
                color: #30343b;
                font-size: 16px;
            }

            QLineEdit:focus {
                border: 1px solid #7d838d;
            }

            QComboBox {
                background: #ffffff;
                border: 1px solid #cfd4dc;
                border-radius: 8px;
                padding: 10px 12px;
                color: #30343b;
                font-size: 15px;
            }

            QComboBox:hover {
                border: 1px solid #aab0ba;
            }

            QComboBox::drop-down {
                border: none;
                width: 30px;
            }

            #primaryButton {
                background: #20232a;
                color: #ffffff;
                border: none;
                border-radius: 9px;
                padding: 12px 28px;
                font-size: 15px;
                font-weight: 700;
            }

            #primaryButton:hover {
                background: #30343c;
            }

            #primaryButton:disabled {
                background: #bfc3c9;
                color: #ffffff;
            }

            #secondaryButton {
                background: #ffffff;
                color: #30343b;
                border: 1px solid #d0d4db;
                border-radius: 9px;
                padding: 12px 28px;
                font-size: 15px;
            }

            #secondaryButton:hover {
                background: #f0f1f3;
            }

            #secondaryButton:disabled {
                color: #aeb3bb;
                background: #f4f5f7;
            }

            #status {
                color: #858b96;
                font-size: 13px;
            }

            QScrollArea {
                background: transparent;
                border: none;
            }
            """
        )

    # ========================================================
    # Escape отключён
    # ========================================================

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:
            return

        super().keyPressEvent(event)


# ============================================================
# Запуск
# ============================================================

def main():

    app = QApplication(sys.argv)

    app.setApplicationName(
        "KleopatraKindomOS OOBE"
    )

    app.setApplicationDisplayName(
        "KleopatraKindomOS"
    )

    app.setFont(
        QFont(
            "Noto Sans",
            10
        )
    )

    window = OOBEWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()