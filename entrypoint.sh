#!/bin/bash
set -e

echo "=== Odoo Entrypoint ==="

# Vérifier si Odoo est déjà initialisé
if ! psql -h "${HOST:-db}" -U "$USER" -d "${POSTGRES_DB:-odoodb}" -c "SELECT 1 FROM ir_module_module LIMIT 1;" > /dev/null 2>&1; then
    echo "Initialisation d'Odoo..."
    # CORRECTION: sans --without-demo=all
    odoo -d "${POSTGRES_DB:-odoodb}" -i base --stop-after-init
    echo "✅ Odoo initialisé avec succès !"
else
    echo "✅ Odoo déjà initialisé."
fi

echo "=== Démarrage d'Odoo ==="
exec odoo "$@"

