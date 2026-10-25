// Mobile menu
const toggle = document.querySelector('.menu-toggle');
const links = document.querySelector('.nav-links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
}

// Fade-up on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// Gallery lightbox
const box = document.createElement('div');
box.className = 'lightbox';
box.innerHTML = '<img alt="">';
document.body.appendChild(box);
document.querySelectorAll('.gallery img').forEach((img) => {
  img.addEventListener('click', () => {
    box.querySelector('img').src = img.dataset.full || img.src;
    box.classList.add('open');
  });
});
box.addEventListener('click', () => box.classList.remove('open'));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') box.classList.remove('open'); });

// Forms have no backend yet: show a note instead of submitting.
// Point the form's action at Formspree, Netlify Forms, etc. to make it live.
document.querySelectorAll('form[data-demo]').forEach((f) => {
  f.addEventListener('submit', (e) => {
    e.preventDefault();
    const note = f.querySelector('.form-note');
    if (note) note.textContent = 'Thanks! (Demo form: connect a form service to receive messages.)';
    f.reset();
  });
});

const y = document.getElementById('year');
if (y) y.textContent = new Date().getFullYear();
