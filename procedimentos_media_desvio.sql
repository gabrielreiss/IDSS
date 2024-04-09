-- Consulta para calcular estatísticas sobre procedimentos

SELECT 
  -- Código do procedimento
  CD_PROCEDIMENTO,

  -- Média do valor do item por evento
  AVG(COALESCE(VL_ITEM_EVENTO_INFORMADO, 0) / COALESCE(QT_ITEM_EVENTO_INFORMADO, 1)) AS 'Média',

  -- Desvio padrão do valor do item por evento
  AVG((COALESCE(VL_ITEM_EVENTO_INFORMADO, 0) / COALESCE(QT_ITEM_EVENTO_INFORMADO, 1))*(COALESCE(VL_ITEM_EVENTO_INFORMADO, 0) / COALESCE(QT_ITEM_EVENTO_INFORMADO, 1))) - AVG((COALESCE(VL_ITEM_EVENTO_INFORMADO, 0) / COALESCE(QT_ITEM_EVENTO_INFORMADO, 1)))*AVG((COALESCE(VL_ITEM_EVENTO_INFORMADO, 0) / COALESCE(QT_ITEM_EVENTO_INFORMADO, 1))) AS 'Variância',

  -- Média do valor do item
  AVG(VL_ITEM_EVENTO_INFORMADO) AS 'Média Valor Item',

  -- Desvio padrão do valor do item
  AVG(VL_ITEM_EVENTO_INFORMADO*VL_ITEM_EVENTO_INFORMADO) - AVG(VL_ITEM_EVENTO_INFORMADO)*AVG(VL_ITEM_EVENTO_INFORMADO) AS 'Variância Valor Item',
  
  -- Soma do valor do item
  SUM(VL_ITEM_EVENTO_INFORMADO) AS 'Soma Valor Item',

  -- Valor mínimo do item
  MIN(VL_ITEM_EVENTO_INFORMADO) AS 'Valor Mínimo Item',

  -- Valor máximo do item
  MAX(VL_ITEM_EVENTO_INFORMADO) AS 'Valor Máximo Item',

  -- Média da quantidade do item por evento
  AVG(QT_ITEM_EVENTO_INFORMADO) AS 'Média Quantidade Item',

  -- Desvio padrão da quantidade do item por evento
  AVG(QT_ITEM_EVENTO_INFORMADO*QT_ITEM_EVENTO_INFORMADO) - AVG(QT_ITEM_EVENTO_INFORMADO)*AVG(QT_ITEM_EVENTO_INFORMADO) AS 'Variância Quantidade Item',
  
  -- Soma da quantidade do item
  SUM(QT_ITEM_EVENTO_INFORMADO) AS 'Soma Quantidade Item',

  -- Valor mínimo da quantidade do item
  MIN(QT_ITEM_EVENTO_INFORMADO) AS 'Valor Mínimo Quantidade Item',

  -- Valor máximo da quantidade do item
  MAX(QT_ITEM_EVENTO_INFORMADO) AS 'Valor Máximo Quantidade Item'

FROM det

GROUP BY CD_PROCEDIMENTO;
