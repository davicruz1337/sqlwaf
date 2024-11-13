# SQLWAF - Advanced SQL Injection Generator

SQLWaf é um gerador avançado de payloads SQL Injection focado em bypass de WAF e técnicas modernas de injeção.

*Apenas para uso educacional e CTFs*

## Features

### Tipos de Payload
```
a - Boolean-based
b - Time-based 
c - Error-based
d - Union-based
e - Stacked queries
```

### Técnicas de Evasão
- Multiple Encoding (URL, Double URL, Hex, CHAR)
- Case Randomization
- Comentários (Inline, Multi-line, Nested)
- Space Bypass
- String Concatenation
- Version Comments
- Alternative Operators
- WAF Filters Bypass

### Funcionalidades
- Geração Dinâmica
- Sistema Anti-duplicação
- Histórico de Payloads (JSON)
- Hash MD5 Tracking
- Timing de Execução 
- Limite de Tamanho
- Output Customizado
- Modo Verbose
- Salvamento em Arquivo

## Uso
```bash
# Ajuda
python sqlwaf.py -h

# Gerar 5 payloads (padrão)
python sqlwaf.py

# Gerar 10 payloads time-based
python sqlwaf.py -n 10 -t b

# Modo verbose com output
python sqlwaf.py -v -o payloads.txt

# Limitar tamanho do payload
python sqlwaf.py --max-length 50

# Salvar histórico
python sqlwaf.py --save-history

# Carregar histórico anterior
python sqlwaf.py --load-history
```

## Argumentos
```
-h, --help      Mostra ajuda
-n N            Número de payloads [padrão: 5]
-t TYPE         Tipo de payload [a,b,c,d,e,all]
-o FILE         Arquivo de output
-v              Modo verbose
--no-encode     Desabilita encoding
--max-length N  Tamanho máximo
--save-history  Salva histórico
--load-history  Carrega histórico
```

## Exemplos de Output

### Modo Normal
```
1. ' AND 1=1--
2. ' UNION SELECT NULL,NULL#
3. ') OR '1'='1'/**/
```

### Modo Verbose
```
1. Type: b
   Length: 45
   Time: 14:23:45  
   Hash: d41d8cd98f00b204e9800998ecf8427e
   Payload: ' AND SLEEP(5)--
```

## Técnicas Avançadas

### Boolean-based
- Comparações Lógicas
- Operadores Alternativos 
- Multiple Conditionals
- Regex Matching

### Time-based
- Sleep Functions
- Heavy Queries
- Conditional Delays
- Benchmark Operations

### Error-based
- XML/UpdateXML
- ExtractValue
- GeometryCollection
- JSON Functions

### Union-based
- Column Number Discovery
- NULL Padding
- DUAL Table
- Information Schema

### Stacked Queries
- Multiple Statements
- Data Modification
- Schema Changes
- Privilege Escalation

## Output Archive
```
history.json
└── Armazena payloads anteriores
    ├── Hash MD5
    └── Payload
```

## Notas
- Gerador dinâmico e aleatório
- Bypass de WAFs modernos
- Técnicas 2023/2024
- Alta taxa de sucesso
- Payload único por hash

## Aviso Legal
```
Ferramenta apenas para fins educacionais e CTFs.
Não use para fins maliciosos.
O autor não é responsável pelo mal uso.
```

## Autor
Created by @davicruz1337
