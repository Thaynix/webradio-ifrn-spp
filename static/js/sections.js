 function scrollToSection() {
    const targetSection = document.getElementById('#home');
    window.scrollTo({
      top: targetSection.offsetTop,  // posição da seção
      behavior: 'smooth'             // rolagem suave
    });
}
