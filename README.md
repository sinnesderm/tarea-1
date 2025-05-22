# STO270 - Lenguajes Formales y Compiladores  
## Tarea 1: Minimización de DFA  

### Información del Estudiante  
- **Nombre completo**: Steven Granda Palencia  
- **Número de clase**: ST0270  
- **Sistema Operativo**: Ubuntu 22.04 LTS  
- **Lenguaje de programación**: Python 3.10.12  
- **Herramientas**: VS Code, Git  

---

### 🔍 Explicación del Algoritmo  
Implementación del **algoritmo de partición refinada** descrito en *Kozen (1997), Lecture 14*:  

#### **Conceptos Clave**  
1. **Estados equivalentes**: Dos estados `p` y `q` son equivalentes si para toda cadena `x ∈ Σ*`, las transiciones desde `p` y `q` llevan a estados indistinguibles (ambos finales o no finales).  
2. **Partición refinada**: Agrupa estados que son equivalentes en iteraciones sucesivas.  

#### **Pasos del Algoritmo**  
1. **Inicialización**:  
   - Crear una partición inicial `P₀` con dos grupos:  
     - `F` (estados finales).  
     - `Q \ F` (estados no finales).  

2. **Refinamiento iterativo**:  
   - Para cada grupo `G` en la partición actual:  
     - Dividir `G` en subgrupos donde, para cada símbolo `a ∈ Σ`, las transiciones de los estados bajo `a` caigan en el **mismo grupo actual**.  
     - Si un subgrupo se divide, actualizar la partición y repetir.  

3. **Terminación**:  
   - Cuando ninguna partición puede refinarse más, los estados en un mismo grupo son equivalentes y pueden colapsarse.  

**Ejemplo**:  
- Si `P_final = [{1, 4}, {5}, {0, 2, 3}]`, los pares equivalentes son `(1, 4)`.  

---

### Instrucciones de Ejecución  
1. **Requisitos**:  
   - Python 3.x instalado (`sudo apt install python3` en Ubuntu).  
   - Terminal de línea de comandos.  

2. **Ejecución**:  
   ```bash
   # Opción 1: Redirección desde archivo (recomendado)
   python3 minimize_dfa.py < input.txt

   # Opción 2: Entrada interactiva
   python3 minimize_dfa.py
