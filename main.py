from tkinter import *
from tkinter import ttk
from tkinter import messagebox

eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
ger_alphabet = "abcdefghijklmnopqrstuvwxyzäöüß"
spa_alphabet = "abcdefghijklmnopqrstuvwxyzáéíóúñü"
fra_alphabet = "abcdefghijklmnopqrstuvwxyzàâæçéèêëîïôœùûüÿ"
ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def Copyright():
    win = Toplevel()
    win.title("Copyright data")
    win.geometry("300x100")
    win.minsize(300, 100)
    win.maxsize(300, 100)
    win.configure(bg="#121212")

    CopyrightLabel = Label(win, text="Copyright ©: \n", bg="#121212", fg="#ffffff", font=("Arial", 12))
    CopyrightLabel.pack(pady=(10, 0))
    CopyrightLabel2 = Label(win, text="spielking", bg="#121212", fg="#ffffff", font=("Arial", 12))
    CopyrightLabel2.pack(pady=(10, 0))

def inputArea(root):
    entry = Entry(root, width=20, bg="#312F2F", fg="#ffffff", font=("Arial", 23), borderwidth=0)
    entry.pack(pady=5)
    return entry

def CaesarCipher(text, key, decrypt=False):
    result = ""
    shift = -key if decrypt else key

    for char in text.lower():
        if char in eng_alphabet:
            idx = (eng_alphabet.index(char) + shift) % len(eng_alphabet)
            result += eng_alphabet[idx]
        elif char in ger_alphabet:
            idx = (ger_alphabet.index(char) + shift) % len(ger_alphabet)
            result += ger_alphabet[idx]
        elif char in spa_alphabet:
            idx = (spa_alphabet.index(char) + shift) % len(spa_alphabet)
            result += spa_alphabet[idx]
        elif char in fra_alphabet:
            idx = (fra_alphabet.index(char) + shift) % len(fra_alphabet)
            result += fra_alphabet[idx]
        elif char in ukr_alphabet:
            idx = (ukr_alphabet.index(char) + shift) % len(ukr_alphabet)
            result += ukr_alphabet[idx]
        elif char in rus_alphabet:
            idx = (rus_alphabet.index(char) + shift) % len(rus_alphabet)
            result += rus_alphabet[idx]
        else:
            result += char
    return result

def handle_process():
    text = textforcaesarArea.get().lower()
    if any(char.isdigit() for char in text):
        messagebox.showerror('Error', 'Your input have some numbers, fix this!')
        return
    allowed_chars = eng_alphabet + ger_alphabet + ukr_alphabet + rus_alphabet + spa_alphabet + fra_alphabet + " "
    
    for char in text:
        if char not in allowed_chars:
            messagebox.showerror('Error', f'Sym "{char}" not supported!')
            return
    try:
        text = textforcaesarArea.get()
        key_val = int(numberforalphabet.get())

        decrypt_mode = cipher_mode.get() == "decrypt"

        res = CaesarCipher(text, key_val)

        output_text.delete("1.0", END)
        output_text.insert(END, res)
    except ValueError:
        messagebox.showerror("Error", "Key must be a number!")

def Arif_Calc():
    try:
        a = int(A_Input.get())
        m = int(M_Input.get())
        
        if m <= 0:
            messagebox.showerror("Error", "M must be greater than 0")
            return

        residues = set()

        for q in range(m):
            res = (a * q) % m
            residues.add(res)

        sorted_residues = sorted(list(residues))

        output_text_arif.delete("1.0", END)
        output_text_arif.insert(END, f"Set of remnants for a={a}, m={m}:\n")
        output_text_arif.insert(END, str(sorted_residues))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def RailFence_Logic(text, key):
    if key <= 1: return text

    rails = [[] for _ in range(key)]
    rail = 0
    direction = 1

    for char in text:
        rails[rail].append(char)
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1
    
    return "".join(["".join(r) for r in rails])

def Praktik3_calc():
    try:
        a = int(Praktik3_inputa.get())
        x = int(Praktik3_keyx.get())
        b = int(Praktik3_inputb.get())
        P3calc_result = pow(a, x, b)
        Praktik3_output.delete("1.0", END)
        Praktik3_output.insert(END, str(P3calc_result))
    except ValueError:
        Praktik3_output.delete("1.0", END)
        Praktik3_output.insert(END, "Error: Input numbers!")

def findpubkey():
    m = int(Task2inputm.get())
    e = int(Task2inpute.get())
    p = int(Task2inputp.get())
    q = int(Task2inputq.get())
    N = p * q
    C = pow(m, e, N)

    Task2output.delete("1.0", END)
    Task2output.insert(END, f"N = {N}\n")
    Task2output.insert(END, f"C = {C}")

def eylerfunc():
    
    p = int(Task3inputp.get())
    q = int(Task3inputq.get())
    e = Task4inpute.get()
    m = Task5inputm.get()
    N = p * q
    FunctionEyler = (p - 1) * (q - 1)
    
    Task3output.delete("1.0", END)
    Task3output.insert(END, f"N = {N}\n")
    Task3output.insert(END, f"FunctionEyler = {FunctionEyler}\n")

    if e != "":
        e = int(e)
        d = pow(e, -1, FunctionEyler)
        Task3output.insert(END, f"d = {d}\n")
    if m != "":
        m = int(m)
        C = pow(m, e, N)
        Task3output.insert(END, f"C = {C}\n")
        M = pow(C, e, N)
        Task3output.insert(END, f"M = {M}")

def RSAcont():
    textfor = textforcrypt.get()
    e = int(Task6inpute.get())
    N = int(Task6inputn.get())
    resultRSA = RSAEncryptText(textfor, e, N)
    Task6output.delete("1.0", END)
    Task6output.insert(END, f"resultRSA = {resultRSA}")

"""
def RSAdecont():
    textfor = cipher_text.get()

    e1 = int(Task7inpute.get())
    p1 = int(Task7inputp.get())
    q1 = int(Task7inputq.get())
    d, steps, numbers, text = RSADecryptText(textfor, e1, p1, q1)

    Task7output.delete("1.0", END)
    Task7output.insert(END, f"d = {d}\n\n")
    Task7output.insert(END, f"{steps}\n\n")
    Task7output.insert(END, f"Numbers:\n{numbers}\n\n")
    Task7output.insert(END, f"Text:\n{text}")
"""

def RSAdecontTask8():
    textfor = cipher_text.get()
    e1 = int(Task8inpute.get())
    p1 = int(Task8inputp.get())
    q1 = int(Task8inputq.get())
    d, steps, text = RSADecryptTask8(textfor, e1, p1, q1)

    Task8output.delete("1.0", END)
    Task8output.insert(END, f"d = {d}\n\n")
    Task8output.insert(END, steps)
    Task8output.insert(END, f"\n\nText:\n{text}")

def RSAEncryptText(text, e, N):
    text = text.lower()
    encrypted = []

    for char in text:
        if char == " ":
            continue
        if char in ukr_alphabet:
            M = ukr_alphabet.index(char)
            C = pow(M, e, N)
            encrypted.append(str(C))
        if char in ger_alphabet:
            M = ger_alphabet.index(char)
            C = pow(M, e, N)
            encrypted.append(str(C))
        if char in fra_alphabet:
            M = fra_alphabet.index(char)
            C = pow(M, e, N)
            encrypted.append(str(C))
        if char in spa_alphabet:
            M = spa_alphabet.index(char)
            C = pow(M, e, N)
            encrypted.append(str(C))
        if char in eng_alphabet:
            M = eng_alphabet.index(char)
            C = pow(M, e, N)
            encrypted.append(str(C))
        if char in rus_alphabet:
            M = rus_alphabet.index(char)
            C = pow(M, e, N)
            encrypted.append(str(C))
    return ", ".join(encrypted)

def RSADecryptText(cipher_text, e, p, q):
    N = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    cipher_numbers = cipher_text.split(",")

    decrypted_numbers = []
    decrypted_text = []
    steps = []
    for num in cipher_numbers:
        C = int(num.strip())
        M = pow(C, d, N)

        decrypted_numbers.append(f"{M:02}")
        if M < len(ukr_alphabet):
            letter = ukr_alphabet[M]
            decrypted_text.append(letter)
            steps.append(
                f"M = {C}^{d} mod {N} = {M:02} = {letter}"
            )

    return (
        d,
        "\n".join(steps),
        ", ".join(decrypted_numbers),
        "".join(decrypted_text)
    )

def RSADecryptTask8(cipher_text, e, p, q):
    N = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    cipher_numbers = cipher_text.split(",")
    result_text = []
    steps = []

    for num in cipher_numbers:
        C = int(num.strip())
        M = pow(C, d, N)
        byte_length = (M.bit_length() + 7) // 8
        M_bytes = M.to_bytes(byte_length, "big")
        try:
            letter = M_bytes.decode("utf-8")
        except:
            letter = "?"

        result_text.append(letter)
        steps.append(f"{C} -> {M} -> {letter}")
    return d, "\n".join(steps), "".join(result_text)

def handle_rail():
    try:
        text = rail_input.get()
        key_val = int(rail_key.get())
        res = RailFence_Logic(text, key_val)
        rail_output.delete("1.0", END)
        rail_output.insert(END, res)
    except ValueError:
        messagebox.showerror("Error", "Key must be a number!")

def Arifmetik():
    global A_Input, M_Input, output_text_arif

    root = Toplevel()
    root.title("Arifmetik")
    root.geometry("800x600")
    root.minsize(800, 600)
    root.maxsize(800, 600)
    root.configure(bg="#121212")

    Label1 = Label(root, text="Set Value A:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    Label1.pack(pady=(10, 0))
    A_Input = inputArea(root)
    Label1 = Label(root, text="Set Value M:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    Label1.pack(pady=(10, 0))
    M_Input = inputArea(root)

    btn_copyright = Button(
        root,
        text="Run",
        command=Arif_Calc,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_copyright.pack(pady=(10, 0))
    
    ResultArea = Label(root, text="Result:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    ResultArea.pack(pady=(10, 0))

    text_frame = Frame(root, bg="#121212")
    text_frame.pack(pady=5)

    scroll_y = Scrollbar(text_frame, orient=VERTICAL)
    scroll_y.pack(side=RIGHT, fill=Y)
    output_text_arif = Text(text_frame, width=80, height=15, bg="#312F2F", fg="#ffffff", font=("Arial", 12))
    output_text_arif.pack(side=LEFT)
    scroll_y.config(command=output_text.yview)

def questionschoose():
    root = Toplevel()
    root.title("Choose your Task")
    root.geometry("300x320")
    root.minsize(300, 320)
    root.maxsize(300, 320)
    root.configure(bg="#121212")

    defaultLabel = Label(root, text="Choose your task: \n", bg="#121212", fg="#ffffff", font=("Arial", 12))
    defaultLabel.pack(pady=(10, 0))
    
    btn_Task1 = Button(
        root,
        text="Modular Exponentiation",
        command=Praktik3_1Window,
        width=19,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_Task1.pack(pady=(10, 0))

    btn_Task2 = Button(
        root,
        text="RSA Encryption",
        command=Task2Window,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_Task2.pack(pady=(10, 0))

    btn_Task3 = Button(
        root,
        text="Euler Function",
        command=Task3Window,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_Task3.pack(pady=(10, 0))

    btn_Task6 = Button(
        root,
        text="RSA Encrypt Text",
        command=Task6Window,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_Task6.pack(pady=(10, 0))

    """
    btn_Task7 = Button(
        root,
        text="RSA Decrypt Text",
        command=Task7Window,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_Task7.pack(pady=(10, 0))
    """

    btn_Task8 = Button(
        root,
        text="RSA Decrypt UTF-8",
        command=Task8Window,
        width=17,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_Task8.pack(pady=(10, 0))

def Praktik3_1Window():
    global Praktik3_inputa, Praktik3_inputb, Praktik3_keyx, Praktik3_output
    root = Toplevel()
    root.title("Modular Exponentiation")
    root.geometry("600x500")
    root.configure(bg="#121212")

    Label(root, text="Base (a):", bg="#121212", fg="#ffffff").pack(pady=5)
    Praktik3_inputa = inputArea(root)
    Label(root, text="Exponent (x):", bg="#121212", fg="#ffffff").pack(pady=5)
    Praktik3_keyx = inputArea(root)
    Label(root, text="Modulus (b):", bg="#121212", fg="#ffffff").pack(pady=5)
    Praktik3_inputb = inputArea(root)
    
    Button(root, text="Calculate", command=Praktik3_calc, bg="#312F2F", fg="#ffffff").pack(pady=10)
    Praktik3_output = Text(root, width=50, height=10, bg="#312F2F", fg="#ffffff")
    Praktik3_output.pack(pady=10)

def Task2Window():
    global Task2inputm, Task2inpute, Task2inputp, Task2inputq, Task2output
    root = Toplevel()
    root.title("RSA Encryption")
    root.geometry("600x600")
    root.configure(bg="#121212")

    Label(root, text="Message (M):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task2inputm = inputArea(root)
    Label(root, text="Public Exponent (e):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task2inpute = inputArea(root)
    Label(root, text="Prime (p):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task2inputp = inputArea(root)
    Label(root, text="Prime (q):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task2inputq = inputArea(root)
    
    Button(root, text="Calculate", command=findpubkey, bg="#312F2F", fg="#ffffff").pack(pady=10)
    Task2output = Text(root, width=50, height=10, bg="#312F2F", fg="#ffffff")
    Task2output.pack(pady=10)

def Task3Window():
    global Task3inputp, Task3inputq, Task3output, Task4inpute, Task5inputm
    root = Toplevel()
    root.title("Euler Function")
    root.geometry("600x600")
    root.configure(bg="#121212")

    Label(root, text="Prime (p):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task3inputp = inputArea(root)
    Label(root, text="Prime (q):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task3inputq = inputArea(root)
    Label(root, text="Public Exponent (e) - for Task4:", bg="#121212", fg="#ffffff").pack(pady=5)
    Task4inpute = inputArea(root)
    Label(root, text="Message (M) - for Task5:", bg="#121212", fg="#ffffff").pack(pady=5)
    Task5inputm = inputArea(root)
    
    Button(root, text="Calculate", command=eylerfunc, bg="#312F2F", fg="#ffffff").pack(pady=10)
    Task3output = Text(root, width=50, height=10, bg="#312F2F", fg="#ffffff")
    Task3output.pack(pady=10)

def Task6Window():
    global textforcrypt, Task6inpute, Task6inputn, Task6output
    root = Toplevel()
    root.title("RSA Encrypt Text")
    root.geometry("700x700")
    root.configure(bg="#121212")

    Label(root, text="Text to encrypt:", bg="#121212", fg="#ffffff").pack(pady=5)
    textforcrypt = inputArea(root)
    Label(root, text="Public Exponent (e):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task6inpute = inputArea(root)
    Label(root, text="Modulus (N):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task6inputn = inputArea(root)
    
    Button(root, text="Encrypt", command=RSAcont, bg="#312F2F", fg="#ffffff").pack(pady=10)
    Task6output = Text(root, width=50, height=10, bg="#312F2F", fg="#ffffff")
    Task6output.pack(pady=10)

"""
#It has bugs
def Task7Window():
    global cipher_text, Task7inpute, Task7inputp, Task7inputq, Task7output
    root = Toplevel()
    root.title("RSA Decrypt Text")
    root.geometry("700x700")
    root.configure(bg="#121212")

    Label(root, text="Cipher Text:", bg="#121212", fg="#ffffff").pack(pady=5)
    cipher_text = inputArea(root)
    Label(root, text="Public Exponent (e):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task7inpute = inputArea(root)
    Label(root, text="Prime (p):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task7inputp = inputArea(root)
    Label(root, text="Prime (q):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task7inputq = inputArea(root)

    Button(root, text="Decrypt", command=RSAdecont, bg="#312F2F", fg="#ffffff").pack(pady=10)
    Task7output = Text(root,width=70,height=20,bg="#312F2F",fg="#ffffff")
    Task7output.pack(pady=10)
"""

def Task8Window():
    global cipher_text, Task8inpute, Task8inputp, Task8inputq, Task8output
    root = Toplevel()
    root.title("RSA Decrypt UTF-8")
    root.geometry("700x700")
    root.configure(bg="#121212")

    Label(root, text="Cipher Text:", bg="#121212", fg="#ffffff").pack(pady=5)
    cipher_text = inputArea(root)
    Label(root, text="Public Exponent (e):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task8inpute = inputArea(root)
    Label(root, text="Prime (p):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task8inputp = inputArea(root)
    Label(root, text="Prime (q):", bg="#121212", fg="#ffffff").pack(pady=5)
    Task8inputq = inputArea(root)

    Button(root, text="Decrypt", command=RSAdecontTask8, bg="#312F2F", fg="#ffffff").pack(pady=10)
    Task8output = Text(root,width=70,height=20,bg="#312F2F",fg="#ffffff")
    Task8output.pack(pady=10)

def railfenceWindow():
    global rail_input, rail_key, rail_output
    root = Toplevel()
    root.title("Rail Fence")
    root.geometry("600x500")
    root.configure(bg="#121212")

    Label(root, text="Text to encrypt:", bg="#121212", fg="#ffffff").pack(pady=5)
    rail_input = inputArea(root)
    Label(root, text="Key (Rows):", bg="#121212", fg="#ffffff").pack(pady=5)
    rail_key = inputArea(root)

    Button(root, text="Run Rail Fence", command=handle_rail, bg="#312F2F", fg="#ffffff").pack(pady=10)
    rail_output = Text(root, width=50, height=10, bg="#312F2F", fg="#ffffff")
    rail_output.pack(pady=10)

def caesarWindow():
    global textforcaesarArea, numberforalphabet, output_text, cipher_mode

    root = Toplevel()
    root.title("Caesar Cipher")
    root.geometry("800x600")
    root.minsize(800, 600)
    root.maxsize(800, 600)
    root.configure(bg="#121212")

    Label1 = Label(root, text="Cipher Method:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    Label1.pack(pady=(10, 0))
    
    cipher_mode = StringVar(value="encrypt")

    radiobtn1 = Radiobutton(
    root,
    text="Encrypt",
    variable=cipher_mode,
    value="encrypt",
    bg="#121212",
    fg="#ffffff",
    selectcolor="#312F2F",
    font=("Arial", 12)
)
    radiobtn1.pack()

    radiobtn2 = Radiobutton(
    root,
    text="Decrypt",
    variable=cipher_mode,
    value="decrypt",
    bg="#121212",
    fg="#ffffff",
    selectcolor="#312F2F",
    font=("Arial", 12)
)
    radiobtn2.pack()
    
    Label2 = Label(root, text="Text for Caesar:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    Label2.pack(pady=(10, 0))
    textforcaesarArea = inputArea(root)
    
    Label3 = Label(root, text="Number for Caesar:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    Label3.pack(pady=(10, 0))
    numberforalphabet = inputArea(root)

    btn_copyright = Button(
        root,
        text="Run Caesar",
        command=handle_process,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_copyright.pack(pady=(10, 0))
    
    ResultArea = Label(root, text="Result:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    ResultArea.pack(pady=(10, 0))

    text_frame = Frame(root, bg="#121212")
    text_frame.pack(pady=5)

    scroll_y = Scrollbar(text_frame, orient=VERTICAL)
    scroll_y.pack(side=RIGHT, fill=Y)

    output_text = Text(text_frame, width=80, height=15, bg="#312F2F", fg="#ffffff", font=("Arial", 12), borderwidth=0, yscrollcommand=scroll_y.set, wrap=WORD)
    output_text.pack(side=LEFT)

    scroll_y.config(command=output_text.yview)

def chooseWindow():
    root = Tk()
    root.title("Cipher Choose")
    root.geometry("300x280")
    root.minsize(300, 280)
    root.maxsize(300, 280)
    root.configure(bg="#121212")

    defaultLabel = Label(root, text="Choose your option: \n", bg="#121212", fg="#ffffff", font=("Arial", 12))
    defaultLabel.pack(pady=(10, 0))
    
    btn_caesar = Button(
        root,
        text="Caesar",
        command=caesarWindow,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_caesar.pack(pady=(10, 0))

    btn_railfence = Button(
        root,
        text="Rail Fence",
        command=railfenceWindow,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_railfence.pack(pady=(10, 0))

    btn_arifmetik = Button(
        root,
        text="Arifmetik",
        command=Arifmetik,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_arifmetik.pack(pady=(10, 0))

    btn_praktik3_1 = Button(
        root,
        text="RSA Math",
        command=questionschoose,
        width=15,
        bg="#312F2F",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_praktik3_1.pack(pady=(10, 0))

    btn_copyright = Button(
        root,
        text="Copyright ©",
        command=Copyright,
        width=15,
        bg="#582B2B",
        fg="#ffffff",
        font=("Arial", 12)
    )
    btn_copyright.pack(pady=(10, 0))
    root.mainloop() 

if __name__ == "__main__":
    chooseWindow()