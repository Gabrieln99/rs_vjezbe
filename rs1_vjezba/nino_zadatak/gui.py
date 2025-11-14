import tkinter as tk
from tkinter import ttk
from nino_telefonino import validiraj_broj_telefona


class TelefonValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validator Telefonskih Brojeva")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Postavi boju pozadine
        self.root.configure(bg="#f0f0f0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Glavni naslov
        title_label = tk.Label(
            self.root,
            text="🔍 Validator Hrvatskih Telefonskih Brojeva",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Frame za unos
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10, padx=20, fill="x")
        
        # Label za unos
        input_label = tk.Label(
            input_frame,
            text="Unesite telefonski broj:",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#34495e"
        )
        input_label.pack(anchor="w", pady=(0, 5))
        
        # Entry polje za unos broja
        self.phone_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=40,
            relief="solid",
            borderwidth=1
        )
        self.phone_entry.pack(fill="x", pady=(0, 10))
        self.phone_entry.bind("<Return>", lambda e: self.validate_phone())
        
        # Gumb za validaciju
        validate_btn = tk.Button(
            input_frame,
            text="Validiraj",
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.validate_phone
        )
        validate_btn.pack()
        
        # Frame za rezultate
        self.result_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=1)
        self.result_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Naslov rezultata
        result_title = tk.Label(
            self.result_frame,
            text="Rezultati validacije:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        result_title.pack(pady=(15, 10))
        
        # Frame za detalje
        self.details_frame = tk.Frame(self.result_frame, bg="white")
        self.details_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Placeholder tekst
        self.placeholder = tk.Label(
            self.details_frame,
            text="Unesite broj telefona i kliknite 'Validiraj'",
            font=("Arial", 10, "italic"),
            bg="white",
            fg="#95a5a6"
        )
        self.placeholder.pack(pady=50)
        
        # Footer
        footer = tk.Label(
            self.root,
            text="Podržani formati: +385..., 00385..., 0...",
            font=("Arial", 9, "italic"),
            bg="#f0f0f0",
            fg="#7f8c8d"
        )
        footer.pack(pady=(0, 10))
    
    def validate_phone(self):
        # Očisti prethodne rezultate
        for widget in self.details_frame.winfo_children():
            widget.destroy()
        
        phone_number = self.phone_entry.get().strip()
        
        if not phone_number:
            self.show_error("Molimo unesite telefonski broj!")
            return
        
        try:
            result = validiraj_broj_telefona(phone_number)
            self.display_result(result)
        except Exception as e:
            self.show_error(f"Greška: {str(e)}")
    
    def display_result(self, result):
        # Status validacije
        is_valid = result.get("validan", False)
        status_color = "#27ae60" if is_valid else "#e74c3c"
        status_text = "✓ VALIDAN" if is_valid else "✗ NEVALIDAN"
        
        status_label = tk.Label(
            self.details_frame,
            text=status_text,
            font=("Arial", 14, "bold"),
            bg="white",
            fg=status_color
        )
        status_label.pack(pady=(10, 20))
        
        # Prikaz detalja
        details = [
            ("Pozivni broj:", result.get("pozivni_broj", "N/A")),
            ("Preostali broj:", result.get("broj_ostatak", "N/A")),
            ("Vrsta:", result.get("vrsta", "N/A")),
            ("Mjesto:", result.get("mjesto", "N/A")),
            ("Operater:", result.get("operater", "N/A"))
        ]
        
        for label_text, value in details:
            if value and value != "N/A":
                detail_frame = tk.Frame(self.details_frame, bg="white")
                detail_frame.pack(fill="x", pady=5, padx=10)
                
                label = tk.Label(
                    detail_frame,
                    text=label_text,
                    font=("Arial", 10, "bold"),
                    bg="white",
                    fg="#34495e",
                    width=15,
                    anchor="w"
                )
                label.pack(side="left")
                
                value_label = tk.Label(
                    detail_frame,
                    text=str(value),
                    font=("Arial", 10),
                    bg="white",
                    fg="#2c3e50",
                    anchor="w"
                )
                value_label.pack(side="left", fill="x", expand=True)
    
    def show_error(self, message):
        error_label = tk.Label(
            self.details_frame,
            text=message,
            font=("Arial", 11),
            bg="white",
            fg="#e74c3c"
        )
        error_label.pack(pady=50)


def main():
    root = tk.Tk()
    app = TelefonValidatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
