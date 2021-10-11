def calculate_mean_target_per_category(df, var):

    # número total de registros
    total_var = len(df)

    # Calcula el porcenaje por categoría
    temp_df = pd.Series(df[var].value_counts() / total_var).reset_index()
    temp_df.columns = [var, 'perc_var']

    # Calcula precio promedio u otro
    temp_df = temp_df.merge(df.groupby([var])['SalePrice'].mean().reset_index(),
                            on=var,
                            how='left')

    return temp_df
  
  
  def plot_categories(df, var):
    
    fig, ax = plt.subplots(figsize=(10, 4))
    plt.xticks(df.index, df[var], rotation=90)

    ax2 = ax.twinx()
    ax.bar(df.index, df["perc_houses"], color='lightgrey')
    ax2.plot(df.index, df["SalePrice"], color='green', label='Seconds')
    ax.axhline(y=0.05, color='red')
    ax.set_ylabel('porcentaje de casas por categoría')
    ax.set_xlabel(var)
    ax2.set_ylabel('Precio promedio SalePrice por categoría')
    plt.show()
  
  
