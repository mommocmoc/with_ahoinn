document.getElementById('generate').onclick = function () {
    // Your html2pdf code here.
    let element = document.getElementById('element-to-print')
    html2pdf(element);
};

document.getElementById('print').onclick = function () {
    // let element = document.getElementById('element-to-print')
    $('#element-to-print').printThis()
}

document.getElementById('textGen').onclick = function () {
    var text = document.getElementById('bodyText').value
    var element = document.getElementById('element-to-print')
    element.innerHTML = text
}
/* document.getElementById('generateCanvas').onclick = function () {
  var element = document.getElementById('element-to-print');
  html2canvas(element).then(function (canvas) {
    document.body.appendChild(canvas);
    canvas.classList.add("test")
  });
};  */
