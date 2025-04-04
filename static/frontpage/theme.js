'use strict';
{
    function setTheme(mode) {
        if (mode !== "light" && mode !== "dark") {
            console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
            mode = "dark";
        }
        document.documentElement.dataset.theme = mode;
        localStorage.setItem("theme", mode);
    }

    function cycleTheme() {
        const currentTheme = localStorage.getItem("theme") || "dark";
        const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

        // Auto (light) -> Dark -> Light
        if (currentTheme === "light") {
             setTheme("dark");
        } else if (currentTheme === "dark") {
            setTheme("light");
        }
    }

    function initTheme() {
        // set theme defined in localStorage if there is one, or fallback to dark mode
        const currentTheme = localStorage.getItem("theme");
        currentTheme ? setTheme(currentTheme) : setTheme("dark");
    }

    window.addEventListener('load', function(_) {
        const buttons = document.getElementsByClassName("theme-toggle");
        Array.from(buttons).forEach((btn) => {
            btn.addEventListener("click", cycleTheme);
        });
    });

    initTheme();
}
