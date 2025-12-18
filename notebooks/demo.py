# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import altair as alt

    return alt, mo, np, pd, plt, sns


@app.cell
def _(mo):
    mo.md("""
    # Demo: Thirteen Floors

    This notebook explores the distribution of building floor numbers, focusing on the phenomenon of missing 13th floors in buildings due to superstition. We'll use a simulated dataset to analyze and visualize the data.
    """)
    return


@app.cell
def _(np, pd):
    # Simulate a dataset of building floors
    np.random.seed(42)
    n_buildings = 200
    max_floors = np.random.randint(10, 50, size=n_buildings)
    building_ids = np.arange(1, n_buildings + 1)

    # For each building, create a list of floor numbers, skipping 13
    floors_data = []
    for b_id, n_floors in zip(building_ids, max_floors):
        for floor in range(1, n_floors + 1):
            if floor == 13:
                continue  # skip 13th floor
            floors_data.append({
                "building_id": b_id,
                "floor": floor
            })

    floors_df = pd.DataFrame(floors_data)
    floors_df.head()
    return (floors_df,)


@app.cell
def _(mo):
    mo.md("""
    ## Data Explorer

    Explore the simulated building floors dataset below. Notice that the 13th floor is missing from all buildings.
    """)
    return


@app.cell
def _(floors_df, mo):
    mo.ui.data_explorer(floors_df)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Floor Distribution Visualization

    Select a floor number to see how many buildings have that floor (excluding the 13th floor).
    """)
    return


@app.cell
def _(floors_df, mo):
    # UI: Select a floor number
    available_floors = sorted(floors_df['floor'].unique())
    floor_selector = mo.ui.dropdown(
        options=[str(f) for f in available_floors],
        value=str(12),
        label="Select Floor Number"
    )
    floor_selector
    return available_floors, floor_selector


@app.cell
def _(floor_selector, floors_df):
    # Calculate how many buildings have the selected floor
    selected_floor = int(floor_selector.value)
    buildings_with_floor = floors_df[floors_df['floor'] == selected_floor]['building_id'].nunique()
    buildings_with_floor
    return buildings_with_floor, selected_floor


@app.cell
def _(buildings_with_floor, mo, selected_floor):
    mo.md(f"""
    **Number of buildings with floor {selected_floor}:** {buildings_with_floor}
    """)
    return


@app.cell
def _(floors_df, plt, sns):
    # Visualize the distribution of floors across all buildings
    plt.figure(figsize=(12, 6))
    sns.countplot(x='floor', data=floors_df, color='skyblue')
    plt.title('Distribution of Floor Numbers Across Buildings')
    plt.xlabel('Floor Number')
    plt.ylabel('Number of Occurrences')
    plt.xticks(rotation=90)
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md("""
    ## Altair Interactive Visualization

    Use the slider to highlight a specific floor in the distribution.
    """)
    return


@app.cell
def _(available_floors, mo):
    # UI: Slider for floor selection in Altair chart
    floor_slider = mo.ui.slider(
        start=min(available_floors),
        stop=max(available_floors),
        value=12,
        label="Highlight Floor"
    )
    floor_slider
    return (floor_slider,)


@app.cell
def _(alt, floor_slider, floors_df, mo):
    # Altair chart: highlight selected floor
    floor_counts = floors_df['floor'].value_counts().reset_index()
    floor_counts.columns = ['floor', 'count']
    floor_counts['highlight'] = floor_counts['floor'] == floor_slider.value

    chart = alt.Chart(floor_counts).mark_bar().encode(
        x=alt.X('floor:O', title='Floor Number'),
        y=alt.Y('count:Q', title='Number of Occurrences'),
        color=alt.condition(
            alt.datum.highlight,
            alt.value('orange'),
            alt.value('steelblue')
        ),
        tooltip=['floor', 'count']
    ).properties(
        width=700,
        height=400,
        title='Floor Number Distribution (Highlight Selected)'
    )
    mo.ui.altair_chart(chart)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Conclusion

    This demo illustrates how the 13th floor is systematically omitted from building floor numbering, a practice rooted in superstition. The interactive tools above allow you to explore the impact of this omission on floor distributions.
    """)
    return


if __name__ == "__main__":
    app.run()
