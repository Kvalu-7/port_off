import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class TelaCadastroAluno:
    def __init__(self, root):
        self.root = root

        self._criar_entradas()

    def _criar_entradas(self):
        # Frames
        self.up_frame = tk.Frame(self.root, bg="#002CA7", height=150)
        self.up_frame.pack(fill="x")

        self.principal_frame = tk.Frame(self.root, bg="#f3f3f3")
        self.principal_frame.pack(fill="both", expand=True, padx=20, pady=10, anchor="center")
        
        self.sub1principal_frame = tk.Frame(self.principal_frame, bg="#f3f3f3")
        self.sub1principal_frame.pack(fill="both", expand=True, padx=20, pady=2, anchor="center")
        
        self.sub2principal_frame = tk.Frame(self.principal_frame, bg="#f3f3f3")
        self.sub2principal_frame.pack(fill="both", expand=True, padx=20, pady=2, anchor="center")

        self.footer_frame = tk.Frame(self.root, bg="#002CA7", height=50)
        self.footer_frame.pack(fill="x")

        self.principal_frame.grid_columnconfigure(0, weight=1)  
        self.principal_frame.grid_columnconfigure(1, weight=1) 

        titulo = tk.Label(self.up_frame, text="🖍️CADASTRAR CURSOS", bg="#002CA7", fg="white",
                          font=("Arial", 28, "bold"))
        titulo.grid(row=0, column=0, pady=10)


            #=========botões==========
        self.btn_cadastrar = tk.Button(self.sub1principal_frame, text="Cadastre", font=("Arial", 12, "bold"),
                                       bg="#002CA7", fg="white", command=self.cadastrar_alunos)
        self.btn_cadastrar.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

        self.btn_consultar = tk.Button(self.sub1principal_frame, text="Consultar registros", font=("Arial", 12, "bold"),
                                       bg="#0055FF", fg="white", command=self.consultar_dados_curso)
        self.btn_consultar.grid(row=0, column=3, columnspan=2, pady=10, sticky="nsew")

            #=========footer==========
        tk.Label(self.footer_frame, text=" Aluv  System - ₢ Todos direitos reservados - (38) 9 9871-8375",
                 bg="#002CA7", fg="white", font=("Arial", 10)).pack(pady=10)



    def cadastrar_alunos(self):
        self.limpar_center()
        self.sub3principal_frame = tk.Frame(self.sub2principal_frame, bg="#f3f3f3")
        self.sub3principal_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Configurar grid para centralizar
        self.sub3principal_frame.grid_columnconfigure(0, weight=1)  # coluna dos labels
        self.sub3principal_frame.grid_columnconfigure(1, weight=2)  # coluna dos entry
        self.sub3principal_frame.grid_columnconfigure(2, weight=1)  # espaço extra

        # Labels e Entradas
        tk.Label(self.sub3principal_frame, text="Nome", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=0, column=0, sticky="e", pady=5)
        self.entry_nome = tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_nome.grid(row=0, column=1, pady=5, sticky="ew")

        tk.Label(self.sub3principal_frame, text="Matrícula", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=1, column=0, sticky="e", pady=5)
        self.entry_matricula = tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_matricula.grid(row=1, column=1, pady=5, sticky="ew")

        tk.Label(self.sub3principal_frame, text="CPF", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=2, column=0, sticky="e", pady=5)
        self.entry_cpf= tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_cpf(row=2, column=1, pady=5, sticky="ew")

        tk.Label(self.sub3principal_frame, text="Email", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=3, column=0, sticky="e", pady=5)
        self.entry_email = tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_email.grid(row=3, column=1, pady=5, sticky="ew")

        self.btn_cadastrar = tk.Button(self.sub3principal_frame, text="Cadastrar", font=("Arial", 12, "bold"),
                                    bg="#002CA7", fg="white", command=self.salvar_cursos)
        self.btn_cadastrar.grid(row=4, column=1, pady=10, sticky="nsew")

    #===============================================================================

    # import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# import sqlite3


# class TelaCadastroCurso(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         self.container = container

#         # --- Configuração da Janela Principal ---
#         # self.container.title("Cadastrar curso")
#         # self.container.geometry("1080x720")
#         # self.container.minsize(700, 600)# Tamanho mínimo para a janela

#         # --- Configuração de Estilos ---
#         self.style = ttk.Style(self.container)
#         self.style.theme_use("clam")
#         BG_COLOR = "#e0e8f0"
#         self.style.configure("TFrame", background=BG_COLOR)
#         self.style.configure("TLabel", background=BG_COLOR, font=("Arial", 12))
#         self.style.configure("Title.TLabel", font=("Arial", 12, "bold"))
#         self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
#         self.style.configure("TEntry", font=("Arial", 12), padding=5)

#         # --- Layout Responsivo ---
#         self.container.grid_rowconfigure(0, weight=1)
#         self.container.grid_columnconfigure(0, weight=1)

#         self.grid(row=0, column=0, sticky="nsew")
#         self.configure(style="TFrame")



#         # Criação dos widgets
#         self._criar_entradas()


#     def _criar_entradas(self):
#     # frames
#         self.up_frame = ttk.Frame(self.container, bg="#002CA7", height=150)
#         self.up_frame.pack(fill="x")
        
#         self.principal_frame = ttk.Frame(self.container, bg="#f3f3f3")
#         self.principal_frame.pack(fill="both", expand=True)

#         self.footer_frame = ttk.Frame(self.container, bg="#002CA7", height=50)
#         self.footer_frame.pack(fill="x")
        
        
        
#     #Cria e organiza todas as informações a serem preenchidas na tela
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=0)
#         self.grid_columnconfigure(2, weight=1)
#         self.grid_columnconfigure(3, weight=1)

#         titulo = ttk.Label(self.up_frame, text="CADASTRAR CURSOS", style="Title.TLabel")
#         titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

#         label_curso=ttk.Label(self.principal_frame, text="Curso", style='TLabel')
#         label_curso.grid(row=1, column=1,sticky='w' )
#         self.entry_curso=ttk.Entry(self.principal_frame, width= 100, style='TEntry')
#         self.entry_curso.grid(row=1, column=2, sticky='w')

#         label_codigot=ttk.Label(self.principal_frame, text="Código da Turma", style='TLabel')
#         label_codigot.grid(row=2, column=1,sticky='w' )
#         self.entry_codigot=ttk.Entry(self.principal_frame, width= 100, style='TEntry')
#         self.entry_codigot.grid(row=2, column=2, sticky='w')

#         label_turno = ttk.Label(self.principal_frame, text="Turno", style='TLabel')
#         label_turno.grid(row=3, column=1, sticky='w')
#         self.combo_turno = ttk.Combobox(self.principal_frame, values=['Manhã', 'Tarde', 'Noite'], font=('Arial', 10))
#         self.combo_turno.grid(row=3, column=2, sticky='w')

#         label_unidade = ttk.Label(self.principal_frame, text="Unidade", style='TLabel')
#         label_unidade.grid(row=4, column=1, sticky='w')
#         self.entry_unidade = ttk.Entry(self.principal_frame, width=100, style='TEntry')
#         self.entry_unidade.grid(row=4, column=2, sticky='w')
           
#         # --- Botões ---
    
#         botao_cadastrar = ttk.Button(self.principal_frame, text="Cadastrar", command=self.cadastrar_cursos)
#         botao_cadastrar.grid(row=6, column=1, columnspan=2, pady=(30, 10), sticky="ew")

#         botao_consultar = ttk.Button(self.principal_frame, text="Consultar registros", command=self.consultar_dados_curso)
#         botao_consultar.grid(row=7, column=1, columnspan=2, pady=(10, 20), sticky="ew")
        
#         # --- FOOTER ---
#         tk.Label(self.footer_frame, text=" Hexa - Soluções Empresariais - ₢ Todos direitos reservados - (38) 9 9917-8063", bg="#002CA7", fg="white", font=("Arial", 10)).pack(pady=10)


#     def cadastrar_cursos(self):
#         try:
#             con = sqlite3.connect("instituicao.db")
#             cur = con.cursor()
#             cur.execute("""
#                 INSERT INTO curso
#                 (Curso, Codigo_da_turma, Turno, Unidade)
#                 VALUES (?, ?, ?, ?)
#             """, (
#                 self.entry_curso.get(),
#                 self.entry_codigot.get(),
#                 self.combo_turno.get(),
#                 self.entry_unidade.get()
                
#             ))
#             con.commit()
#             con.close()

#             messagebox.showinfo("Sucesso", "Dados cadastrado com sucesso!")
#             self._limpar_campos()

#         except Exception as e:
#             messagebox.showerror("Erro", f"Falha ao salvar os dados:\n{e}")

#     def consultar_dados_curso(self):
#         consulta_win = tk.Toplevel(self.container)
#         consulta_win.title("Dados do Curso")
#         consulta_win.geometry("900x400")

#         colunas = ("ID", "Curso", "Codigo da turma", "Turno", "Unidade")
#         tree = ttk.Treeview(consulta_win, columns=colunas, show="headings")

#         for col in colunas:
#             tree.heading(col, text=col.capitalize())
#             tree.column(col, width=100)

#         tree.pack(expand=True, fill="both")

#         con = sqlite3.connect("instituicao.db")
#         cursor = con.cursor()
#         cursor.execute("SELECT * FROM curso")
#         for row in cursor.fetchall():
#             tree.insert("", "end", values=row)
#         con.close()

#         #=====Botão de deletar=======
#         def deletar_selecionado():
#             item = tree.selection()
#             if not item:
#                 messagebox.showerror("Erro", "Selecione a opção que você deseja deletar!")
#                 return

#             curso_id = tree.item(item)["values"][0]

#             con = sqlite3.connect("instituicao.db")
#             cursor = con.cursor()
#             cursor.execute("DELETE FROM curso WHERE id=?", (curso_id,))
#             con.commit()
#             con.close()

#             tree.delete(item)
#             messagebox.showinfo("Sucesso", "Professor deletado com sucesso!")

#         botao_deletar = ttk.Button(consulta_win, text="Deletar Selecionado", command=deletar_selecionado)
#         botao_deletar.pack(pady=10)

#     def _limpar_campos(self): #apos salvar os dados limpar os campos
#         self.entry_curso.delete(0, tk.END)
#         self.entry_codigot.delete(0, tk.END)
#         self.combo_turno.set(" ")
#         self.entry_unidade.delete(0, tk.END)
        



# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TelaCadastroCurso(root)
#     root.mainloop()


#=============================
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class TelaCadastroCurso:
    def __init__(self, root):
        self.root = root

        # Configuração da janela
        # self.root.title("Cadastrar curso")
        # self.root.geometry("1080x720")
        # self.root.minsize(700, 600)
        # self.root.configure(bg="#e0e8f0")

        # Criação dos widgets
        self._criar_entradas()

        # Banco de dados
        # self._criar_tabela()

    # def _criar_tabela(self):
    #     con = sqlite3.connect("instituicao.db")
    #     cur = con.cursor()
    #     cur.execute("""
    #         CREATE TABLE IF NOT EXISTS curso(
    #             ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #             Curso TEXT NOT NULL,
    #             Codigo_da_turma TEXT NOT NULL UNIQUE,
    #             Turno TEXT NOT NULL,
    #             Unidade TEXT NOT NULL
    #         )
    #     """)
    #     con.commit()
    #     con.close()

    def _criar_entradas(self):
        # Frames
        self.up_frame = tk.Frame(self.root, bg="#002CA7", height=150)
        self.up_frame.pack(fill="x")

        self.principal_frame = tk.Frame(self.root, bg="#f3f3f3")
        self.principal_frame.pack(fill="both", expand=True, padx=20, pady=10, anchor="center")
        
        self.sub1principal_frame = tk.Frame(self.principal_frame, bg="#f3f3f3")
        self.sub1principal_frame.pack(fill="both", expand=True, padx=20, pady=2, anchor="center")
        
        self.sub2principal_frame = tk.Frame(self.principal_frame, bg="#f3f3f3")
        self.sub2principal_frame.pack(fill="both", expand=True, padx=20, pady=2, anchor="center")

        self.footer_frame = tk.Frame(self.root, bg="#002CA7", height=50)
        self.footer_frame.pack(fill="x")
        
        # Configurar o peso das colunas e linhas
        self.principal_frame.grid_columnconfigure(0, weight=1)  # Coluna 0 se expande
        self.principal_frame.grid_columnconfigure(1, weight=1)  # Coluna 1 se expande
        # self.principal_frame.grid_rowconfigure(0, weight=1)     # Linha 0 se expande
        # self.principal_frame.grid_rowconfigure(1, weight=1)     # Linha 1 se expande
        # self.principal_frame.grid_rowconfigure(1, weight=1)     # Linha 0 se expande
        # self.principal_frame.grid_rowconfigure(2, weight=1)     # Linha 1 se expande

        # Título
        titulo = tk.Label(self.up_frame, text="🖍️CADASTRAR CURSOS", bg="#002CA7", fg="white",
                          font=("Arial", 28, "bold"))
        titulo.grid(row=0, column=0, pady=10)

        # # Labels e Entradas
        # tk.Label(self.sub2principal_frame, text="Curso", bg="#f3f3f3", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        # self.entry_curso = tk.Entry(self.sub2principal_frame, font=("Arial", 12), width=50)
        # self.entry_curso.grid(row=0, column=1, pady=5, sticky="nsew")

        # tk.Label(self.sub2principal_frame, text="Código da Turma", bg="#f3f3f3", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        # self.entry_codigot = tk.Entry(self.sub2principal_frame, font=("Arial", 12), width=50)
        # self.entry_codigot.grid(row=1, column=1, pady=5, sticky="nsew")

        # tk.Label(self.sub2principal_frame, text="Turno", bg="#f3f3f3", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        # self.combo_turno = ttk.Combobox(self.sub2principal_frame, values=["Manhã", "Tarde", "Noite"], font=("Arial", 12), width=48)
        # self.combo_turno.grid(row=2, column=1, pady=5, sticky="nsew")

        # tk.Label(self.sub2principal_frame, text="Unidade", bg="#f3f3f3", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", pady=5)
        # self.entry_unidade = tk.Entry(self.sub2principal_frame, font=("Arial", 12), width=50)
        # self.entry_unidade.grid(row=3, column=1, pady=5, sticky="nsew")

        # Botões
        self.btn_cadastrar = tk.Button(self.sub1principal_frame, text="Cadastre", font=("Arial", 12, "bold"),
                                       bg="#002CA7", fg="white", command=self.cadastrar_cursos)
        self.btn_cadastrar.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")
        
        # self.btn_cadastrar = tk.Button(self.sub2principal_frame, text="Cadastrar", font=("Arial", 12, "bold"),
        #                                bg="#002CA7", fg="white", command=self.salvar_cursos)
        # self.btn_cadastrar.grid(row=0, column=0, columnspan=2, pady=(20, 5), sticky="nsew")

        self.btn_consultar = tk.Button(self.sub1principal_frame, text="Consultar registros", font=("Arial", 12, "bold"),
                                       bg="#0055FF", fg="white", command=self.consultar_dados_curso)
        self.btn_consultar.grid(row=0, column=3, columnspan=2, pady=10, sticky="nsew")

        # Footer
        tk.Label(self.footer_frame, text=" Aluv  System - ₢ Todos direitos reservados - (38) 9 9871-8375",
                 bg="#002CA7", fg="white", font=("Arial", 10)).pack(pady=10)
        
        
        
    def cadastrar_cursos(self):
        self.limpar_center()
        self.sub3principal_frame = tk.Frame(self.sub2principal_frame, bg="#f3f3f3")
        self.sub3principal_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Configurar grid para centralizar
        self.sub3principal_frame.grid_columnconfigure(0, weight=1)  # coluna dos labels
        self.sub3principal_frame.grid_columnconfigure(1, weight=2)  # coluna dos entry
        self.sub3principal_frame.grid_columnconfigure(2, weight=1)  # espaço extra

        # Labels e Entradas
        tk.Label(self.sub3principal_frame, text="Curso", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=0, column=0, sticky="e", pady=5)
        self.entry_curso = tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_curso.grid(row=0, column=1, pady=5, sticky="ew")

        tk.Label(self.sub3principal_frame, text="Código da Turma", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=1, column=0, sticky="e", pady=5)
        self.entry_codigot = tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_codigot.grid(row=1, column=1, pady=5, sticky="ew")

        tk.Label(self.sub3principal_frame, text="Turno", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=2, column=0, sticky="e", pady=5)
        self.combo_turno = ttk.Combobox(self.sub3principal_frame, values=["Manhã", "Tarde", "Noite"],
                                        font=("Arial", 12), justify="center")
        self.combo_turno.grid(row=2, column=1, pady=5, sticky="ew")

        tk.Label(self.sub3principal_frame, text="Unidade", bg="#f3f3f3", font=("Arial", 12, "bold"))\
            .grid(row=3, column=0, sticky="e", pady=5)
        self.entry_unidade = tk.Entry(self.sub3principal_frame, font=("Arial", 12), justify="center")
        self.entry_unidade.grid(row=3, column=1, pady=5, sticky="ew")

        self.btn_cadastrar = tk.Button(self.sub3principal_frame, text="Cadastrar", font=("Arial", 12, "bold"),
                                    bg="#002CA7", fg="white", command=self.salvar_cursos)
        self.btn_cadastrar.grid(row=4, column=1, pady=10, sticky="nsew")

        
        
    def salvar_cursos(self):
        curso = self.entry_curso.get().strip()
        codigo = self.entry_codigot.get().strip()
        turno = self.combo_turno.get().strip()
        unidade = self.entry_unidade.get().strip()

        if not (curso and codigo and turno and unidade):
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            con = sqlite3.connect("instituicao.db")
            cur = con.cursor()
            cur.execute("INSERT INTO curso (Curso, Codigo_da_turma, Turno, Unidade) VALUES (?, ?, ?, ?)",
                        (curso, codigo, turno, unidade))
            con.commit()
            con.close()
            messagebox.showinfo("Sucesso", "Curso cadastrado com sucesso!")
            self._limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar os dados:\n{e}")

    def limpar_center(self):
        for widget in self.sub2principal_frame.winfo_children():
            widget.destroy()


    def consultar_dados_curso(self):
        self.limpar_center()
        consulta_win = (self.sub2principal_frame)
        # consulta_win.title("Dados do Curso")
        # consulta_win.geometry("800x400")

        colunas = ("ID", "Curso", "Código da turma", "Turno", "Unidade")
        tree = ttk.Treeview(consulta_win, columns=colunas, show="headings")
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(expand=True, fill="both", pady=10, padx=10)

        con = sqlite3.connect("instituicao.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM curso")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        con.close()

        def deletar_selecionado():
            item = tree.selection()
            if not item:
                messagebox.showerror("Erro", "Selecione um curso para deletar!")
                return
            curso_id = tree.item(item)["values"][0]
            con = sqlite3.connect("instituicao.db")
            cursor = con.cursor()
            cursor.execute("DELETE FROM curso WHERE ID=?", (curso_id,))
            con.commit()
            con.close()
            tree.delete(item)
            messagebox.showinfo("Sucesso", "Curso deletado com sucesso!")

        tk.Button(consulta_win, text="Deletar Selecionado", bg="#FF0000", fg="white",
                  font=("Arial", 12, "bold"), command=deletar_selecionado).pack(pady=10)

    def _limpar_campos(self):
        self.entry_curso.delete(0, tk.END)
        self.entry_codigot.delete(0, tk.END)
        self.combo_turno.set("")
        self.entry_unidade.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroCurso(root)
    root.mainloop()



#===============================================================================
    
#     def criar_banco(self):
#         conn=sqlite3.connect("instituicao.db")
#         cursor=conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS alunos(
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 Nome TEXT NOT NULL,
#                 Matricula TEXT NOT NULL UNIQUE,
#                 CPF TEXT NOT NULL UNIQUE CHECK(length(cpf)=11 AND CPF GLOB '[0-9]*'),
#                 Email TEXT NOT NULL CHECK((instr(email, '@'))>1),
#                 Curso TEXT
#         )
#     """)
#         conn.commit()
#         conn.close()

#     def informacoes_alunos(self):
#         # --- Configuração do Grid Interno para Centralização ---
#         # Colunas 0 e 3 são espaçadores invisíveis que empurram o conteúdo para o centro.
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=0) # Coluna dos labels
#         self.grid_columnconfigure(2, weight=1) # Coluna dos entries (com peso para expandir)
#         self.grid_columnconfigure(3, weight=1)

#         # --- Título ---
#         titulo = ttk.Label(self, text="CADASTRAR ALUNOS", style="Title.TLabel")
#         titulo.grid(row=0, column=1, columnspan=2, pady=(20, 30))

#         label_nome=ttk.Label(self, text="Nome", style='TLabel')
#         label_nome.grid(row=1, column=1,sticky='w' )
#         self.entry_nome=ttk.Entry(self, width= 100, style='TEntry')
#         self.entry_nome.grid(row=1, column=2, sticky='w')

#         label_matricula=ttk.Label(self, text="Matricula", style='TLabel')
#         label_matricula.grid(row=2, column=1,sticky='w' )
#         self.entry_matricula=ttk.Entry(self, width= 100, style='TEntry')
#         self.entry_matricula.grid(row=2, column=2, sticky='w')

#         label_cpf=ttk.Label(self, text="CPF", style='TLabel')
#         label_cpf.grid(row=3, column=1,sticky='w' )
#         self.entry_cpf=ttk.Entry(self, width= 100, style='TEntry')
#         self.entry_cpf.grid(row=3, column=2, sticky='w')

#         label_email=ttk.Label(self, text="Email", style='TLabel')
#         label_email.grid(row=4, column=1,sticky='w' )
#         self.entry_email=ttk.Entry(self, width= 100, style='TEntry')
#         self.entry_email.grid(row=4, column=2, sticky='w')

#         label_curso=ttk.Label(self, text="Curso", style='TLabel')
#         label_curso.grid(row=5, column=1,sticky='w' )
#         self.combo_curso=ttk.Combobox(self,values=[' '], font=("Arial", 12))
#         self.combo_curso.grid(row=5, column=2, sticky='w')

#         #========Botões==========

#         botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.cadastrar_alunos)
#         botao_cadastrar.grid(row=8, column=1, columnspan=2, pady=(30, 10), sticky="ew")

#         botao_consultar = ttk.Button(self, text="Consultar registros", command=self.consultar_dados_alunos)
#         botao_consultar.grid(row=9, column=1, columnspan=2, pady=(10, 20), sticky="ew")

#     def cadastrar_alunos(self):
#         try:
#             con= sqlite3.connect("instituicao.db")
#             cur=con.cursor()
#             cur.execute("""
#                 INSERT INTO alunos
#                 (Nome, Matricula, CPF, Email, Curso)
#                 VALUES(?, ?, ?, ?, ?)
#             """,(
#                 self.entry_nome.get(),
#                 self.entry_matricula.get(),
#                 self.entry_cpf.get(),
#                 self.entry_email.get(),
#                 self.combo_curso.get()
            
#             ))
#             con.commit()
#             con.close()

#             messagebox.showinfo("Ok", "Aluno cadastrado com sucesso")
#             self._limpar_campos()
        
#         except Exception as e:
#             messagebox.showerror("Erro", f"Erro ao salvar dados{e}")

#     def consultar_dados_alunos(self):
#         area_consulta = tk.Toplevel(self.container)
#         area_consulta.title("Dados dos alunos")
#         area_consulta.geometry("900x400")

#         colunas = ("ID", "Nome", "Matrícula", "CPF", "Email", "Curso")
#         tree = ttk.Treeview(area_consulta, columns=colunas, show="headings")

#         for col in colunas:
#             tree.heading(col, text=col.capitalize())
#             tree.column(col, width=100)

#         tree.pack(expand=True, fill="both")

#         con = sqlite3.connect("instituicao.db")
#         cursor = con.cursor()
#         cursor.execute("SELECT * FROM alunos")
#         for row in cursor.fetchall():
#             tree.insert("", "end", values=row)
#         con.close()

#         def deletar_selecionado():
#                 item = tree.selection()
#                 if not item:
#                     messagebox.showerror("Erro", "Selecione um aluno para deletar!")
#                     return

#                 aluno_id = tree.item(item)["values"][0]

#                 con = sqlite3.connect("instituicao.db")
#                 cursor = con.cursor()
#                 cursor.execute("DELETE FROM alunos WHERE id=?", (aluno_id,))
#                 con.commit()
#                 con.close()

#                 tree.delete(item)
#                 messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
#         #============botão para deletar um registro=============
#         botao_deletar = ttk.Button(area_consulta, text="Deletar Selecionado", command=deletar_selecionado)
#         botao_deletar.pack(pady=10)

#     def _limpar_campos(self): #apos salvar os dados limpar os campos
#         self.entry_nome.delete(0, tk.END)
#         self.entry_matricula.delete(0, tk.END)
#         self.entry_cpf.delete(0, tk.END)
#         self.entry_email.delete(0, tk.END)
#         self.combo_curso.set(" ")




# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TelaCadastroAluno(root)
#     root.mainloop()
