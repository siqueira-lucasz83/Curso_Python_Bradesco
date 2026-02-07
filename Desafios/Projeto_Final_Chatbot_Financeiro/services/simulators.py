def juros_compostos(valor, taxa, meses):
    return valor * (1 + taxa) ** meses

def simular_cdi(valor, taxa_anual, meses):
    taxa_mensal = taxa_anual / 12
    return valor * (1 + taxa_mensal) ** meses

def simular_financiamento(valor, taxa, meses):
    taxa_mensal = taxa / 100
    parcela = valor * (taxa_mensal * (1 + taxa_mensal) ** meses) / ((1 + taxa_mensal) ** meses - 1)
    return parcela
