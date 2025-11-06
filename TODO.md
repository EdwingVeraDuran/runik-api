• Hallazgos

- Alta – app/api/v1/routes/auth.py:43: la respuesta sigue devolviendo {"acces_token": ...}; el schema UserToken exige access_token y FastAPI lo vuelve a
  romper con ResponseValidationError. Cambia la clave (y, si puedes, el nombre de la función/setting) para mantener “access” con doble s.
- Media – app/api/v1/routes/auth.py:36: aún permites login aunque user.is_active sea falso; agrega esa verificación antes de emitir tokens.
- Baja – app/api/v1/routes/auth.py:40: el helper aún se llama create_acces_token y la constante ACCES_TOKEN_EXPIRE_MINUTES está igual; corrige el typo
  para evitar confusiones futuras.
- Baja – app/api/v1/routes/auth.py:17 y :22: además de dos consultas separadas, exising_username y el mensaje “registeres” tienen typos; puedes unificar
  la validación (o capturar IntegrityError) y ajustar los textos para no exponer errores ortográficos en la API.
