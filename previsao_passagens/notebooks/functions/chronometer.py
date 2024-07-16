def check_time(start, end):
    seg = end - start
    dias = seg // 86400
    Seg_Restantes_Após_Dias = seg % 86400
    horas = Seg_Restantes_Após_Dias // 3600         # Divisão inteira
    Seg_Restantes_Apos_Hora = seg % 3600            # Resto da divisão por 3600
    minutos = Seg_Restantes_Apos_Hora // 60         # Divisão inteira dos segundos restantes
    Seg_Restantes_Apos_Minutos = seg % 60
    #print(minutos,'minutos','e', '%.2f' % Seg_Restantes_Apos_Minutos,'segundos')
    print(dias,'dias', horas,'horas', minutos,'minutos','e', '%.2f' % Seg_Restantes_Apos_Minutos,'segundos')