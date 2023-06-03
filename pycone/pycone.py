"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pigra", font_size="2em"),
            pc.box("A place for all your Data Visualization Needs!!"),
 pc.upload(
            pc.vstack(
                pc.button(
                    "Select File",
                                   bg="white",
                    border=f"1px solid black",
                ),
                pc.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            multiple=True,
            accept={
                         "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                    },
            max_files=1,
            disabled=False,
            on_keyboard=True,
            border=f"1px dotted black",
            padding="5em",
        ),            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
