document.addEventListener('DOMContentLoaded', function() {
    // Delete User Confirmation
    document.getElementById('confirmUserDelete').addEventListener('click', function() {
        // Lógica para eliminar usuario
        this.closest('.modal').modal('hide');
    });

    // Edit User Modal
    document.querySelectorAll('.btn-edit').forEach(btn => {
        btn.addEventListener('click', function() {
            const row = this.closest('tr');
            const cells = row.cells;
            
            // Llenar formulario de edición
            const form = document.querySelector('#editUserModal form');
            form.elements[0].value = cells[0].textContent;
            form.elements[1].value = cells[1].textContent;
            // Continuar para todos los campos...
        });
    });
});