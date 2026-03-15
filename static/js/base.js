/* =========================
   BASE.JS - NEXUS
========================= */

document.addEventListener("DOMContentLoaded", function() {
    
    /* ===== MENU UTILISATEUR ===== */
    const toggleBtn = document.getElementById("settingsToggle");
    const menu = document.getElementById("settingsMenu");

    if (toggleBtn && menu) {
        toggleBtn.addEventListener("click", function(e) {
            e.stopPropagation();
            menu.classList.toggle("active");
        });

        // Fermer menu si clic à l'extérieur
        document.addEventListener("click", function(e) {
            if (!menu.contains(e.target) && !toggleBtn.contains(e.target)) {
                menu.classList.remove("active");
            }
        });
    }

    /* ===== DARK MODE ===== */
    const darkModeSwitch = document.getElementById("darkModeSwitch");
    if(darkModeSwitch) {
        darkModeSwitch.addEventListener("change", function() {
            document.body.classList.toggle("dark-mode", this.checked);
        });
    }

    /* ===== MENU HAMBURGER ===== */
    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".nav-links");

    if(hamburger && navLinks) {
        hamburger.addEventListener("click", function() {
            navLinks.classList.toggle("active");
        });

        // Fermer le menu si clic sur un lien (mobile)
        navLinks.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", function() {
                navLinks.classList.remove("active");
            });
        });
    }

}); 





document.addEventListener("DOMContentLoaded", function() {
    // Sélectionne tous les boutons Like de la page
    const likeButtons = document.querySelectorAll(".like-btn");
    
    likeButtons.forEach(btn => {
        btn.addEventListener("click", function() {
            const articleId = this.dataset.articleId;
            const likeCount = document.querySelector(`#like-count-${articleId}`);

            fetch("{% url 'utilisateur:like_article_ajax' %}", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": "{{ csrf_token }}"
                },
                body: `article_id=${articleId}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    btn.classList.add("liked");
                } else {
                    btn.classList.remove("liked");
                }
                if(likeCount) likeCount.textContent = data.total_likes;
            })
            .catch(error => console.error("Erreur Like AJAX :", error));
        });
    });
});
