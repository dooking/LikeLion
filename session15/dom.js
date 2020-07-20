const goGoogle = document.querySelector(".go");
goGoogle.attributes[0].textContent = "https://www.google.com";
const goPicture = document.querySelector(".picture");
goPicture.attributes[0].textContent =
  "https://pds.joins.com/news/component/htmlphoto_mmdata/202001/01/f86957cb-ee94-4611-bc81-a5478ca91f92.jpg";

const title = document.querySelector("h1");
const btn1 = document.querySelector(".btn-1");
const btn2 = document.querySelector(".btn-2");
const btn3 = document.querySelector(".btn-3");
btn1.addEventListener("click", (event) => {
  btn1.textContent = "짜잔!";
});
btn2.addEventListener("click", (event) => {
  btn2.textContent = "짜잔!";
});
btn3.addEventListener("click", (event) => {
  btn3.textContent = "짜잔!";
});

const result = document.querySelector("#result");
const input = document.querySelector("#input");
input.addEventListener("keyup", function (event) {
  if (
    event.key === "Enter" ||
    event.key === "Alt" ||
    event.key === "Control" ||
    event.key === "Shift"
  ) {
    result.textContent = event.key + "키를 눌렀네요";
  }
  console.log(event.target.value.length);
});
