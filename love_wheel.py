import tkinter as tk
import math
import random


LOVE_100 = [
    "I love you", "Tum meri duniya ho", "I adore you", "Dil se chahta hoon tumhe",
    "You mean everything to me", "Meri har khushi tumse hai", "I'm crazy about you", "Tum mere dil ki dhadkan ho",
    "You have my heart", "Har pal tumhari yaad aati hai", "I love you endlessly", "Tum ho toh sab kuch hai",
    "You are my world", "Meri subah aur shaam tum ho", "I'm deeply in love with you", "Tumse mil kar zindagi badal gayi",
    "You complete me", "Tum meri sabse pyari aadat ho", "I love you more each day", "Meri har dua mein tum ho",
    "You're my favorite person", "Tumhari muskaan sabse anmol hai", "I cherish you", "Dil bas tumhe hi maangta hai",
    "My heart belongs to you", "Tum meri jaan ho", "I love you to the moon", "Har lamha tumhare saath jeena hai",
    "You're my everything", "Tumse behtar kuch nahi", "I'm madly in love with you", "Meri duniya tum par rukti hai",
    "I treasure every moment with you", "Tum meri roshni ho", "You light up my life", "Dil ke sabse kareeb tum ho",
    "I love you unconditionally", "Har baat mein tumhara zikr hota hai", "You are my home", "Tumhare bina adhoora hoon",
    "I can't get enough of you", "Tum meri sabse badi taqat ho", "You're my sunshine", "Meri har khwahish tum ho",
    "I love you beyond words", "Tumhari aankhon mein apni duniya dekhi", "My heart skips a beat for you", "Har din tumpe naya pyaar aata hai",
    "You're the best part of my day", "Tum ho toh dar kaisa", "I'm so lucky to have you", "Mera dil sirf tumhara hai",
    "I love you forever and always", "Tum meri kismat ka sabse haseen hissa ho", "You're my soulmate", "Har saans tumhare naam",
    "I fall for you every single day", "Tumhari baatein dil ko chhoo jaati hain", "You're my greatest blessing", "Mera har sapna tumse shuru hota hai",
    "I love you with all my heart", "Tum meri pehli aur aakhiri pasand ho", "You're my safe place", "Dil ko sukoon sirf tumse milta hai",
    "I'm hopelessly in love with you", "Tum meri zindagi ki sabse khoobsurat kahani ho", "You make life magical", "Har pal tumhe aur chahta hoon",
    "I love you purely", "Tum meri har muskaan ki wajah ho", "You're my dream come true", "Meri har khushi ka raaz tum ho",
    "I'm drawn to you endlessly", "Tumse juda hona namumkin hai", "You're my guiding star", "Andheron mein mera sahara tum ho",
    "I love you fiercely", "Dil ne bas tumhe chuna hai", "My soul recognizes yours", "Humara rishta sabse khaas hai",
    "You're my sweetest obsession", "Har waqt bas tumhara khayal rehta hai", "I love you through every season", "Dhoop ho ya chhaon, main tumhare saath hoon",
    "You're my heart's desire", "Meri har chahat tum par khatam hoti hai", "I'm devoted to you", "Tumhare liye sab kuch qubool hai",
    "You bring peace to my soul", "Tumhari aawaz se dil shaant ho jaata hai", "I love you more than yesterday", "Aaj kal se zyada pyaar karta hoon",
    "You're my forever person", "Har janam mein tumhe hi chahunga", "I admire everything about you", "Tumhara har andaaz pyara lagta hai",
    "You're the reason I smile", "Tumhari ek hansi kaafi hai", "I love you without limits", "Pyaar ki koi seema nahi",
    "My world revolves around you", "Meri duniya ka markaz tum ho", "You're my true north", "Bhatakne par rasta dikhane waale tum ho",
    "I'm fond of every little thing about you", "Tumhari chhoti-chhoti baatein bhi yaad rehti hain", "You're my heart's melody", "Dil ka geet tum ho",
    "I love you completely", "Poora ka poora dil tumhara hai", "You're my favorite place to be", "Tumhare paas rehna sabse achha lagta hai",
    "I'm enchanted by you", "Tumhara jaadoo dil par chha gaya hai", "You're my eternal love", "Hamesha rehne waala pyaar",
    "I love you softly and deeply", "Gehraiyon se nikla hua pyaar", "You're my comfort and joy", "Mera chain aur meri khushi tum ho",
    "I'm wrapped around your heart", "Dil tumhare haathon mein mehfooz hai", "You're my one and only", "Tum jaisa koi aur nahi",
    "I love you in every universe", "Har duniya mein sirf tumhara", "You're my quiet happiness", "Khamoshi mein bhi tumhara saath",
    "I'm captivated by your spirit", "Tumhari zindadili sabse alag hai", "You're my precious gem", "Mera sabse keemti heera tum ho",
    "I love you faithfully", "Wafa ka doosra naam tum ho", "You're my warm embrace", "Tumhari baahon mein sukoon hai",
    "I'm thrilled to call you mine", "Tumhe apna kehna sabse bada garv hai", "You're my constant inspiration", "Aage badhne ki prerana tum ho",
    "I love you generously", "Bina kisi shart ke pyaar", "You're my sweetest memory", "Sabse meethi yaad tum ho",
    "I love you. Always.", "Main tumse pyaar karta hoon. Hamesha."
][:100]


# Auto-cycling themes: Rose Gold & Velvet, Aurora Pink, Sunset Coral, Royal Berry
THEMES = [
    {
        "name": "Rose Gold & Velvet",
        "bg": (22, 6, 20),
        "ring_outer": (244, 162, 97),
        "ring_inner": (255, 77, 141),
        "c1": (255, 110, 165),
        "c2": (255, 205, 130),
        "c3": (245, 155, 225),
        "center_fill": (34, 9, 30),
        "text_main": (255, 245, 248),
    },
    {
        "name": "Aurora Pink",
        "bg": (12, 8, 28),
        "ring_outer": (255, 125, 200),
        "ring_inner": (165, 130, 255),
        "c1": (255, 130, 210),
        "c2": (185, 145, 255),
        "c3": (255, 195, 235),
        "center_fill": (22, 13, 44),
        "text_main": (252, 245, 255),
    },
    {
        "name": "Sunset Coral",
        "bg": (25, 8, 12),
        "ring_outer": (255, 140, 90),
        "ring_inner": (255, 95, 115),
        "c1": (255, 105, 120),
        "c2": (255, 175, 105),
        "c3": (255, 215, 150),
        "center_fill": (40, 12, 18),
        "text_main": (255, 248, 242),
    },
    {
        "name": "Royal Berry",
        "bg": (16, 5, 26),
        "ring_outer": (225, 120, 255),
        "ring_inner": (255, 80, 165),
        "c1": (215, 110, 255),
        "c2": (255, 90, 175),
        "c3": (255, 180, 230),
        "center_fill": (28, 8, 42),
        "text_main": (255, 244, 255),
    },
]


def lerp(a, b, t):
    return a + (b - a) * t


def lerp_rgb(rgb1, rgb2, t):
    return (
        int(lerp(rgb1[0], rgb2[0], t)),
        int(lerp(rgb1[1], rgb2[1], t)),
        int(lerp(rgb1[2], rgb2[2], t)),
    )


def to_hex(rgb):
    r, g, b = [max(0, min(255, int(v))) for v in rgb]
    return f"#{r:02x}{g:02x}{b:02x}"


class AutoLovelyWheel:
    def __init__(self, root):
        self.root = root
        self.root.title("100 Ways to Say I Love You ♥")

        self.width = 900
        self.height = 900
        self.cx = self.width // 2
        self.cy = self.height // 2

        self.clean_mode = False

        # Minimal top bar only for Clean View toggle
        self.top_bar = tk.Frame(root, bg="#160614", pady=5, padx=10)
        self.top_bar.pack(fill=tk.X)

        self.clean_btn = tk.Button(
            self.top_bar,
            text="✨ Clean View Mode",
            command=self.toggle_clean_mode,
            bg="#2d0d29",
            fg="#ffd6e7",
            relief=tk.FLAT,
            padx=12,
            pady=3,
            font=("Consolas", 9, "bold"),
        )
        self.clean_btn.pack(side=tk.RIGHT)

        # Floating exit hint button for Clean View Mode (top-right corner)
        self.exit_clean_btn = tk.Button(
            root,
            text="Exit Clean View",
            command=self.toggle_clean_mode,
            bg="#240a21",
            fg="#fbcfe8",
            relief=tk.FLAT,
            padx=8,
            pady=2,
            font=("Consolas", 8),
        )

        self.canvas = tk.Canvas(
            root, width=self.width, height=self.height,
            bg="#160614", highlightthickness=0
        )
        self.canvas.pack()

        # Shortcut key 'c' or 'Escape' to toggle Clean View Mode
        self.root.bind("c", lambda _e: self.toggle_clean_mode())
        self.root.bind("<Escape>", lambda _e: self.exit_clean_if_active())

        self.angle_offset = 0.0
        self.orbit_angle = 0.0
        self.visible_count = 0
        self.frame = 0

        # Auto theme cycling state
        self.theme_progress = 0.0  # Smoothly advances across THEMES

        # Auto spotlight state (changes every ~110 frames once lines appear)
        self.spotlight_idx = 0
        self.spotlight_timer = 0

        # Typewriter state for center message
        self.target_center_msg = ""
        self.typed_chars = 0
        self.type_tick = 0

        # Twinkling stars
        self.stars = [
            (
                random.randint(15, self.width - 15),
                random.randint(15, self.height - 15),
                random.uniform(0.7, 2.3),
                random.uniform(0, math.pi * 2),
            )
            for _ in range(125)
        ]

        self.animate()

    def toggle_clean_mode(self):
        self.clean_mode = not self.clean_mode
        if self.clean_mode:
            self.top_bar.pack_forget()
            self.exit_clean_btn.place(x=self.width - 115, y=12)
        else:
            self.exit_clean_btn.place_forget()
            self.top_bar.pack(fill=tk.X, before=self.canvas)

    def exit_clean_if_active(self):
        if self.clean_mode:
            self.toggle_clean_mode()

    def get_current_palette(self):
        total_themes = len(THEMES)
        idx_a = int(self.theme_progress) % total_themes
        idx_b = (idx_a + 1) % total_themes
        t = self.theme_progress - int(self.theme_progress)
        # Smooth ease in-out
        smooth_t = t * t * (3 - 2 * t)

        t_a = THEMES[idx_a]
        t_b = THEMES[idx_b]

        return {
            "bg": to_hex(lerp_rgb(t_a["bg"], t_b["bg"], smooth_t)),
            "ring_outer": to_hex(lerp_rgb(t_a["ring_outer"], t_b["ring_outer"], smooth_t)),
            "ring_inner": to_hex(lerp_rgb(t_a["ring_inner"], t_b["ring_inner"], smooth_t)),
            "c1": lerp_rgb(t_a["c1"], t_b["c1"], smooth_t),
            "c2": lerp_rgb(t_a["c2"], t_b["c2"], smooth_t),
            "c3": lerp_rgb(t_a["c3"], t_b["c3"], smooth_t),
            "center_fill": to_hex(lerp_rgb(t_a["center_fill"], t_b["center_fill"], smooth_t)),
            "text_main": to_hex(lerp_rgb(t_a["text_main"], t_b["text_main"], smooth_t)),
        }

    def get_gradient_color(self, idx, total, pal):
        ratio = idx / max(1, total)
        if ratio < 0.5:
            col = lerp_rgb(pal["c1"], pal["c2"], ratio * 2)
        else:
            col = lerp_rgb(pal["c2"], pal["c3"], (ratio - 0.5) * 2)
        return to_hex(col)

    def draw_mini_heart(self, x, y, size, color):
        pts = []
        for deg in range(0, 360, 24):
            rad = math.radians(deg)
            hx = 16 * (math.sin(rad) ** 3)
            hy = -(13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
            pts.append(x + (hx / 16.0) * size)
            pts.append(y + (hy / 16.0) * size)
        self.canvas.create_polygon(pts, fill=color, outline="", smooth=True)

    def draw_stars(self, pal):
        star_col = to_hex(pal["c3"])
        for x, y, r, phase in self.stars:
            tw = (math.sin(self.frame * 0.07 + phase) + 1) / 2
            rad = r * (0.65 + 0.55 * tw)
            self.canvas.create_oval(x - rad, y - rad, x + rad, y + rad, fill=star_col, outline="")

    def draw_orbiting_ring_and_hearts(self, pal):
        orbit_r = 382
        ring_col = pal["ring_outer"]

        # Dotted orbital ring rotating at its own speed
        for deg in range(0, 360, 8):
            rad = math.radians(deg + self.orbit_angle * 0.65)
            dx = self.cx + orbit_r * math.cos(rad)
            dy = self.cy + orbit_r * math.sin(rad)
            self.canvas.create_oval(dx - 1.4, dy - 1.4, dx + 1.4, dy + 1.4, fill=ring_col, outline="")

        # 8 orbiting mini hearts along the outer orbital ring
        num_hearts = 8
        for h_idx in range(num_hearts):
            h_deg = (360.0 / num_hearts) * h_idx - self.orbit_angle * 1.15
            h_rad = math.radians(h_deg)
            hx = self.cx + orbit_r * math.cos(h_rad)
            hy = self.cy + orbit_r * math.sin(h_rad)
            pulse_size = 6.5 + 1.8 * math.sin(self.frame * 0.1 + h_idx)
            h_color = self.get_gradient_color(h_idx, num_hearts, pal)
            self.draw_mini_heart(hx, hy, pulse_size, h_color)

    def update_auto_spotlight_and_typewriter(self):
        if self.visible_count > 0:
            self.spotlight_timer += 1
            if self.spotlight_timer >= 105:
                self.spotlight_timer = 0
                self.spotlight_idx = (self.spotlight_idx + 1) % self.visible_count

            desired_msg = LOVE_100[self.spotlight_idx]
            if desired_msg != self.target_center_msg:
                self.target_center_msg = desired_msg
                self.typed_chars = 0
                self.type_tick = 0

            if self.typed_chars < len(self.target_center_msg):
                self.type_tick += 1
                if self.type_tick % 2 == 0:
                    self.typed_chars += 1

    def animate(self):
        pal = self.get_current_palette()
        self.canvas.configure(bg=pal["bg"])
        if not self.clean_mode:
            self.top_bar.configure(bg=pal["bg"])

        self.canvas.delete("all")
        self.draw_stars(pal)
        self.draw_orbiting_ring_and_hearts(pal)

        total = len(LOVE_100)
        if self.visible_count < total and self.frame % 2 == 0:
            self.visible_count += 1

        self.update_auto_spotlight_and_typewriter()

        # Base outer & inner wheel rings
        outer_r = 342
        inner_r = 124
        self.canvas.create_oval(
            self.cx - outer_r, self.cy - outer_r,
            self.cx + outer_r, self.cy + outer_r,
            outline=pal["ring_outer"], width=1.6
        )
        self.canvas.create_oval(
            self.cx - inner_r, self.cy - inner_r,
            self.cx + inner_r, self.cy + inner_r,
            outline=pal["ring_inner"], width=1.4
        )

        # Wave breathing ring: each text position breathes along a sine wave
        for i in range(self.visible_count):
            deg = (360.0 / total) * i + self.angle_offset
            rad = math.radians(deg)

            wave_offset = math.sin(self.frame * 0.06 + i * 0.28) * 11.0
            is_spot = (i == self.spotlight_idx)
            text_r = 236 + wave_offset + (7.0 if is_spot else 0.0)

            tx = self.cx + text_r * math.cos(rad)
            ty = self.cy + text_r * math.sin(rad)

            disp_angle = -deg % 360
            if 90 < disp_angle < 270:
                disp_angle = (disp_angle + 180) % 360

            col = pal["text_main"] if is_spot else self.get_gradient_color(i, total, pal)
            fnt = ("Consolas", 8, "bold") if is_spot else ("Consolas", 7)

            self.canvas.create_text(
                tx, ty,
                text=LOVE_100[i],
                fill=col,
                font=fnt,
                angle=disp_angle
            )

        # Center medallion
        beat = math.sin(self.frame * 0.11) ** 2
        core_r = 114 + beat * 3.5
        self.canvas.create_oval(
            self.cx - core_r, self.cy - core_r,
            self.cx + core_r, self.cy + core_r,
            fill=pal["center_fill"], outline=pal["ring_inner"], width=2
        )

        self.canvas.create_text(
            self.cx, self.cy - 44,
            text="100 WAYS TO SAY\nI LOVE YOU ♥",
            fill=to_hex(pal["c3"]),
            font=("Georgia", 8, "bold"),
            justify="center"
        )

        # Line number badge (#01 .. #100)
        num_str = f"#{self.spotlight_idx + 1:02d}" if self.visible_count > 0 else "#00"
        self.canvas.create_text(
            self.cx, self.cy - 18,
            text=num_str,
            fill=pal["ring_outer"],
            font=("Consolas", 9, "bold")
        )

        # Typewriter message reveal in center
        typed_text = self.target_center_msg[:self.typed_chars]
        cursor = "|" if (self.typed_chars < len(self.target_center_msg) and (self.frame // 6) % 2 == 0) else ""
        self.canvas.create_text(
            self.cx, self.cy + 10,
            text=typed_text + cursor,
            fill=pal["text_main"],
            font=("Georgia", 11, "bold italic"),
            width=192,
            justify="center"
        )

        self.canvas.create_text(
            self.cx, self.cy + 48,
            text=f"{self.visible_count} / {total}",
            fill=to_hex(pal["c2"]),
            font=("Consolas", 8, "bold")
        )

        # Advance animations & smooth auto color cycling
        self.angle_offset = (self.angle_offset + 0.35) % 360
        self.orbit_angle = (self.orbit_angle + 0.7) % 360
        self.theme_progress = (self.theme_progress + 0.0022) % len(THEMES)
        self.frame += 1

        self.root.after(28, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoLovelyWheel(root)
    root.mainloop()