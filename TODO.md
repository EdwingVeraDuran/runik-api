Hallazgos

y caches intermedios. Usa un cuerpo (OAuth2PasswordRequestForm o un UserLogin schema) para sacar la contraseña de la query string y aprovecha la
validación de Pydantic.

- Media – app/api/v1/routes/auth.py:33: al rechazar credenciales no se envía el header WWW-Authenticate: Bearer, obligatorio para que los clientes
  entiendan el motivo del 401 según la especificación OAuth2.
- Media – app/api/v1/routes/auth.py:32: no se verifica user.is_active; un usuario deshabilitado puede iniciar sesión. Añade este control para poder
  suspender cuentas.
- Baja – app/core/security.py:14: create*acces_token y las constantes relacionadas (ACCES_TOKEN*...) tienen el mismo typo. Aparte de la confusión,
  complica buscar código o mapear variables de entorno.T
