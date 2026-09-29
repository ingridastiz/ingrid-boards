# ingridastiz.com

Sitio de Ingrid Astiz como Board Member y Consejera independiente. HTML, CSS y
JavaScript planos: sin framework, sin build, sin dependencias. Se publica tal cual
está en el repositorio.

- Producción: https://ingridastiz.com
- Hosting: Netlify, publica automáticamente cada push a la rama `main`
- Dominio: registrado en Porkbun, apuntado a Netlify (ver "DNS" más abajo)

## Estructura

```
index.html                 Página única con secciones ancladas (ES + EN)
aviso-legal.html           Aviso legal
privacidad.html            Política de privacidad
cookies.html               Política de cookies
styles.css                 Todos los estilos del sitio
script.js                  Cambio de idioma persistente
assets/ingrid.jpg          Retrato (foto de Xavi Cervera)
assets/og.jpg              Imagen de previsualización para redes (1200x630)
docs/og-source.webp        Imagen original (ChatGPT, 1536x1024) de la que sale og.jpg
netlify.toml               Configuración de publicación y cabeceras
docs/COPY.md               Especificaciones de diseño y textos aprobados (DECO)
docs/fuente-linkedin-*.md  Datos extraídos del perfil de LinkedIn, fuente del copy
```

## Cómo funciona el bilingüe

Cada página contiene los dos idiomas en el mismo HTML. Los textos se duplican en
`<span class="es">` y `<span class="en">` (o `div`, `ul`, `blockquote` con esas
clases cuando es un bloque entero), y `styles.css` muestra uno u otro según la clase
`lang-en` que `script.js` pone o saca del `<body>`.

`script.js` guarda el idioma elegido en `localStorage`, con la clave
`ingridastiz-lang`, y marca como activo el botón ES o EN del selector. Si no hay
nada guardado, arranca en castellano.

Para agregar un texto bilingüe nuevo, repetir el patrón de los dos spans. Para
agregar una sección, copiar una existente y sumar el enlace en el `<nav>`.

## Desarrollo local

No hace falta instalar nada para editar. Para previsualizar conviene levantar un
servidor estático, porque los enlaces del pie no llevan extensión (`/privacidad`,
no `/privacidad.html`):

```
python3 -m http.server 8080
```

Netlify resuelve las URL sin extensión con su opción de "pretty URLs". En local, el
servidor de Python no lo hace: las páginas legales se abren con `.html`.

## Publicación

Netlify publica automáticamente cada push a la rama `main`. No hay paso de build:
`netlify.toml` indica que se publique la raíz del repositorio.

Para revertir, hacer un commit nuevo o restaurar un deploy anterior desde el panel
de Netlify.

## DNS (Porkbun)

El dominio se gestiona en Porkbun con los nameservers de Porkbun. Para que apunte al
sitio en Netlify hacen falta estos registros, y nada más para el sitio web:

| Tipo  | Host | Valor                      |
|-------|------|----------------------------|
| A     | @    | 75.2.60.5                  |
| CNAME | www  | ingridastiz.netlify.app    |

Además hay que borrar cualquier "URL forwarding" (reenvío) que Porkbun tenga
configurado para el dominio, porque compite con los registros anteriores. Netlify
emite el certificado HTTPS solo cuando ve que el dominio apunta a sus servidores;
puede tardar desde minutos hasta unas horas por la propagación de DNS.

En Netlify el dominio ya está cargado como dominio principal, con www redirigiendo.

## De dónde salen los textos

Los textos están en `docs/COPY.md`, redactados a partir del perfil de LinkedIn de
Ingrid (`docs/fuente-linkedin-2026-09-29.md`). Si Ingrid mantiene un documento DECO
propio fuera del repositorio, manda ese documento: el HTML se corrige a partir de él.

## Regenerar la imagen para redes

`assets/og.jpg` se genera con Python y Pillow recortando `docs/og-source.webp`:

```
python3 docs/make-og.py
```

## Licencia

Código bajo MIT No Attribution: se puede copiar, modificar y reutilizar sin permiso y
sin atribuir. Los textos, las imágenes de `assets/` (la fotografía es de Xavi Cervera)
y la identidad de marca no están incluidos y conservan todos sus derechos. Ver LICENSE.
