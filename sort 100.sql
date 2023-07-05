INSERT INTO sprinter SELECT a.* FROM 
OPENROWSET  (BULK N'C:\Users\\icefl\sprint\data\100_M.csv', FORMATFILE = N'C:\Users\\icefl\sprint\data\100_M.fmt') AS a;