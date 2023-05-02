






from tkinter import *
from tkinter import messagebox

class RecipeHaven:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Haven")
        self.master.geometry("500x500")

        # create the menu bar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create the file menu
        file_menu = Menu(menubar)
        file_menu.add_command(label="New Recipe", command=self.new_recipe)
        file_menu.add_command(label="Save Recipe", command=self.save_recipe)
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        # create the edit menu
        edit_menu = Menu(menubar)
        edit_menu.add_command(label="Edit Recipe", command=self.edit_recipe)
        edit_menu.add_command(label="Delete Recipe", command=self.delete_recipe)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # create the search box
        search_label = Label(self.master, text="Search Recipe: ")
        search_label.grid(row=0, column=0)

        self.search_entry = Entry(self.master)
        self.search_entry.grid(row=0, column=1)

        search_button = Button(self.master, text="Search", command=self.search_recipe)
        search_button.grid(row=0, column=2)

        # create the recipe listbox
        self.recipe_listbox = Listbox(self.master)
        self.recipe_listbox.grid(row=1, column=0, columnspan=3)

        # create the recipe details frame
        details_frame = Frame(self.master)
        details_frame.grid(row=2, column=0, columnspan=3)

        # create the recipe details labels
        name_label = Label(details_frame, text="Recipe Name: ")
        name_label.grid(row=0, column=0)

        ingredients_label = Label(details_frame, text="Ingredients: ")
        ingredients_label.grid(row=1, column=0)

        directions_label = Label(details_frame, text="Directions: ")
        directions_label.grid(row=2, column=0)

        # create the recipe details textboxes
        self.name_textbox = Text(details_frame, height=1, width=30)
        self.name_textbox.grid(row=0, column=1)

        self.ingredients_textbox = Text(details_frame, height=5, width=30)
        self.ingredients_textbox.grid(row=1, column=1)

        self.directions_textbox = Text(details_frame, height=10, width=30)
        self.directions_textbox.grid(row=2, column=1)

        # load the recipes
        self.recipes = []
        self.load_recipes()

        # select the first recipe in the listbox
        self.recipe_listbox.selection_set(0)

        # show the details of the selected recipe
        self.show_recipe_details()

    def new_recipe(self):
        self.name_textbox.delete(1.0, END)
        self.ingredients_textbox.delete(1.0, END)
        self.directions_textbox.delete(1.0, END)

    def edit_recipe(self):
        # get the recipe name from the entry widget
        recipe_name = self.recipe_name.get()

        # make sure the recipe exists
        if recipe_name not in self.recipes:
            messagebox.showerror("Error", "Recipe not found.")
            return

        # get the current recipe data
        current_ingredients = self.recipes[recipe_name]["ingredients"]
        current_directions = self.recipes[recipe_name]["directions"]

        # update the ingredient and direction text widgets with current data
        self.ingredients_text.delete(1.0, END)
        self.ingredients_text.insert(END, current_ingredients)

        self.directions_text.delete(1.0, END)
        self.directions_text.insert(END, current_directions)

        # update the recipe data with user input
        new_ingredients = self.ingredients_text.get(1.0, END)
        new_directions = self.directions_text.get(1.0, END)

        self.recipes[recipe_name]["ingredients"] = new_ingredients
        self.recipes[recipe_name]["directions"] = new_directions

        # save the updated recipe data to file
        self.save_recipes()

        # notify the user that the recipe has been updated
        messagebox.showinfo("Success", "Recipe updated successfully.")

    def save_recipe(self):
        name = self.name_textbox.get("1.0", END).strip()
        ingredients = self.ingredients_textbox.get("1.0", END).strip()
        directions = self.directions_textbox.get("1.0", END).strip()

        # check if all fields are filled

    def delete_recipe(self):
        # get the recipe name from the listbox widget
        selected_recipe = self.recipe_listbox.get(ACTIVE)

        # make sure the recipe exists
        if selected_recipe not in self.recipes:
            messagebox.showerror("Error", "Recipe not found.")
            return

        # delete the recipe from the dictionary
        del self.recipes[selected_recipe]

        # clear the text widgets and the recipe listbox
        self.recipe_name.delete(0, END)
        self.ingredients_text.delete(1.0, END)
        self.directions_text.delete(1.0, END)
        self.recipe_listbox.delete(0, END)

        # re-populate the recipe listbox with updated data
        self.populate_recipe_listbox()

        # save the updated recipe data to file
        self.save_recipes()

        # notify the user that the recipe has been deleted
        messagebox.showinfo("Success", "Recipe deleted successfully.")

    def search_recipe(self):
        # get the search term from the user
        search_term = simpledialog.askstring("Search Recipes", "Enter a search term:")

        # clear the recipe listbox
        self.recipe_listbox.delete(0, END)

        # search for recipes containing the search term and add them to the recipe listbox
        for recipe_name in self.recipes:
            if search_term.lower() in recipe_name.lower():
                self.recipe_listbox.insert(END, recipe_name)

    def load_recipes(self):
        # clear the recipe listbox
        self.recipe_listbox.delete(0, END)

        # load the recipes from the file
        try:
            with open(self.recipe_file, 'r') as file:
                self.recipes = json.load(file)
        except FileNotFoundError:
            self.recipes = {}

        # add the recipe names to the recipe listbox
        for recipe_name in self.recipes:
            self.recipe_listbox.insert(END, recipe_name)



    def run(self):
        root = Tk()
        app = RecipeHaven(root)
        root.mainloop()

    def exit_app(self):
        self.master.destroy()
        

if __name__ == "__main__":
    root = Tk()
    app = RecipeHaven(root)
    root.mainloop()

    converter_gui = RecipeHaven()
    converter_gui.run()
