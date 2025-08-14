import tkinter as tk
from tkinter import messagebox

# ---------- Actions ----------
def show_results():
    destination = dest_entry.get().strip()
    budget = budget_entry.get().strip()
    people = people_entry.get().strip()

    if not destination or not budget or not people:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Hide form, show results
    form_frame.pack_forget()
    results_frame.pack(fill="both", expand=True, pady=20)

    # Clear previous widgets
    for widget in results_frame.winfo_children():
        widget.destroy()

    # Title
    tk.Label(results_frame, text=f"Travel Options for {destination}", font=("Arial", 14, "bold")).pack(pady=10)

    # Flights Section
    tk.Label(results_frame, text="✈ Flights", font=("Arial", 12, "underline")).pack()
    tk.Button(results_frame, text="Book Flight ($200)", width=25, bg="#4CAF50", fg="white",
              command=lambda: messagebox.showinfo("Booking", "Flight booked!")).pack(pady=5)

    # Hotels Section
    tk.Label(results_frame, text="🏨 Hotels", font=("Arial", 12, "underline")).pack(pady=(20,0))
    tk.Button(results_frame, text="Book Hotel ($100/night)", width=25, bg="#2196F3", fg="white",
              command=lambda: messagebox.showinfo("Booking", "Hotel booked!")).pack(pady=5)

    # Back Button
    tk.Button(results_frame, text="← Back", width=15, command=show_form).pack(pady=20)

def show_form():
    results_frame.pack_forget()
    form_frame.pack(fill="both", expand=True, pady=20)

# ---------- Root Window ----------
root = tk.Tk()
root.title("Travel Agent")
root.geometry("350x400")
root.configure(bg="#f4f4f4")

# ---------- Form Screen ----------
form_frame = tk.Frame(root, bg="#f4f4f4")
form_frame.pack(fill="both", expand=True, pady=20)

tk.Label(form_frame, text="Travel Agent", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

tk.Label(form_frame, text="Destination:", anchor="w", bg="#f4f4f4").pack(pady=(10,0))
dest_entry = tk.Entry(form_frame, width=30)
dest_entry.pack()

tk.Label(form_frame, text="Budget:", anchor="w", bg="#f4f4f4").pack(pady=(10,0))
budget_entry = tk.Entry(form_frame, width=30)
budget_entry.pack()

tk.Label(form_frame, text="Number of people:", anchor="w", bg="#f4f4f4").pack(pady=(10,0))
people_entry = tk.Entry(form_frame, width=30)
people_entry.pack()

tk.Button(form_frame, text="Search", width=20, bg="#4CAF50", fg="white", command=show_results).pack(pady=20)

# ---------- Results Screen ----------
results_frame = tk.Frame(root, bg="#f4f4f4")

root.mainloop()
