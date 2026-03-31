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
        text_cpf.value =f"cpf :{input_cpf.value}"
        text_email.value = f"Email: {input_email.value}"
        text_salario.value = f"Salario :${input_salario.value}"
        var = input_nome.value
        navegar("/msg")

        page.update()

        tem_erro =False
        if input_nome.value:
            input_nome.error =None
        else:
            tem_erro = False
            input_nome.error="Campo obrigatorio"

        if input_cpf.value:
            input_cpf.error =None
        else:
            tem_erro = False
            input_cpf.error="Campo obrigatorio"

        if input_email.value:
            input_email.error =None
        else:
            tem_erro = False
            input_email.error="Campo obrigatorio"

        if input_salario.value:
            input_salario.error =None
        else:
            tem_erro = False
            input_salario.error="Campo obrigatorio"





#Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/msg",
                controls=[
                    flet.AppBar(
                        title="Cadrastrar Funcionario",
                        bgcolor=Colors.BROWN_400

                    ),
                    Text("Digite seu nome:"),

                    input_nome,
                    Text("Digite seu CPF:"),
                    input_cpf,
                    Text("Digite seu Email:"),
                    input_email,
                    Text("Digite seu Salario:"),
                    input_salario,
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

                        text_msg,
                        text_cpf,
                        text_email,
                        text_salario,
                        btn_certo_nome

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
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()
    input_nome = TextField(label="Nome")
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="Email")
    input_salario = TextField(label="Salario")
    btn_salvar_nome = Button("Salvar", on_click=digite_name,)
    btn_certo_nome = Button("Certo?", on_click=digite_name,)
    if input_nome.value and input_cpf.value and input_email.value and input_salario.value:

        input_nome.value =""
        input_cpf.value=""
        input_email=""
        input_salario=""
        navegar("/tela_msg")
    else:
        input_cpf.error="Campo obrigatorio"


    page.on_route_change = route_change
    page.on_view = view_pop

    route_change()

flet.run(main)