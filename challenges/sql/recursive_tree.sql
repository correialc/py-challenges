with recursive node(id, lvl) as (
    select id, 1 as lvl 
    from tree where pid is null
    union all
    select t.id, n.lvl+1 as lvl
    from node n
    inner join tree t
        on n.id = t.pid
)
select id, 
    case 
        when lvl=1 then 'Root'
        when lead(lvl) over() then 'Leaf'
        else 'Inner'
        end as type
from node;
