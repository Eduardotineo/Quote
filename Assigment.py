import flet as ft

def main(page: ft.Page):

    def cambiar(e):
        if idioma.value == "English":
            quote.value = "If you're the palm tree, I'm the coconut; if I'm no good, neither are you bam, bam"

        if idioma.value == "Spanish":
            quote.value = "Si tu eres palma yo soy coco, si yo no sirvo tu tampoco bam bam."

        if idioma.value == "French":
            quote.value = "Si tu es le palmier je suis la noix de coco, si je ne vaux rien, toi non plus bam, bam "

        page.update()

    quote = ft.Text("Si tu eres palma yo soy coco, si yo no sirvo tu tampoco bam bam.")

    idioma = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="English", label="English"),
            ft.Radio(value="Spanish", label="Spanish"),
            ft.Radio(value="French", label="French")
        ]),
        
    )

    page.add(
        quote,
        idioma
    )

ft.app(target=main)