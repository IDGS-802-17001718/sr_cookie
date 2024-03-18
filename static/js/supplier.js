$(document).ready(function() {
    $('#supplierForm').submit(function(e) {
        e.preventDefault(); // Evita que el formulario se envíe de manera tradicional
        
        // Obtener los datos del formulario
        var formData = $(this).serialize();
        
        // Realizar la solicitud AJAX
        $.ajax({
            url: "/suppliers/save", // URL del endpoint en el servidor para registrar/modificar proveedores
            type: "POST", // Método HTTP para enviar los datos
            data: formData, // Datos del formulario
            success: function(response) {
                // Manejar la respuesta del servidor (por ejemplo, mostrar un mensaje de éxito)
                alert("Proveedor registrado/modificado correctamente");
            },
            error: function(xhr, status, error) {
                // Manejar errores de la solicitud AJAX (por ejemplo, mostrar un mensaje de error)
                alert("Error al registrar/modificar proveedor");
            }
        });
    });
    $('#tblSupplier').DataTable({
        "ajax": {
            url: "/suppliers/getall", // Ruta en Flask que manejará la solicitud AJAX
            type: "GET",
            datatype: "json",
        },
        columns: [
            { data: "id", "className": "hidden"},
            { data: "name" },
            { data: "email" },
            { data: "phone"},
            { data: "address"},
            { data: "city"},
            { data: "state" },
            { data: "zip"},
            { data: "country"},
            { data: "status"},
            { data: null, defaultContent: "<button class='btn btn-warning' onclick='modifySupplier()'><i class='fa-solid fa-pen'></i></button>" },
            { data: null, defaultContent: "<button class='btn btn-danger' onclick='deleteSupplier()'><i class='fa-solid fa-trash-can'></i></button>"}
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.childRowImmediate,
                type: ''
            }
        },
        columnDefs: [
            {
                targets: [2,3,4,5,6], // Índices de las columnas que se van a ocultar
                visible: true, // Oculta estas columnas por defecto
                responsivePriority: 1 // Prioridad de ocultación en resoluciones pequeñas
            }
        ],
        scrollCollapse: true,
        scrollY: '50vh',
        scrollX: true,
    });
});