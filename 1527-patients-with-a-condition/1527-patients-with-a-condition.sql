# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE patient_name LIKE 'DIAB1%' OR patient_name LIKE '% DIAB1%' OR
conditions LIKE 'DIAB1%'OR conditions LIKE '% DIAB1%'