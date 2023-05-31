Para la documentación interna del equipo es muy importante tener claro el esquema de datos sobre el que se está trabajando, el acceso a la información será más fácil y rápido. El siguiente diagrama contiene el resultado final del modelo que utiliza actualmente la aplicación. En la sección correspondiente de la memoria se encuentran las explicaciones necesarias en caso de que no se entienda alguna relación con solo esta información.

```mermaid
erDiagram
	CULTIVO ||--o{ CULTIVO : is
	CULTIVO ||--o{ MIRAR_FENOLOGICO : contains
	CULTIVO {
		string nombre FK
		string es_variedad FK
	}

    INDICE ||--o{ MIRAR_INDICE : contains
    INDICE {
        string nombre FK
        string descripcion
    }
    PIXEL ||--o{ MIRAR_INDICE : contains
    PIXEL ||--o{ PARCELA : is
    PIXEL {
        string parcela FK 
        polygon geom
        string idx
    }
    PARCELA ||--o{ ESTACION : contains
    PARCELA ||--o{ MIRAR_FENOLOGICO : contains
    PARCELA {
        string idx 
        string estacion FK
        float altitud
        polygon geom
    }
    MIRAR_INDICE {
        string indice FK
        string pixel FK
        date fecha
        geojson json
        float valor
    }
    MIRAR_FENOLOGICO {
        string cultivo FK
        string parcela FK
        date fecha
        string estado
    }
    ESTACION ||--o{ ESTACION_HISTORICO : contains
    ESTACION {
		string nombre FK
    }
    ESTACION_HISTORICO {
		string estacion FK
		date fecha
		charfield file
    }
```

