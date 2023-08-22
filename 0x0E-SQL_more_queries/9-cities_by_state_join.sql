-- Lists all cities in the database hbtn_0d_usa
-- Records are sorted in an ascending cities.id order.
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
	INNER JOIN `states` AS s
	ON c.`states_id` = s.`id`
  ORDER BY c.`id`;
