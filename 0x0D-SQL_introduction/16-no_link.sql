-- Lists all of the second_table's records having a name value.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `score_table`
WHERE `name` != ""
ORDER BY `score` DESC
