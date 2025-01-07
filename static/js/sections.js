function scrollToSection(sectionId) {
  // Seleciona a seção com o ID fornecido
  const section = document.querySelector(sectionId);

  // Rola até a seção com transição suave
  section.scrollIntoView({
      behavior: 'smooth'
  });
}