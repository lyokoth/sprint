SELECT name, nat, mark 
FROM sprinter
WHERE mark = (SELECT MAX(mark) FROM sprinter)
ORDER BY name ASC, nat DESC;
```