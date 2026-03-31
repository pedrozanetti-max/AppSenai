import asyncio

import flet
from flet import ThemeMode, View, Colors, Button
from flet.controls import page


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




#Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="primeira pagina",
                        bgcolor=Colors.BROWN_400
                    ),
                    Button("ir para segunda tela",on_click=lambda:navegar("/segunda_tela"))
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="segunda pagina",
                        )
                    ]
                )
            )


#Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)




    page.on_route_change = route_change
    page.on_view = view_pop

    route_change()

flet.run(main)