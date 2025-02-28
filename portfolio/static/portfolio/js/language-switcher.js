// language switcher for Next.js app
document.addEventListener("DOMContentLoaded", function () {
    const languageSelect = document.getElementById("language-select");
    
    if (languageSelect) {
        languageSelect.addEventListener("change", function () {
            const selectedLang = this.value;

            // Save language in localStorage for Next.js
            localStorage.setItem("language", selectedLang);

            // Notify Next.js about language change
            window.dispatchEvent(new Event("languageChange"));

            // Submit the Django form to apply changes
            document.getElementById("language-form").submit();
        });
    }
});
