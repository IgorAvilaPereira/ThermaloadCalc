from tkinter import *
import sqlite3
import psychrolib
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.calc_cid.delete(0, END)
        self.calc_tem1.delete(0, END)
        self.calc_alt.delete(0, END)
        self.calc_um1.delete(0, END)
        self.calc_tem2.delete(0, END)
        self.calc_um2.delete(0, END)

    def limpa_tela2(self):
        self.pedirc.delete(0, END)
        self.comp1.delete(0, END)
        self.comp2.delete(0, END)
        self.comp3.delete(0, END)
        self.comp4.delete(0, END)
        self.selected_item1.set("Selecione um")
        self.selected_item2.set("Selecione um")
        self.selected_item3.set("Selecione um")
        self.selected_item4.set("Selecione um")
        self.selected_item5.set("Selecione um")
        self.selected_item6.set("Selecione um")
        self.selected_item7.set("Selecione um")
        self.selected_item8.set("Selecione um")
        self.selected_item9.set("Selecione um")
        self.selected_item10.set("Selecione um")
        self.selected_item11.set("Selecione um")
        self.selected_item12.set("Selecione um")

    def limpa_tela3(self):
        self.pedirc.delete(0, END)
        self.pared_ent.delete(0, END)
        self.pared2_ent.delete(0, END)
        self.vidr_ent.delete(0, END)
        self.vidr2_ent.delete(0, END)
        self.piso_ent.delete(0, END)
        self.piso2_ent.delete(0, END)
        self.teto_ent.delete(0, END)
        self.teto2_ent.delete(0, END)
        self.selected_item13.set("Selecione um")
        self.selected_item14.set("Selecione um")
        self.selected_item15.set("Selecione um")
        self.selected_item16.set("Selecione um")
        self.selected_item17.set("Selecione um")
        self.selected_item18.set("Selecione um")

    def limpa_tela4(self):
        self.janen_ent.delete(0, END)
        self.janes_ent.delete(0, END)
        self.janel_ent.delete(0, END)
        self.janeo_ent.delete(0, END)
        self.janen2_ent.delete(0, END)
        self.janes2_ent.delete(0, END)
        self.janel2_ent.delete(0, END)
        self.janeo2_ent.delete(0, END)
        self.janen3_ent.delete(0, END)
        self.janes3_ent.delete(0, END)
        self.janel3_ent.delete(0, END)
        self.janeo3_ent.delete(0, END)
        self.selected_item19.set("Selecione um")
        self.selected_item20.set("Selecione um")
        self.selected_item21.set("Selecione um")
        self.selected_item22.set("Selecione um")
        self.selected_item23.set("Selecione um")
        self.selected_item24.set("Selecione um")
        self.selected_item25.set("Selecione um")
        self.selected_item26.set("Selecione um")

    def limpa_tela5(self):
        self.cpe()
        self.lista_selecionados0.append((self.hom1_ent.get(), self.mul1_ent.get(), self.cria1_ent.get(), self.selected_item27.get(), self.cps1, self.cpl1))
        self.hom1_ent.delete(0, END)
        self.mul1_ent.delete(0, END)
        self.cria1_ent.delete(0, END)
        self.selected_item27.set("Selecione um")
        
    def adicionar(self):
        self.lista_selecionados.append((self.equip_ent.get(), self.quant_ent.get(), self.ces_ent.get(), self.cel_ent.get()))
        self.quant_ent.delete(0, END)
        self.equip_ent.delete(0, END)
        self.ces_ent.delete(0, END)
        self.cel_ent.delete(0, END)
        
    def limpa_tela6(self):
        self.cria4_ent.delete(0, END)
        self.selected_item27.set("Selecione um")

    def limpa_tela7(self):
        self.selected_item30.set("Tipo")
        self.selected_item31.set("Ajustamento")
        self.selected_item32.set("Tipo")
        self.selected_item33.set("Ajustamento")
        self.selected_item34.set("Tipo de Local")

    def limpa_tela8(self):
        print("OK!")


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        #self.help_icon = PhotoImage(file='C:/Users/W10/Documents/Códigos/Teste/zajuda.png')
        #self.img_rv1 = PhotoImage(file='C:/Users/W10/Documents/Códigos/Teste/rv1.png')
        #self.img_rv2 = PhotoImage(file='C:/Users/W10/Documents/Códigos/Teste/rv2.png')
        self.help_icon = PhotoImage(file='C:/Users/felto/Downloads/zajuda1.png')
        self.img_rv1 = PhotoImage(file='C:/Users/felto/Downloads/rv1.png')
        self.img_rv2 = PhotoImage(file='C:/Users/felto/Downloads/rv2.png')
        self.botoes()
        self.selected_item1 = StringVar()
        self.selected_item2 = StringVar()
        self.selected_item3 = StringVar()
        self.selected_item4 = StringVar()
        self.selected_item5 = StringVar()
        self.selected_item6 = StringVar()
        self.selected_item7 = StringVar()
        self.selected_item8 = StringVar()
        self.selected_item9 = StringVar()
        self.selected_item10 = StringVar()
        self.selected_item11 = StringVar()
        self.selected_item12 = StringVar()
        self.selected_item13 = StringVar()
        self.selected_item14 = StringVar()
        self.selected_item15 = StringVar()
        self.selected_item16 = StringVar()
        self.selected_item17 = StringVar()
        self.selected_item18 = StringVar()
        self.selected_item19 = StringVar()
        self.selected_item20 = StringVar()
        self.selected_item21 = StringVar()
        self.selected_item22 = StringVar()
        self.selected_item23 = StringVar()
        self.selected_item24 = StringVar()
        self.selected_item25 = StringVar()
        self.selected_item26 = StringVar()
        self.selected_item27 = StringVar()
        self.selected_item28 = StringVar()
        self.selected_item29 = StringVar()
        self.selected_item30 = StringVar()
        self.selected_item31 = StringVar()
        self.selected_item32 = StringVar()
        self.selected_item33 = StringVar()
        self.selected_item34 = StringVar()
        self.lista_selecionados = []
        root.mainloop()


    def tela(self):
        self.root.title("ThermaloadCalc")
        self.root.configure(background='#483D8B')
        #self.root.iconbitmap('C:/Users/W10/Downloads/L2.ico')
        self.root.iconbitmap('C:/Users/felto/Downloads/L2.ico')        
        self.root.geometry("1000x640")
        self.root.resizable(True,True)
        self.root.maxsize(width=1440, height=960)
        self.root.minsize(width=500, height=320)


    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frame_2 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)
        
    def frames_da_tela2(self):
        
        self.frame_1.place_forget()

        self.frame_3 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_3.place(relx=0.02, rely=0.08, relwidth=0.96, relheight=0.42)

        self.frame_4 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_4.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.top_fr = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.top_fr.place(relx=0.42, rely=0.01, relwidth=0.15, relheight=0.06)

        self.botoes()
        
    def frames_da_tela3(self):
        self.frame_5 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_5.place(relx=0.02, rely=0.08, relwidth=0.96, relheight=0.42)

        self.frame_6 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_6.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()

    def frames_da_tela4(self):
        self.frame_7 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_7.place(relx=0.02, rely=0.08, relwidth=0.96, relheight=0.42)

        self.frame_8 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_8.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()

    def frames_da_tela5(self):
        self.top_fr.place_forget()

        self.frame_9 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_9.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frame_10 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_10.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()

    def frames_da_tela6(self):
        self.frame_11 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_11.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frame_12 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_12.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()
    
    def frames_da_tela7(self):
        self.frame_13 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_13.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frame_14 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_14.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()

    def frames_da_tela8(self):
        self.frame_15 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_15.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frame_16 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_16.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()

    def frames_da_tela9(self):
        self.frame_17 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_17.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frame_18 = Frame(self.root, bd= 4, bg='#E0FFFF', highlightbackground='gray', highlightthickness=6)
        self.frame_18.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        self.botoes()
        #self.ativar_fim()

    def frames_da_tela10(self):
        root.destroy()

    def ativar_fim(self):
        self.printar_result9()


    def liberar_botao_prox(self):
        self.prox1["state"] = "normal"  # Habilita o botão prox1
        self.printar_result()

    def liberar_botao_prox2(self):
        self.prox2["state"] = "normal"  # Habilita o botão prox2
        self.printar_result2()

    def liberar_botao_prox3(self):
        self.prox3["state"] = "normal"  # Habilita o botão prox3
        self.printar_result3()

    def liberar_botao_prox4(self):
        self.prox4["state"] = "normal"  # Habilita o botão prox3
        self.printar_result4()

    def liberar_botao_prox5(self):
        self.prox5["state"] = "normal"  # Habilita o botão prox3
        self.printar_result5()

    def liberar_botao_prox6(self):
        self.prox6["state"] = "normal"  # Habilita o botão prox
        self.printar_result6()

    def liberar_botao_prox7(self):
        self.prox7["state"] = "normal"  # Habilita o botão prox
        self.printar_result7()
    
    def liberar_botao_prox8(self):
        self.prox8["state"] = "normal"  # Habilita o botão prox
        self.printar_result8()


    def voltar_para_frames_anteriores(self):
        self.frame_1.tkraise()  # Exibe o frame_1
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)
        self.frame_2.tkraise()  # Exibe o frame_2

        self.frame_3.destroy()
        self.frame_4.destroy()
        self.top_fr.destroy()

    def voltar_para_frames_anteriores2(self):
        self.frame_3.tkraise()  # Exibe o frame_3
        self.frame_4.tkraise()  # Exibe o frame_4

        self.frame_5.destroy()
        self.frame_6.destroy()

    def voltar_para_frames_anteriores3(self):
        self.frame_5.tkraise()  # Exibe o frame_5
        self.frame_6.tkraise()  # Exibe o frame_6

        self.resultado_label4.config(" ")

        self.frame_7.destroy()
        self.frame_8.destroy()

    def voltar_para_frames_anteriores4(self):
        self.frame_7.tkraise()  # Exibe o frame_7
        self.frame_8.tkraise()  # Exibe o frame_8
        self.top_fr.tkraise()
        self.top_fr.place(relx=0.42, rely=0.01, relwidth=0.15, relheight=0.06)


        self.frame_9.destroy()
        self.frame_10.destroy()
       
    def voltar_para_frames_anteriores5(self):
        self.frame_9.tkraise()  # Exibe o frame_9
        self.frame_10.tkraise()  # Exibe o frame_10

        self.frame_11.destroy()
        self.frame_12.destroy()

    def voltar_para_frames_anteriores6(self):
        self.frame_11.tkraise() 
        self.frame_12.tkraise()  

        self.frame_13.destroy()
        self.frame_14.destroy()

    def voltar_para_frames_anteriores7(self):
        self.frame_13.tkraise()
        self.frame_14.tkraise()

        self.frame_15.destroy()
        self.frame_16.destroy()

    def voltar_para_frames_anteriores8(self):
        self.frame_15.tkraise()
        self.frame_16.tkraise()

        self.frame_17.destroy()
        self.frame_18.destroy()
    
    def voltar_para_frames_anteriores9(self):
        print("Q?")


    def verificar_campos(self):
        campos_preenchidos = all([
            self.calc_cid.get(),
            self.calc_tem1.get(),
            self.calc_alt.get(),
            self.calc_um1.get(),
            self.calc_tem2.get(),
            self.calc_um2.get()
        ])

        if campos_preenchidos:
            self.liberar_botao_prox()

    def verificar_campos2(self):
        campos_preenchidos = all([
            self.pedirc.get(),
            self.comp1.get(),
            self.comp2.get(),
            self.comp3.get(),
            self.comp3.get(),
            self.selected_item1.get(),
            self.selected_item2.get(),
            self.selected_item3.get(),
            self.selected_item4.get(),
            self.selected_item5.get(),
            self.selected_item6.get(),
            self.selected_item7.get(),
            self.selected_item8.get(),
            self.selected_item9.get(),
            self.selected_item10.get(),
            self.selected_item11.get(),
            self.selected_item12.get()
        ])

        if campos_preenchidos:
            self.liberar_botao_prox2()
    
    def verificar_campos3(self):
        campos_preenchidos = all([
            self.pared_ent.get(),
            self.pared2_ent.get(),
            self.vidr_ent.get(),
            self.vidr2_ent.get(),
            self.piso_ent.get(),
            self.piso2_ent.get(),
            self.teto_ent.get(),
            self.teto2_ent.get(),
            self.selected_item13.get(),
            self.selected_item14.get(),
            self.selected_item15.get(),
            self.selected_item16.get(),
            self.selected_item17.get(),
            self.selected_item18.get()
        ])
        if campos_preenchidos:
            self.liberar_botao_prox3()

    def verificar_campos4(self):
        campos_preenchidos = all([
            self.janen_ent.get(),
            self.janes_ent.get(),
            self.janel_ent.get(),
            self.janeo_ent.get(),
            self.janen2_ent.get(),
            self.janes2_ent.get(),
            self.janel2_ent.get(),
            self.janeo2_ent.get(),
            self.janen3_ent.get(),
            self.janes3_ent.get(),
            self.janel3_ent.get(),
            self.janeo3_ent.get(),
            self.selected_item19.get(),
            self.selected_item20.get(),
            self.selected_item21.get(),
            self.selected_item22.get(),
            self.selected_item23.get(),
            self.selected_item24.get(),
            self.selected_item25.get(),
            self.selected_item26.get()
        ])

        if campos_preenchidos:
            self.liberar_botao_prox4()

    def verificar_campos5(self):
        self.limpa_tela5()
        self.calculos5()
        self.liberar_botao_prox5()
        self.printar_result5()
    
    def verificar_campos6(self):
        self.adicionar()
        self.calculos6()
        self.liberar_botao_prox6()
        self.printar_result6()

    def verificar_campos7(self):
        campos_preenchidos = all([
            self.selected_item28.get(),
            self.selected_item29.get()
        ])

        if campos_preenchidos:
            self.liberar_botao_prox7()
        
    def verificar_campos8(self):
        campos_preenchidos = all([
            self.selected_item30.get(),
            self.selected_item31.get(),
            self.selected_item32.get(),
            self.selected_item33.get(),
            self.selected_item34.get()
        ])

        if campos_preenchidos:
            self.liberar_botao_prox8()

    def verificar_campos9(self):
        print("Ok!")


    def mostrar_item_selecionado(self, event):
        self.selected_item1.set(self.combobox1.get())
        self.item_selecionado1 = self.selected_item1.get()

        self.selected_item2.set(self.combobox2.get())
        self.item_selecionado2 = self.selected_item2.get()

        self.selected_item3.set(self.combobox3.get())
        self.item_selecionado3 = self.selected_item3.get()

        self.selected_item4.set(self.combobox4.get())
        self.item_selecionado4 = self.selected_item4.get()

        self.selected_item5.set(self.combobox5.get())
        self.item_selecionado5 = self.selected_item5.get()

        self.selected_item6.set(self.combobox6.get())
        self.item_selecionado6 = self.selected_item6.get()

        self.selected_item7.set(self.combobox7.get())
        self.item_selecionado7 = self.selected_item7.get()

        self.selected_item8.set(self.combobox8.get())
        self.item_selecionado8 = self.selected_item8.get()

        self.selected_item9.set(self.combobox9.get())
        self.item_selecionado9 = self.selected_item9.get()

        self.selected_item10.set(self.combobox10.get())
        self.item_selecionado10 = self.selected_item10.get()

        self.selected_item11.set(self.combobox11.get())
        self.item_selecionado11 = self.selected_item11.get()

        self.selected_item12.set(self.combobox12.get())
        self.item_selecionado12 = self.selected_item12.get()

        self.selected_item13.set(self.combobox13.get())
        self.item_selecionado13 = self.selected_item13.get()

        self.selected_item14.set(self.combobox14.get())
        self.item_selecionado14 = self.selected_item14.get()

        self.selected_item15.set(self.combobox15.get())
        self.item_selecionado15 = self.selected_item15.get()

        self.selected_item16.set(self.combobox16.get())
        self.item_selecionado16 = self.selected_item16.get()

        self.selected_item17.set(self.combobox17.get())
        self.item_selecionado17 = self.selected_item17.get()

        self.selected_item18.set(self.combobox18.get())
        self.item_selecionado18 = self.selected_item18.get()

        self.selected_item19.set(self.combobox19.get())
        self.item_selecionado19 = self.selected_item19.get()

        self.selected_item20.set(self.combobox20.get())
        self.item_selecionado20 = self.selected_item20.get()

        self.selected_item21.set(self.combobox21.get())
        self.item_selecionado21 = self.selected_item21.get()

        self.selected_item22.set(self.combobox22.get())
        self.item_selecionado22 = self.selected_item22.get()

        self.selected_item23.set(self.combobox23.get())
        self.item_selecionado23 = self.selected_item23.get()

        self.selected_item24.set(self.combobox24.get())
        self.item_selecionado24 = self.selected_item24.get()

        self.selected_item25.set(self.combobox25.get())
        self.item_selecionado25 = self.selected_item25.get()

        self.selected_item26.set(self.combobox26.get())
        self.item_selecionado26 = self.selected_item26.get()

        self.selected_item27.set(self.combobox27.get())
        self.item_selecionado27 = self.selected_item27.get()

        self.selected_item28.set(self.combobox28.get())
        self.item_selecionado28 = self.selected_item28.get()

        self.selected_item29.set(self.combobox29.get())
        self.item_selecionado29 = self.selected_item29.get()

        self.selected_item30.set(self.combobox30.get())
        self.item_selecionado30 = self.selected_item30.get()

        self.selected_item31.set(self.combobox31.get())
        self.item_selecionado31 = self.selected_item31.get()

        self.selected_item32.set(self.combobox32.get())
        self.item_selecionado32 = self.selected_item32.get()

        self.selected_item33.set(self.combobox33.get())
        self.item_selecionado33 = self.selected_item33.get()

        self.selected_item34.set(self.combobox34.get())
        self.item_selecionado34 = self.selected_item34.get()


        print("A opção foi selecionada")
       
        
        
    def atualizar_orientacao1(self):
        self.pareden = "Parede Norte"
        self.label_pareden.config(text=self.pareden)
        
        self.paredes = "Parede Sul"
        self.label_paredes.config(text=self.paredes)
        
        self.paredel = "Parede Leste"
        self.label_paredel.config(text=self.paredel)
        
        self.paredeo = "Parede Oeste"
        self.label_paredeo.config(text=self.paredeo)
        
    def atualizar_orientacao2(self):
        self.pareden = "Parede Noroeste"
        self.label_pareden.config(text=self.pareden)

        self.paredes = "Parede Sudeste"
        self.label_paredes.config(text=self.paredes)

        self.paredel = "Parede Nordeste"
        self.label_paredel.config(text=self.paredel)

        self.paredeo = "Parede Sudoeste"
        self.label_paredeo.config(text=self.paredeo)


    def botoes(self):
        
        # Botões
        if hasattr(self, 'frame_1'):

            
            self.bt_limpar = Button(self.frame_1, text='Limpar', bg= '#107db2',fg='white',
                                    font=('verdana', 8, "bold"), command= self.limpa_tela)
            self.bt_limpar.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular = Button(self.frame_1, text='Calcular', bg= '#107db2',fg='white',
                                    font=('verdana', 8, "bold"), command= self.verificar_campos)
            self.bt_calcular.place(relx=0.505, rely=0.85, relwidth=.1, relheight=.15)


            self.prox1 = Button(self.frame_1, text='Próximo', bg= '#107db2',fg='white',
                                    font=('verdana', 8, "bold"), command= self.frames_da_tela2)
            #state="disabled"
            self.prox1.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        if hasattr(self, 'frame_3'):
            self.bt_limpar2 = Button(self.frame_4, text='Limpar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela2)
            self.bt_limpar2.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular2 = Button(self.frame_4, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos2)
            self.bt_calcular2.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar = Button(self.frame_4, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores)
            self.bt_voltar.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox2 = Button(self.frame_4, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela3)
            #state="disabled"
            self.prox2.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_rv1 = Button(self.frame_3, image=self.img_rv1, command=self.atualizar_orientacao1)
            self.bt_rv1.place(relx=0.8, rely=0.005)

            self.bt_rv2 = Button(self.frame_3, image=self.img_rv2, command=self.atualizar_orientacao2)
            self.bt_rv2.place(relx=0.9, rely=0.005)

            # Itens pré-definidos no combobox
            itens_pre_definidos1 = ["Claro", "Médio", "Escuro"]
            itens_pre_definidos2 = ["Claro", "Médio", "Escuro"]
            itens_pre_definidos3 = ["Claro", "Médio", "Escuro"]
            itens_pre_definidos4 = ["Claro", "Médio", "Escuro"]
            itens_pre_definidos5 = ["Sim", "Não"]
            itens_pre_definidos6 = ["Sim", "Não"]
            itens_pre_definidos7 = ["Sim", "Não"]
            itens_pre_definidos8 = ["Sim", "Não"]
            itens_pre_definidos9 = ["Tij. maciços (14 cm)= 10 tij. + 2 revest.","Tij. maciços ( 24 cm) = 20 tij. + 2 revest.","Tij. Furados ( 14 cm) = 10 tij. + 2 revest.", "Tij. Furados ( 24 cm) = 20 tij. + 2 revest."]
            itens_pre_definidos10 = ["Tij. maciços (14 cm)= 10 tij. + 2 revest.","Tij. maciços ( 24 cm) = 20 tij. + 2 revest.","Tij. Furados ( 14 cm) = 10 tij. + 2 revest.", "Tij. Furados ( 24 cm) = 20 tij. + 2 revest."]
            itens_pre_definidos11 = ["Tij. maciços (14 cm)= 10 tij. + 2 revest.","Tij. maciços ( 24 cm) = 20 tij. + 2 revest.","Tij. Furados ( 14 cm) = 10 tij. + 2 revest.", "Tij. Furados ( 24 cm) = 20 tij. + 2 revest."]
            itens_pre_definidos12 = ["Tij. maciços (14 cm)= 10 tij. + 2 revest.","Tij. maciços ( 24 cm) = 20 tij. + 2 revest.","Tij. Furados ( 14 cm) = 10 tij. + 2 revest.", "Tij. Furados ( 24 cm) = 20 tij. + 2 revest."]

            # Variável para armazenar o item selecionado
            self.selected_item1 = StringVar()
            self.selected_item1.set("Selecione um")  # padrão

            self.selected_item2 = StringVar()
            self.selected_item2.set("Selecione um")

            self.selected_item3 = StringVar()
            self.selected_item3.set("Selecione um")

            self.selected_item4 = StringVar()
            self.selected_item4.set("Selecione um")

            self.selected_item5 = StringVar()
            self.selected_item5.set("Selecione um")

            self.selected_item6 = StringVar()
            self.selected_item6.set("Selecione um")

            self.selected_item7 = StringVar()
            self.selected_item7.set("Selecione um")

            self.selected_item8 = StringVar()
            self.selected_item8.set("Selecione um")

            self.selected_item9 = StringVar()
            self.selected_item9.set("Selecione um")

            self.selected_item10 = StringVar()
            self.selected_item10.set("Selecione um")

            self.selected_item11 = StringVar()
            self.selected_item11.set("Selecione um")

            self.selected_item12 = StringVar()
            self.selected_item12.set("Selecione um")

            # Combobox personalizado
            self.combobox1 = ttk.Combobox(self.frame_3, textvariable=self.selected_item1, values=itens_pre_definidos1, state="readonly")
            self.combobox1.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox1.place(relx=0.12, rely=0.63)

            self.combobox2 = ttk.Combobox(self.frame_3, textvariable=self.selected_item2, values=itens_pre_definidos2, state="readonly")
            self.combobox2.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox2.place(relx=0.3, rely=0.63)

            self.combobox3 = ttk.Combobox(self.frame_3, textvariable=self.selected_item3, values=itens_pre_definidos3, state="readonly")
            self.combobox3.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox3.place(relx=0.48, rely=0.63)

            self.combobox4 = ttk.Combobox(self.frame_3, textvariable=self.selected_item4, values=itens_pre_definidos4, state="readonly")
            self.combobox4.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox4.place(relx=0.66, rely=0.63)

            self.combobox5 = ttk.Combobox(self.frame_3, textvariable=self.selected_item5, values=itens_pre_definidos5, state="readonly")
            self.combobox5.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox5.place(relx=0.12, rely=0.76)

            self.combobox6 = ttk.Combobox(self.frame_3, textvariable=self.selected_item6, values=itens_pre_definidos6, state="readonly")
            self.combobox6.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox6.place(relx=0.3, rely=0.76)

            self.combobox7 = ttk.Combobox(self.frame_3, textvariable=self.selected_item7, values=itens_pre_definidos7, state="readonly")
            self.combobox7.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox7.place(relx=0.48, rely=0.76)

            self.combobox8 = ttk.Combobox(self.frame_3, textvariable=self.selected_item8, values=itens_pre_definidos8, state="readonly")
            self.combobox8.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox8.place(relx=0.66, rely=0.76)

            self.combobox9 = ttk.Combobox(self.frame_3, textvariable=self.selected_item9, values=itens_pre_definidos9, state="readonly")
            self.combobox9.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox9.place(relx=0.12, rely=0.89)

            self.combobox10 = ttk.Combobox(self.frame_3, textvariable=self.selected_item10, values=itens_pre_definidos10, state="readonly")
            self.combobox10.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox10.place(relx=0.3, rely=0.89)

            self.combobox11 = ttk.Combobox(self.frame_3, textvariable=self.selected_item11, values=itens_pre_definidos11, state="readonly")
            self.combobox11.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox11.place(relx=0.48, rely=0.89)

            self.combobox12 = ttk.Combobox(self.frame_3, textvariable=self.selected_item12, values=itens_pre_definidos12, state="readonly")
            self.combobox12.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox12.place(relx=0.66, rely=0.89)

        if hasattr(self, 'frame_5'):
            self.bt_limpar3 = Button(self.frame_6, text='Limpar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela3)
            self.bt_limpar3.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular3 = Button(self.frame_6, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos3)
            self.bt_calcular3.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar2 = Button(self.frame_6, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores2)
            self.bt_voltar2.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox3 = Button(self.frame_6, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela4, state="normal")
            self.prox3.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)
            #state="disabled"

        if hasattr(self, 'frame_7'):
            self.bt_limpar4 = Button(self.frame_8, text='Limpar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela4)
            self.bt_limpar4.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular4 = Button(self.frame_8, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos4)
            self.bt_calcular4.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar4 = Button(self.frame_8, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores3)
            self.bt_voltar4.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox4 = Button(self.frame_8, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela5, state="normal")
            #"disabled"
            self.prox4.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        if hasattr(self, 'frame_9'):
            self.bt_limpar5 = Button(self.frame_10, text='Adicionar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela5)
            self.bt_limpar5.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular5 = Button(self.frame_10, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos5)#verificar_campos4
            self.bt_calcular5.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar5 = Button(self.frame_10, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores4)
            self.bt_voltar5.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox5 = Button(self.frame_10, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela6, state="normal")
            #"disabled"
            self.prox5.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        if hasattr(self, 'frame_11'):
            self.bt_adicionar = Button(self.frame_12, text='Adicionar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.adicionar)#6
            self.bt_adicionar.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular6 = Button(self.frame_12, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos6)
            self.bt_calcular6.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar6 = Button(self.frame_12, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores5)
            self.bt_voltar6.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox6 = Button(self.frame_12, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela7, state="normal")
            #"disabled"
            self.prox6.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        if hasattr(self,'frame_13'):
            self.bt_limpar6 = Button(self.frame_14, text='Limpar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela6)
            self.bt_limpar6.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular7 = Button(self.frame_14, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos7)
            self.bt_calcular7.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar7 = Button(self.frame_14, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores6)
            self.bt_voltar7.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox7 = Button(self.frame_14, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela8, state="normal")
            #"disabled"
            self.prox7.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        if hasattr(self, 'frame_15'):
            self.bt_limpar7 = Button(self.frame_16, text='Limpar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela7)
            self.bt_limpar7.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular8 = Button(self.frame_16, text='Calcular', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos8)
            self.bt_calcular8.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar8 = Button(self.frame_16, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores7)
            self.bt_voltar8.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox8 = Button(self.frame_16, text='Próximo', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela9, state="normal")
            #"disabled"
            self.prox8.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        if hasattr(self, 'frame_17'):
            self.bt_limpar8 = Button(self.frame_18, text='Limpar', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.limpa_tela8)
            self.bt_limpar8.place(relx=0.40, rely=0.85, relwidth=.1, relheight=.15)

            self.bt_calcular9 = Button(self.frame_18, text='Salvar com PDF', bg= '#107db2',fg='white',
                font=('verdana', 8, "bold"), command= self.verificar_campos9)
            self.bt_calcular9.place(relx=0.5, rely=0.85, relwidth=.1, relheight=.15)
        
            self.bt_voltar9 = Button(self.frame_18, text='Voltar', bg='#107db2', fg='white', font=('verdana', 8, "bold"), command=self.voltar_para_frames_anteriores8)
            self.bt_voltar9.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.15)

            self.prox9 = Button(self.frame_18, text='Finalizar', bg= '#107db2',fg='white',
                                 font=('verdana', 8, "bold"), command= self.frames_da_tela10, state="normal")
            #"disabled"
            self.prox9.place(relx=0.85, rely=0.85, relwidth=.1, relheight=.15)

        # Lista de seleções
        if hasattr(self, 'frame_5'):
            itens_pre_definidos13 = ["Divisórias",
            "Divisórias Junto de Cozinha, lavandeirias ou aquecedores",
            "Não possui"]

            itens_pre_definidos14 = ["Nas divisórias",
            "Vitrinas de lojas com grande carga de luz",
            "Não possui"]

            itens_pre_definidos15 = ["Sobre recintos não condicionados",
            "Do térreo",
            "Sobre Porão",
            "Sobre Porão com cozinha, lavandeirias ou aquecedores",
            "Sobre espaços ventilados",
            "Sobre espaços não ventilados"]

            itens_pre_definidos16 = ["Sobre espaços não condicionados",
            "Sobre espaços com cozinhas, lavandeirias e aquecedores",
            "Sob telhados com ou sem sotão"]

            itens_pre_definidos17 = ["Tijolos maciços (14 cm)= 10 tijolos + 2 revestimentos",
            "Tijolos maciços (10 cm) = 6 tijolos + 2 revestimentos",
            "Tijolos maciços ( 24 cm) = 20 tijolos + 2 revestimentos",
            "Tijolos Furados (10 cm) = 6 tijolos + 2 revestimentos",
            "Tijolos Furados ( 14 cm) = 10 tijolos + 2 revestimentos",
            "Tijolos Furados ( 24 cm) = 20 tijolos + 2 revestimentos",
            "Não possui"]

            itens_pre_definidos18 = ["De vidros Comuns",
            "Vidros Duplos",
            "Vidros Triplos",
            "Não possui"]

            self.selected_item13 = StringVar()
            self.selected_item13.set("Selecione um")

            self.selected_item14 = StringVar()
            self.selected_item14.set("Selecione um")

            self.selected_item15 = StringVar()
            self.selected_item15.set("Selecione um")

            self.selected_item16 = StringVar()
            self.selected_item16.set("Selecione um")

            self.selected_item17 = StringVar()
            self.selected_item17.set("Selecione um")

            self.selected_item18 = StringVar()
            self.selected_item18.set("Selecione um")

            self.combobox13 = ttk.Combobox(self.frame_5, textvariable=self.selected_item13, values=itens_pre_definidos13, state="readonly")
            self.combobox13.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox13.place(relx=0.36, rely=0.3, relwidth=.3, relheight=.10)

            self.combobox14 = ttk.Combobox(self.frame_5, textvariable=self.selected_item14, values=itens_pre_definidos14, state="readonly")
            self.combobox14.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox14.place(relx=0.36, rely=0.43, relwidth=.3, relheight=.10)

            self.combobox15 = ttk.Combobox(self.frame_5, textvariable=self.selected_item15, values=itens_pre_definidos15, state="readonly")
            self.combobox15.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox15.place(relx=0.36, rely=0.56, relwidth=.3, relheight=.10)

            self.combobox16 = ttk.Combobox(self.frame_5, textvariable=self.selected_item16, values=itens_pre_definidos16, state="readonly")
            self.combobox16.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox16.place(relx=0.36, rely=0.69, relwidth=.3, relheight=.10)

            self.combobox17 = ttk.Combobox(self.frame_5, textvariable=self.selected_item17, values=itens_pre_definidos17, state="readonly")
            self.combobox17.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox17.place(relx=0.68, rely=0.3, relwidth=.3, relheight=.10)

            self.combobox18 = ttk.Combobox(self.frame_5, textvariable=self.selected_item18, values=itens_pre_definidos18, state="readonly")
            self.combobox18.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox18.place(relx=0.68, rely=0.43, relwidth=.3, relheight=.10)

        if hasattr(self, 'frame_7'):
            itens_pre_definidos19 = ["Toldos ou Persianas Externas",
            "Persianas Internas e Reflexoras",
            "Cortinas Internas Brancas",
            "Não Possui"]

            itens_pre_definidos20 = ["Toldos ou Persianas Externas",
            "Persianas Internas e Reflexoras",
            "Cortinas Internas Brancas",
            "Não Possui"]

            itens_pre_definidos21 = ["Toldos ou Persianas Externas",
            "Persianas Internas e Reflexoras",
            "Cortinas Internas Brancas",
            "Não Possui"]

            itens_pre_definidos22 = ["Toldos ou Persianas Externas",
            "Persianas Internas e Reflexoras",
            "Cortinas Internas Brancas",
            "Não Possui"]

            itens_pre_definidos23 = ["Esquadrias de Madeira",
            "Esquadrias de Metal",
            "Não possui"]

            itens_pre_definidos24 = ["Esquadrias de Madeira",
            "Esquadrias de Metal",
            "Não possui"]

            itens_pre_definidos25 = ["Esquadrias de Madeira",
            "Esquadrias de Metal",
            "Não possui"]

            itens_pre_definidos26 = ["Esquadrias de Madeira",
            "Esquadrias de Metal",
            "Não possui"]

            self.selected_item19 = StringVar()
            self.selected_item19.set("Selecione um")

            self.selected_item20 = StringVar()
            self.selected_item20.set("Selecione um")

            self.selected_item21 = StringVar()
            self.selected_item21.set("Selecione um")

            self.selected_item22 = StringVar()
            self.selected_item22.set("Selecione um")

            self.selected_item23 = StringVar()
            self.selected_item23.set("Selecione um")

            self.selected_item24 = StringVar()
            self.selected_item24.set("Selecione um")

            self.selected_item25 = StringVar()
            self.selected_item25.set("Selecione um")

            self.selected_item26 = StringVar()
            self.selected_item26.set("Selecione um")

            self.combobox19 = ttk.Combobox(self.frame_7, textvariable=self.selected_item19, values=itens_pre_definidos19, state="readonly")
            self.combobox19.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox19.place(relx=0.56, rely=0.3, relwidth=.15, relheight=.10)

            self.combobox20 = ttk.Combobox(self.frame_7, textvariable=self.selected_item20, values=itens_pre_definidos20, state="readonly")
            self.combobox20.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox20.place(relx=0.56, rely=0.43, relwidth=.15, relheight=.10)

            self.combobox21 = ttk.Combobox(self.frame_7, textvariable=self.selected_item21, values=itens_pre_definidos21, state="readonly")
            self.combobox21.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox21.place(relx=0.56, rely=0.56, relwidth=.15, relheight=.10)

            self.combobox22 = ttk.Combobox(self.frame_7, textvariable=self.selected_item22, values=itens_pre_definidos22, state="readonly")
            self.combobox22.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox22.place(relx=0.56, rely=0.69, relwidth=.15, relheight=.10)

            self.combobox23 = ttk.Combobox(self.frame_7, textvariable=self.selected_item23, values=itens_pre_definidos23, state="readonly")
            self.combobox23.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox23.place(relx=0.74, rely=0.3, relwidth=.15, relheight=.10)

            self.combobox24 = ttk.Combobox(self.frame_7, textvariable=self.selected_item24, values=itens_pre_definidos24, state="readonly")
            self.combobox24.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox24.place(relx=0.74, rely=0.43, relwidth=.15, relheight=.10)

            self.combobox25 = ttk.Combobox(self.frame_7, textvariable=self.selected_item25, values=itens_pre_definidos25, state="readonly")
            self.combobox25.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox25.place(relx=0.74, rely=0.56, relwidth=.15, relheight=.10)

            self.combobox26 = ttk.Combobox(self.frame_7, textvariable=self.selected_item26, values=itens_pre_definidos26, state="readonly")
            self.combobox26.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox26.place(relx=0.74, rely=0.69, relwidth=.15, relheight=.10)

        if hasattr(self, 'frame_9'):
            itens_pre_definidos27 = ["Sentado no Teatro",
            "Sentado no Teatro, noite",
            "Sentado Trabalho Leve",
            "Atividades moderada em trabalho de escritório",
            "Parado em pé, trabalho moderado, caminhando",
            "Caminhando, parado em pé",
            "Trabalho sedentário",
            "Trabalho leve em bancada",
            "Dançando moderadamente",
            "Caminhando 4,8 Km/h, trabalho leve em maquina operatriz",
            "Jogando boliche",
            "Trabalho Pesado",
            "Trabalho Pesado em maquina operatriz, Carregando Carga",
            "Praticando Esportes",
            "Nenhum"
            ]


            self.selected_item27 = StringVar()
            self.selected_item27.set("Selecione um")


            self.combobox27 = ttk.Combobox(self.frame_9, textvariable=self.selected_item27, values=itens_pre_definidos27, state="readonly")
            self.combobox27.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox27.place(relx=0.56, rely=0.3, relwidth=.40, relheight=.10)

        if hasattr(self, 'frame_13'):
            itens_pre_definidos28 = ["Supermecado de Alto Padrão",
            "Supermecado de Padrão Médio",
            "Supermecado Popular",
            "Mall de Centros Comerciais",
            "Lojas (exceto abaixo)",
            "Salão de Beleza e/ou Barbearia",
            "Animais de estimação",
            "Lavanderia 'self-service'",
            "Hall do edifício, recepção",
            "Escritórios de Diretoria",
            "Escritório com Baixa Densidade",
            "Escritório com Média Densidade",
            "Escritório com Alta Densidade",
            "Sala de Reunião",
            "CPD ( exceto impressoras)",
            "Sala de Impressoras, Copiadoras",
            "Sala de Digitação",
            "Call Center",
            "Bancos ( área do público)",
            "Caixa Forte",
            "Aeroporto - Saguão",
            "Aeroporto - Sala de Embarque",
            "Biblioteca",
            "Museu, Galeria de Arte",
            "Local de Culto",
            "Legislativo - Plenário",
            "Teatro, Cinema, Auditório - Lobby",
            "Teatro, Cinema, Auditório e Platéia",
            "Teatro, Cinema, Auditório -Palco",
            "Tribunal - Sala de Audiências",
            "Boliche - Área do Público",
            "Ginásio Coberto ( Área do Público)",
            "Ginásio Coberto (Quadra)",
            "Piscina Coberta",
            "'Fitness Center' - Aeróbica",
            "'Fitness Center' - Aparelhos"
            "Sala de Aula",
            "Laboratório de Informática",
            "Laboratório de Ciências",
            "Apartamento de Hóspedes",
            "Lobby, sala de estar",
            "Sala de Convenções",
            "Dormitório Coletivo",
            "Restaurantes - Salão de Refeições",
            "Bar, Salão de Coquetel",
            "Cafeteria, Lanchonete, Refeitório",
            "Salão de Jogos",
            "Discoteca, Danceteria",
            "Jogos Eletrônicos"]

            itens_pre_definidos29 = ["Nível 1", "Nível 2", "Nível 3"]


            self.selected_item28 = StringVar()
            self.selected_item28.set("Selecione um")

            self.selected_item29 = StringVar()
            self.selected_item29.set("Selecione um")

            self.combobox28 = ttk.Combobox(self.frame_13, textvariable=self.selected_item28, values=itens_pre_definidos28, state="readonly")
            self.combobox28.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox28.place(relx=0.35, rely=0.3, relwidth=.250, relheight=.10)

            self.combobox29 = ttk.Combobox(self.frame_13, textvariable=self.selected_item29, values=itens_pre_definidos29, state="readonly")
            self.combobox29.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox29.place(relx=0.35, rely=0.43, relwidth=.25, relheight=.10)

        if hasattr(self, 'frame_15'):
            itens_pre_definidos30 = ["Comum",
                                "Basculante",
                                "Guilhotina com caxilho de madeira",
                                "Guilhotina com caxilho metálico"]

            itens_pre_definidos31 = ["Mal Ajustada",
                                    "Bem Ajustada"]

            itens_pre_definidos32 = ["Porta Giratória 1,80 m",
                                    "Porta Vaivém 0,9 m"]

            itens_pre_definidos33 = ["Mal Ajustada",
                                    "Bem Ajustada"]

            itens_pre_definidos34 = ["Barbearias",
                                    "Drogarias e Farmácias",
                                    "Escritórios de Corretagem",
                                    "Escritórios Privados",
                                    "Escritórios em Geral",
                                    "Lojas de Cigarros",
                                    "Lojas em Geral",
                                    "Quartos de Hospitais",
                                    "Restaurantes",
                                    "Salas de Chá ou Café"]


            self.selected_item30 = StringVar()
            self.selected_item30.set("Tipo")

            self.selected_item31 = StringVar()
            self.selected_item31.set("Ajustamento")

            self.selected_item32 = StringVar()
            self.selected_item32.set("Tipo")

            self.selected_item33 = StringVar()
            self.selected_item33.set("Ajustamento")

            self.selected_item34 = StringVar()
            self.selected_item34.set("Tipo de Local")


            self.combobox30 = ttk.Combobox(self.frame_15, textvariable=self.selected_item30, values=itens_pre_definidos30, state="readonly")
            self.combobox30.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox30.place(relx=0.32, rely=0.3, relwidth=.20, relheight=.10)

            self.combobox31 = ttk.Combobox(self.frame_15, textvariable=self.selected_item31, values=itens_pre_definidos31, state="readonly")
            self.combobox31.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox31.place(relx=0.54, rely=0.3, relwidth=.20, relheight=.10)

            self.combobox32 = ttk.Combobox(self.frame_15, textvariable=self.selected_item32, values=itens_pre_definidos32, state="readonly")
            self.combobox32.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox32.place(relx=0.32, rely=0.43, relwidth=.20, relheight=.10)

            self.combobox33 = ttk.Combobox(self.frame_15, textvariable=self.selected_item33, values=itens_pre_definidos33, state="readonly")
            self.combobox33.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox33.place(relx=0.54, rely=0.43, relwidth=.20, relheight=.10)

            self.combobox34 = ttk.Combobox(self.frame_15, textvariable=self.selected_item34, values=itens_pre_definidos34, state="readonly")
            self.combobox34.bind('<<ComboboxSelected>>', self.mostrar_item_selecionado)  # Associa a função ao evento de seleção
            self.combobox34.place(relx=0.32, rely=0.60, relwidth=.20, relheight=.10)


        # Rótulos
        if hasattr(self, 'frame_1'):

            
            self.titulo_1 = Label(self.frame_1, text="Dados Gerais", font=("verdana",10,"bold"), bg='#E0FFFF')
            self.titulo_1.place(relx=0.45, rely=0.01)

            self.lb_cid = Label(self.frame_1, text="Local:", bg='#E0FFFF')
            self.lb_cid.place(relx=0.07, rely=0.15)

            self.lb_tem1= Label(self.frame_1, text="Temperatura de bulbo seco:", bg='#E0FFFF')
            self.lb_tem1.place(relx=0.07, rely=0.31)

            self.lb_alt = Label(self.frame_1, text="Altitude:", bg='#E0FFFF')
            self.lb_alt.place(relx=0.07, rely=0.47)

            self.lb_um1 = Label(self.frame_1, text="Umidade relativa:", bg='#E0FFFF')
            self.lb_um1.place(relx=0.07, rely=0.63)

            self.lb_tem2 = Label(self.frame_1, text="Temperatura de bulbo seco:", bg='#E0FFFF')
            self.lb_tem2.place(relx=0.55, rely=0.31)

            self.lb_um2 = Label(self.frame_1, text="Umidade relativa:", bg='#E0FFFF')
            self.lb_um2.place(relx=0.55, rely=0.47)

        if hasattr(self, 'frame_3'):
            self.titulo_2 = Label(self.top_fr, text="Condução", font=("verdana",10,"bold"), bg='#E0FFFF')
            self.titulo_2.place(relx=0.2, rely=0)

            self.sub_titulo = Label(self.frame_3, text="Paredes externas", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.sub_titulo.place(relx=0.425, rely=0.005)

            self.result_t = self.temperatura_bulbo_seco - self.temperatura_bulbo_seco2
            self.t_label = Label(self.frame_3, text=f'Variação de temperatura: {self.result_t} °C', bg='#E0FFFF')
            self.t_label.place(relx=0.0025, rely=0.06)

            self.pedir = Label(self.frame_3, text=f'Altura do pé direito: ', bg='#E0FFFF')
            self.pedir.place(relx=0.0025, rely=0.205)

            self.orientacao = Label(self.frame_3, text='Escolha a orientação: ', bg='#E0FFFF', justify="left")
            self.orientacao.place(relx=0.65, rely=0.115)

            self.pareden = "Parede Norte"      
            self.label_pareden = Label(self.frame_3, text=self.pareden, font=("Arial", 10), bg='#E0FFFF')
            self.label_pareden.place(relx=.12, rely=0.37)

            self.paredes = "Parede Sul"      
            self.label_paredes = Label(self.frame_3, text=self.paredes, font=("Arial", 10), bg='#E0FFFF')
            self.label_paredes.place(relx=.30, rely=0.37)

            self.paredel = "Parede Leste"      
            self.label_paredel = Label(self.frame_3, text=self.paredel, font=("Arial", 10), bg='#E0FFFF')
            self.label_paredel.place(relx=.48, rely=0.37)

            self.paredeo = "Parede Oeste"      
            self.label_paredeo = Label(self.frame_3, text=self.paredeo, font=("Arial", 10), bg='#E0FFFF')
            self.label_paredeo.place(relx=.66, rely=0.37)

            self.dimen1 = Label(self.frame_3, text="Comprimento: ", bg='#E0FFFF')
            self.dimen1.place(relx=0.002,rely=0.5)

            self.cor = Label(self.frame_3, text="Cor da parede: ", bg='#E0FFFF')
            self.cor.place(relx=0.002,rely=0.63)

            self.radia = Label(self.frame_3, text="Possui radiação: ", bg='#E0FFFF')
            self.radia.place(relx=0.002,rely=0.76)

            self.tipoparede = Label(self.frame_3, text="Tipo de parede: ", bg='#E0FFFF')
            self.tipoparede.place(relx=0.002,rely=0.89)

        if hasattr(self, 'frame_5'):

            self.sub_titulo2 = Label(self.frame_5, text="Divisórias Internas (ÁREAS NÃO CONDICIONADAS)", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.sub_titulo2.place(relx=0.325, rely=0.005)

            self.compd = Label(self.frame_5, text="Comprimento ", bg='#E0FFFF')
            self.compd.place(relx=0.10,rely=0.15)

            self.lard = Label(self.frame_5, text="Largura ", bg='#E0FFFF')
            self.lard.place(relx=0.23,rely=0.15)

            self.tipd = Label(self.frame_5, text="Tipo ", bg='#E0FFFF')
            self.tipd.place(relx=0.36,rely=0.15)

            self.subtipd = Label(self.frame_5, text="Subtipo ", bg='#E0FFFF')
            self.subtipd.place(relx=0.68,rely=0.15)

            self.pared = Label(self.frame_5, text="Parede: ", bg='#E0FFFF')
            self.pared.place(relx=0.01,rely=0.3)

            self.vidr = Label(self.frame_5, text="Vidros: ", bg='#E0FFFF')
            self.vidr.place(relx=0.01,rely=0.43)

            self.piso = Label(self.frame_5, text="Piso: ", bg='#E0FFFF')
            self.piso.place(relx=0.01,rely=0.56)

            self.teto = Label(self.frame_5, text="Teto: ", bg='#E0FFFF')
            self.teto.place(relx=0.01,rely=0.69)
            
        if hasattr(self, 'frame_7'):
            self.sub_titulo3 = Label(self.frame_7, text="Superficíes Transparentes (INSOLAÇÃO DIRETA)", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.sub_titulo3.place(relx=0.325, rely=0.005)

            self.janen = "Janela Norte/ Nordeste: "
            self.label_janen = Label(self.frame_7, text=self.janen, bg='#E0FFFF')
            self.label_janen.place(relx=0.01,rely=0.3)

            self.janes = "Janela Sul/ Sudoeste: "
            self.label_janes = Label(self.frame_7, text=self.janes, bg='#E0FFFF')
            self.label_janes.place(relx=0.01,rely=0.43)

            self.janeo = "Janela Oeste/ Noroeste: "
            self.label_janeo = Label(self.frame_7, text=self.janeo, bg='#E0FFFF')
            self.label_janeo.place(relx=0.01,rely=0.56)

            self.janel = "Janela Leste/ Sudeste: "
            self.label_janel = Label(self.frame_7, text=self.janel, bg='#E0FFFF')
            self.label_janel.place(relx=0.01,rely=0.69)

            self.compv = Label(self.frame_7, text="Comprimento ", bg='#E0FFFF')
            self.compv.place(relx=0.17,rely=0.15)

            self.larv = Label(self.frame_7, text="Largura ", bg='#E0FFFF')
            self.larv.place(relx=0.3,rely=0.15)

            self.fs = Label(self.frame_7, text="Fator Solar ", bg='#E0FFFF')
            self.fs.place(relx=0.43,rely=0.15)

            self.tipov = Label(self.frame_7, text="Tipo ", bg='#E0FFFF')
            self.tipov.place(relx=0.56,rely=0.15)

            self.esqv = Label(self.frame_7, text="Esquadria ", bg='#E0FFFF')
            self.esqv.place(relx=0.74,rely=0.15)

        if hasattr(self, 'frame_9'):
            self.sub_titulo4 = Label(self.frame_9, text="Pessoas", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.sub_titulo4.place(relx=0.45, rely=0.005)

            self.atv1 = "Em atividade: "
            self.label_atv1 = Label(self.frame_9, text=self.atv1, bg='#E0FFFF')
            self.label_atv1.place(relx=0.01,rely=0.3)

            
            self.hom = Label(self.frame_9, text="Homens ", bg='#E0FFFF')
            self.hom.place(relx=0.17,rely=0.15)

            self.mul = Label(self.frame_9, text="Mulheres ", bg='#E0FFFF')
            self.mul.place(relx=0.3,rely=0.15)

            self.cria = Label(self.frame_9, text="Crianças ", bg='#E0FFFF')
            self.cria.place(relx=0.43,rely=0.15)

            self.natv = Label(self.frame_9, text="Nível de atividade ", bg='#E0FFFF')
            self.natv.place(relx=0.56,rely=0.15)

        if hasattr(self, 'frame_11'):
            self.titulo5 = Label(self.frame_11, text="Calor dos Equipamentos", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.titulo5.place(relx=0.45, rely=0.005)

            self.atv1 = "Equipamento: "
            self.label_atv1 = Label(self.frame_11, text=self.atv1, bg='#E0FFFF')
            self.label_atv1.place(relx=0.15,rely=0.3)

            self.atv2 = "Quantidade: "
            self.label_atv2 = Label(self.frame_11, text=self.atv2, bg='#E0FFFF')
            self.label_atv2.place(relx=0.15,rely=0.43)

            self.atv3 = "Calor Sensível: "
            self.label_atv3 = Label(self.frame_11, text=self.atv3, bg='#E0FFFF')
            self.label_atv3.place(relx=0.15,rely=0.56)

            self.atv4 = "Calor Latente: "
            self.label_atv4 = Label(self.frame_11, text=self.atv4, bg='#E0FFFF')
            self.label_atv4.place(relx=0.15,rely=0.69)

        if hasattr(self, 'frame_13'):
            self.titulo6 = Label(self.frame_13, text="Ventilação", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.titulo6.place(relx=0.45, rely=0.005)

            self.tpl = "Tipo de Local: "
            self.label_tpl = Label(self.frame_13, text=self.tpl, bg='#E0FFFF')
            self.label_tpl.place(relx=0.15,rely=0.3)

            self.nlv = "Nível de Ventilação: "
            self.label_nlv = Label(self.frame_13, text=self.nlv, bg='#E0FFFF')
            self.label_nlv.place(relx=0.15,rely=0.43)

            self.ocup = Label(self.frame_13, text="Ocupação do ambiente (Em %):", bg='#E0FFFF')
            self.ocup.place(relx=0.15,rely=0.56)

        if hasattr(self, 'frame_15'):
            self.titulo7 = Label(self.frame_15, text="Infiltração:", font=("verdana",10,"bold"), bg='#E0FFFF', justify="left")
            self.titulo7.place(relx=0.45, rely=0.005)

            self.label_janin = Label(self.frame_15, text="Janelas:", bg='#E0FFFF')
            self.label_janin.place(relx=0.15,rely=0.3)

            self.label_portin = Label(self.frame_15, text="Portas:", bg='#E0FFFF')
            self.label_portin.place(relx=0.15,rely=0.43)

            self.label_relpess = Label(self.frame_15, text="Relacionado a pessoas:", bg='#E0FFFF')
            self.label_relpess.place(relx=0.15,rely=0.60)

        if hasattr(self, 'frame_17'):

            self.calculos9()

            self.text1 = Label(self.frame_17, text="   Resultado Cálculos:\n\n\n"
                                    f"Condução:\n"
                                    f"Pessoas:\n"
                                    f"Equipamentos:\n"
                                    f"Ventilação:\n"
                                    f"Infiltração:\n"
                                    f"Subtotal:\n"
                                    f"Total:\n"
                                    f"Total (+10%):", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
            self.text1.place(relx=0.01, rely=0.005)

            self.text2 = Label(self.frame_17, text="        \n\n"
                                    f"Calor Sensível\n"
                                    f"{round(self.cargaext, 2)} KCal/h\n"
                                    f"{round(self.cs0_total, 2)} KCal/h\n"
                                    f"{round(self.cs_total, 2)} KCal/h\n"
                                    f"{round(self.calsen_ven, 2)} KCal/h\n"
                                    f"{round(self.csti, 2)} KCal/h\n"
                                    f"{round(self.scals, 2)} KCal/h\n"
                                    f"          {round(self.caltotal, 2)} KCal/h\n"
                                    f"          {round(self.caltotal_up, 2)} KCal/h", justify="right",bg="#E0FFFF", font=("verdana",12,"bold"))
            self.text2.place(relx=0.13, rely=0.005)

            self.text3 = Label(self.frame_17, text="        \n\n"
                                    f"Calor Latente\n"
                                    f"0 KCal/h\n"
                                    f"{round(self.cl0_total, 2)} KCal/h\n"
                                    f"{round(self.cl_total, 2)} KCal/h\n"
                                    f"{round(self.callat_ven, 2)} KCal/h\n"
                                    f"{round(self.clti, 2)} KCal/h\n"
                                    f"{round(self.scall, 2)} KCal/h"
                                    , justify="right",bg="#E0FFFF", font=("verdana",12,"bold"))
            self.text3.place(relx=0.36, rely=0.005)

            self.text4 = Label(self.frame_17, text="        \n\n"
                                    f"Vazão de ar a 10°C\n"
                                    f"{round(self.v_ark1, 2)} Kg/h\n"
                                    f"{round(self.v_ark2, 2)} Kg/h\n"
                                    f"{round(self.v_ark3, 2)} Kg/h\n"
                                    f"{round(self.v_ark4, 2)} Kg/h\n"
                                    f"{round(self.v_ark5, 2)} Kg/h\n"
                                    f"{round(self.v_art1, 2)} Kg/h"
                                    , justify="right",bg="#E0FFFF", font=("verdana",12,"bold"))
            self.text4.place(relx=0.54, rely=0.005)

            self.text5 = Label(self.frame_17, text="        \n\n"
                                    f"Vazão de ar a 15°C\n"
                                    f"{round(self.v_ark6, 2)} Kg/h\n"
                                    f"{round(self.v_ark7, 2)} Kg/h\n"
                                    f"{round(self.v_ark8, 2)} Kg/h\n"
                                    f"{round(self.v_ark9, 2)} Kg/h\n"
                                    f"{round(self.v_ark10, 2)} Kg/h\n"
                                    f"{round(self.v_art2, 2)} Kg/h"
                                    , justify="right",bg="#E0FFFF", font=("verdana",12,"bold"))
            self.text5.place(relx=0.76, rely=0.005)

            self.text6 = Label(self.frame_18, text="   Outros Resultados:\n\n\n"
                                    f"Vazão (ar insulflado a 10°C): {round(self.v_arm1, 2)} m³/h\n"
                                    f"Vazão (ar insulflado a 15°C): {round(self.v_arm2, 2)} m³/h\n"
                                    f"Água a ser retirada:{round(self.agret, 2)} Kg\n"
                                    f"RCS:{round(self.rcs, 2)}", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
            self.text6.place(relx=0.01, rely=0.005)

            # Vazão de ar, água a ser retirada e RCS
            self.v_arm1 = self.v_art1/1.2466
            self.v_arm2 = self.v_art2/1.2466
            self.agret = self.scals/583
            self.rcs = self.scals/self.caltotal_up


        # Caixa de entradas
        if hasattr(self, 'frame_1'):

            self.calc_cid = Entry(self.frame_1)
            self.calc_cid.place(relx=0.25, rely=0.15, relwidth=0.17, relheight=0.08)

            self.calc_tem1 = Entry(self.frame_1)
            self.calc_tem1.place(relx=0.25, rely=0.31, relwidth=0.17, relheight=0.08)

            self.calc_alt = Entry(self.frame_1)
            self.calc_alt.place(relx=0.25, rely=0.47, relwidth=0.17, relheight=0.08)

            self.calc_um1 = Entry(self.frame_1)
            self.calc_um1.place(relx=0.25, rely=0.63, relwidth=0.17, relheight=0.08)

            self.calc_tem2 = Entry(self.frame_1)
            self.calc_tem2.place(relx=0.73, rely=0.31, relwidth=0.17, relheight=0.08)

            self.calc_um2 = Entry(self.frame_1)
            self.calc_um2.place(relx=0.73, rely=0.47, relwidth=0.17, relheight=0.08)

        if hasattr(self, 'frame_3'):

            self.pedirc = Entry(self.frame_3)
            self.pedirc.place(relx=0.12, rely=0.205, relwidth=0.15, relheight=0.08)

            self.comp1 = Entry(self.frame_3)
            self.comp1.place(relx=0.12, rely=0.5, relwidth=0.15, relheight=0.08)

            self.comp2 = Entry(self.frame_3)
            self.comp2.place(relx=0.3, rely=0.5, relwidth=0.15, relheight=0.08)

            self.comp3 = Entry(self.frame_3)
            self.comp3.place(relx=0.48, rely=0.5, relwidth=0.15, relheight=0.08)

            self.comp4 = Entry(self.frame_3)
            self.comp4.place(relx=0.66, rely=0.5, relwidth=0.15, relheight=0.08)

        if hasattr(self, 'frame_5'):

            self.pared_ent = Entry(self.frame_5)
            self.pared_ent.place(relx=0.1,rely=0.3, relwidth=0.1, relheight=0.08)

            self.vidr_ent = Entry(self.frame_5)
            self.vidr_ent.place(relx=0.1,rely=0.43, relwidth=0.1, relheight=0.08)

            self.piso_ent = Entry(self.frame_5)
            self.piso_ent.place(relx=0.1,rely=0.56, relwidth=0.1, relheight=0.08)

            self.teto_ent = Entry(self.frame_5)
            self.teto_ent.place(relx=0.1,rely=0.69, relwidth=0.1, relheight=0.08)

            self.pared2_ent = Entry(self.frame_5)
            self.pared2_ent.place(relx=0.23,rely=0.3, relwidth=0.1, relheight=0.08)

            self.vidr2_ent = Entry(self.frame_5)
            self.vidr2_ent.place(relx=0.23,rely=0.43, relwidth=0.1, relheight=0.08)

            self.piso2_ent = Entry(self.frame_5)
            self.piso2_ent.place(relx=0.23,rely=0.56, relwidth=0.1, relheight=0.08)

            self.teto2_ent = Entry(self.frame_5)
            self.teto2_ent.place(relx=0.23,rely=0.69, relwidth=0.1, relheight=0.08)

        if hasattr(self, 'frame_7'):
            self.janen_ent = Entry(self.frame_7)
            self.janen_ent.place(relx=0.17,rely=0.3, relwidth=0.1, relheight=0.08)

            self.janes_ent = Entry(self.frame_7)
            self.janes_ent.place(relx=0.17,rely=0.43, relwidth=0.1, relheight=0.08)

            self.janel_ent = Entry(self.frame_7)
            self.janel_ent.place(relx=0.17,rely=0.56, relwidth=0.1, relheight=0.08)

            self.janeo_ent = Entry(self.frame_7)
            self.janeo_ent.place(relx=0.17,rely=0.69, relwidth=0.1, relheight=0.08)

            self.janen2_ent = Entry(self.frame_7)
            self.janen2_ent.place(relx=0.3,rely=0.3, relwidth=0.1, relheight=0.08)

            self.janes2_ent = Entry(self.frame_7)
            self.janes2_ent.place(relx=0.3,rely=0.43, relwidth=0.1, relheight=0.08)

            self.janel2_ent = Entry(self.frame_7)
            self.janel2_ent.place(relx=0.3,rely=0.56, relwidth=0.1, relheight=0.08)

            self.janeo2_ent = Entry(self.frame_7)
            self.janeo2_ent.place(relx=0.3,rely=0.69, relwidth=0.1, relheight=0.08)

            self.janen3_ent = Entry(self.frame_7)
            self.janen3_ent.place(relx=0.43,rely=0.3, relwidth=0.1, relheight=0.08)

            self.janes3_ent = Entry(self.frame_7)
            self.janes3_ent.place(relx=0.43,rely=0.43, relwidth=0.1, relheight=0.08)

            self.janel3_ent = Entry(self.frame_7)
            self.janel3_ent.place(relx=0.43,rely=0.56, relwidth=0.1, relheight=0.08)

            self.janeo3_ent = Entry(self.frame_7)
            self.janeo3_ent.place(relx=0.43,rely=0.69, relwidth=0.1, relheight=0.08)
        
        if hasattr(self, 'frame_9'):
            self.lista_selecionados0 = []

            self.hom1_ent = Entry(self.frame_9)
            self.hom1_ent.place(relx=0.17,rely=0.3, relwidth=0.1, relheight=0.08)

            self.mul1_ent = Entry(self.frame_9)
            self.mul1_ent.place(relx=0.3,rely=0.3, relwidth=0.1, relheight=0.08)

            self.cria1_ent = Entry(self.frame_9)
            self.cria1_ent.place(relx=0.43,rely=0.3, relwidth=0.1, relheight=0.08)

        if hasattr(self, 'frame_11'):
            self.lista_selecionados = []

            self.equip_ent = Entry(self.frame_11)
            self.equip_ent.place(relx=0.3,rely=0.3, relwidth=0.15, relheight=0.08)

            self.quant_ent = Entry(self.frame_11)
            self.quant_ent.place(relx=0.3,rely=0.43, relwidth=0.15, relheight=0.08)

            self.ces_ent = Entry(self.frame_11)
            self.ces_ent.place(relx=0.3,rely=0.56, relwidth=0.15, relheight=0.08)

            self.cel_ent = Entry(self.frame_11)
            self.cel_ent.place(relx=0.3,rely=0.69, relwidth=0.15, relheight=0.08)

        if hasattr(self, 'frame_13'):
            
            self.label_ocup = Entry(self.frame_13)
            self.label_ocup.place(relx=0.35,rely=0.56, relwidth=0.15, relheight=0.08)
        
        if hasattr(self, 'frame_15'):
            self.label_qtdport = Entry(self.frame_15)
            self.label_qtdport.insert(0, "Quantidade de portas")  # Adiciona o texto indicativo
            self.label_qtdport.place(relx=0.76, rely=0.43, relwidth=0.15, relheight=0.08)

            # Função para remover o texto indicativo quando a entry é clicada
            def on_entry_click(event):
                if self.label_qtdport.get() == "Quantidade de portas":
                    self.label_qtdport.delete(0, "end")
                    self.label_qtdport.insert(0, "")
                    self.label_qtdport.config(fg='black')

            self.label_qtdport.bind('<FocusIn>', on_entry_click)  # Associa o evento de clique à função


        # Botões de ajuda
        if hasattr(self, 'frame_1'):

            
            help_cid = Button(self.frame_1, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_cid.place(relx=0.44, rely=0.15)
            tooltip1_text = "Cidade onde está localizado o ambiente."
            tooltip1 = ToolTip(help_cid, tooltip1_text)

            help_tem1 = Button(self.frame_1, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_tem1.place(relx=0.44, rely=0.31)
            tooltip2_text = "Temperatura na rua, ou temperatura externa.\nRecomendado utilizar a maior temperatura do ano para saber o pior caso de operação."
            tooltip2 = ToolTip(help_tem1, tooltip2_text)

            help_alt = Button(self.frame_1, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_alt.place(relx=0.44, rely=0.47)
            tooltip3_text = "Altitude da cidade.\nExemplo: ao nível do mar é 0 metros."
            tooltip3 = ToolTip(help_alt, tooltip3_text)

            help_um1 = Button(self.frame_1, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_um1.place(relx=0.44, rely=0.63)
            tooltip4_text = "Umidade relativa externa, em porcentagem (%)."
            tooltip4 = ToolTip(help_um1, tooltip4_text)

            help_tem2 = Button(self.frame_1, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_tem2.place(relx=0.92, rely=0.31)
            tooltip5_text = "Temperatura de conforto, a temperatura interna.\nRecomendado 24°C."
            tooltip5 = ToolTip(help_tem2, tooltip5_text)
            
            help_um2 = Button(self.frame_1, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_um2.place(relx=0.92, rely=0.47)
            tooltip6_text = "Umidade relativa de conforto, umidade interna, em porcentagem (%).\nRecomendado entre 55 e 65%."
            tooltip6 = ToolTip(help_um2, tooltip6_text)
        
        if hasattr(self, 'frame_3'):

            
            help_pedir = Button(self.frame_3, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_pedir.place(relx=0.27, rely=0.19)
            tooltip7_text = "A distância do piso até o teto em metros"
            tooltip7 = ToolTip(help_pedir, tooltip7_text)

            help_comp = Button(self.frame_3, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_comp.place(relx=0.82, rely=0.48)
            tooltip8_text = "A distância de um lado outro de uma parede em metros"
            tooltip8 = ToolTip(help_comp, tooltip8_text)

            help_pared = Button(self.frame_3, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_pared.place(relx=0.82, rely=0.63)
            tooltip9_text = "O tom da cor aplicada a parede para definir a absorção de calor"
            tooltip9 = ToolTip(help_pared, tooltip9_text)

            help_rad = Button(self.frame_3, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_rad.place(relx=0.82, rely=0.76)
            tooltip10_text = "Definir se a orientação está livre para receber radiação solar ou se possui algum tipo de construção\n dos lados ou atrás que impeça a passagem de radiação"
            tooltip10 = ToolTip(help_rad, tooltip10_text)

            help_tipared = Button(self.frame_3, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_tipared.place(relx=0.82, rely=0.89)
            tooltip11_text = "Tipo de tijolo usado na construção da parede, espessura e se maciço ou furado"
            tooltip11 = ToolTip(help_tipared, tooltip11_text)

        if hasattr(self, 'frame_5'):
            help_compad = Button(self.frame_5, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_compad.place(relx=0.183, rely=0.15)
            tooltip12_text = "Distância de um lado ao outro do especificado, parede, vidros, piso ou teto."
            tooltip12 = ToolTip(help_compad, tooltip12_text)

            help_lard = Button(self.frame_5, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_lard.place(relx=0.29,rely=0.15)
            tooltip13_text = "Distância de cima a baixo do especificado, parede, vidros, piso ou teto."
            tooltip13 = ToolTip(help_lard, tooltip13_text)


            help_tipd = Button(self.frame_5, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_tipd.place(relx=0.42,rely=0.15)
            tooltip14_text = "Onde está localizado ou ou tipo de divisória que está inserido."
            tooltip14 = ToolTip(help_tipd, tooltip14_text)

            help_subtipd = Button(self.frame_5, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_subtipd.place(relx=0.74,rely=0.15)
            tooltip15_text = "Tipo do tijolo ou vidro."
            tooltip15 = ToolTip(help_subtipd, tooltip15_text)
        
        if hasattr(self, 'frame_7'):
            help_compv = Button(self.frame_7, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_compv.place(relx=0.26,rely=0.15)
            tooltip16_text = "Distância de um lado ao outro da janela."
            tooltip16 = ToolTip(help_compv, tooltip16_text)

            help_larv = Button(self.frame_7, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_larv.place(relx=0.35,rely=0.15)
            tooltip17_text = "Distância de cima a baixo da janela."
            tooltip17 = ToolTip(help_larv, tooltip17_text)

            help_fs = Button(self.frame_7, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_fs.place(relx=0.50,rely=0.15)
            tooltip18_text = "Fator solar da região em que está o ambiente,\n Clicar no botão 'Tabela FS' para abrir a tabela com o fator solar."
            tooltip18 = ToolTip(help_fs, tooltip18_text)

            help_tipov = Button(self.frame_7, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_tipov.place(relx=0.59,rely=0.15)
            tooltip19_text = "Tipo de proteção da janela, e caso não tenha também."
            tooltip19 = ToolTip(help_tipov, tooltip19_text)

            help_esqv = Button(self.frame_7, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_esqv.place(relx=0.81,rely=0.15)
            tooltip20_text = "Tipo de esquadria da janela, e caso não tenha também."
            tooltip20 = ToolTip(help_esqv, tooltip20_text)
        
        if hasattr(self, 'frame_9'):
            help_hom = Button(self.frame_9, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_hom.place(relx=0.23,rely=0.15)
            tooltip21_text = "Quantidade de homens fazendo a atividade selecionada."
            tooltip21 = ToolTip(help_hom, tooltip21_text)

            help_mul = Button(self.frame_9, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_mul.place(relx=0.36,rely=0.15)
            tooltip22_text = "Quantidade de mulheres fazendo a atividade selecionada."
            tooltip22 = ToolTip(help_mul, tooltip22_text)

            help_cria = Button(self.frame_9, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_cria.place(relx=0.49,rely=0.15)
            tooltip23_text = "Quantidade de crianças fazendo a atividade selecionada."
            tooltip23 = ToolTip(help_cria, tooltip23_text)

            help_natv = Button(self.frame_9, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_natv.place(relx=0.67,rely=0.15)
            tooltip24_text = "Nível da atividade ou atividade sendo feita."
            tooltip24 = ToolTip(help_natv, tooltip24_text)

        if hasattr(self, 'frame_11'):
            help_equip_ent = Button(self.frame_11, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_equip_ent.place(relx=0.46,rely=0.3)
            tooltip25_text = "Nomear o equipamento que vai ser indicado."
            tooltip25 = ToolTip(help_equip_ent, tooltip25_text)

            help_quant_ent = Button(self.frame_11, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_quant_ent.place(relx=0.46,rely=0.43)
            tooltip26_text = "Quantidade desse equipamento no Ambiente."
            tooltip26 = ToolTip(help_quant_ent, tooltip26_text)

            help_ces_ent = Button(self.frame_11, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_ces_ent.place(relx=0.46,rely=0.56)
            tooltip27_text = "Calor Sensível gerado pelo equipamento."
            tooltip27 = ToolTip(help_ces_ent, tooltip27_text)

            help_cel_ent = Button(self.frame_11, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_cel_ent.place(relx=0.46,rely=0.69)
            tooltip28_text = "Calor Latente gerado pelo equipamento."
            tooltip28 = ToolTip(help_cel_ent, tooltip28_text)

        if hasattr(self, 'frame_13'):
            help_combobox28 = Button(self.frame_13, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_combobox28.place(relx=0.6, rely=0.3)
            tooltip29_text = "Tipo de Local a ser ventilado."
            tooltip29 = ToolTip(help_combobox28, tooltip29_text)
            
            help_combobox29 = Button(self.frame_13, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_combobox29.place(relx=0.6, rely=0.43)
            tooltip30_text = "Nível de ventilação, sendo:\n Nível 1 - Nível Mínimo vazão de ar exterior para ventilção.\n Nível 2 - Nível intermediário da vazão de ar exterior para ventilação.\n Nível 3 - Vazões de ar exterior para ventilação que segundo estudos\n existem evidências de redução de reclamações e manifestações alergicas."
            tooltip30 = ToolTip(help_combobox29, tooltip30_text)

            help_label_ocup = Button(self.frame_13, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_label_ocup.place(relx=0.51,rely=0.56)
            tooltip31_text = "Ocupação do Local em porcentagem (%), levando em consideração moveis, equipamento e pessoas no local.\nConsiderar a parte do ESPAÇO ocupado."
            tooltip31 = ToolTip(help_label_ocup, tooltip31_text)
            
        if hasattr(self, 'frame_15'):
            help_a = Button(self.frame_15, image= self.help_icon,bg='#E0FFFF', bd=0, padx=0, pady=0)
            help_a.place(relx=0.54,rely=0.59)
            tooltip32_text = "Ocupação do Local em porcentagem (%), levando em consideração moveis, equipamento e pessoas no local.\nConsiderar a parte do ESPAÇO ocupado."
            tooltip32 = ToolTip(help_a, tooltip32_text)

        # FAZER BOTÕES DE AJUDA PARA OS OUTROS FRAMES (frame_13, frame_15)!!!


        # Label de resultados
        if hasattr(self, 'frame_1'):
            # Label de resultados Dados Gerais
            self.resultado_label1 = Label(self.frame_2, text=" ", bg="#E0FFFF")
            self.resultado_label1.place(relx=0.08, rely=0.2)

            self.resultado_label2 = Label(self.frame_2, text=" ", bg="#E0FFFF")
            self.resultado_label2.place(relx=0.5, rely=0.2)
        
        if hasattr(self, 'frame_3'):
             
            self.resultado_label3 = Label(self.frame_4, text=" ", bg="#E0FFFF")
            self.resultado_label3.place(relx=0.08, rely=0.2)

        if hasattr(self, 'frame_5'):
            # Label de resultados 
            self.resultado_label4 = Label(self.frame_6, text=" ", bg="#E0FFFF")
            self.resultado_label4.place(relx=0.08, rely=0.2)

        if hasattr(self, 'frame_7'):

            self.resultado_label5 = Label(self.frame_8, text=" ", bg="#E0FFFF")
            self.resultado_label5.place(relx=0.08, rely=0.2)

        if hasattr(self, 'frame_9'):
            self.resultado_label6 = Label(self.frame_10, text=" ", bg="#E0FFFF")
            self.resultado_label6.place(relx=0.08, rely=0.2)

        if hasattr(self,'frame_11'):
            self.resultado_label7 = Label(self.frame_12, text=" ", bg="#E0FFFF")
            self.resultado_label7.place(relx=0.08, rely=0.2)
        
        if hasattr(self, 'frame_13'):
            self.resultado_label8 = Label(self.frame_14, text=" ", bg="#E0FFFF")
            self.resultado_label8.place(relx=0.08, rely=0.2)

        if hasattr(self, 'frame_15'):
            self.resultado_label9 = Label(self.frame_16, text=" ", bg="#E0FFFF")
            self.resultado_label9.place(relx=0.08, rely=0.2)

        if hasattr(self, 'frame_17'):
            self.resultado_label10 = Label(self.frame_17, text=" ", bg="#E0FFFF")
            self.resultado_label10.place(relx=0.08, rely=0.2)

            self.resultado_label11 = Label(self.frame_18, text=" ", bg="#E0FFFF")
            self.resultado_label11.place(relx=0.08, rely=0.2)

    def calculos(self):
        if hasattr(self, 'frame_1'):
            # Converte as entradas em valores númericos
            tmp1 = float(self.calc_tem1.get())
            umd1 = float(self.calc_um1.get())
            tmp2 = float(self.calc_tem2.get())
            umd2 = float(self.calc_um2.get())
            att = float(self.calc_alt.get())

            # Definir o sistema de unidades SI ou IP
            psychrolib.SetUnitSystem(psychrolib.SI)

            # Definir as variáveis conhecidas
            self.temperatura_bulbo_seco = tmp1  # em graus Celsius
            self.altitude = att  # em metros
            umit_rel = umd1
            self.umidade_relativa = umit_rel / 100

            self.temperatura_bulbo_seco2 = tmp2
            umit_rel2 = umd2
            self.umidade_relativa2 = umit_rel2 / 100

            # Calcular a pressão atmosférica a partir da altitude
            self.pressao_atmosferica = psychrolib.GetStandardAtmPressure(self.altitude)
            self.pressao_atmosferica = round(self.pressao_atmosferica, 2)

            # Calcular a temperatura de bulbo úmido a partir da temperatura de bulbo seco e da umidade relativa
            self.temperatura_bulbo_umido = psychrolib.GetTWetBulbFromRelHum(self.temperatura_bulbo_seco, self.umidade_relativa,
                                                                    self.pressao_atmosferica)
            self.temperatura_bulbo_umido = round(self.temperatura_bulbo_umido, 2)

            # Calcular a umidade absoluta a partir da temperatura de bulbo seco e da umidade relativa
            self.umidade_absoluta = psychrolib.GetHumRatioFromRelHum(self.temperatura_bulbo_seco, self.umidade_relativa,
                                                                self.pressao_atmosferica)
            self.umidade_absoluta = round(self.umidade_absoluta, 7)

            # Calcular o ponto de orvalho a partir da temperatura de bulbo seco e da umidade relativa
            self.ponto_orvalho = psychrolib.GetTDewPointFromRelHum(self.temperatura_bulbo_seco, self.umidade_relativa)
            self.ponto_orvalho = round(self.ponto_orvalho, 2)

            # Calcular a pressão atmosférica a partir da altitude
            self.pressao_atmosferica2 = psychrolib.GetStandardAtmPressure(self.altitude)
            self.pressao_atmosferica2 = round(self.pressao_atmosferica2, 2)

            # Calcular a temperatura de bulbo úmido a partir da temperatura de bulbo seco e da umidade relativa
            self.temperatura_bulbo_umido2 = psychrolib.GetTWetBulbFromRelHum(self.temperatura_bulbo_seco2, self.umidade_relativa2,
                                                                        self.pressao_atmosferica2)
            self.temperatura_bulbo_umido2 = round(self.temperatura_bulbo_umido2, 2)

            # Calcular a umidade absoluta a partir da temperatura de bulbo seco e da umidade relativa
            self.umidade_absoluta2 = psychrolib.GetHumRatioFromRelHum(self.temperatura_bulbo_seco2, self.umidade_relativa2,
                                                                self.pressao_atmosferica2)
            self.umidade_absoluta2 = round(self.umidade_absoluta2, 7)

            # Calcular o ponto de orvalho a partir da temperatura de bulbo seco e da umidade relativa
            self.ponto_orvalho2 = psychrolib.GetTDewPointFromRelHum(self.temperatura_bulbo_seco2, self.umidade_relativa2)
            self.ponto_orvalho2 = round(self.ponto_orvalho2, 2)

    def calculos2(self):
        if hasattr(self, 'frame_3'):
            if self.item_selecionado1 == "Claro":
                if self.pareden == "Parede Norte":
                    self.dt1 = 5
                else:
                    self.dt1 = 5.3
            elif self.item_selecionado1 == "Médio":
                if self.pareden == "Parede Norte":
                    self.dt1 = 5.5
                else:
                    self.dt1 = 8.3
            else:
                if self.pareden == "Parede Norte":
                    self.dt1 = 8.3
                else:
                    self.dt1 = 12.5

            if self.item_selecionado2 == "Claro":
                if self.paredes == "Parede Sul":
                    self.dt2 = 0
                else:
                    self.dt2 = 2.8
            elif self.item_selecionado2 == "Médio":
                if self.paredes == "Parede Sul":
                    self.dt2 = 0
                else:
                    self.dt2 = 5.6
            else:
                if self.paredes == "Parede Sul":
                    self.dt2 = 0
                else:
                    self.dt2 = 8.3

            if self.item_selecionado3 == "Claro":
                if self.paredel == "Parede Leste":
                    self.dt3 = 5.5
                else:
                    self.dt3 = 5.3
            elif self.item_selecionado3 == "Médio":
                if self.paredel == "Parede Leste":
                    self.dt3 = 11.1
                else:
                    self.dt3 = 8.3
            else:
                if self.paredel == "Parede Leste":
                    self.dt3 = 16.6
                else:
                    self.dt3 = 12.5

            if self.item_selecionado4 == "Claro":
                if self.paredeo == "Parede Oeste":
                    self.dt4 = 5.5
                else:
                    self.dt4 = 2.8
            elif self.item_selecionado4 == "Médio":
                if self.paredeo == "Parede Oeste":
                    self.dt4 = 11.1
                else:
                    self.dt4 = 5.6
            else:
                if self.paredeo == "Parede Oeste":
                    self.dt4 = 16.6
                else:
                    self.dt4 = 8.3

            if self.item_selecionado5 == "Sim":
                self.op1 = 1
            else:
                self.op1 = 0

            if self.item_selecionado6 == "Sim":
                self.op2 = 1
            else:
                self.op2 = 0

            if self.item_selecionado7 == "Sim":
                self.op3 = 1
            else:
                self.op3 = 0

            if self.item_selecionado8 == "Sim":
                self.op4 = 1
            else:
                self.op4 = 0

            if self.item_selecionado9 == "Tij. maciços (14 cm)= 10 tij. + 2 revest.":
                self.cu1 = 2.88
            elif self.item_selecionado9 == "Tij. maciços ( 24 cm) = 20 tij. + 2 revest.":
                self.cu1 = 1.95
            elif self.item_selecionado9 == "Tij. Furados ( 14 cm) = 10 tij. + 2 revest.":
                self.cu1 = 2.59
            else:
                self.cu1 = 1.90

            if self.item_selecionado10 == "Tij. maciços (14 cm)= 10 tij. + 2 revest.":
                self.cu2 = 2.88
            elif self.item_selecionado10 == "Tij. maciços ( 24 cm) = 20 tij. + 2 revest.":
                self.cu2 = 1.95
            elif self.item_selecionado10 == "Tij. Furados ( 14 cm) = 10 tij. + 2 revest.":
                self.cu2 = 2.59
            else:
                self.cu2 = 1.90

            if self.item_selecionado11 == "Tij. maciços (14 cm)= 10 tij. + 2 revest.":
                self.cu3 = 2.88
            elif self.item_selecionado11 == "Tij. maciços ( 24 cm) = 20 tij. + 2 revest.":
                self.cu3 = 1.95
            elif self.item_selecionado11 == "Tij. Furados ( 14 cm) = 10 tij. + 2 revest.":
                self.cu3 = 2.59
            else:
                self.cu3 = 1.90

            if self.item_selecionado12 == "Tij. maciços (14 cm)= 10 tij. + 2 revest.":
                self.cu4 = 2.88
            elif self.item_selecionado12 == "Tij. maciços ( 24 cm) = 20 tij. + 2 revest.":
                self.cu4 = 1.95
            elif self.item_selecionado12 == "Tij. Furados ( 14 cm) = 10 tij. + 2 revest.":
                self.cu4 = 2.59
            else:
                self.cu4 = 1.90


            self.pedirce = float(self.pedirc.get())
            self.comp1e = float(self.comp1.get())
            self.comp2e = float(self.comp2.get())
            self.comp3e = float(self.comp3.get())
            self.comp4e = float(self.comp4.get())

            self.cargan = (self.dt1+self.result_t)*self.op1*self.cu1*self.pedirce*self.comp1e
            self.cargas = (self.dt2+self.result_t)*self.op2*self.cu2*self.pedirce*self.comp2e
            self.cargal = (self.dt3+self.result_t)*self.op3*self.cu3*self.pedirce*self.comp3e
            self.cargao = (self.dt4+self.result_t)*self.op4*self.cu4*self.pedirce*self.comp4e

            self.cargaext = self.cargan + self.cargas + self.cargal + self.cargao
            print("Carga externa :", self.cargaext)
      
    def calculos3(self):
        if hasattr(self, 'frame_5'):
            if self.item_selecionado13 == "Divisórias":
                self.dv1 = 5.5
            elif self.item_selecionado13 == "Divisórias Junto de Cozinha, lavandeirias ou aquecedores":
                self.dv1 = 13,8
            else:
                self.dv1 = 0
            
            if self.item_selecionado17 == "Tijolos maciços (14 cm)= 10 tijolos + 2 revestimentos":
                self.sdv1 = 2.29
            elif self.item_selecionado17 == "Tijolos maciços (10 cm) = 6 tijolos + 2 revestimentos":
                self.sdv1 = 2.68
            elif self.item_selecionado17 == "Tijolos maciços ( 24 cm) = 20 tijolos + 2 revestimentos":
                self.sdv1 = 1.66
            elif self.item_selecionado17 == "Tijolos Furados (10 cm) = 6 tijolos + 2 revestimentos":
                self.sdv1 = 2.54
            elif self.item_selecionado17 == "Tijolos Furados ( 14 cm) = 10 tijolos + 2 revestimentos":
                self.sdv1 = 2.10
            elif self.item_selecionado17 == "Tijolos Furados ( 24 cm) = 20 tijolos + 2 revestimentos":
                self.sdv1 = 1.61
            else:
                self.sdv1 = 0

            if self.item_selecionado14 == "Nas divisórias":
                self.dv2 = 5.5
            elif self.item_selecionado14 == "Vitrinas de lojas com grande carga de luz":
                self.dv2 = 16.6
            else:
                self.dv2 = 0

            if self.item_selecionado18 == "De vidros Comuns":
                self.sdv2 = 5.18
            elif self.item_selecionado18 == "Vidros Duplos":
                self.sdv2 = 3.13
            elif self.item_selecionado18 == "Vidros Triplos":
                self.sdv2 = 1.66
            else:
                self.sdv2 = 0

            if self.item_selecionado15 == "Sobre recintos não condicionados":
                self.dv3 = 5.5
            elif self.item_selecionado15 == "Do térreo":
                self.dv3 = 0
            elif self.item_selecionado15 == "Sobre Porão":
                self.dv3 = 0
            elif self.item_selecionado15 == "Sobre Porão com cozinha, lavandeirias ou aquecedores":
                self.dv3 = 19.4
            elif self.item_selecionado15 == "Sobre espaços ventilados":
                self.dv3 = 9.4
            else:
                self.dv3 = 0

            if self.item_selecionado16 == "Sobre espaços não condicionados":
                self.dv4 = 5.5
            elif self.item_selecionado16 == "Sobre espaços com cozinhas, lavandeirias e aquecedores":
                self.dv4 = 11.1
            else:
                self.dv4 = 9.4

            self.div_parcomp = float(self.pared_ent.get())
            self.div_parlarg = float(self.pared2_ent.get())
            self.div_vidcomp = float(self.vidr_ent.get())
            self.div_vidlar = float(self.vidr2_ent.get())
            self.div_piscomp = float(self.piso_ent.get())
            self.div_pislar = float(self.piso2_ent.get())
            self.div_tetcomp = float(self.teto_ent.get())
            self.div_tetlar = float(self.teto2_ent.get())

            self.divpar = (self.dv1+self.result_t)*self.div_parcomp*self.div_parlarg*self.sdv1
            self.divvid = (self.dv2+self.result_t)*self.div_vidcomp*self.div_vidlar*self.sdv2
            self.divpis = (self.dv3+self.result_t)*self.div_piscomp*self.div_pislar
            self.divtet = (self.dv4+self.result_t)*self.div_tetcomp*self.div_tetlar

            self.cargadiv = self.divpar + self.divvid + self.divpis + self.divtet
            
    def calculos4(self):
        if hasattr(self, 'frame_7'):
            if self.item_selecionado19 == "Toldos ou Persianas Externas" and self.item_selecionado23 == "Esquadrias de Madeira":
                self.fs1 = 0.18
            elif self.item_selecionado19 == "Toldos ou Persianas Externas" and self.item_selecionado23 == "Esquadrias de Metal":
                self.fs1 = 0.2
            elif self.item_selecionado19 == "Persianas Internas e Reflexoras" and self.item_selecionado23 == "Esquadrias de Madeira":
                self.fs1 = 0.58
            elif self.item_selecionado19 == "Persianas Internas e Reflexoras" and self.item_selecionado23 == "Esquadrias de Metal":
                self.fs1 = 0.67
            elif self.item_selecionado19 == "Cortinas Internas Brancas" and self.item_selecionado23 == "Esquadrias de Madeira":
                self.fs1 = 0.43
            elif self.item_selecionado19 == "Cortinas Internas Brancas" and self.item_selecionado23 == "Esquadrias de Metal":
                self.fs1 = 0.49
            elif self.item_selecionado19 == "Não Possui" and self.item_selecionado23 == "Esquadrias de Madeira":
                self.fs1 = 1
            elif self.item_selecionado19 == "Não Possui" and self.item_selecionado23 == "Esquadrias de Metal":
                self.fs1 = 1
            elif self.item_selecionado19 == "Não Possui" and self.item_selecionado23 == "Não possui":
                self.fs1 = 1
            elif self.item_selecionado19 == 'Toldos ou Persianas Externas' and self.item_selecionado23 == 'Não Possui':
                self.fs1 = ValueError
            elif self.item_selecionado19 == 'Persianas Internas e Reflexoras' and self.item_selecionado23 == 'Não Possui':
                self.fs1 = ValueError
            elif self.item_selecionado19 == 'Cortinas Internas Brancas' and self.item_selecionado23 == 'Não Possui':
                self.fs1 = ValueError
            
            if self.item_selecionado20 == "Toldos ou Persianas Externas" and self.item_selecionado24 == "Esquadrias de Madeira":
                self.fs2 = 0.18
            elif self.item_selecionado20 == "Toldos ou Persianas Externas" and self.item_selecionado24 == "Esquadrias de Metal":
                self.fs2 = 0.2
            elif self.item_selecionado20 == "Persianas Internas e Reflexoras" and self.item_selecionado24 == "Esquadrias de Madeira":
                self.fs2 = 0.58
            elif self.item_selecionado20 == "Persianas Internas e Reflexoras" and self.item_selecionado24 == "Esquadrias de Metal":
                self.fs2 = 0.67
            elif self.item_selecionado20 == "Cortinas Internas Brancas" and self.item_selecionado24 == "Esquadrias de Madeira":
                self.fs2 = 0.43
            elif self.item_selecionado20 == "Cortinas Internas Brancas" and self.item_selecionado24 == "Esquadrias de Metal":
                self.fs2 = 0.49
            elif self.item_selecionado20 == "Não Possui" and self.item_selecionado24 == "Esquadrias de Madeira":
                self.fs2 = 1
            elif self.item_selecionado20 == "Não Possui" and self.item_selecionado24 == "Esquadrias de Metal":
                self.fs2 = 1
            elif self.item_selecionado20 == "Não Possui" and self.item_selecionado24 == "Não possui":
                self.fs2 = 1
            elif self.item_selecionado20 == 'Toldos ou Persianas Externas' and self.item_selecionado24 == 'Não Possui':
                self.fs2 = ValueError
            elif self.item_selecionado20 == 'Persianas Internas e Reflexoras' and self.item_selecionado24 == 'Não Possui':
                self.fs2 = ValueError
            elif self.item_selecionado20 == 'Cortinas Internas Brancas' and self.item_selecionado24 == 'Não Possui':
                self.fs2 = ValueError
            
            if self.item_selecionado21 == "Toldos ou Persianas Externas" and self.item_selecionado25 == "Esquadrias de Madeira":
                self.fs3 = 0.18
            elif self.item_selecionado21 == "Toldos ou Persianas Externas" and self.item_selecionado25 == "Esquadrias de Metal":
                self.fs3 = 0.2
            elif self.item_selecionado21 == "Persianas Internas e Reflexoras" and self.item_selecionado25 == "Esquadrias de Madeira":
                self.fs3 = 0.58
            elif self.item_selecionado21 == "Persianas Internas e Reflexoras" and self.item_selecionado25 == "Esquadrias de Metal":
                self.fs3 = 0.67
            elif self.item_selecionado21 == "Cortinas Internas Brancas" and self.item_selecionado25 == "Esquadrias de Madeira":
                self.fs3 = 0.43
            elif self.item_selecionado21 == "Cortinas Internas Brancas" and self.item_selecionado25 == "Esquadrias de Metal":
                self.fs3 = 0.49
            elif self.item_selecionado21 == "Não Possui" and self.item_selecionado25 == "Esquadrias de Madeira":
                self.fs3 = 1
            elif self.item_selecionado21 == "Não Possui" and self.item_selecionado25 == "Esquadrias de Metal":
                self.fs3 = 1
            elif self.item_selecionado21 == "Não Possui" and self.item_selecionado25 == "Não possui":
                self.fs3 = 1
            elif self.item_selecionado21 == 'Toldos ou Persianas Externas' and self.item_selecionado25 == 'Não Possui':
                self.fs3 = ValueError
            elif self.item_selecionado21 == 'Persianas Internas e Reflexoras' and self.item_selecionado25 == 'Não Possui':
                self.fs3 = ValueError
            elif self.item_selecionado21 == 'Cortinas Internas Brancas' and self.item_selecionado25 == 'Não Possui':
                self.fs3 = ValueError

            if self.item_selecionado22 == "Toldos ou Persianas Externas" and self.item_selecionado26 == "Esquadrias de Madeira":
                self.fs4 = 0.18
            elif self.item_selecionado22 == "Toldos ou Persianas Externas" and self.item_selecionado26 == "Esquadrias de Metal":
                self.fs4 = 0.2
            elif self.item_selecionado22 == "Persianas Internas e Reflexoras" and self.item_selecionado26 == "Esquadrias de Madeira":
                self.fs4 = 0.58
            elif self.item_selecionado22 == "Persianas Internas e Reflexoras" and self.item_selecionado26 == "Esquadrias de Metal":
                self.fs4 = 0.67
            elif self.item_selecionado22 == "Cortinas Internas Brancas" and self.item_selecionado26 == "Esquadrias de Madeira":
                self.fs4 = 0.43
            elif self.item_selecionado22 == "Cortinas Internas Brancas" and self.item_selecionado26 == "Esquadrias de Metal":
                self.fs4 = 0.49
            elif self.item_selecionado22 == "Não Possui" and self.item_selecionado26 == "Esquadrias de Madeira":
                self.fs4 = 1
            elif self.item_selecionado22 == "Não Possui" and self.item_selecionado26 == "Esquadrias de Metal":
                self.fs4 = 1
            elif self.item_selecionado22 == "Não Possui" and self.item_selecionado26 == "Não possui":
                self.fs4 = 1 
            elif self.item_selecionado22 == 'Toldos ou Persianas Externas' and self.item_selecionado26 == 'Não Possui':
                self.fs4 = ValueError
            elif self.item_selecionado22 == 'Persianas Internas e Reflexoras' and self.item_selecionado26 == 'Não Possui':
                self.fs4 = ValueError
            elif self.item_selecionado22 == 'Cortinas Internas Brancas' and self.item_selecionado26 == 'Não Possui':
                self.fs4 = ValueError
            

            self.jann = float(self.janen_ent.get())
            self.jann2 = float(self.janen2_ent.get())
            self.jann3 = float(self.janen3_ent.get())
            self.jans = float(self.janes_ent.get())
            self.jans2 = float(self.janes2_ent.get())
            self.jans3 = float(self.janes3_ent.get())
            self.janl = float(self.janel_ent.get())
            self.janl2 = float(self.janel2_ent.get())
            self.janl3 = float(self.janel3_ent.get())
            self.jano = float(self.janeo_ent.get())
            self.jano2 = float(self.janeo2_ent.get())
            self.jano3 = float(self.janeo3_ent.get())

            self.carg_jann = self.jann*self.jann2*self.jann3*self.fs1
            self.carg_jans = self.jans*self.jans2*self.jans3*self.fs2
            self.carg_janl = self.janl*self.janl2*self.janl3*self.fs3
            self.carg_jano = self.jano*self.jano2*self.jano3*self.fs4

            self.carg_jant = self.carg_jann+self.carg_jans+self.carg_janl+self.carg_jano

            print(f"O valor é", self.carg_jann,"e",self.carg_jans,"e",self.carg_janl,"e",self.carg_jano,"e por final",self.carg_jant)             

    def cpe(self):
        if self.item_selecionado27 == "Sentado no Teatro":
            self.cps1 = 65
            self.cpl1 = 30
        elif self.item_selecionado27 == "Sentado no Teatro, noite":
            self.cps1 = 70
            self.cpl1 = 35
        elif self.item_selecionado27 == "Sentado Trabalho Leve":
            self.cps1 = 70
            self.cpl1 = 45
        elif self.item_selecionado27 == "Atividades moderada em trabalho de escritório":
            self.cps1 = 75
            self.cpl1 = 55
        elif self.item_selecionado27 == "Parado em pé, trabalho moderado, caminhando":
            self.cps1 = 75
            self.cpl1 = 55
        elif self.item_selecionado27 == "Caminhando, parado em pé":
            self.cps1 = 75
            self.cpl1 = 70
        elif self.item_selecionado27 == "Trabalho sedentário":
            self.cps1 = 80
            self.cpl1 = 80
        elif self.item_selecionado27 == "Trabalho leve em bancada":
            self.cps1 = 80
            self.cpl1 = 140
        elif self.item_selecionado27 == "Dançando moderadamente":
            self.cps1 = 90
            self.cpl1 = 160
        elif self.item_selecionado27 == "Caminhando 4,8 Km/h, trabalho leve em maquina operatriz":
            self.cps1 = 110
            self.cpl1 = 185
        elif self.item_selecionado27 == "Jogando boliche":
            self.cps1 = 170
            self.cpl1 = 255
        elif self.item_selecionado27 == "Trabalho Pesado":
            self.cps1 = 170
            self.cpl1 = 255
        elif self.item_selecionado27 == "Trabalho Pesado em maquina operatriz, Carregando Carga":
            self.cps1 = 185
            self.cpl1 = 285
        elif self.item_selecionado27 == "Praticando Esportes":
            self.cps1 = 210
            self.cpl1 = 315
        elif self.item_selecionado27 == "Nenhum":
            self.cps1 = 0
            self.cpl1 = 0   

    def calculos5(self):
        if hasattr(self, 'frame_9'):
        
            self.resultado0 = []
            self.soma_total0 = 0
            self.cs0_total = 0
            self.cl0_total = 0
            self.total_pes = 0
            for item in self.lista_selecionados0:
                valor_a = float(item[0])
                valor_b = float(item[1])
                valor_c = float(item[2])
                self.multiplicacao0 = ((valor_a + (valor_b * 0.85) + (valor_c * 0.75)) * item[4]) + ((valor_a + (valor_b * 0.85) + (valor_c * 0.75)) * item[5])
                self.carg_st = (valor_a * item[4]) + (valor_b * item[4] * 0.85) + (valor_c * item[4] * 0.75)
                self.carg_lt = (valor_a * item[5]) + (valor_b * item[5] * 0.85) + (valor_c * item[5] * 0.75)
                self.resultado0.append((valor_a, valor_b, valor_c, item[3], item[4], item[5], self.multiplicacao0))
                self.cs0_total += self.carg_st
                self.cl0_total += self.carg_lt
                self.soma_total0 += self.multiplicacao0
                self.total_pes += valor_a + valor_b +valor_c
            for res in self.resultado0:
                print(f"Selecionado: {res[3]}, Valor A: {res[0]}, Valor B: {res[1]}, Valor C: {res[2]} Multiplicação: {res[6]} W\nCps1 {res[4]} e Cpl1 {res[5]}")
            print(f"Calor Sensível Total: {self.cs0_total} W.\nCalor Latente Total: {self.cl0_total} W.\nCalor Total: {self.soma_total0} W")
            print(f"Total de pessoas:{self.total_pes}")

    def calculos6(self):
        if hasattr(self, 'frame_11'):
            self.resultado = []
            self.soma_total = 0
            self.cs_total = 0
            self.cl_total = 0
            for item in self.lista_selecionados:
                self.multiplicacao = float(item[1]) * (float(item[2]) + float(item[3]))
                self.calors = float(item[1]) * float(item[2])
                self.calorl = float(item[1]) * float(item[3])
                self.resultado.append((item[0], item[1], item[2], item[3], self.multiplicacao))
                self.cs_total += self.calors
                self.cl_total += self.calorl
                self.soma_total += self.multiplicacao
            for res in self.resultado:
                print(f"Selecionado: {res[0]}, Valor A: {res[1]}, Valor B: {res[2]}, Valor C: {res[3]} Multiplicação: {res[4]} W")
            print(f"Calor Sensível Total: {self.calors} W.\nCalor Latente Total: {self.calorl} W.\nCalor Total: {self.soma_total} W")
            
    def calculos7(self):
        if hasattr(self, 'frame_13'):
            # Nível 1
            if self.item_selecionado28 == "Supermecado de Alto Padrão" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Supermecado de Padrão Médio" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Supermecado Popular" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Mall de Centros Comerciais" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Lojas (exceto abaixo)" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.6
            elif self.item_selecionado28 == "Salão de Beleza e/ou Barbearia" and self.item_selecionado29 == "Nível 1":
                self.fa = 10
                self.fp = 0.6
            elif self.item_selecionado28 == "Animais de estimação" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.9
            elif self.item_selecionado28 == "Lavanderia 'self-service" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Hall do edifício, recepção" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Escritórios de Diretoria" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Escritório com Baixa Densidade" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Escritório com Média Densidade" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Escritório com Alta Densidade" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Sala de Reunião" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "CPD (exceto impressoras)" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Sala de Impressoras, Copiadoras" and self.item_selecionado29 == "Nível 1":
                self.fa = 0
                self.fp = 0
            elif self.item_selecionado28 == "Sala de Digitação" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "'Call Center'" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.6
            elif self.item_selecionado28 == "Bancos (área do público)" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.6
            elif self.item_selecionado28 == "Caixa Forte" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.6
            elif self.item_selecionado28 == "Aeroporto - Saguão" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Aeroporto - Sala de Embarque" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Biblioteca" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.6
            elif self.item_selecionado28 == "Museu, Galeria de Arte" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Local de Culto" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Legislativo - Plenário" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório - Lobby" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório e Platéia" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório -Palco" and self.item_selecionado29 == "Nível 1":
                self.fa = 5
                self.fp = 0.3
            elif self.item_selecionado28 == "Tribunal - Sala de Audiências" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Boliche - Área do Público" and self.item_selecionado29 == "Nível 1":
                self.fa = 5
                self.fp = 0.6
            elif self.item_selecionado28 == "Ginásio Coberto (Área do Público)" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Ginásio Coberto (Quadra)" and self.item_selecionado29 == "Nível 1":
                self.fa = 0
                self.fp = 0.3
            elif self.item_selecionado28 == "Piscina Coberta" and self.item_selecionado29 == "Nível 1":
                self.fa = 0
                self.fp = 2.4
            elif self.item_selecionado28 == "'Fitness Center' - Aeróbica" and self.item_selecionado29 == "Nível 1":
                self.fa = 10
                self.fp = 0.3
            elif self.item_selecionado28 == "'Fitness Center' - Aparelhos" and self.item_selecionado29 == "Nível 1":
                self.fa = 5
                self.fp = 0.6
            elif self.item_selecionado28 == "Sala de Aula" and self.item_selecionado29 == "Nível 1":
                self.fa = 5
                self.fp = 0.6
            elif self.item_selecionado28 == "Laboratório de Informática" and self.item_selecionado29 == "Nível 1":
                self.fa = 5
                self.fp = 0.6
            elif self.item_selecionado28 == "Laboratório de Ciências" and self.item_selecionado29 == "Nível 1":
                self.fa = 5
                self.fp = 0.9
            elif self.item_selecionado28 == "Apartamento de Hóspedes" and self.item_selecionado29 == "Nível 1":
                self.fa = 5.5
                self.fp = 0
            elif self.item_selecionado28 == "Banheiro Privativo" and self.item_selecionado29 == "Nível 1":
                self.fa = 0
                self.fp = 0
            elif self.item_selecionado28 == "Lobby, sala de estar" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.3
            elif self.item_selecionado28 == "Sala de Convenções" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Dormitório Coletivo" and self.item_selecionado29 == "Nível 1":
                self.fa = 2.5
                self.fp = 0.3
            elif self.item_selecionado28 == "Restaurantes - Salão de Refeições" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.9
            elif self.item_selecionado28 == "Bar, Salão de Coquetel" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.9
            elif self.item_selecionado28 == "Cafeteria, Lanchonete, Refeitório" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.9
            elif self.item_selecionado28 == "Salão de Jogos" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.9
            elif self.item_selecionado28 == "Discoteca, Danceteria" and self.item_selecionado29 == "Nível 1":
                self.fa = 10
                self.fp = 0.3
            elif self.item_selecionado28 == "Jogos Eletrônicos" and self.item_selecionado29 == "Nível 1":
                self.fa = 3.8
                self.fp = 0.9
            # Nível 2
            elif self.item_selecionado28 == "Supermecado de Alto Padrão" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Supermecado de Padrão Médio" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Supermecado Popular" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Mall de Centros Comerciais" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Lojas (exceto abaixo)" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.8
            elif self.item_selecionado28 == "Salão de Beleza e/ou Barbearia" and self.item_selecionado29 == "Nível 2":
                self.fa = 12.5
                self.fp = 0.8
            elif self.item_selecionado28 == "Animais de estimação" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 1.1
            elif self.item_selecionado28 == "Lavanderia 'self-service" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Hall do edifício, recepção" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Escritórios de Diretoria" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Escritório com Baixa Densidade" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Escritório com Média Densidade" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Escritório com Alta Densidade" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Sala de Reunião" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "CPD (exceto impressoras)" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Sala de Impressoras, Copiadoras" and self.item_selecionado29 == "Nível 2":
                self.fa = 0
                self.fp = 0
            elif self.item_selecionado28 == "Sala de Digitação" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "'Call Center'" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.8
            elif self.item_selecionado28 == "Bancos (área do público)" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Caixa Forte" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Aeroporto - Saguão" and self.item_selecionado29 == "Nível 2":
                self.fa = 5.3
                self.fp = 0.4
            elif self.item_selecionado28 == "Aeroporto - Sala de Embarque" and self.item_selecionado29 == "Nível 2":
                self.fa = 5.3
                self.fp = 0.4
            elif self.item_selecionado28 == "Biblioteca" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.5
                self.fp = 0.8
            elif self.item_selecionado28 == "Museu, Galeria de Arte" and self.item_selecionado29 == "Nível 2":
                self.fa = 5.3
                self.fp = 0.4
            elif self.item_selecionado28 == "Local de Culto" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.5
                self.fp = 0.4
            elif self.item_selecionado28 == "Legislativo - Plenário" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.5
                self.fp = 0.4
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório - Lobby" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.5
                self.fp = 0.4
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório e Platéia" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.5
                self.fp = 0.4
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório -Palco" and self.item_selecionado29 == "Nível 2":
                self.fa = 6.3
                self.fp = 0.4
            elif self.item_selecionado28 == "Tribunal - Sala de Audiências" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.5
                self.fp = 0.4
            elif self.item_selecionado28 == "Boliche - Área do Público" and self.item_selecionado29 == "Nível 2":
                self.fa = 6,3
                self.fp = 0.8
            elif self.item_selecionado28 == "Ginásio Coberto (Área do Público)" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Ginásio Coberto (Quadra)" and self.item_selecionado29 == "Nível 2":
                self.fa = 0
                self.fp = 0.4
            elif self.item_selecionado28 == "Piscina Coberta" and self.item_selecionado29 == "Nível 2":
                self.fa = 0
                self.fp = 3
            elif self.item_selecionado28 == "'Fitness Center' - Aeróbica" and self.item_selecionado29 == "Nível 2":
                self.fa = 12.5
                self.fp = 0.4
            elif self.item_selecionado28 == "'Fitness Center' - Aparelhos" and self.item_selecionado29 == "Nível 2":
                self.fa = 6.3
                self.fp = 0.8
            elif self.item_selecionado28 == "Sala de Aula" and self.item_selecionado29 == "Nível 2":
                self.fa = 6.3
                self.fp = 0.8
            elif self.item_selecionado28 == "Laboratório de Informática" and self.item_selecionado29 == "Nível 2":
                self.fa = 6.3
                self.fp = 0.8
            elif self.item_selecionado28 == "Laboratório de Ciências" and self.item_selecionado29 == "Nível 2":
                self.fa = 6.3
                self.fp = 1.1
            elif self.item_selecionado28 == "Apartamento de Hóspedes" and self.item_selecionado29 == "Nível 2":
                self.fa = 6.9
                self.fp = 0
            elif self.item_selecionado28 == "Banheiro Privativo" and self.item_selecionado29 == "Nível 2":
                self.fa = 0
                self.fp = 0
            elif self.item_selecionado28 == "Lobby, sala de estar" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 0.4
            elif self.item_selecionado28 == "Sala de Convenções" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Dormitório Coletivo" and self.item_selecionado29 == "Nível 2":
                self.fa = 3.1
                self.fp = 0.4
            elif self.item_selecionado28 == "Restaurantes - Salão de Refeições" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 1.1
            elif self.item_selecionado28 == "Bar, Salão de Coquetel" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 1.1
            elif self.item_selecionado28 == "Cafeteria, Lanchonete, Refeitório" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 1.1
            elif self.item_selecionado28 == "Salão de Jogos" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 1.1
            elif self.item_selecionado28 == "Discoteca, Danceteria" and self.item_selecionado29 == "Nível 2":
                self.fa = 12.5
                self.fp = 0.4
            elif self.item_selecionado28 == "Jogos Eletrônicos" and self.item_selecionado29 == "Nível 2":
                self.fa = 4.8
                self.fp = 1.1
            # Nível 3
            elif self.item_selecionado28 == "Supermecado de Alto Padrão" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Supermecado de Padrão Médio" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Supermecado Popular" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Mall de Centros Comerciais" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Lojas (exceto abaixo)" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.9
            elif self.item_selecionado28 == "Salão de Beleza e/ou Barbearia" and self.item_selecionado29 == "Nível 3":
                self.fa = 15
                self.fp = 0.9
            elif self.item_selecionado28 == "Animais de estimação" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 1.4
            elif self.item_selecionado28 == "Lavanderia 'self-service" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Hall do edifício, recepção" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Escritórios de Diretoria" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Escritório com Baixa Densidade" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Escritório com Média Densidade" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Escritório com Alta Densidade" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Sala de Reunião" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "CPD (exceto impressoras)" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Sala de Impressoras, Copiadoras" and self.item_selecionado29 == "Nível 3":
                self.fa = 0
                self.fp = 0
            elif self.item_selecionado28 == "Sala de Digitação" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "'Call Center'" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.9
            elif self.item_selecionado28 == "Bancos (área do público)" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Caixa Forte" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Aeroporto - Saguão" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Aeroporto - Sala de Embarque" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Biblioteca" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.9
            elif self.item_selecionado28 == "Museu, Galeria de Arte" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Local de Culto" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Legislativo - Plenário" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório - Lobby" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório e Platéia" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Teatro, Cinema, Auditório -Palco" and self.item_selecionado29 == "Nível 3":
                self.fa = 7.5
                self.fp = 0.5
            elif self.item_selecionado28 == "Tribunal - Sala de Audiências" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Boliche - Área do Público" and self.item_selecionado29 == "Nível 3":
                self.fa = 7.5
                self.fp = 0.9
            elif self.item_selecionado28 == "Ginásio Coberto (Área do Público)" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.9
            elif self.item_selecionado28 == "Ginásio Coberto (Quadra)" and self.item_selecionado29 == "Nível 3":
                self.fa = 0
                self.fp = 0.5
            elif self.item_selecionado28 == "Piscina Coberta" and self.item_selecionado29 == "Nível 3":
                self.fa = 0
                self.fp = 3.6
            elif self.item_selecionado28 == "'Fitness Center' - Aeróbica" and self.item_selecionado29 == "Nível 3":
                self.fa = 15
                self.fp = 0.5
            elif self.item_selecionado28 == "'Fitness Center' - Aparelhos" and self.item_selecionado29 == "Nível 3":
                self.fa = 7.5
                self.fp = 0.9
            elif self.item_selecionado28 == "Sala de Aula" and self.item_selecionado29 == "Nível 3":
                self.fa = 7.5
                self.fp = 0.9
            elif self.item_selecionado28 == "Laboratório de Informática" and self.item_selecionado29 == "Nível 3":
                self.fa = 7.5
                self.fp = 0.9
            elif self.item_selecionado28 == "Laboratório de Ciências" and self.item_selecionado29 == "Nível 3":
                self.fa = 7.5
                self.fp = 1.4
            elif self.item_selecionado28 == "Apartamento de Hóspedes" and self.item_selecionado29 == "Nível 3":
                self.fa = 10.3
                self.fp = 0
            elif self.item_selecionado28 == "Banheiro Privativo" and self.item_selecionado29 == "Nível 3":
                self.fa = 0
                self.fp = 0
            elif self.item_selecionado28 == "Lobby, sala de estar" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 0.5
            elif self.item_selecionado28 == "Sala de Convenções" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Dormitório Coletivo" and self.item_selecionado29 == "Nível 3":
                self.fa = 3.8
                self.fp = 0.5
            elif self.item_selecionado28 == "Restaurantes - Salão de Refeições" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 1.4
            elif self.item_selecionado28 == "Bar, Salão de Coquetel" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 1.4
            elif self.item_selecionado28 == "Cafeteria, Lanchonete, Refeitório" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 1.4
            elif self.item_selecionado28 == "Salão de Jogos" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 1.4
            elif self.item_selecionado28 == "Discoteca, Danceteria" and self.item_selecionado29 == "Nível 3":
                self.fa = 15
                self.fp = 0.5
            elif self.item_selecionado28 == "Jogos Eletrônicos" and self.item_selecionado29 == "Nível 3":
                self.fa = 5.7
                self.fp = 1.4
        
        self.ocupp = float(self.label_ocup.get())
        self.area_total = ((self.comp1e+self.comp2e)/2)*((self.comp3e+self.comp4e)/2)
        self.area_util = self.area_total - self.area_total*(self.ocupp/100)
        self.vaz_efex = (self.fp*self.total_pes + self.fa*self.area_util)/1000
        self.vaz_efzo = self.vaz_efex/.5
        self.calsen_ven = .288*(self.vaz_efex)*self.result_t*3600
        self.callat_ven = .72*self.vaz_efzo*(self.umidade_absoluta - self.umidade_absoluta2)*36000
        self.caltot_ven = self.callat_ven + self.calsen_ven

    def calculos8(self):
        if hasattr(self, 'frame_15'):
            if self.item_selecionado30 == "Comum" and self.item_selecionado31 == "Mal Ajustada":
                self.qjan = 3
            elif self.item_selecionado30 == "Comum" and self.item_selecionado31 == "Bem Ajustada":
                self.qjan = 3
            elif self.item_selecionado30 == "Basculante" and self.item_selecionado31 == "Mal Ajustada":
                self.qjan = 3
            elif self.item_selecionado30 == "Basculante" and self.item_selecionado31 == "Bem Ajustada":
                self.qjan = 3
            elif self.item_selecionado30 == "Guilhotina com caxilho de madeira" and self.item_selecionado31 == "Bem Ajustada":
                self.qjan = 2
            elif self.item_selecionado30 == "Guilhotina com caxilho de madeira" and self.item_selecionado31 == "Mal Ajustada":
                self.qjan = 6.5
            elif self.item_selecionado30 == "Guilhotina com caxilho metálico" and self.item_selecionado31 == "Bem Ajustada":
                self.qjan = 1.8
            elif self.item_selecionado30 == "Guilhotina com caxilho metálico" and self.item_selecionado31 == "Bem Ajustada":
                self.qjan = 4.5
            
            if self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado33 == "Mal Ajustada":
                self.qport = 13
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado33 == "Mal Ajustada":
                self.qport = 6.5
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado33 == "Mal Ajustada":
                self.qport = 13
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado33 == "Mal Ajustada":
                self.qport = 6.5

            if self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Barbearias":
                self.qrp = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Drogarias e Farmácias":
                self.qrp = 10
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Escritórios de Corretagem":
                self.qrp = 9
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Escritórios Privados":
                self.qrp = 4
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Escritórios em Geral":
                self.qrp = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Lojas de Cigarros":
                self.qrp = 32
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Lojas em Geral":
                self.qrp = 12
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Quartos de Hospitais":
                self.qrp = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Restaurantes":
                self.qrp = 3
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Salas de Chá ou Café":
                self.qrp = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Bancos":
                self.qrp = 11
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Barbearias":
                self.qrp = 9
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Drogarias e Farmácias":
                self.qrp = 12
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Escritórios de Corretagem":
                self.qrp = 9
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Escritórios Privados":
                self.qrp = 4
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Escritórios em Geral":
                self.qrp = 7
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Lojas de Cigarros":
                self.qrp = 51
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Lojas em Geral":
                self.qrp = 14
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Quartos de Hospitais":
                self.qrp = 7
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Restaurantes":
                self.qrp = 4
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Salas de Chá ou Café":
                self.qrp = 9
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Bancos":
                self.qrp = 14

            if self.item_selecionado32 == "Porta Vaivém 0,9 m":
                self.plar = 0.9
            else:
                self.plar = 1.8

            if self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Barbearias":
                self.apl = 9
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Drogarias e Farmácias":
                self.apl = 12
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Escritórios de Corretagem":
                self.apl = 9
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Escritórios Privados":
                self.apl = 4
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Escritórios em Geral":
                self.apl = 7
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Lojas de Cigarros":
                self.apl = 51
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Lojas em Geral":
                self.apl = 14
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Quartos de Hospitais":
                self.apl = 7
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Restaurantes":
                self.apl = 4
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Salas de Chá ou Café":
                self.apl = 9
            elif self.item_selecionado32 == "Porta Vaivém 0,9 m" and self.item_selecionado34 == "Bancos":
                self.apl = 14
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Barbearias":
                self.apl = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Drogarias e Farmácias":
                self.apl = 10
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Escritórios de Corretagem":
                self.apl = 9
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Escritórios Privados":
                self.apl = 4
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Escritórios em Geral":
                self.apl = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Lojas de Cigarros":
                self.apl = 32
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Lojas em Geral":
                self.apl = 12
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Quartos de Hospitais":
                self.apl = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Restaurantes":
                self.apl = 4
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Salas de Chá ou Café":
                self.apl = 7
            elif self.item_selecionado32 == "Porta Giratória 1,80 m" and self.item_selecionado34 == "Bancos":
                self.apl = 11
            

            self.qtdpor = float(self.label_qtdport.get())


            self.callateni = 0.72*((2*(self.jann + self.jann2 + self.jans + self.jans2 + self.janl + self.janl2 + self.jano+self.jano2)) + (2.1*self.plar*self.qtdpor))*(self.umidade_absoluta - self.umidade_absoluta2)*1000
            self.calseni = 0.288*((2*(self.jann + self.jann2 + self.jans + self.jans2 + self.janl + self.janl2 + self.jano+self.jano2)) + (2.1*self.plar*self.qtdpor))*(self.result_t)
            
            self.callatenp = 0.72*((self.total_pes*self.apl))*(self.umidade_absoluta - self.umidade_absoluta2)*1000
            self.calsenp = 0.288*((self.total_pes*self.apl))*(self.result_t)

            self.clti = self.callateni + self.callatenp
            self.csti = self.calseni + self.calsenp

            self.cti = self.clti + self.csti

    def calculos9(self):
        # Cálculo dos calores sensíveis e latente
        self.scals = (self.cargaext + self.cargadiv + self.carg_jant) + self.cs0_total + self.cs_total*0.86 + self.calsen_ven + self.csti
        self.scall = self.cl0_total + self.cl_total*0.86 + self.callat_ven + self.clti

        self.caltotal = self.scals + self.scall
        self.caltotal_up = self.caltotal + self.caltotal*0.1

        # Cálculo da vazão de ar com ar insulflado a 10°C
        self.v_ark1 = (self.cargaext + self.cargadiv + self.carg_jant)/(0.24*(self.temperatura_bulbo_seco2-10))
        self.v_ark2 = self.cs0_total*.86/(0.24*(self.temperatura_bulbo_seco2-10))
        self.v_ark3 = self.cs_total/(0.24*(self.temperatura_bulbo_seco2-10))
        self.v_ark4 = self.calsen_ven/(0.24*(self.temperatura_bulbo_seco2-10))
        self.v_ark5 = self.csti/(0.24*(self.temperatura_bulbo_seco2-10))
        self.v_art1 = self.v_ark1 + self.v_ark2 + self.v_ark3 + self.v_ark4 + self.v_ark5

        # Cálculo da vazão de ar com ar insulflado a 15°C
        self.v_ark6 = (self.cargaext + self.cargadiv + self.carg_jant)/(0.24*(self.temperatura_bulbo_seco2-15))
        self.v_ark7 = self.cs0_total*.86/(0.24*(self.temperatura_bulbo_seco2-15))
        self.v_ark8 = self.cs_total/(0.24*(self.temperatura_bulbo_seco2-15))
        self.v_ark9 = self.calsen_ven/(0.24*(self.temperatura_bulbo_seco2-15))
        self.v_ark10 = self.csti/(0.24*(self.temperatura_bulbo_seco2-15))
        self.v_art2 = self.v_ark6 + self.v_ark7 + self.v_ark8 + self.v_ark9 + self.v_ark10


        # Vazão de ar, água a ser retirada e RCS
        self.v_arm1 = self.v_art1/1.2466
        self.v_arm2 = self.v_art2/1.2466
        self.agret = self.scals/583
        self.rcs = self.scals/self.caltotal_up


    def printar_result(self):

        # Exibindo o resultado
        try:
            
            self.calculos()

            if hasattr(self,'frame_1'):
                self.resultado_label1.config(
                    text=f"Dados Externos:\n\nCidade: {self.calc_cid.get()}\nPressão atmosférica: {self.pressao_atmosferica} Pa\n"
                        f"Temperatura de bulbo seco: {self.temperatura_bulbo_seco} °C\n"
                        f"Temperatura de bulbo úmido: {self.temperatura_bulbo_umido} °C\n"
                        f"Umidade absoluta: {self.umidade_absoluta} g/kg\n"
                        f"Ponto de orvalho: {self.ponto_orvalho} °C", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                self.resultado_label2.config(
                    text=f"Dados Internos:\n\nPressão atmosférica: {self.pressao_atmosferica2} Pa\n"
                        f"Temperatura de bulbo seco: {self.temperatura_bulbo_seco2} °C\n"
                        f"Temperatura de bulbo úmido: {self.temperatura_bulbo_umido2} °C\n"
                        f"Umidade absoluta: {self.umidade_absoluta2} g/kg\n"
                        f"Ponto de orvalho: {self.ponto_orvalho2} °C",bg="#E0FFFF", justify="left", font=("verdana",12,"bold"))
            
            # Aqui o messagebox está funcionando
                
        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos.")

        return self.temperatura_bulbo_seco, self.temperatura_bulbo_seco2
    
    def printar_result2(self):

        
        # Exibindo o resultado
        try:
            self.calculos2()

            if hasattr(self,'frame_3'):
                self.resultado_label3.config(
                    text=f"Resultados:\n\nParede Norte/ Nordeste: {round(self.cargan, 2)} KCal/h\n"
                        f"Parede Sul/ Sudeste: {round(self.cargas, 2)} KCal/h\n"
                        f"Parede Leste/ Noroeste: {round(self.cargal, 2)} KCal/h\n"
                        f"Parede Oeste/ Sudoeste: {round(self.cargao, 2)} KCal/h\n"
                        f"Carga de Condução: {round(self.cargaext, 2)} KCal/h", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                
                

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos.")
        except AttributeError:
            messagebox.showerror("Erro", "O atributo necessário não foi encontrado. Verifique se todos os atributos estão devidamente inicializados.")
        return self.cargan, self.cargas

    def printar_result3(self):

        
        # Exibindo o resultado
        try:
            self.calculos3()

            if hasattr(self, 'frame_5'):
                self.resultado_label4.config(
                    text=f"Resultados divisórias:\n\nCarga nas paredes internas: {round(self.divpar, 2)} KCal/h\n"
                        f"Carga nos vidros internos: {round(self.divvid, 2)} KCal/h\n"
                        f"Carga no piso: {round(self.divpis, 2)} KCal/h\n"
                        f"Carga no teto: {round(self.divtet, 2)} KCal/h\n"
                        f"Carga total nas divisórias: {round(self.cargadiv, 2)} KCal/h", justify="left", bg="#E0FFFF", font=("verdana", 12, "bold"))

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos.")
        except AttributeError:
            messagebox.showerror("Erro", "Verifique se o tipo de proteção da janela foi selecionado, se sim, a esquadria não pode ser 'Não Possui'.")

        return self.divvid, self.divpis

    def printar_result4(self):

            # Exibindo o resultado
            try:

                self.calculos4()

                if hasattr(self,'frame_7'):

                    self.resultado_label5.config(
                        text=f"Resultados Insolação Janelas:\n\nCarga na janela Norte/ Noroeste: {round(self.carg_jann, 2)} KCal/h\n"
                            f"Carga na janela Sul/ Sudeste: {round(self.carg_jans, 2)} KCal/h\n"
                            f"Carga na janela Leste/ Nordeste: {round(self.carg_janl, 2)} KCal/h\n"
                            f"Carga na janela Oeste/ Sudoeste: {round(self.carg_jano, 2)} KCal/h\n"
                            f"Carga total nas janelas: {round(self.carg_jant, 2)} KCal/h", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                        
                    

            except ValueError:
                messagebox.showerror("Erro", "Digite valores numéricos válidos ou verifique alguma incoerencia nas opções selecionadas")

            except AttributeError:
                messagebox.showerror("Erro", "O atributo necessário não foi encontrado. Verifique se todos os atributos estão devidamente inicializados.")
            return self.carg_jant

    def printar_result5(self):
        

        # Exibindo o resultado
        try:

            self.calculos5()

            if hasattr(self,'frame_9'):

                self.resultado_label6.config(
                    text=f"Resultados Calor Pessoas:\n\nCarga Sensível Total: {round(self.cs0_total, 2)} KCal/h\n"
                        f"Carga Latente Total: {round(self.cl0_total, 2)} KCal/h\n\n"
                        f"Carga Total: {round(self.soma_total0, 2)} KCal/h", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                    
                

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos ou verifique alguma incoerencia nas opções selecionadas")

        except AttributeError:
            messagebox.showerror("Erro", "O atributo necessário não foi encontrado. Verifique se todos os atributos estão devidamente inicializados.")
        
    def printar_result6(self):
        try:

            self.calculos6()

            if hasattr(self,'frame_11'):

                self.resultado_label7.config(
                    text=f"Resultados Calor Equipamentos:\n\nCarga Sensível Total: {round(self.cs_total, 2)} W\n"
                        f"Carga Latente Total: {round(self.cl_total, 2)} W\n\n"
                        f"Carga Total: {round(self.soma_total, 2)} W", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                    
                

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos ou verifique alguma incoerencia nas opções selecionadas")

    def printar_result7(self):
        try:

            self.calculos7()

            if hasattr(self,'frame_13'):

                self.resultado_label8.config(
                    text=f"Resultados Ventilação:\n\nÁrea útil: {round(self.area_util, 2)} m²\n"
                        f"Vazão eficaz de ar exterior: {round(self.vaz_efex, 2)} m³/s\n"
                        f"Vazão de ar exterior a ser suprido na zona: {round(self.vaz_efzo, 2)} m³/s\n"
                        f"Calor Sensível: {round(self.calsen_ven, 2)} KCal/h\n"
                        f"Calor Latente: {round(self.callat_ven, 2)} KCal/h\n\n"
                        f"Carga Total: {round(self.caltot_ven, 2)} W", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                    
                

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos ou verifique alguma incoerencia nas opções selecionadas")

    def printar_result8(self):
        try:

            self.calculos8()

            if hasattr(self,'frame_15'):

                self.resultado_label9.config(
                    text=f"Resultados Infiltração:\n\nCalor Sensível: {round(self.csti, 2)} KCal/h\n"
                        f"Calor Latente: {round(self.clti, 2)} KCal/h\n\n"
                        f"Carga Total: {round(self.cti, 2)} KCal/h", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                    

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos ou verifique alguma incoerencia nas opções selecionadas")
    
    def printar_result9(self):
        try:

            self.calculos9()

            if hasattr(self,'frame_17'):

                self.resultado_label10.config(
                    text=f"Resultados Calculos:\n\n"
                        f"Condução:         {round(self.cargaext, 2)} KCal/h         0 KCal/h        {round(self.v_ark1, 2)} Kg/h        {round(self.v_ark6, 2)} Kg/h\n"
                        f"Pessoas:            {round(self.cs0_total, 2)} KCal/h       {round(self.cl0_total, 2)} KCal/h        {round(self.v_ark2, 2)} Kg/h        {round(self.v_ark7, 2)} Kg/h\n"
                        f"Equipamentos: {round(self.cs_total, 2)} KCal/h        {round(self.cl_total, 2)} KCal/h        {round(self.v_ark3, 2)} Kg/h        {round(self.v_ark8, 2)} Kg/h\n"
                        f"Ventilação:        {round(self.calsen_ven, 2)} KCal/h       {round(self.callat_ven, 2)} KCal/h        {round(self.v_ark4, 2)} Kg/h        {round(self.v_ark9, 2)} Kg/h\n"
                        f"Infiltração:        {round(self.csti, 2)} KCal/h        {round(self.clti, 2)} KCal/h        {round(self.v_ark5, 2)} Kg/h        {round(self.v_ark10, 2)} Kg/h\n"
                        f"SubTotal:           {round(self.scals, 2)} KCal/h       {round(self.scall, 2)} KCal/h        {round(self.v_art1, 2)} Kg/h        {round(self.v_art2, 2)} Kg/h\n"
                        f"Total (+10%):             {round(self.caltotal_up, 2)} KCal/h\n", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                
                self.resultado_label11.config(
                    text=f"Resultados Infiltração:\n\nCalor Sensível: {round(self.csti, 2)} KCal/h\n"
                        f"Calor Latente: {round(self.clti, 2)} KCal/h\n\n"
                        f"Carga Total: {round(self.cti, 2)} KCal/h", justify="left",bg="#E0FFFF", font=("verdana",12,"bold"))
                    

        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos ou verifique alguma incoerencia nas opções selecionadas")



class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        # Cria e exibe o balão de ajuda
        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=5, ipady=2)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None



Application()


