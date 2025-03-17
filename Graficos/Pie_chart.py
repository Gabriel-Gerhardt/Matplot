import matplotlib.pyplot as plt
import numpy as np

# Dados
atend = np.array([90, 62, 31, 44, 13])
dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']

# Calculando os percentuais
atend_rel = np.round(atend / np.sum(atend) * 100, 1)

# Adicionando o símbolo de porcentagem
labels_rel = [f'{p}%' for p in atend_rel]

# Criando os gráficos de pizza
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico de pizza com frequência absoluta
axs[0].pie(atend, labels=atend, colors=plt.cm.gray(np.arange(5)/4), 
           autopct='%1.1f%%', startangle=140)
axs[0].set_title('Atendimentos_numeros', fontsize=16)
axs[0].legend(dias_semana, loc="best")

# Gráfico de pizza com frequência relativa
axs[1].pie(atend, labels=labels_rel, colors=plt.cm.gray(np.arange(5)/4), 
           autopct='%1.1f%%', startangle=140)
axs[1].set_title('Atendimentos_porcentagem', fontsize=16)
axs[1].legend(dias_semana, loc="best")

plt.show()