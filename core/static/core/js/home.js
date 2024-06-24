function previewImage(event){
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('output_image');
        output.src = reader.result;
        output.style.display = 'block';
    }
    if (event.target.files.length > 0){
        reader.readAsDataURL(event.target.files[0]);
    }
}