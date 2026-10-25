# Signalling & Telecom Company Website (template)

A static 8-page business website. Its layout and design follow a Hostinger Website Builder site for a railway signalling and telecom contractor. All text is placeholder. The images and hero video are free stock media from Unsplash and Pexels.

## Pages
- `index.html`: hero video, about split, services cards, client logos, project gallery
- `about.html`: history, stats, how we work, safety, team
- `services.html`: service cards, testimonials, locations
- `projects.html`: two project categories plus a gallery
- `metro-railways.html` and `open-railways.html`: project galleries
- `contact-us.html`: contact form, locations, testimonials
- `privacy-policy.html`

## Editing
1. Change the company name, phone numbers and emails at the top of `build.py`.
2. Edit the page text inside `build.py`.
3. Run `python3 build.py` to regenerate the HTML.

You can change colours and fonts in the `:root` block at the top of `assets/css/style.css`.

The forms are demo-only. Connect them to a form service (Formspree, Netlify Forms, etc.) to receive messages.

## Preview locally
```bash
python3 -m http.server 8000
```
Then open http://localhost:8000.

## Deploy
This is a plain static site, so it runs on GitHub Pages, Netlify, Vercel or any web host without a build step.
