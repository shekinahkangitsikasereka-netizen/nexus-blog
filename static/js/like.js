document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll(".like-btn");

    buttons.forEach(button => {
        button.addEventListener("click", function () {

            const articleId = this.dataset.articleId;
            const likeCount = document.querySelector("#like-count-" + articleId);

            fetch("/like-ajax/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: "article_id=" + articleId
            })

            .then(response => response.json())

            .then(data => {

                if (data.liked) {
                    button.classList.add("liked");
                } else {
                    button.classList.remove("liked");
                }

                likeCount.textContent = data.total_likes;
            });
        });
    });

});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {

        const cookies = document.cookie.split(";");

        for (let i = 0; i < cookies.length; i++) {

            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}