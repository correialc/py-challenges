USE labs;

SELECT DISTINCT extended_node.id AS node_id, 
    CASE 
        WHEN extended_node.pid IS NULL THEN 'Root'
        WHEN extended_node.child_id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END as node_type
FROM 
(   SELECT current.id, current.pid, child.id AS child_id
    FROM node current
    LEFT JOIN node child
    ON current.id = child.pid
    ) AS extended_node
ORDER BY node_id;
