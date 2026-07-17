# ============================================================
# MODERN GUI MODULE
# ============================================================

import webbrowser
import customtkinter as ctk
from tkinter import filedialog, messagebox

from engine import plagiarism_search
from document_reader import read_document


def start_gui():

    # -----------------------------
    # App Configuration
    # -----------------------------
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Intelligent Plagiarism Detector")
    app.geometry("820x520")


    # -----------------------------
    # Header
    # -----------------------------
    header = ctk.CTkLabel(
        app,
        text="AI Plagiarism Detection System",
        font=("Segoe UI", 28, "bold")
    )
    header.pack(pady=20)


    # -----------------------------
    # File Selection Frame
    # -----------------------------
    file_frame = ctk.CTkFrame(app)
    file_frame.pack(fill="x", padx=40, pady=10)

    file_label = ctk.CTkLabel(
        file_frame,
        text="No document selected",
        font=("Segoe UI", 14)
    )
    file_label.pack(pady=15)

    selected_file = {"path": None}


    # -----------------------------
    # Status Label
    # -----------------------------
    status_label = ctk.CTkLabel(
        app,
        text="Status: Waiting for document...",
        font=("Segoe UI", 13)
    )
    status_label.pack(pady=5)


    # -----------------------------
    # Progress Bar
    # -----------------------------
    progress = ctk.CTkProgressBar(app, width=500)
    progress.set(0)
    progress.pack(pady=10)


    # -----------------------------
    # Result Box
    # -----------------------------
    result_box = ctk.CTkTextbox(
        app,
        width=700,
        height=200,
        font=("Consolas", 13)
    )
    result_box.pack(pady=15)

    result_box.insert("0.0", "Plagiarism results will appear here...")
    result_box.configure(state="disabled")


    # -----------------------------
    # Functions
    # -----------------------------
    def select_document():

        path = filedialog.askopenfilename(
            title="Select Document",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Word Files", "*.docx"),
                ("PDF Files", "*.pdf")
            ]
        )

        if path:
            selected_file["path"] = path
            file_label.configure(text=path)


    def run_detection():

        if not selected_file["path"]:
            messagebox.showwarning("Warning", "Please select a document first")
            return

        try:

            status_label.configure(text="Loading document...")

            doc = read_document(selected_file["path"])

            status_label.configure(text="Running plagiarism detection...")
            progress.start()

            report = plagiarism_search(doc)

            progress.stop()

            status_label.configure(text="Report generated successfully")

            result_box.configure(state="normal")
            result_box.delete("0.0", "end")
            result_box.insert("0.0", report)
            result_box.configure(state="disabled")

            webbrowser.open("plagiarism_report.html")

        except Exception as e:

            progress.stop()
            status_label.configure(text="Error occurred")

            messagebox.showerror("Error", str(e))


    # -----------------------------
    # Buttons
    # -----------------------------
    button_frame = ctk.CTkFrame(app)
    button_frame.pack(pady=10)

    select_btn = ctk.CTkButton(
        button_frame,
        text="Select Document",
        width=180,
        command=select_document
    )
    select_btn.grid(row=0, column=0, padx=15)

    scan_btn = ctk.CTkButton(
        button_frame,
        text="Run Plagiarism Scan",
        width=180,
        command=run_detection
    )
    scan_btn.grid(row=0, column=1, padx=15)

    report_btn = ctk.CTkButton(
        button_frame,
        text="Open HTML Report",
        width=180,
        command=lambda: webbrowser.open("plagiarism_report.html")
    )
    report_btn.grid(row=0, column=2, padx=15)


    # -----------------------------
    # Footer
    # -----------------------------
    footer = ctk.CTkLabel(
        app,
        text="AI Powered Detection Engine",
        font=("Segoe UI", 11)
    )
    footer.pack(pady=10)


    app.mainloop()