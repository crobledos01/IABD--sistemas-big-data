#!/bin/bash
set -x

NN_DIR="/opt/hadoop/data/nameNode"

echo "[namenode] Iniciando NameNode"
echo "[namenode] Directorio de metadatos: $NN_DIR"

# Formatear SOLO la primera vez
if [ ! -d "$NN_DIR/current" ]; then
  echo "[namenode] No se encuentra un NameNode inicializado. Formateando..."
  hdfs namenode -format -force -nonInteractive
else
  echo "[namenode] NameNode ya inicializado. Se omite el formateo."
fi

echo "[namenode] Arrancando YARN ResourceManager..."
yarn --daemon start resourcemanager

echo "[namenode] Arrancando servicio NameNode (foreground)..."
# Mantiene el contenedor vivo
hdfs namenode
