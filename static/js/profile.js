// Script para vista previa de avatar
document.getElementById('avatarInput').addEventListener('change', function(e) {
    const reader = new FileReader();
    reader.onload = function(event) {
        document.querySelector('.profile-image').src = event.target.result;
    }
    reader.readAsDataURL(e.target.files[0]);
});