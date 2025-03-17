import pandas as pd

# Carregar dados
rappers = pd.read_csv('../data/rappers.csv')

# Calcular pontuação média
rappers['score'] = rappers[['flow', 'lyrics', 'originality', 'stage_presence', 'cultural_impact']].mean(axis=1)

# Ordenar por pontuação
rappers = rappers.sort_values(by='score', ascending=False)

# Salvar resultados
rappers.to_csv('../results/evaluation_results.csv', index=False)
print(rappers)
