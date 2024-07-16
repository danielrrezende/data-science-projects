def define_features(clients_sample):
    # features
    features = ['cssocialsecno_encrypted', 'customer_tenure', 'm0_qt_involuntary_suspension', 'm0_qt_voluntary_suspension', 
                'nxt_3g_traffic_volume_m0', 'nxt_4g_traffic_volume_m0', 'vivo_traffic_volume_m0', 'contract_loyalty_flag',
                'person_type', 'payment_method', 'inar_rate_plan', 'contract_status', 'contract_status_reason', 'device_type_m0',
                'm0_call_term_err', 'billing_ticket_m0', 'billing_ticket_m1', 'billing_ticket_m2', 'billing_ticket_m3', 
                'billing_ticket_m4', 'billing_ticket_m5']

    # set features in dataframe
    clients_sample = clients_sample[features]

    # drop cssocialsecno_encrypted rows that have nan
    clients_sample = clients_sample.dropna(subset=['cssocialsecno_encrypted'])

    # fill with 0 some features that cannot receive fillna mean
    clients_sample["m0_qt_involuntary_suspension"] = clients_sample["m0_qt_involuntary_suspension"].fillna(0)
    clients_sample["m0_qt_voluntary_suspension"] = clients_sample["m0_qt_voluntary_suspension"].fillna(0)
    clients_sample["nxt_3g_traffic_volume_m0"] = clients_sample["nxt_3g_traffic_volume_m0"].fillna(0)
    clients_sample["nxt_4g_traffic_volume_m0"] = clients_sample["nxt_4g_traffic_volume_m0"].fillna(0)
    clients_sample["vivo_traffic_volume_m0"] = clients_sample["vivo_traffic_volume_m0"].fillna(0)
    clients_sample["m0_call_term_err"] = clients_sample["m0_call_term_err"].fillna(0)
    clients_sample["billing_ticket_m0"] = clients_sample["billing_ticket_m0"].fillna(0)
    clients_sample["billing_ticket_m1"] = clients_sample["billing_ticket_m1"].fillna(0)
    clients_sample["billing_ticket_m2"] = clients_sample["billing_ticket_m2"].fillna(0)
    clients_sample["billing_ticket_m3"] = clients_sample["billing_ticket_m3"].fillna(0)
    clients_sample["billing_ticket_m4"] = clients_sample["billing_ticket_m4"].fillna(0)
    clients_sample["billing_ticket_m5"] = clients_sample["billing_ticket_m5"].fillna(0)

    # fill with 'other' some features that cannot receive fillna mean
    clients_sample['device_type_m0'] = clients_sample['device_type_m0'].fillna('Other')
    
    # fill with mean
    clients_sample['customer_tenure'] = clients_sample['customer_tenure'].fillna(clients_sample['customer_tenure'].mean())
    
    return clients_sample

##############################################################################################################################
def edit_features(X):
    # Filtrando as 31 categorias de 'contract_status_reason' em 3 no total.
    column_IN = ['ativando', 'reativando', 'Reativação Port-in', 'Suspensao Port-in', 'Desativacao Port-in', 
                 'IN-Suspensão Parcial', 'IN-Não Pagamento', 'IN-Reativação 15 dias', 
                 'IN-Reativação 15 dias A', 'IN-Fraude', 'IN-Fraude ', 'IN-Não Pagamento', 'IN-Não Pagamento ', 
                 'IN-Suspensão para Regularização']

    column_VO = ['VO', 'VO-Suspensao Roubo/Furto', 'VO-Suspensao Perda', 'VO-Suspensao 120 dias', 'VO-Suspensão 30 dias', 
                 'VO-Processando Cancelamento', 'VO-Custo equip/conserto equip', 'VO-Custo equip/conserto equip ',
                 'VO-Problemas financeiros/estrutural', 'VO-Problemas financeiros/estrutural ', 
                 'VO-Falta orientação sobre serv/prod', 'VO-Suspensao 60 dias', 'VO-Suspensão Perda / Roubo', 
                 'VO-Planos de Serv/Prod da concor', 'VO-Suspensao 90 dias', 'VO-Suspensão Parcial Sem Cobrança',
                 'VO-Falta orientação sobre serv/prod ', 'VO-Planos de Serv/Prod da concor ', 
                 'VO-Neces. novas áreas de cobertura ', 'VO-Insatisfação com a fatura ' ]

    column_FC = ['FC-Fulfil/Trans Comodato/Locação', 'FC-Fulfil/Trans Comodato/Locação ', 'FC-Regularização de Usuario', 
                 'TAKEOVER', 'Aparelho Localizado', 'Targys aguardando', 'RV-Devolução entrega/Recusa entrega', 
                 'RV-Devolução entrega/Recusa entrega ', 'FC-Transf serviços terceiros', 'FC-SubstituiçãoxVenda ']
    
    # Substituição das 31 categorias em 3 no total.
    X['contract_status_reason'] = X['contract_status_reason'].replace([column_IN], 'IN')
    X['contract_status_reason'] = X['contract_status_reason'].replace([column_VO], 'VO')
    X['contract_status_reason'] = X['contract_status_reason'].replace([column_FC], 'FC')
    X['contract_status_reason'] = X['contract_status_reason'].replace(['Should not display'], 'IN')
