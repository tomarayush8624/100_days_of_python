// const URL =
//   "https://api.sheety.co/470596daafe9cb70135b0c7a68931928/details/sheet1";

// console.log("hir");
// const data = {
//   sheet1: {
//     name: "John",
//   },
// };

// // Make the request to post the data to the sheet
// fetch(URL, {
//   method: "POST",
//   body: JSON.stringify(data),
// });

let url =
  "https://api.sheety.co/470596daafe9cb70135b0c7a68931928/details/sheet1";
let body = {
  sheet1: {
    name: "John doe",
    password: "123",
  },
};
fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(body),
})
  .then((response) => response.json())
  .then((json) => {
    // Do something with object
    console.log(json.sheet1);
  });
