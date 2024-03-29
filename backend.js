function myFunction() {
  const file = document.querySelector("#uploadImage").files[0];
  var reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = function () {
    localStorage.setItem("image", reader.result);
    document
      .getElementById("imagePreview")
      .setAttribute("src", localStorage.getItem("image"));
  };

  $.ajax({
    type: "POST",
    url: "/runScript.py",
    //or some other path like /scripts/test.py
    dataType: "text",
    success: function (data) {
      alert(data);
    },
    error: function (data) {
      alert(data);
    },
  });
}

if (localStorage.getItem("image"))
  document
    .getElementById("imagePreview")
    .setAttribute("src", localStorage.getItem("image"));
