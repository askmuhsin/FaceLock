from fasthtml.fastapp import fast_app
from fasthtml.core import serve
from fasthtml.common import (
    H1, H2, H3, P, Div, Span, A, Button,
    Form, Input, Label, Ul, Li, 
    Title, Meta, Script, Titled, Container
)
# from fasthtml.common import *
from monsterui.core import Theme
from monsterui.all import Card, Button as UIButton, Alert, DivLAligned, UkIconLink, TextPresets
# from monsterui.all import *

app, rt = fast_app(hdrs=Theme.blue.headers())

@rt
def index():
    return Titled("FastHTML + MonsterUI Demo", 
        Alert("Welcome to FastHTML with MonsterUI styling!", cls="mb-4"),
        
        Card(
            H3("Beautiful Components"),
            P("MonsterUI provides shadcn-like components for FastHTML:"),
            Ul(
                Li("🎨 Tailwind CSS + FrankenUI + DaisyUI"),
                Li("🎯 Pre-built components (Cards, Buttons, Forms)"),
                Li("🌈 Built-in themes (blue, slate, gray, etc.)"),
                Li("✨ Ready to use, no configuration needed")
            ),
            cls="mb-4"
        ),
        
        Div(
            UIButton("Primary Button", cls="mr-2"),
            UIButton("Secondary", variant="outline"),
            cls="space-x-2"
        )
    )

serve()