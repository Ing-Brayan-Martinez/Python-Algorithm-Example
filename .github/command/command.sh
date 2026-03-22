# Instalar black
pip install black

# Formatear todo el proyecto
black src/ test/

# Ver cambios sin aplicar
black --diff src/

# Solo verificar sin cambiar
black --check src/





# 1. Formatear automáticamente
black src/ test/

# 2. Verificar con pylint
pylint src/

# 3. Ejecutar tests
pytest




pylint src/
#Analizar todo el código

pylint --errors-only src/
#Solo errores críticos

black src/
#Formatear automáticamente

black --check src/
#Verificar sin modificar

pylint --generate-rcfile > .pylintrc
#Generar config completa
