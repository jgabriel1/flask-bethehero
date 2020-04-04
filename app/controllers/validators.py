create_incident = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "maxLength": 50
        },
        "description": {
            "type": "string",
            "maxLength": 500
        },
        "value": {
            "type": "number"
        }
    },
    "additionalProperties": False,
    "minProperties": 3
}

create_ong = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "maxLength": 50
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "whatsapp": {
            "type": "string",
            "minLength": 10,
            "maxLength": 11
        },
        "city": {
            "type": "string"
        },
        "uf": {
            "type": "string",
            "minLength": 2,
            "maxLength": 2
        }
    },
    "additionalProperties": False,
    "minProperties": 5
}

ong_login = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        }
    },
    "addiotionalProperties": False,
    "minProperties": 1
}
