#!/bin/bash
set -e

DN_DIR="/opt/hadoop/data/dataNode"

echo "[$(hostname)] Iniciando DataNode"
echo "[$(hostname)] Directorio de datos: $DN_DIR"

# Persistente: no borramos el directorio si ya existe
if [ ! -d "$DN_DIR" ]; then
  echo "[$(hostname)] El directorio datanode no existe. Creando..."
  mkdir -p "$DN_DIR"
else
  echo "[$(hostname)] Directorio datanode ya existe. No se borra (persistente)."
fi

echo "[$(hostname)] Estableciendo propietario y permisos"
chown -R hadoop:hadoop "$DN_DIR" || true
chmod 755 "$DN_DIR" || true

echo "[$(hostname)] Arrancando YARN NodeManager..."
yarn --daemon start nodemanager

echo "[$(hostname)] Arrancando servicio DataNode (foreground)..."
# Mantiene el contenedor vivo
hdfs datanode
