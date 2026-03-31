import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, OutlinedButton, Container, Column, Row, Icon, \
    CrossAxisAlignment
from flet.controls import page
from flet.controls.material.icons import Icons


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
        text_celular.value = f"{input_celular.value}"
        text_marca.value=f"marca:{input_marca.value}"
        text_modelo.value=f"modelo:{input_modelo.value}"
        text_ano.value=f"ano:{input_ano.value}"
        var = input_celular.value
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
                        title="cadastrar celular: ",
                        bgcolor=Colors.BROWN_400

                    ),
                    Text("Digite o  nome:"),
                    input_celular,
                    input_modelo,
                    input_marca,
                    input_ano,
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

                        Container(
                            Column([
                                text_celular,
                                Row([
                                    Icon(Icons.PHONE_ANDROID, color=Colors.PRIMARY, size=20),
                                    text_ano,

                                ],

                                ),
                                Row([
                                    Icon(Icons.BRANDING_WATERMARK, color=Colors.PRIMARY, size=20),
                                    text_marca
                                ]),
                                Row([
                                    Icon(Icons.MODEL_TRAINING, color=Colors.PRIMARY, size=20),
                                    text_modelo
                                ])
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            )

                        ),


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
    text_celular = Text()
    text_marca = Text()
    text_ano = Text()
    text_modelo = Text()
    input_celular = TextField(label="Nome")
    input_marca = TextField(label="Marca")
    input_modelo = TextField(label="Modelo")
    input_ano = TextField(label="Ano")
    btn_salvar_nome = Button("Salvar", on_click=digite_name,)

    page.on_route_change = route_change
    page.on_view = view_pop

    route_change()

flet.run(main)