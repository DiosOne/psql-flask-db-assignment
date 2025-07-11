-- order data by year
SELECT * FROM Books
ORDER BY YearPublished ASC;

-- filter data by fantasy
SELECT * FROM Books
WHERE Genre = 'Fantasy';

-- calculate loans by staff member
SELECT Staff.FirstName, COUNT(Loans.LoanID) AS TotalLoans
FROM Loans
JOIN Staff ON Loans.StaffID = Staff.StaffID
GROUP BY Staff.FirstName;
