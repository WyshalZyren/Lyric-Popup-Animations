import tkinter as tk
import pygame
import time


# SETTINGS

SONG = "song.mp3"

COLOR_SWITCH_MS = 1000

CARD_LIFETIME_MS = 5200

ANIMATION_FRAMES = 13
ANIMATION_SPEED = 14

SLIDE_SPEED = 12

# LYRICS

lyrics = [
    (0.00, "𑣲⋆"),

    (5.00, "AND I REMEBER ALL THOSE CRAZY THINGS YOU SAID"),
    (8.30, "YOU LEFT THEM RUNNIN' THROUGH MY HEAD"),
    (11.50, "YOU'RE ALWAYS THERE, YOU'RE EVERYWERE"),

    (14.40, "BUT RIGHT NOW, I WISH YOU WERE HERE"),
    (17.50, "ALL THOSE CRAZY THINGS WE DID"),
    (20.30, "DIDN'T THINK ABOUT IT, JUST WENT WITH IT"),
    (23.10, "YOU'RE ALWAYS THERE, YOU'RE EVERYWHERE"),

    (26.00, "BUT RIGHT NOW, I WISH YOU WERE HERE"),
    (28.90, "DAMN, DAMN, DAMN"),
    (32.60, "WHAT I'D DO TO HAVE YOU HERE, HERE, HERE"),

    (38.50, "I WISH YOU WERE HERE"),
    (40.40, "DAMN, DAMN, DAMN"),
    (44.40, "WHAT I'D DO TO HAVE YOU NEAR, NEAR, NEAR")
]


root = tk.Tk()

root.withdraw()

root.update_idletasks()


# Screen size
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()


LEFT_X = 30
CENTER_X = SCREEN_WIDTH // 2
RIGHT_X = SCREEN_WIDTH - 30

TOP_Y = 50
MIDDLE_Y = SCREEN_HEIGHT // 2 - 80
BOTTOM_Y = SCREEN_HEIGHT - 210


placements = [

    # 1 - TOP LEFT
    (
        LEFT_X,
        TOP_Y,
        360,
        110
    ),

    # 2 - TOP CENTER
    (
        CENTER_X - 210,
        TOP_Y,
        420,
        115
    ),

    # 3 - TOP RIGHT
    (
        RIGHT_X - 360,
        TOP_Y,
        360,
        110
    ),


    # 4 - MIDDLE LEFT
    (
        LEFT_X,
        MIDDLE_Y,
        390,
        115
    ),

    # 5 - CENTER
    (
        CENTER_X - 210,
        MIDDLE_Y,
        420,
        120
    ),

    # 6 - MIDDLE RIGHT
    (
        RIGHT_X - 390,
        MIDDLE_Y,
        390,
        115
    ),


    # 7 - BOTTOM LEFT
    (
        LEFT_X,
        BOTTOM_Y,
        360,
        110
    ),

    # 8 - BOTTOM CENTER
    (
        CENTER_X - 210,
        BOTTOM_Y,
        420,
        115
    ),

    # 9 - BOTTOM RIGHT
    (
        RIGHT_X - 360,
        BOTTOM_Y,
        360,
        110
    )
]


popup_index = 0


# PYGAME
pygame.mixer.init()


def show_lyric(text):

    global popup_index

    position = placements[
        popup_index % len(placements)
    ]

    popup_index += 1


    x, y, final_width, final_height = position


    popup = tk.Toplevel(root)

    popup.title("")

    popup.attributes(
        "-topmost",
        True
    )


    # Start white
    popup.configure(
        bg="white"
    )



    start_width = 70
    start_height = 10


    start_x = (
        x
        + (final_width - start_width) // 2
    )


    start_y = (
        y + 25
    )


    popup.geometry(
        f"{start_width}x{start_height}"
        f"+{start_x}+{start_y}"
    )


    popup.attributes(
        "-alpha",
        0.0
    )


    label = tk.Label(
        popup,

        text=text,

        font=(
            "Arial",
            17,
            "bold"
        ),

        bg="white",
        fg="black",

        wraplength=final_width - 35,

        justify="center"
    )


    label.pack(
        expand=True,
        fill="both",
        padx=15,
        pady=12
    )


    color_state = False


    def alternate_colors():

        nonlocal color_state


        try:

            if color_state:

                # WHITE BACKGROUND
                # BLACK TEXT

                popup.configure(
                    bg="white"
                )

                label.configure(
                    bg="white",
                    fg="black"
                )


            else:

                # BLACK BACKGROUND
                # WHITE TEXT

                popup.configure(
                    bg="black"
                )

                label.configure(
                    bg="black",
                    fg="white"
                )


            color_state = not color_state


            popup.after(
                COLOR_SWITCH_MS,
                alternate_colors
            )


        except tk.TclError:

            pass




    frame = 0


    def animate_in():

        nonlocal frame


        try:

            progress = (
                frame
                / ANIMATION_FRAMES
            )


            # Smooth ease-out
            eased = (
                1
                - (1 - progress) ** 3
            )


            current_width = int(

                start_width

                + (
                    final_width
                    - start_width
                )

                * eased
            )


            current_height = int(

                start_height

                + (
                    final_height
                    - start_height
                )

                * eased
            )


            current_x = int(

                start_x

                + (
                    x
                    - start_x
                )

                * eased
            )


            current_y = int(

                start_y

                + (
                    y
                    - start_y
                )

                * eased
            )


            alpha = min(
                1.0,
                progress * 1.8
            )


            popup.geometry(

                f"{current_width}"
                f"x{current_height}"
                f"+{current_x}"
                f"+{current_y}"
            )


            popup.attributes(
                "-alpha",
                alpha
            )


            frame += 1


            if frame <= ANIMATION_FRAMES:

                popup.after(
                    ANIMATION_SPEED,
                    animate_in
                )


            else:

                popup.geometry(

                    f"{final_width}"
                    f"x{final_height}"
                    f"+{x}"
                    f"+{y}"
                )


                popup.attributes(
                    "-alpha",
                    1.0
                )


                bounce()


        except tk.TclError:

            pass




    def bounce():

        try:

            extra_width = 12
            extra_height = 6


            bounce_x = (
                x
                - extra_width // 2
            )


            bounce_y = (
                y
                - extra_height // 2
            )


            popup.geometry(

                f"{final_width + extra_width}"
                f"x{final_height + extra_height}"
                f"+{bounce_x}"
                f"+{bounce_y}"
            )


            popup.after(
                60,
                bounce_back
            )


        except tk.TclError:

            pass


    def bounce_back():

        try:

            popup.geometry(

                f"{final_width}"
                f"x{final_height}"
                f"+{x}"
                f"+{y}"
            )


        except tk.TclError:

            pass


    def animate_out():

        out_frame = 0
        out_frames = 12


        def shrink():

            nonlocal out_frame


            try:

                progress = (
                    out_frame
                    / out_frames
                )


                eased = (
                    progress ** 2
                )


                current_width = int(

                    final_width

                    - (
                        final_width
                        - start_width
                    )

                    * eased
                )


                current_height = int(

                    final_height

                    - (
                        final_height
                        - start_height
                    )

                    * eased
                )


                current_x = int(

                    x

                    + (
                        final_width
                        - current_width
                    )

                    / 2
                )


                current_y = int(

                    y
                    - progress * 20
                )


                alpha = max(
                    0,
                    1 - progress
                )


                popup.geometry(

                    f"{current_width}"
                    f"x{current_height}"
                    f"+{current_x}"
                    f"+{current_y}"
                )


                popup.attributes(
                    "-alpha",
                    alpha
                )


                out_frame += 1


                if out_frame <= out_frames:

                    popup.after(
                        15,
                        shrink
                    )


                else:

                    popup.destroy()


            except tk.TclError:

                pass


        shrink()


    alternate_colors()

    animate_in()


    popup.after(
        CARD_LIFETIME_MS,
        animate_out
    )


def slide_text(text):


    width = 520
    height = 80

    y = (
        SCREEN_HEIGHT // 2
        - height // 2
    )

    current_x = -width


    slide = tk.Toplevel(root)

    slide.overrideredirect(True)


    slide.attributes(
        "-topmost",
        True
    )


    slide.configure(
        bg="black"
    )


    slide.geometry(

        f"{width}"
        f"x{height}"
        f"+{current_x}"
        f"+{y}"
    )


    label = tk.Label(

        slide,

        text=text,

        font=(
            "Arial",
            21,
            "bold"
        ),

        bg="black",
        fg="white"
    )


    label.pack(
        expand=True,
        fill="both"
    )


    color_state = False


    def slide_colors():

        nonlocal color_state


        try:

            if color_state:

                slide.configure(
                    bg="white"
                )

                label.configure(
                    bg="white",
                    fg="black"
                )


            else:

                slide.configure(
                    bg="black"
                )

                label.configure(
                    bg="black",
                    fg="white"
                )


            color_state = not color_state


            slide.after(
                COLOR_SWITCH_MS,
                slide_colors
            )


        except tk.TclError:

            pass


    def move():

        nonlocal current_x


        try:

            current_x += SLIDE_SPEED


            slide.geometry(

                f"{width}"
                f"x{height}"
                f"+{current_x}"
                f"+{y}"
            )



            if current_x < SCREEN_WIDTH:

                slide.after(
                    15,
                    move
                )


            else:

                slide.destroy()


        except tk.TclError:

            pass


    slide_colors()

    move()


def start():

    pygame.mixer.music.load(
        SONG
    )


    pygame.mixer.music.play()


    start_time = (
        time.perf_counter()
    )


    lyric_index = 0


    def update():

        nonlocal lyric_index


        current_time = (

            time.perf_counter()

            - start_time
        )


        while (

            lyric_index < len(lyrics)

            and

            current_time
            >= lyrics[lyric_index][0]

        ):


            item = lyrics[
                lyric_index
            ]


            lyric_text = item[1]


            if len(item) >= 3:

                effect = item[2]

            else:

                effect = "popup"

            if effect == "slide":

                slide_text(
                    lyric_text
                )


            else:

                show_lyric(
                    lyric_text
                )


            lyric_index += 1

        if lyric_index < len(lyrics):

            root.after(
                10,
                update
            )


    update()


root.after(
    500,
    start
)


root.mainloop()