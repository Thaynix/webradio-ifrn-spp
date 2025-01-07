// document.addEventListener("DOMContentLoaded", () => {
//     const body = document.body;
//     const apresentationSection = document.querySelector(".apresentation");
  
//     const observer = new IntersectionObserver(
//       (entries) => {
//         entries.forEach((entry) => {
//           if (entry.isIntersecting) {
//             body.style.backgroundColor = getComputedStyle(apresentationSection).backgroundColor;
//           } else {
//             body.style.backgroundColor = ""; // Volta para a cor padrão do body (definida no CSS).
//           }
//         });
//       },
//       {
//         threshold: 0.5, // Define a visibilidade mínima da seção (50% visível).
//       }
//     );
  
//     if (apresentationSection) {
//       observer.observe(apresentationSection);
//     }
//   });
  