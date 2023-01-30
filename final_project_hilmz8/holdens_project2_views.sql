-- Write a query to create a view named “EmployeesPerRegion” that shows the region_name and the number of employees from that region in a column called “Number of Employees”.
CREATE VIEW EmployeesPerRegion AS
SELECT r.region_name, COUNT(DISTINCT e.employee_id) AS "Number of Employees"
FROM regions r, employees e, countries c, locations l, departments d
WHERE r.region_id = c.region_id AND c.country_id = l.country_id AND l.location_id = d.location_id AND d.department_id = e.department_id
GROUP BY r.region_name;

-- Write a query to create a view named “managers” to display all the managers. Include the manager’s name (first, last), phone number, email, job title, and department name.
CREATE VIEW managers AS
SELECT e.first_name, e.last_name, e.phone_number, e.email, j.job_title, d.department_name
FROM employees e, departments d, jobs j
WHERE e.employee_id IN (SELECT DISTINCT manager_id FROM employees) AND e.job_id = j.job_id AND e.department_id = d.department_id;

-- Write a query to create a view named “DependentsByDepartment” to get a count of how many dependents there are in each department.
CREATE VIEW DependentsByDepartment AS
SELECT COUNT(DISTINCT dd.dependent_id) AS "Number of Dependents", d.department_name
FROM dependents dd, departments d, employees e
WHERE dd.employee_id = e.employee_id AND e.department_id = d.department_id
GROUP BY d.department_name;

-- Write a query to create a view named “HiresByYear” that calculates the number of employees hired each year. Remember the SQL $year function.
CREATE VIEW HiresByYear AS
SELECT COUNT(DISTINCT employee_id) AS "Hires", YEAR(hire_date) AS "Year"
FROM employees
GROUP BY YEAR(hire_date);

-- Write a query to create a view named “SalaryByDepartment” to calculate total salaries for each department.
CREATE VIEW SalaryByDepartment AS 
SELECT SUM(e.salary), d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id
GROUP BY d.department_name;

-- Write a query to create a view named “SalaryByJobTitle” to calculate total salaries for each job title.
CREATE VIEW SalaryByJobTitle AS
SELECT SUM(e.salary) AS "TotalSalary", j.job_title
FROM employees e, jobs j
WHERE e.job_id = j.job_id
GROUP BY j.job_title;

-- Write a query to create a view named “EmployeeDependents” that calculates the number of dependents each employees has. This query should show employees even if they have 0 dependents. 
-- Display the employee name (first, last), email, phone number, and number of dependents. Hint: left or right join.
CREATE VIEW EmployeeDependents AS
SELECT e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.dependent_id) AS "Dependents"
FROM employees e
LEFT JOIN dependents d ON e.employee_id = d.employee_id
GROUP BY e.employee_id;

-- Write a query to create a view named “CountryLocation” that calculates the number of locations in each country. 
-- This query should show countries even if they have 0 locations. Display the country name and number of locations.
CREATE VIEW CountryLocation AS
SELECT c.country_name, COUNT(l.location_id) AS "NumOfLocations"
FROM countries c
LEFT JOIN locations l ON c.country_id = l.country_id
GROUP BY c.country_id;