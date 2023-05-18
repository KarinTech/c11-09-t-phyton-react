int retirarDinero(struct NodoDeCliente *nodo, char *numeroCuenta, double cantidad)
{
    while (nodo != NULL)
    {
        if (strcmp(nodo->numeroCuenta, numeroCuenta) == 0)
        {
            if (nodo->saldo >= cantidad)
            {
                nodo->saldo = nodo->saldo - cantidad;
                return 1;
            }
            else
            {
                return 0;
            
        }
        
    }
    return 0;
}

int depositarDinero(struct NodoDeCliente *nodo, char *numeroCuenta, double cantidad)
{
    return retirarDinero(nodo, numeroCuenta, -cantidad);
}