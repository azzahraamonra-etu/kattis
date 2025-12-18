import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import sys
    current_dir = os.getcwd()
    if os.path.basename(current_dir) == "notebooks":
        # If we are in the notebooks folder, the project root is one level up
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
    else:
        # If we are running from root, just ensure current dir is in path
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
    print(1)
    from src.kattis.counting import counting
    from src.kattis.fallingleaves import fallingleaves
    from src.kattis.favourable import favourable
    from src.kattis.four_thought import four_thought
    from src.kattis.frog_1d_easy import frog_1d_easy
    from src.kattis.goingnuts import goingnuts
    from src.kattis.lvable import lvable
    from src.kattis.popcount import popcount
    from src.kattis.r2 import r2
    from src.kattis.thirteen_floors import thirteen_floors

    # --- 2. Map names to functions ---
    solutions = {
        "Counting": counting,
        "Falling Leaves": fallingleaves,
        "Favourable": favourable,
        "Four Thought": four_thought,
        "Frog 1D Easy": frog_1d_easy,
        "Going Nuts": goingnuts,
        "Lvable": lvable,
        "Popcount": popcount,
        "R2": r2,
        "Thirteen Floors": thirteen_floors,
    }

    # --- 3. Create UI Widgets ---
    problem_selector = mo.ui.dropdown(
        options=solutions,
        value="R2",
        label="Select Problem:"
    )

    input_widget = mo.ui.text_area(
        label="Paste Input Data Here:",
        placeholder="Example: 1 2 ...",
        full_width=True,
        rows=6
    )

    # Display the inputs
    mo.vstack([
        mo.md("# Interactive Kattis Solver"),
        mo.hstack([problem_selector], justify="start"),
        input_widget
    ])
    return input_widget, mo, problem_selector


@app.cell
def _(input_widget, mo, problem_selector):
    # --- 4. Logic & Display ---
    # This cell runs automatically whenever the widgets in Cell 1 change
    def get_result():
        if not input_widget.value:
            return "Waiting for input..."
        try:
            # Get the function chosen in the dropdown and run it
            selected_function = problem_selector.value
            return selected_function(input_widget.value)
        except Exception as e:
            return f"Error: {e}"

    mo.md(f"### Result:\n```text\n{get_result()}\n```")
    return


if __name__ == "__main__":
    app.run()
