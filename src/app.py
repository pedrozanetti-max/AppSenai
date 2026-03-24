import datetime
from time import strptime

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
from flet.controls.border_radius import horizontal
from datetime import date


def main(page: flet.Page):
    #configuraçoes
    page.title ="primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700
    #funçoes

    def salvar_nome(nome):
        text.value =f"Bom dia  {input_nome.value} {input_sobrenome.value}"

        page.update()

    def par_impar():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            txt_numero.value = f'o numero é {input_numero.value} PAR'

        else:
            txt_numero.value = f'o numero é {input_numero.value} IMPAR'
        page.update()

    def verificar_maioridade(e):
            data_texto = input_data.value
            nascimento = datetime.datetime.strptime(data_texto, "%d/%m/%Y")
            hoje = date.today()

            idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

            if idade >= 18:
                txt_nascimento.value = f"Você tem {idade} anos e é MAIOR de idade."
            else:
                txt_nascimento.value = f"Você tem {idade} anos e é MENOR de idade."




    #componente
    text = Text()
    txt_numero = Text()
    txt_nascimento = Text()
    input_numero = TextField(label="numero")
    btn_par_ou_impar = OutlinedButton("salvar", on_click=par_impar)
    input_nome = TextField(label="Nome")
    input_data = TextField(label="Data")
    btn_nascimento = OutlinedButton("salvar", on_click=verificar_maioridade)
    input_sobrenome = TextField(label="sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome,)


    #construçao da tela
    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,

                btn_salvar,
                text,
                input_numero,
                btn_par_ou_impar,
                txt_numero,

                text,
                input_data,
                btn_nascimento,
                txt_nascimento,






            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )



flet.app(main)


