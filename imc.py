import flet as ft

def main(pagina:ft.Page):
    pagina.title = "Calculadora de IMC"
    pagina.bgcolor = "#DBEBFF"
    pagina.horizontal_alignment = "center"
    pagina.window.width = 600
    pagina.window.width = 1000 
    pagina.spacing = 20 


    def calcular_peso():
        if campo_altura.value == "":
            mensagem = ft.SnackBar(content="O campo  altura precisa ser preechido",
            duration= 4000)
            pagina.show_dialog(mensagem)
            return
        if campo_peso.value == "":
            mensagem = ft.SnackBar(content="O campo peso precisa ser preechido",
            duration= 4000)
            pagina.show_dialog(mensagem)
            return
        altura = float(campo_altura.value)
        peso = float(campo_peso.value)
        conta = peso / (altura*altura)

       

        if conta <= 18.5:
            resultado = "Magreza"
            imagem_pesos.src= "img/magresa2.png"

        elif conta > 18.5 and conta <= 24.9:
            imagem_pesos.src= "img/normal.png"
            resultado = "Normal"
        elif conta >= 25 and conta <=29.9:
            resultado = "Sobrepeso"
            imagem_pesos.src= "img/acimadopeso.png"
        elif conta >= 30 and conta <= 34.9:
            resultado = "Obesidade I"
            imagem_pesos.src= "img/ob1.png"
        elif conta >= 35 and conta <= 39.9:
            resultado= "Obesidade II"
            imagem_pesos.src= "img/ob2.png"
        elif conta >= 40:
            resultado = "Obesidade III"
            imagem_pesos.src= "img/ob3.png"

        campo_resultado.value= resultado

    imagem_pesos = ft.Image(src="#",
                            visible= True,
                            width=200,
                            height=300)



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
                       campo_resultado,
                       imagem_pesos
                       
                       ]
   
    pagina.update()




ft.run(main)