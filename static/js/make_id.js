function swipe() {
    const largeImage = document.getElementById('chosen_image');
    largeImage.style.display = 'block';
   largeImage.style.width=200+"px";
   largeImage.style.height=200+"px";
    const url = largeImage.getAttribute('src');
    window.open(url,'Image','width=largeImage.stylewidth,height=largeImage.style.height,resizable=1');
}