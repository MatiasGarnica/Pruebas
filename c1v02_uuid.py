# identificador unico. Se usan para identificar información que debe ser unica y no debe repetirse
import uuid

codigo_uuid = uuid.uuid4()
print(codigo_uuid, type(codigo_uuid))

codigo_str = str(codigo_uuid)
print(codigo_str, type(codigo_str))