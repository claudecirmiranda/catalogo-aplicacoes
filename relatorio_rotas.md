
# Relatório de Rotas

## 1. Endpoint para criar lista de produtos favoritos do usuário logado.

- **URL interna:** 
  `POST /api/nagem/favorite_products/create_list_products`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para criar lista de produtos favoritos do usuário logado.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "updateFavoriteItems",
    "in": "body",
    "description": "payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/updateFavoriteItems"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "201": {
    "description": "Created"
  },
  "401": {
    "description": "Unauthorized"
  },
  "500": {
    "description": "Internal Server Error"
  }
}
```

---

## 2. Endpoint obter o login do usuário

- **URL interna:** 
  `POST /api/nagem/login`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint obter o login do usuário

**Entrada:**
```json
[]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 3. Endpoint para cadastrar pedido atual

- **URL interna:** 
  `POST /api/nagem/order/current/itens/add`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para cadastrar pedido atual

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "AddCurrentItem",
    "in": "body",
    "description": "Payload da requisição",
    "schema": {
      "$ref": "#/definitions/AddCurrentItem"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 4. Endpoint para calcular o preço do pedido atual do usuário.

- **URL interna:** 
  `POST /api/nagem/order/current/price`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para calcular o preço do pedido atual do usuário.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "UserOrder",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/UserOrder"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 5. Endpoint para adicionar pagamento ao pedido atual do usuário.

- **URL interna:** 
  `POST /api/nagem/order/current/payments/add`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para adicionar pagamento ao pedido atual do usuário.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "currentPaymentAdd",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/currentPaymentAdd"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 6. Endpoint para obter métodos de pagamento do pedido atual do usuário.

- **URL interna:** 
  `POST /api/nagem/order/current/payment_methods`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para obter métodos de pagamento do pedido atual do usuário.

**Entrada:**
```json
[
  {
    "name": "paymentMethods",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/paymentMethods"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 7. Endpoint para enviar o pedido atual do usuário.

- **URL interna:** 
  `POST /api/nagem/order/current/submit`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para enviar o pedido atual do usuário.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "UserOrder",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/UserOrder"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 8. Endpoint para repetir pedido. 

- **URL interna:** 
  `POST /api/nagem/order/retry`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para repetir pedido. 

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 9. Endpoint para repetir pedido legacy.

- **URL interna:** 
  `POST /api/nagem/order/retry_legacy`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para repetir pedido legacy.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "retryOrderLegacy",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/retryOrderLegacy"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 10. Endpoint para obter produtos visualizados.

- **URL interna:** 
  `POST /api/nagem/viewed_products`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para obter produtos visualizados.

**Entrada:**
```json
[
  {
    "name": "body",
    "in": "body",
    "schema": {
      "type": "object",
      "properties": {
        "customer_id": {
          "example": "any"
        },
        "product_id": {
          "example": "any"
        },
        "cart_products": {
          "example": "any"
        }
      }
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 11. Endpoint para obter as notificações de um produto

- **URL interna:** 
  `POST /api/nagem/addProductNotification`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para obter as notificações de um produto

**Entrada:**
```json
[
  {
    "name": "body",
    "in": "body",
    "schema": {
      "type": "object",
      "properties": {
        "email": {
          "example": "any"
        },
        "product_id": {
          "example": "any"
        },
        "site_id": {
          "example": "any"
        }
      }
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 12. Endpoint para obter os produtos que podem ser comprados juntos.

- **URL interna:** 
  `POST /api/nagem/buy_together`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para obter os produtos que podem ser comprados juntos.

**Entrada:**
```json
[
  {
    "name": "buyToGether",
    "in": "body",
    "description": "payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/buyToGether"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 13. Endpoint para obter produtos relacionados ao interesse do cliente.

- **URL interna:** 
  `POST /api/nagem/related_to_your_interest`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para obter produtos relacionados ao interesse do cliente.

**Entrada:**
```json
[
  {
    "name": "relatedToYourInterest",
    "in": "body",
    "description": "payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/relatedToYourInterest"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 14. Endpoint para obter produtos quem viu comprou.

- **URL interna:** 
  `POST /api/nagem/who_saw_who_bought`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para obter produtos quem viu comprou.

**Entrada:**
```json
[
  {
    "name": "whoSawWhoBought",
    "in": "body",
    "description": "paylod da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/whoSawWhoBought"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 15. Endpoint para Informações do serviço de frete.

- **URL interna:** 
  `POST /api/nagem/shipping`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para Informações do serviço de frete.

**Entrada:**
```json
[
  {
    "name": "shipping",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/shipping"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 16. Endpoint para registo de informações do usuário.

- **URL interna:** 
  `POST /api/nagem/user/register`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para registo de informações do usuário.

**Entrada:**
```json
[
  {
    "name": "UserRegister",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/UserRegister"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 17. Endpoint para verificar cpf do usuário.

- **URL interna:** 
  `POST /api/nagem/user/verify/cpf`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para verificar cpf do usuário.

**Entrada:**
```json
[
  {
    "name": "VerifyCpf",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/VerifyCpf"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 18. Endpoint para login do usuário.

- **URL interna:** 
  `POST /api/nagem/user/login`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para login do usuário.

**Entrada:**
```json
[
  {
    "name": "login",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/login"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 19. Endpoint para verificar o token do usuário.

- **URL interna:** 
  `POST /api/nagem/user/token/verify`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para verificar o token do usuário.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 20. Endpoint para atualizar o token do usuário.

- **URL interna:** 
  `POST /api/nagem/user/token/refresh`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para atualizar o token do usuário.

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 21. Endpoint para enviar uma push notification para o usuário.

- **URL interna:** 
  `POST /api/nagem/user/push/register`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para enviar uma push notification para o usuário.

**Entrada:**
```json
[]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 22. Endpoint para cadastro de endereço do usuário

- **URL interna:** 
  `GET /api/nagem/user/address`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para cadastro de endereço do usuário

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "UserAddressAdd",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/UserAddressAdd"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 23. Endpoint para cadastro de endereço do usuário

- **URL interna:** 
  `POST /api/nagem/user/address`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para cadastro de endereço do usuário

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "UserAddressAdd",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/UserAddressAdd"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 24. Endpoint para resetar o password do usuário .

- **URL interna:** 
  `POST /api/nagem/user/reset_password`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para resetar o password do usuário .

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "login",
    "description": "email do usuário para reset de senha.",
    "in": "query",
    "type": "string"
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 25. Endpoint para resetar o password do usuário .

- **URL interna:** 
  `POST /api/nagem/user/login/reset_password`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para resetar o password do usuário .

**Entrada:**
```json
[
  {
    "name": "login",
    "description": "email do usuário para reset de senha.",
    "in": "query",
    "type": "string"
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 26. Endpoint para cadastrar cartão de crédito do atual. 

- **URL interna:** 
  `GET /api/nagem/user/credit_card`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para cadastrar cartão de crédito do atual. 

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "Requisição",
    "in": "body",
    "description": "Payload da requisição",
    "schema": {
      "$ref": "#/definitions/creditCard"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 27. Endpoint para cadastrar cartão de crédito do atual. 

- **URL interna:** 
  `POST /api/nagem/user/credit_card`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para cadastrar cartão de crédito do atual. 

**Entrada:**
```json
[
  {
    "name": "authorization",
    "in": "header",
    "type": "string"
  },
  {
    "name": "Requisição",
    "in": "body",
    "description": "Payload da requisição",
    "schema": {
      "$ref": "#/definitions/creditCard"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  },
  "401": {
    "description": "Unauthorized"
  }
}
```

---

## 28. Endpoint para envio de mensagem do usuário

- **URL interna:** 
  `POST /api/nagem/user/contact_us`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para envio de mensagem do usuário

**Entrada:**
```json
[
  {
    "name": "contactUS",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/contactUS"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---

## 29. Endpoint para login social

- **URL interna:** 
  `POST /api/nagem/user/social_login`
- **URL OCC:** 
  `https://p9351450c1prd-store.occa.ocs.oraclecloud.com/ccstore/v1/purchaseLists`
- **Descrição:**
  Endpoint para login social

**Entrada:**
```json
[
  {
    "name": "loginSocial",
    "in": "body",
    "description": "Payload da requisição",
    "required": true,
    "schema": {
      "$ref": "#/definitions/loginSocial"
    }
  }
]
```

**Saída:**
```json
{
  "200": {
    "description": "OK"
  },
  "400": {
    "description": "Bad Request"
  }
}
```

---
