//apply code font on numbers for wiki table admonition

const admonition = document.querySelectorAll(".admonition.wiki table td");
admonition.forEach((item) => {
	if (item.textContent.match(/^\d+$/)) {
		item.style.fontFamily = "var(--md-code-font)";
	}
});
