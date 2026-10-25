"""Builds the static pages from one shared header and footer.

Run:  python3 build.py
Edit BRAND / CONTACT below, or the page bodies, then rebuild.
"""
from pathlib import Path

ROOT = Path(__file__).parent

BRAND = "Your Company"
SHORT = "YC"
TAGLINE = "Signalling & Telecom Solutions"
CONTACT = {
    "phone": "+91-00000-00000",
    "phone2": "+91-00000-00001",
    "email": "hello@example.com",
    "email2": "projects@example.com",
}
ANNOUNCE = "Announcement bar: share your latest project news or an important update here."


def u(photo_id, w=1200, h=None):
    if not photo_id.startswith("photo-"):  # a local file from assets/images/photos
        return photo_id
    """Free Unsplash stock photo URL."""
    size = f"&w={w}" + (f"&h={h}" if h else "")
    return f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&q=70{size}"


HERO_VIDEO = "https://videos.pexels.com/video-files/18831305/18831305-uhd_2730_1440_60fps.mp4"
HERO_POSTER = "https://images.pexels.com/videos/18831305/bangalore-india-metro-indian-city-indian-metro-18831305.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=630&w=1200"

PHOTOS = [
    "photo-1621905251918-48416bd8575a",
    "photo-1605222206265-cd76ac927f4f",
    "photo-1611018037597-e59bf545e517",
    "photo-1623070861283-17d2c364fc03",
    "photo-1626063240117-dd2de78657fb",
    "photo-1631510565971-b800a52e8847",
    "photo-1646159084835-8e7573f6a922",
    "photo-1670234196024-7437f887bf3a",
    "photo-1677751809692-7203a121432f",
    "photo-1678803262992-d79d06dd5d96",
    "photo-1680136806874-a7bb24d0cfc9",
    "photo-1683223203587-0fbbfe0ff60a",
    "photo-1685119166946-d4050647b0e3",
    "photo-1690088566900-d9e857a8b416",
    "photo-1697503100939-a0bf4507cd50",
    "photo-1698177370663-e51d194ef653",
    "photo-1701149494438-16c0876bf4ed",
    "photo-1701623915769-5bf99f785f5e",
    "photo-1702092043573-aabb83669022",
    "photo-1702259686739-5cd39686e23b",
    "photo-1495573258723-2c7be7a646ce",
    "photo-1528541606507-b5013b125572",
    "photo-1529919295059-91ffde496943",
    "photo-1586883935530-8c2e0a69d3f0",
    "photo-1611156231877-c5224cc7f45e",
]

# Drop-in brand assets: put your own files here and rebuild.
#   assets/images/logo.png (or .svg/.jpg/.webp)  -> replaces the text logo
#   assets/images/photos/*.jpg|png|webp           -> replace the stock photos, in name order
_IMG_EXT = (".jpg", ".jpeg", ".png", ".webp", ".svg")
LOGO = next((f"assets/images/logo{e}" for e in _IMG_EXT if (ROOT / f"assets/images/logo{e}").exists()), None)
_local = sorted(
    f"assets/images/photos/{f.name}" for f in (ROOT / "assets/images/photos").glob("*")
    if f.suffix.lower() in _IMG_EXT
) if (ROOT / "assets/images/photos").is_dir() else []
if _local:
    # repeat if there are fewer files than photo slots
    PHOTOS = (_local * (len(PHOTOS) // len(_local) + 1))[:max(len(PHOTOS), len(_local))]

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("projects.html", "Projects"),
    ("contact-us.html", "Contact us"),
]

ICONS = {
    "facebook": '<path d="M14 9V7c0-.6.4-1 1-1h2V2h-3a4 4 0 0 0-4 4v3H8v4h2v9h4v-9h3l1-4h-4z"/>',
    "instagram": '<path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm5-9a1 1 0 1 0 0 2 1 1 0 0 0 0-2zM7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7z"/>',
    "x": '<path d="M17.8 3h3.1l-6.8 7.7L22 21h-6.2l-4.9-6.3L5.3 21H2.2l7.2-8.2L2 3h6.4l4.4 5.8L17.8 3zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5z"/>',
}


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {BRAND}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
"""


def logo_html():
    if LOGO:
        return f'<img class="logo-img" src="{LOGO}" alt="{BRAND}">'
    return f'<span class="logo-mark">{SHORT}</span>\n      <span class="logo-text">{BRAND.upper()}</span>'


def header(active):
    active_attr = ' class="active"'
    links = "\n".join(
        f'        <li><a href="{href}"{active_attr if href == active else ""}>{label}</a></li>'
        for href, label in NAV
    )
    return f"""<div class="announce">{ANNOUNCE}</div>
<header class="site-header">
  <div class="container nav">
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav aria-label="Main">
      <ul class="nav-links">
{links}
      </ul>
    </nav>
    <a class="logo" href="index.html" aria-label="{BRAND} home">
      {logo_html()}
    </a>
    <a class="btn btn-primary nav-cta" href="contact-us.html">Get a consultation</a>
  </div>
</header>
<main>
"""


def footer():
    social = "".join(
        f'<a href="#" aria-label="{n}"><svg viewBox="0 0 24 24">{p}</svg></a>' for n, p in ICONS.items()
    )
    return f"""</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <h4>Contact us</h4>
      <ul class="footer-list">
        <li><a href="tel:{CONTACT['phone']}">{CONTACT['phone']}</a></li>
        <li><a href="tel:{CONTACT['phone2']}">{CONTACT['phone2']}</a></li>
        <li><a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></li>
        <li><a href="mailto:{CONTACT['email2']}">{CONTACT['email2']}</a></li>
      </ul>
      <div class="social">{social}</div>
    </div>
    <div>
      <h4>Quick links</h4>
      <ul class="footer-list">
        {''.join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)}
        <li><a href="privacy-policy.html">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h4>Stay in touch</h4>
      <p>See our <a href="privacy-policy.html"><u>Privacy Policy</u></a> for how we handle your information.</p>
      <form class="sub-form" data-demo>
        <input type="email" required placeholder="Enter your email address" aria-label="Email address">
        <button class="btn btn-light" type="submit">Submit your inquiry now</button>
        <span class="form-note"></span>
      </form>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; <span id="year"></span> {BRAND}. All rights reserved.</span>
    <span>{TAGLINE}</span>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def page_hero(title, text, photo):
    return f"""<section class="page-hero">
  <img class="hero-media" src="{u(photo, 1600)}" alt="">
  <div class="container reveal">
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>
"""


def gallery(photos, cols=4):
    cls = "gallery cols-3" if cols == 3 else "gallery"
    imgs = "\n".join(
        f'    <img loading="lazy" src="{u(p, 600, 600)}" data-full="{u(p, 1600)}" alt="Project photo">' for p in photos
    )
    return f'<div class="{cls}">\n{imgs}\n</div>'


def contact_form():
    return """<form class="form" data-demo>
  <label>Name<input type="text" required></label>
  <label>Email<input type="email" required></label>
  <label>Phone<input type="tel"></label>
  <label>Message<textarea rows="5" required></textarea></label>
  <button class="btn btn-primary" type="submit">Send message</button>
  <span class="form-note"></span>
</form>"""


QUOTES = """<div class="quotes">
  <div class="quote reveal"><div class="stars">★★★★★</div><p>“Placeholder testimonial. Add a short quote from a client about the quality and timeliness of your work.”</p><cite>Client name, Organisation</cite></div>
  <div class="quote reveal"><div class="stars">★★★★★</div><p>“Placeholder testimonial. Mention a specific project and the result the client saw.”</p><cite>Client name, Organisation</cite></div>
  <div class="quote reveal"><div class="stars">★★★★★</div><p>“Placeholder testimonial. Keep it to two or three sentences for the best layout.”</p><cite>Client name, Organisation</cite></div>
</div>"""

LOCATIONS = """<div class="locations">
  <div class="location reveal"><h4>Head office</h4><p>Street address<br>City, State PIN</p></div>
  <div class="location reveal"><h4>Regional office</h4><p>Street address<br>City, State PIN</p></div>
  <div class="location reveal"><h4>Site office</h4><p>Street address<br>City, State PIN</p></div>
</div>"""


PAGES = {}

PAGES["index.html"] = ("Home", "Installation and maintenance of signalling and telecom systems.", f"""
<section class="hero">
  <video class="hero-media" autoplay muted loop playsinline poster="{HERO_POSTER}">
    <source src="{HERO_VIDEO}" type="video/mp4">
  </video>
  <div class="container reveal">
    <h1>Installation and maintenance of signalling &amp; telecom systems for railways</h1>
    <p>Placeholder intro: one or two sentences on what you do, who you do it for, and how long you have been doing it.</p>
    <a class="btn btn-primary" href="contact-us.html">Contact us</a>
    <div class="rating"><span>Trusted by many clients</span><span class="stars">★★★★★</span></div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <h3 class="section-title">A dependable partner for signalling and telecom work</h3>
      <p>Placeholder about text. Describe your company's background, the sectors you serve, the scope of work you take on (supply, installation, commissioning, maintenance) and the regions you cover.</p>
      <p>Add a second short paragraph about your credentials and track record.</p>
      <a class="btn btn-outline" href="about.html">Learn more about us</a>
    </div>
    <img class="reveal" src="{u(PHOTOS[0], 900, 1000)}" alt="Railway signal">
  </div>
</section>

<section class="bg-soft">
  <div class="container cards">
    <div class="card-intro reveal">
      <h3 class="section-title">What we do</h3>
      <p>Placeholder summary of your main services across railways, metro and industry.</p>
      <a class="btn btn-primary" href="services.html" style="align-self:flex-start">Our services</a>
    </div>
    <a class="card-img reveal" href="services.html">
      <img src="{u(PHOTOS[2], 700, 900)}" alt="">
      <h3>Installation Services</h3>
      <p>Placeholder: short description of your installation work.</p>
    </a>
    <a class="card-img reveal" href="services.html">
      <img src="{u(PHOTOS[9], 700, 900)}" alt="">
      <h3>Maintenance Support</h3>
      <p>Placeholder: short description of your maintenance work.</p>
    </a>
  </div>
</section>

<section class="clients">
  <div class="container">
    <h3 class="section-title center reveal">Our happy clients</h3>
    <div class="logo-row reveal">
      <div class="logo-box">CLIENT LOGO</div><div class="logo-box">CLIENT LOGO</div>
      <div class="logo-box">CLIENT LOGO</div><div class="logo-box">CLIENT LOGO</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center lead reveal">
      <h3 class="section-title">Our Projects</h3>
      <p>Placeholder: a line introducing your project portfolio.</p>
    </div>
    <div class="reveal">{gallery(PHOTOS[6:14])}</div>
    <p class="center" style="margin-top:32px"><a class="btn btn-outline" href="projects.html">View all projects</a></p>
  </div>
</section>
""")

PAGES["about.html"] = ("About", "About our company, team and approach.", page_hero(
    "Get to know us", "Placeholder: one line on who you are and what drives the company.", PHOTOS[1]) + f"""
<section>
  <div class="container split">
    <div class="reveal">
      <h3 class="section-title">Established in [year]</h3>
      <p>Placeholder company history. Explain how and why the company started and how it has grown.</p>
      <p>Mention the main sectors and clients you work with in general terms.</p>
    </div>
    <img class="reveal" src="{u(PHOTOS[3], 900, 800)}" alt="">
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="stats reveal">
      <div class="stat"><strong>00+</strong>Years of experience</div>
      <div class="stat"><strong>00+</strong>Projects completed</div>
      <div class="stat"><strong>00+</strong>Team members</div>
      <div class="stat"><strong>00</strong>States covered</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center lead reveal"><h3 class="section-title">How we work</h3><p>Placeholder: describe your process from survey to handover.</p></div>
    <div class="feature-grid">
      <div class="feature reveal"><div class="icon">①</div><h3>Our expertise</h3><p>Placeholder: the systems and equipment you specialise in.</p></div>
      <div class="feature reveal"><div class="icon">②</div><h3>Our strength</h3><p>Placeholder: your people, tools and project management.</p></div>
      <div class="feature reveal"><div class="icon">③</div><h3>Safety first</h3><p>Placeholder: your safety standards and certifications.</p></div>
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container split reverse">
    <div class="reveal">
      <h3 class="section-title">Safety is our first priority</h3>
      <p>Placeholder: explain your on-site safety practices, training and compliance.</p>
    </div>
    <img class="reveal" src="{u(PHOTOS[9], 900, 800)}" alt="">
  </div>
</section>

<section>
  <div class="container">
    <h3 class="section-title center reveal">Our team</h3>
    <div class="team">
      <div class="member reveal"><div class="avatar">A</div><h4>Name Surname</h4><p>Managing Director</p></div>
      <div class="member reveal"><div class="avatar">B</div><h4>Name Surname</h4><p>Project Head</p></div>
      <div class="member reveal"><div class="avatar">C</div><h4>Name Surname</h4><p>Operations</p></div>
      <div class="member reveal"><div class="avatar">D</div><h4>Name Surname</h4><p>Accounts</p></div>
    </div>
  </div>
</section>
""")

SERVICES = [
    ("Signalling installation", PHOTOS[14]), ("Telecom systems", PHOTOS[15]),
    ("Testing & commissioning", PHOTOS[16]), ("Annual maintenance", PHOTOS[17]),
    ("Cabling & OFC work", PHOTOS[18]), ("Supply of equipment", PHOTOS[19]),
]
PAGES["services.html"] = ("Services", "Our signalling and telecom services.", page_hero(
    "Solutions and Services", "Placeholder: one line summarising the range of services you offer.", PHOTOS[13]) + """
<section>
  <div class="container cards">
""" + "\n".join(
    f'    <div class="card-img reveal"><img src="{u(p, 700, 900)}" alt=""><h3>{t}</h3><p>Placeholder: describe this service in one or two sentences.</p></div>'
    for t, p in SERVICES) + f"""
  </div>
</section>
<section class="bg-soft"><div class="container"><h3 class="section-title center reveal">Customer Feedback</h3>{QUOTES}</div></section>
<section><div class="container"><h3 class="section-title center reveal">Our Locations</h3>{LOCATIONS}</div></section>
""")

PAGES["projects.html"] = ("Projects", "Highlights from our project portfolio.", page_hero(
    "Project Highlights", "Placeholder: a line about the scale and range of your projects.", PHOTOS[20]) + f"""
<section>
  <div class="container project-cats">
    <a class="card-img reveal" href="metro-railways.html"><img src="{u(PHOTOS[21], 900, 900)}" alt=""><h3>Signalling Solutions</h3><p>Metro railway projects →</p></a>
    <a class="card-img reveal" href="open-railways.html"><img src="{u(PHOTOS[22], 900, 900)}" alt=""><h3>Telecommunication Solutions</h3><p>Open railway projects →</p></a>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <h3 class="section-title center reveal">Gallery</h3>
    <div class="reveal">{gallery(PHOTOS[:16])}</div>
  </div>
</section>
""")

PAGES["metro-railways.html"] = ("Metro Railways Projects", "Our metro railway projects.", page_hero(
    "Metro Railways Projects", "Placeholder: summary of your metro work.", PHOTOS[23]) + f"""
<section><div class="container"><div class="reveal">{gallery(PHOTOS[8:17], 3)}</div></div></section>
""")

PAGES["open-railways.html"] = ("Open Railways Projects", "Our open railway projects.", page_hero(
    "Open Railways Projects", "Placeholder: summary of your open-line railway work.", PHOTOS[24]) + f"""
<section><div class="container"><div class="reveal">{gallery(PHOTOS[16:25], 3)}</div></div></section>
""")

PAGES["contact-us.html"] = ("Contact Us", "Get in touch for a consultation.", page_hero(
    "Contact Us", "Placeholder: invite visitors to get in touch about their project.", PHOTOS[5]) + f"""
<section>
  <div class="container split">
    <div class="reveal">
      <h3 class="section-title">Let's talk about your project</h3>
      <p>Placeholder: tell visitors what to include and how quickly you reply.</p>
      <p><strong>Phone:</strong> <a href="tel:{CONTACT['phone']}">{CONTACT['phone']}</a><br>
      <strong>Email:</strong> <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></p>
    </div>
    <div class="reveal">{contact_form()}</div>
  </div>
</section>
<section class="bg-soft"><div class="container"><h3 class="section-title center reveal">Our Locations</h3>{LOCATIONS}</div></section>
<section><div class="container"><h3 class="section-title center reveal">Customer Feedback</h3>{QUOTES}</div></section>
""")

PAGES["privacy-policy.html"] = ("Privacy Policy", "How we handle your information.", f"""
<section>
  <div class="container prose">
    <h1>Privacy Policy</h1>
    <p>Placeholder privacy policy. Replace this with a policy that fits your business and local law.</p>
    <h2>Information we collect</h2>
    <p>Describe what you collect through the contact and newsletter forms (for example name, email, phone).</p>
    <h2>How we use it</h2>
    <p>Describe how you use it, such as replying to enquiries.</p>
    <h2>Sharing</h2>
    <p>State whether and with whom information is shared.</p>
    <h2>Contact</h2>
    <p>Questions about this policy: <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>.</p>
  </div>
</section>
""")


def main():
    for name, (title, desc, body) in PAGES.items():
        active = name if name in dict(NAV) else ("projects.html" if "railways" in name else "")
        html = head(title, desc) + header(active) + body + footer()
        (ROOT / name).write_text(html, encoding="utf-8")
        print("wrote", name)


if __name__ == "__main__":
    main()
