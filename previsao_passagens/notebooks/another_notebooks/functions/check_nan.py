# Check NaN Pandas and Numpy
def just_check_nan(df):
    missing_val_count_by_column = (df.isna().sum())
    columns_with_nan = missing_val_count_by_column[missing_val_count_by_column > 0]
    print('Dados com NaN:')
    print(columns_with_nan)
    print('')
    print('columns_with_nan.shape', columns_with_nan.shape)
    print('')

    
#########################################################################################################
# fix NaN Pandas and Numpy
def fix_nan(df):
    missing_val_count_by_column = (df.isna().sum())
    columns_with_nan = missing_val_count_by_column[missing_val_count_by_column > 0]
    print('Dados com NaN:')
    print(columns_with_nan)
    print('')
    print('columns_with_nan.shape', columns_with_nan.shape)
    print('')

    # if database have some NA column, fillna this
    if (columns_with_nan.any() == 1):
        print('df.shape antes de retirar NaN', df.shape)
        print('')
        print('================= DataFrame COM NaN =================')
        print('')
        #df[column] = df[column].fillna('Other')
        df = df.fillna(df.mean())
        print('df.shape depois de retirar NaN', df.shape)
        print('')
    else:
        print('================= DataFrame SEM NaN =================')
        print('')
    
    return df