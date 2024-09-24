let selectHeader = document.querySelector('header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('scrolled')
      } else {
        selectHeader.classList.remove('scrolled')
      }
    }
    document.addEventListener("scroll", headerScrolled)
  }

  const sections = document.querySelectorAll("section");
  const navLinks = document.querySelectorAll("nav a");
  
  window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (window.scrollY >= sectionTop - sectionHeight / 2.75) {
        current = section.getAttribute("id");
      }
    });
  
    navLinks.forEach((link) => {
      link.classList.remove("active");
      if (link.getAttribute("href").slice(1) === current) {
        link.classList.add("active");
      }
    });
  });