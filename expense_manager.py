import customtkinter as ctk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime


# =========================
# Appearance
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================
# Main Application
# =========================

class Rent_App(ctk.CTk):

    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.bill_data = None
        self.bill_number = None

        self.title("Hostel & Flat Expense Manager")
        self.geometry("760x720")
        self.minsize(620, 500)

        # Main Form
        self.formBox = ctk.CTkScrollableFrame(
            self,
            corner_radius=20,
            border_width=1
        )
        self.formBox.pack(
            padx=14, pady=14, fill="both", expand=True
        )

        self.formBox.grid_columnconfigure(1, weight=1)

        # Title
        self.titleLabel = ctk.CTkLabel(
            self.formBox,
            text="HOSTEL & FLAT EXPENSE MANAGER",
            font=("Segoe UI", 25, "bold")
        )
        self.titleLabel.grid(
            row=0, column=0, columnspan=2,
            padx=20, pady=(12, 8)
        )

        # Rent
        self.rentLabel = ctk.CTkLabel(
            self.formBox, text="Rent:",
            font=("Segoe UI", 17, "bold")
        )
        self.rentLabel.grid(
            row=1, column=0, padx=20, pady=4, sticky="w"
        )

        self.rentEntry = ctk.CTkEntry(
            self.formBox,
            placeholder_text="Enter monthly rent",
            height=40, font=("Segoe UI", 14)
        )
        self.rentEntry.grid(
            row=1, column=1, padx=20, pady=4, sticky="ew"
        )

        # Food
        self.foodLabel = ctk.CTkLabel(
            self.formBox, text="Food:",
            font=("Segoe UI", 17, "bold")
        )
        self.foodLabel.grid(
            row=2, column=0, padx=20, pady=4, sticky="w"
        )

        self.foodEntry = ctk.CTkEntry(
            self.formBox,
            placeholder_text="Enter total food expense",
            height=40, font=("Segoe UI", 14)
        )
        self.foodEntry.grid(
            row=2, column=1, padx=20, pady=4, sticky="ew"
        )

        # Electricity Units
        self.electricity_unitsLabel = ctk.CTkLabel(
            self.formBox, text="Electricity Units:",
            font=("Segoe UI", 17, "bold")
        )
        self.electricity_unitsLabel.grid(
            row=3, column=0, padx=20, pady=4, sticky="w"
        )

        self.electricity_unitsEntry = ctk.CTkEntry(
            self.formBox,
            placeholder_text="Enter electricity units",
            height=40, font=("Segoe UI", 14)
        )
        self.electricity_unitsEntry.grid(
            row=3, column=1, padx=20, pady=4, sticky="ew"
        )

        # Charge Per Unit
        self.charge_per_unitsLabel = ctk.CTkLabel(
            self.formBox, text="Charge Per Unit:",
            font=("Segoe UI", 17, "bold")
        )
        self.charge_per_unitsLabel.grid(
            row=4, column=0, padx=20, pady=4, sticky="w"
        )

        self.charge_per_unitsEntry = ctk.CTkEntry(
            self.formBox,
            placeholder_text="Enter charge per unit",
            height=40, font=("Segoe UI", 14)
        )
        self.charge_per_unitsEntry.grid(
            row=4, column=1, padx=20, pady=4, sticky="ew"
        )

        # Number of Persons
        self.personsLabel = ctk.CTkLabel(
            self.formBox, text="Number of Persons:",
            font=("Segoe UI", 17, "bold")
        )
        self.personsLabel.grid(
            row=5, column=0, padx=20, pady=4, sticky="w"
        )

        self.personsOption = ctk.CTkOptionMenu(
            self.formBox,
            values=["2", "4", "6", "8", "10"],
            font=("Segoe UI", 14),
            height=38
        )
        self.personsOption.set("2")
        self.personsOption.grid(
            row=5, column=1, padx=20, pady=4, sticky="ew"
        )

        # Calculate Button
        self.generateResultsButton = ctk.CTkButton(
            self.formBox,
            text="Calculate Expenses",
            font=("Segoe UI", 15, "bold"),
            height=44,
            command=self.calculate_bill
        )
        self.generateResultsButton.grid(
            row=6, column=0,
            padx=(20, 10), pady=8, sticky="ew"
        )

        # Download PDF Button
        self.downloadButton = ctk.CTkButton(
            self.formBox,
            text="Download PDF",
            font=("Segoe UI", 15, "bold"),
            height=44,
            command=self.download_bill
        )
        self.downloadButton.grid(
            row=6, column=1,
            padx=(10, 20), pady=8, sticky="ew"
        )

        # Dashboard
        self.summaryFrame = ctk.CTkFrame(
            self.formBox, fg_color="transparent"
        )
        self.summaryFrame.grid(
            row=7, column=0, columnspan=2,
            padx=20, pady=4, sticky="ew"
        )
        self.summaryFrame.grid_columnconfigure((0, 1), weight=1)

        # Total Card
        self.totalCard = ctk.CTkFrame(
            self.summaryFrame, corner_radius=14
        )
        self.totalCard.grid(
            row=0, column=0, padx=5, pady=5, sticky="ew"
        )

        self.totalTitle = ctk.CTkLabel(
            self.totalCard,
            text="TOTAL BILL",
            font=("Segoe UI", 13, "bold")
        )
        self.totalTitle.pack(padx=15, pady=(15, 5))

        self.totalValue = ctk.CTkLabel(
            self.totalCard,
            text="Rs. 0.00",
            font=("Segoe UI", 23, "bold")
        )
        self.totalValue.pack(padx=15, pady=(0, 15))

        # Per Person Card
        self.personCard = ctk.CTkFrame(
            self.summaryFrame, corner_radius=14
        )
        self.personCard.grid(
            row=0, column=1, padx=5, pady=5, sticky="ew"
        )

        self.personTitle = ctk.CTkLabel(
            self.personCard,
            text="PER PERSON",
            font=("Segoe UI", 13, "bold")
        )
        self.personTitle.pack(padx=15, pady=(15, 5))

        self.personValue = ctk.CTkLabel(
            self.personCard,
            text="Rs. 0.00",
            font=("Segoe UI", 23, "bold")
        )
        self.personValue.pack(padx=15, pady=(0, 15))

        # Bill Summary Display
        self.displayBox = ctk.CTkTextbox(
            self.formBox,
            height=150,
            font=("Consolas", 13),
            corner_radius=10
        )
        self.displayBox.grid(
            row=8, column=0, columnspan=2,
            padx=20, pady=(5, 10), sticky="ew"
        )

        # Reset Button
        self.resetButton = ctk.CTkButton(
            self.formBox,
            text="Reset Form",
            font=("Segoe UI", 14, "bold"),
            height=40,
            command=self.reset_form
        )
        self.resetButton.grid(
            row=9, column=0, columnspan=2,
            padx=20, pady=5, sticky="ew"
        )

        # Apply initial dark theme
        self.apply_theme()

    # =========================
    # Dark Mode Theme
    # =========================

    def apply_theme(self):
        bg = "#0B1120"
        form = "#111C2E"
        card = "#17263D"
        entry_bg = "#0B1424"
        text = "#E2E8F0"
        title_text = "#F8FAFC"
        muted = "#94A3B8"
        border = "#263B57"
        button_bg = "#2563EB"
        secondary_button = "#1E3A5F"
        reset_bg = "#263B57"
        total_color = "#60A5FA"
        person_color = "#38BDF8"

        self.configure(fg_color=bg)

        self.formBox.configure(
            fg_color=form,
            border_color=border,
            scrollbar_button_color=border,
            scrollbar_button_hover_color=button_bg
        )

        self.titleLabel.configure(text_color=title_text)

        for label in (
            self.rentLabel,
            self.foodLabel,
            self.electricity_unitsLabel,
            self.charge_per_unitsLabel,
            self.personsLabel
        ):
            label.configure(text_color=text)

        for entry in (
            self.rentEntry,
            self.foodEntry,
            self.electricity_unitsEntry,
            self.charge_per_unitsEntry
        ):
            entry.configure(
                fg_color=entry_bg,
                text_color=text,
                placeholder_text_color=muted,
                border_color=border
            )

        self.personsOption.configure(
            fg_color=secondary_button,
            button_color=button_bg,
            button_hover_color="#1D4ED8",
            dropdown_fg_color=form,
            dropdown_hover_color=border,
            text_color=text,
            dropdown_text_color=text
        )

        for frame in (self.totalCard, self.personCard):
            frame.configure(
                fg_color=card,
                border_width=1,
                border_color=border
            )

        self.totalTitle.configure(text_color=muted)
        self.personTitle.configure(text_color=muted)
        self.totalValue.configure(text_color=total_color)
        self.personValue.configure(text_color=person_color)

        self.displayBox.configure(
            fg_color=entry_bg,
            text_color=text,
            border_color=border,
            scrollbar_button_color=border,
            scrollbar_button_hover_color=button_bg
        )

        self.generateResultsButton.configure(
            fg_color=button_bg,
            hover_color="#1D4ED8",
            text_color="#FFFFFF"
        )

        self.downloadButton.configure(
            fg_color=secondary_button,
            hover_color=button_bg,
            text_color=text
        )

        self.resetButton.configure(
            fg_color=reset_bg,
            hover_color=border,
            text_color=text
        )

    # =========================
    # Calculate Bill
    # =========================

    def calculate_bill(self):
        try:
            rent = float(self.rentEntry.get())
            food = float(self.foodEntry.get())
            electricity_units = float(
                self.electricity_unitsEntry.get()
            )
            charge_per_unit = float(
                self.charge_per_unitsEntry.get()
            )
            persons = int(self.personsOption.get())

            if rent < 0:
                raise ValueError("Rent cannot be negative.")
            if food < 0:
                raise ValueError("Food expense cannot be negative.")
            if electricity_units < 0:
                raise ValueError("Electricity units cannot be negative.")
            if charge_per_unit < 0:
                raise ValueError("Charge per unit cannot be negative.")

            electricity_bill = electricity_units * charge_per_unit
            total_bill = rent + food + electricity_bill
            per_person = total_bill / persons

            bill_date = datetime.now()
            self.bill_number = "HFE-" + bill_date.strftime(
                "%Y%m%d-%H%M%S"
            )

            self.bill_data = {
                "bill_number": self.bill_number,
                "date": bill_date.strftime("%d %B %Y, %I:%M %p"),
                "rent": rent,
                "food": food,
                "electricity_units": electricity_units,
                "charge_per_unit": charge_per_unit,
                "electricity_bill": electricity_bill,
                "total_bill": total_bill,
                "persons": persons,
                "per_person": per_person
            }

            self.totalValue.configure(
                text=f"Rs. {total_bill:,.2f}"
            )
            self.personValue.configure(
                text=f"Rs. {per_person:,.2f}"
            )

            self.displayBox.delete("1.0", "end")
            self.displayBox.insert(
                "end",
                "========== BILL SUMMARY ==========\n\n"
                f"Bill Number:       {self.bill_number}\n"
                f"Date:              {self.bill_data['date']}\n\n"
                f"Rent:              Rs. {rent:,.2f}\n"
                f"Food:              Rs. {food:,.2f}\n"
                f"Electricity Units: {electricity_units:g}\n"
                f"Rate Per Unit:     Rs. {charge_per_unit:,.2f}\n"
                f"Electricity:       Rs. {electricity_bill:,.2f}\n"
                "----------------------------------\n"
                f"Total Bill:        Rs. {total_bill:,.2f}\n"
                f"Number of Persons: {persons}\n"
                f"Each Person Pays:  Rs. {per_person:,.2f}"
            )

        except ValueError as error:
            self.bill_data = None
            self.bill_number = None

            self.totalValue.configure(text="Rs. 0.00")
            self.personValue.configure(text="Rs. 0.00")

            self.displayBox.delete("1.0", "end")
            self.displayBox.insert(
                "end", f"Invalid input: {error}"
            )

    # =========================
    # Reset Form
    # =========================

    def reset_form(self):
        self.rentEntry.delete(0, "end")
        self.foodEntry.delete(0, "end")
        self.electricity_unitsEntry.delete(0, "end")
        self.charge_per_unitsEntry.delete(0, "end")

        self.personsOption.set("2")
        self.displayBox.delete("1.0", "end")

        self.totalValue.configure(text="Rs. 0.00")
        self.personValue.configure(text="Rs. 0.00")

        self.bill_data = None
        self.bill_number = None

    # =========================
    # Simple PDF Download
    # =========================

    def download_bill(self):
        if self.bill_data is None:
            messagebox.showwarning(
                "Warning",
                "Please calculate the bill first."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile=f"{self.bill_number}.pdf",
            title="Save Bill"
        )

        if not file_path:
            return

        try:
            pdf = canvas.Canvas(file_path, pagesize=A4)
            width, height = A4

            pdf.setFont("Helvetica-Bold", 18)
            pdf.drawCentredString(
                width / 2,
                height - 60,
                "HOSTEL & FLAT EXPENSE RECEIPT"
            )

            pdf.setFont("Helvetica", 11)
            pdf.drawString(
                50, height - 110,
                f"Bill Number: {self.bill_data['bill_number']}"
            )
            pdf.drawString(
                50, height - 135,
                f"Date: {self.bill_data['date']}"
            )

            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, height - 180, "Bill Details")

            pdf.setFont("Helvetica", 12)
            pdf.drawString(
                50, height - 215,
                f"Rent: Rs. {self.bill_data['rent']:,.2f}"
            )
            pdf.drawString(
                50, height - 245,
                f"Food: Rs. {self.bill_data['food']:,.2f}"
            )
            pdf.drawString(
                50, height - 275,
                f"Electricity Units: "
                f"{self.bill_data['electricity_units']:g}"
            )
            pdf.drawString(
                50, height - 305,
                f"Rate Per Unit: Rs. "
                f"{self.bill_data['charge_per_unit']:,.2f}"
            )
            pdf.drawString(
                50, height - 335,
                f"Electricity Bill: Rs. "
                f"{self.bill_data['electricity_bill']:,.2f}"
            )

            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(
                50, height - 385,
                f"Total Bill: Rs. "
                f"{self.bill_data['total_bill']:,.2f}"
            )
            pdf.drawString(
                50, height - 420,
                f"Number of Persons: {self.bill_data['persons']}"
            )
            pdf.drawString(
                50, height - 455,
                f"Per Person Amount: Rs. "
                f"{self.bill_data['per_person']:,.2f}"
            )

            pdf.setFont("Helvetica-Oblique", 10)
            pdf.drawCentredString(
                width / 2,
                50,
                "Generated by Hostel & Flat Expense Manager"
            )

            pdf.save()

            messagebox.showinfo(
                "Success",
                "PDF saved successfully!"
            )

        except Exception as error:
            messagebox.showerror(
                "PDF Error",
                f"Could not save PDF:\n{error}"
            )


# =========================
# Run Application
# =========================

if __name__ == "__main__":
    app = Rent_App()
    app.mainloop()
