import asyncio


import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, OutlinedButton
from flet.controls import page
from rich.table import Column


def main(page: flet.Page):
    #configuraçoes
    page.title ="primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

#funçao
#navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def digite_name(nome):
        text_msg.value = f"Bomdia {input_nome.value},Tudo bem?"
        var = input_nome.value
        navegar("/msg")

        page.update()


#Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/msg",
                controls=[
                    flet.AppBar(
                        title="Bem vindo a primeira pagina",
                        bgcolor=Colors.BROWN_400

                    ),
                    Text("Digite seu nome:"),
                    input_nome,
                    btn_salvar_nome
                ]
            )
        )
        if page.route == "/msg":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="segunda pagina",
                        ),
                        text_msg
                    ]
                )
            )

#Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

#componentes
    text_msg = Text()
    input_nome = TextField(label="Nome")
    btn_salvar_nome = Button("Salvar", on_click=digite_name,)

    page.on_route_change = route_change
    page.on_view = view_pop

    route_change()

flet.run(main)