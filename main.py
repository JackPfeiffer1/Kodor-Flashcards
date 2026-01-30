from flet import *
import apkgExtraction

def main(page: Page):
    
    
    flashcards_dict = apkgExtraction.ankiExtract("testdata.apkg")

    
    BG = "#101622"
    SURFACE = "#1a2332"

    page.bgcolor = BG
    page.title = "Kodor Flashcards"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    container = Container(
        width=600,
        height=400,
        bgcolor=SURFACE,
        border_radius=10,
        padding=padding.all(20),
        alignment=alignment.center,
    )
    page.add(container)


app(target=main)