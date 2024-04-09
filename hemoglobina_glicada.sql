/*
select *
from sib
inner join planos
on sib.CD_PLANO = planos.ID_PLANO
where CD_OPERADORA = 417599
limit 5;
*/

select *
from (select * from DET WHERE CD_PROCEDIMENTO in (40302075,40302733)) as DET

inner join CONS
on DET.ID_EVENTO_ATENCAO_SAUDE = CONS.ID_EVENTO_ATENCAO_SAUDE

inner join planos
on CONS.ID_PLANO = planos.ID_PLANO

inner join operadoras
on CONS.ID_PLANO = operadoras.ID_PLANO

WHERE operadoras.CD_OPERADORA = 417599
;
