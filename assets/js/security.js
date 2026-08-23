// security.js

(function() {
    // 1. Validar sesión
    const sessionStr = localStorage.getItem('flotapro_session');
    let sessionData = null;
    
    if (sessionStr) {
        try {
            sessionData = JSON.parse(sessionStr);
        } catch(e) {}
    }
    
    // Si no hay sesión o expiró (8 horas = 28800000 ms)
    if (!sessionData || (Date.now() - sessionData.timestamp > 28800000)) {
        localStorage.removeItem('flotapro_session');
        localStorage.removeItem('flotapro_permisos');
        window.location.href = '/'; // Redirigir al login
        return;
    }

    // 2. Validar permisos
    const permisosStr = localStorage.getItem('flotapro_permisos');
    let permisos = {};
    if (permisosStr) {
        try {
            permisos = JSON.parse(permisosStr);
        } catch(e) {}
    }

    // Configuración de rutas y permisos requeridos
    const routePermissions = {
        'dashboard.html': 'mod_dashboard',
        'mantenimiento.html': 'mod_mantenimiento',
        'garita.html': 'mod_garita',
        'tesoreria.html': 'mod_tesoreria',
        'admin.html': 'mod_admin',
        'siniestros.html': 'mod_siniestros',
        'permisos.html': 'mod_admin' // Gestión de permisos requiere mod_admin
    };

    const currentPath = window.location.pathname;
    let currentPage = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'dashboard.html';
    if (currentPage && !currentPage.endsWith('.html')) {
        currentPage += '.html';
    }
    
    // Si no hay permisos almacenados en absoluto, forzar un re-login para obtenerlos
    if (!permisosStr || Object.keys(permisos).length === 0) {
        localStorage.removeItem('flotapro_session');
        localStorage.removeItem('flotapro_permisos');
        window.location.href = '/';
        return;
    }

    // Verificar si la página actual está protegida y si el usuario tiene permiso
    const requiredPermission = routePermissions[currentPage];
    if (requiredPermission && permisos[requiredPermission] !== true) {
        if (currentPage !== 'dashboard.html') {
            alert('Acceso denegado: No tienes permisos para ingresar a este módulo.');
            window.location.href = 'dashboard.html';
            return;
        } else {
            // Si no tiene acceso al dashboard (muy raro), expúlsalo completamente.
            localStorage.removeItem('flotapro_session');
            window.location.href = '/';
            return;
        }
    }

    // 3. Ejecutar actualización de UI una vez que el DOM cargue
    window.addEventListener('DOMContentLoaded', () => {
        // Mostrar email
        const emailSpan = document.getElementById('userEmailTop');
        if (emailSpan) {
            emailSpan.innerText = sessionData.email;
            emailSpan.title = "Nivel de acceso actual";
        }

        // Ocultar opciones de menú lateral para las que no se tiene permiso
        const menuItems = {
            'navDashboard': 'mod_dashboard',
            'navMantenimiento': 'mod_mantenimiento',
            'navGarita': 'mod_garita',
            'navTesoreria': 'mod_tesoreria',
            'navAdmin': 'mod_admin',
            'navSiniestros': 'mod_siniestros',
            'navPermisos': 'mod_admin'
        };

        for (const [id, perm] of Object.entries(menuItems)) {
            const el = document.getElementById(id);
            if (el) {
                if (permisos[perm] === true) {
                    // El CSS original usa display: flex; en .sidebar-item
                    el.style.display = 'flex';
                } else {
                    el.style.display = 'none';
                }
            }
        }
    });
})();
