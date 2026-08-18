import flet as ft

def main(pagina:ft.Page):
    pagina.title = "Calculadora de IMC"
    pagina.bgcolor = "#DBEBFF"
    pagina.horizontal_alignment = "center"
    pagina.window.width = 600
    pagina.window.width = 800 
    pagina.spacing = 20 

    def calcular_peso():
        altura = float(campo_altura.value)
        peso = float(campo_peso.value)
        conta = peso / (altura*altura)

        if conta <= 18.5:
            resultado = "Magreza"
        elif conta > 18.5 and conta <= 24.9:
            resultado = "Normal"
        elif conta >= 25 and conta <=29.9:
            resultado = "Sobrepeso"
        elif conta >= 30 and conta <= 34.9:
            resultado = "Obesidade I"
        elif conta >= 35 and conta <= 39.9:
            resultado= "Obesidade II"
        elif conta >= 40:
            resultado = "Obesidade III"

        campo_resultado.value = resultado



    titulo = ft.Text(value="Você Está No Peso Ideal?",
                     size=40,
                     font_family="Georgia",
                     color="#1E39B3",
                     weight=ft.FontWeight.BOLD)
    
    campo_altura = ft.TextField(label="Altura",
                                border_color="#1E39B3",
                                border_width=2)
    
    campo_peso = ft.TextField(label="Peso",
                                border_color="#1E39B3",
                                border_width=2)
    
    botao = ft.Button(content="Calcular",
                      height=40,
                      color="#1E39B3",
                      on_click=calcular_peso)
    
    campo_resultado = ft.TextField(label="Resultado",
                            border_color="#1E39B3",
                            border_width=2)
    










    linha = ft.Row(controls=[campo_altura,
                             campo_peso],
                             alignment="center",
                             spacing=20)
    
    pagina.controls = [titulo,
                       linha,
                       botao,
                       campo_resultado]
    pagina.update()



ft.run(main)