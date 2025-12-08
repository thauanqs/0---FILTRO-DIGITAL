import numpy as np
from scipy.io import wavfile
from scipy.signal import chirp

def gerar_audio_full_range(nome_arquivo="teste_sweep.wav", duracao=20):
    # 1. Configurações
    fs = 96000          # 96 KHz Taxa usada em estudios profissionais - audio Hi-res
    f_inicio = 20       # Frequência inicial (Hz)
    f_fim = 20000       # Frequência final (Hz)
    
    # 2. Vetor de tempo
    t = np.linspace(0, duracao, int(fs * duracao))

    # 3. Geração do sinal "Chirp" (Varredura Logarítmica)
    # 'logarithmic' é melhor para áudio pois nossa audição e os gráficos de Bode são log
    sinal = chirp(t, f0=f_inicio, f1=f_fim, t1=duracao, method='logarithmic')

    # 4. Controle de Amplitude (evitar clipping)
    amplitude = 0.8 # 80% do volume máximo
    sinal = sinal * amplitude

    # 5. Converter para formato de áudio de 16-bit PCM (padrão .wav)
    sinal_inteiro = np.int16(sinal * 32767)

    # 6. Salvar
    wavfile.write(nome_arquivo, fs, sinal_inteiro)
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

# Executar a função
gerar_audio_full_range()