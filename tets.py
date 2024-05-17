import tkinter as tk
from tkinter import ttk

# Define a function that will be called when the button is clicked
def find_shortest_path():
    driver_code = driver_code_entry.get()
    departure_date = departure_date_entry.get()
    departure_location = departure_location_entry.get()
    destination = destination_entry.get()
    expected_time = expected_time_entry.get()
    # Code to calculate and display the shortest path

# Create the main window
root = tk.Tk()
root.title("Find Shortest Path")

# Create labels and entry widgets
tk.Label(root, text="Driver Code:").grid(row=0, column=0)
driver_code_entry = tk.Entry(root)
driver_code_entry.grid(row=0, column=1)

tk.Label(root, text="Mã chuyến xe:").grid(row=1, column=0)
taxi_code_entry = tk.Entry(root)
taxi_code_entry.grid(row=1, column=1)

tk.Label(root, text="Ngày xuất phát:").grid(row=2, column=0)
departure_date_entry = tk.Entry(root)
departure_date_entry.grid(row=2, column=1)

tk.Label(root, text="Địa điểm xuất phát:").grid(row=3, column=0)
departure_location_entry = tk.Entry(root)
departure_location_entry.grid(row=3, column=1)

tk.Label(root, text="Địa điểm đến:").grid(row=4, column=0)
destination_entry = tk.Entry(root)
destination_entry.grid(row=4, column=1)

tk.Label(root, text="Thời gian dự kiến:").grid(row=5, column=0)
expected_time_entry = tk.Entry(root)
expected_time_entry.grid(row=5, column=1)

# Create a button
find_shortest_path_button = tk.Button(root, text="Tìm đường", command=find_shortest_path)
find_shortest_path_button.grid(row=6, column=0, columnspan=2)

# Start the main loop
root.mainloop()