SELECT nomeprof, sum(numhoras) 
FROM Professor AS p 
JOIN (SELECT codprof, pt.numdisc, numhoras 
FROM Profturma AS pt 
JOIN Horario AS h 
ON pt.numdisc=h.numdisc) AS b 
ON p.codprof=b.codprof 
GROUP BY nomeprof;