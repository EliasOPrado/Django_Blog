

const titleInput = document.querySelector("input[name='title']")
const slugInput = document.querySelector("input[name='slug']")

const slugfy = (val) => {
  return val.toString().toLowerCase().trim()
  .replace(/&/g, '-and-') // replace & with -and-
  .replace(/[\s\W-]+/g, '-') // replace non spaces, non words chars and dashes with a single dash
};

titleInput.addEventListener('keyup',(e) =>{
  slugInput.setAttribute('value', slugfy(titleInput.value));
});
