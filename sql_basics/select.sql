SELECT
    first_name,
    last_name,
    COUNT(DISTINCT orders.id) AS total_orders,
    SUM(quantity) AS total_items_bought,
    SUM(quantity*(price-discount)) AS total_money_spent
FROM
    person LEFT JOIN orders
    ON person.id = orders.person_id
    left join order_item
    ON orders.id = order_item.order_id
    LEFT JOIN item
    ON item.id = order_item.item_id
GROUP BY orders.person_id
ORDER BY person.id;
