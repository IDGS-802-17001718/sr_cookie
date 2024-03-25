// Inicializa la tabla con DataTables
var table = $('#tblSupplier').DataTable();function editSupplier(id) {
    // Encuentra la fila que tiene el ID correspondiente
    var row = document.querySelector('#tblSupplier tbody tr[data-id="' + id + '"]');

    // Obtiene los datos de la fila
    var nombre = row.children[0].textContent;
    var rfc = row.children[1].textContent;
    var correo = row.children[2].textContent;
    var telefono = row.children[3].textContent;
    // etc.

    var modal = document.getElementById('supplierModal');
    var bsModal = new bootstrap.Modal(modal);
    var modalTitle = document.getElementById('supplierModalLabel');
    var saveButton = modal.querySelector('button[type="submit"]');

    // Estamos editando un proveedor existente
    modalTitle.textContent = 'Editar Proveedor';
    saveButton.textContent = 'Actualizar';

    // Rellena los campos del formulario en el modal con los datos del proveedor
    document.getElementById('idSupplier').value = id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('rfc').value = rfc;
    document.getElementById('correo').value = correo;
    document.getElementById('telefono').value = telefono;
    // etc.

    // Abre el modal
    bsModal.show();
}