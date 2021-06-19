var dropdown = document.querySelector('#dropdown_1');
dropdown_1.addEventListener('click', function(event) {
  event.stopPropagation();
  dropdown.classList.toggle('is-active');
});
