-- ============================================================
-- CORRECCIÓN DE CODIFICACIÓN — rpg_platform
-- Ejecutar en phpMyAdmin: selecciona rpg_platform → pestaña SQL
-- ============================================================

SET NAMES utf8mb4;

-- ============================================================
-- TABLA: clase
-- ============================================================

UPDATE `clase` SET
    `nombre` = 'Mago',
    `descripcion` = 'Estudioso de las artes arcanas. Lanza poderosos hechizos a costa de una baja resistencia física. Su inteligencia es su mayor arma.'
WHERE `id_clase` = 2;

UPDATE `clase` SET
    `nombre` = 'Bárbaro',
    `descripcion` = 'Guerrero salvaje que entra en furia para devastar enemigos. Increíble resistencia física y poder bruto, pero poco control emocional.'
WHERE `id_clase` = 3;

UPDATE `clase` SET
    `nombre` = 'Pícaro',
    `descripcion` = 'Especialista en sigilo, trampas y ataques furtivos. Ágil y calculador, prefiere atacar desde las sombras antes que el combate directo.'
WHERE `id_clase` = 4;

UPDATE `clase` SET
    `nombre` = 'Clérigo',
    `descripcion` = 'Devoto de una deidad que canaliza poder divino. Puede sanar aliados, bendecir al grupo y castigar a los no muertos con luz sagrada.'
WHERE `id_clase` = 5;

-- ============================================================
-- TABLA: raza
-- ============================================================

UPDATE `raza` SET
    `descripcion` = 'Pueblo robusto forjado bajo las montañas. Conocidos por su resistencia, lealtad y maestría en la herrería. Viven siglos y jamás olvidan una deuda.'
WHERE `id_raza` = 1;

UPDATE `raza` SET
    `descripcion` = 'Raza ancestral de gracia sobrenatural. Dotados de agudos sentidos y afinidad innata con la magia. Su longevidad les otorga una perspectiva única del mundo.'
WHERE `id_raza` = 2;

UPDATE `raza` SET
    `descripcion` = 'Guerreros feroces nacidos de tierras salvajes. Su fuerza bruta supera a casi cualquier raza. Aunque temidos, muchos buscan honor y redención en el campo de batalla.'
WHERE `id_raza` = 3;

UPDATE `raza` SET
    `descripcion` = 'Pequeños y ágiles, conocidos por su suerte extraordinaria. Pasan desapercibidos con facilidad y poseen un carisma natural que encanta a quienes los rodean.'
WHERE `id_raza` = 4;

UPDATE `raza` SET
    `descripcion` = 'La raza más adaptable y ambiciosa. Sin una habilidad dominante, los humanos compensan con versatilidad, determinación y una increíble capacidad de aprendizaje.'
WHERE `id_raza` = 5;

-- ============================================================
-- TABLA: usuarios_rol
-- ============================================================

UPDATE `usuarios_rol` SET
    `nombre` = 'Administrador',
    `descripcion` = 'Dios del Sistema con control total sobre el portal. Gestiona usuarios, roles, campañas y configuraciones globales. Puede crear, editar y eliminar cualquier elemento de la plataforma. Acceso completo al panel de administración de Django.'
WHERE `id` = 1;

UPDATE `usuarios_rol` SET
    `nombre` = 'Jugador',
    `descripcion` = 'Aventurero que se une a las partidas del portal. Puede explorar campañas activas, gestionar su personaje y participar en sesiones de juego. Acceso básico a la plataforma sin permisos de administración.'
WHERE `id` = 2;

UPDATE `usuarios_rol` SET
    `nombre` = 'Narrador',
    `descripcion` = 'Maestro del Dungeon encargado de dirigir las partidas. Puede crear y gestionar campañas, definir historias, administrar encuentros y guiar a los jugadores a través de la aventura. Tiene permisos extendidos sobre el contenido de las sesiones.'
WHERE `id` = 3;

UPDATE `usuarios_rol` SET
    `nombre` = 'Guardián del Tesoro',
    `descripcion` = 'Protege los recursos y activos de la campaña. Acceso a inventarios y recompensas del grupo.'
WHERE `id` = 4;

UPDATE `usuarios_rol` SET
    `nombre` = 'Cronista de Batallas',
    `descripcion` = 'Registra el historial de partidas y eventos. Puede editar bitácoras y reportes de sesión.'
WHERE `id` = 5;

UPDATE `usuarios_rol` SET
    `nombre` = 'Heraldo del Rey',
    `descripcion` = 'Mensajero oficial con permisos de comunicación entre facciones del sistema.'
WHERE `id` = 6;

UPDATE `usuarios_rol` SET
    `nombre` = 'Archimago',
    `descripcion` = 'Rol técnico avanzado. Acceso a configuraciones especiales del portal.'
WHERE `id` = 7;

UPDATE `usuarios_rol` SET
    `nombre` = 'Explorador de Tierras',
    `descripcion` = 'Usuario nuevo en la plataforma. Permisos de solo lectura en la mayoría de secciones.'
WHERE `id` = 8;

UPDATE `usuarios_rol` SET
    `nombre` = 'Forjador de Leyendas',
    `descripcion` = 'Creador de contenido. Puede crear y editar campañas, mapas e historias.'
WHERE `id` = 9;

UPDATE `usuarios_rol` SET
    `nombre` = 'Oráculo',
    `descripcion` = 'Rol de moderación. Puede visualizar todas las partidas activas sin intervenir.'
WHERE `id` = 10;

UPDATE `usuarios_rol` SET
    `nombre` = 'Paladín de la Alianza',
    `descripcion` = 'Mediador entre jugadores. Gestiona conflictos y reportes dentro del sistema.'
WHERE `id` = 11;

UPDATE `usuarios_rol` SET
    `nombre` = 'Mercader Errante',
    `descripcion` = 'Acceso limitado al módulo de ítems y economía del juego.'
WHERE `id` = 12;

UPDATE `usuarios_rol` SET
    `nombre` = 'Semidiós Ascendido',
    `descripcion` = 'Rol temporal de prueba con permisos elevados bajo supervisión del Administrador.'
WHERE `id` = 13;
