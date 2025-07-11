# Library Database

## Scripts Overview

### **Schema**

- **File**: `schema/01_create_tables.sql`
- **Purpose**: Creates all tables for the library system, including appropriate primary keys, foreign keys, and constraints.  
- **Highlights**:
  - Uses `SERIAL` for auto-incrementing IDs.
  - Enforces referential integrity with `FOREIGN KEY` constraints.

---

### **Seed Data**

- **File**: `seed/02_insert_seed_data.sql`
- **Purpose**: Populates the `Authors`, `Books`, `Members`, and `Staff` tables with initial data to simulate a working library system.  
- **Highlights**:
  - Contains realistic data for testing relationships.
  - Uses `DEFAULT` values for fields like `JoinDate`.

---

### **Operations**

- **Files**:  
  - `03_select_queries.sql` – Queries individual and joined tables for single records.  
  - `04_insert_operations.sql` – Inserts new data, including rows with foreign key dependencies.  
  - `05_update_delete.sql` – Updates and deletes existing records while demonstrating cascading behavior.  
  - `06_order_filter_calculate.sql` – Demonstrates ordering, filtering, and aggregate functions.  
- **Purpose**: Demonstrates CRUD operations and advanced querying for assessment requirements.

---

## How To Run

1. Connect to your database:

```bash
psql -U postgres -d library_db
```

2. Run scripts in order

```sql
\i schema/01_create_tables.sql
\i seed/02_insert_seed_data.sql
\i operations/03_select_queries.sql
\i operations/04_insert_operations.sql
\i operations/05_update_delete.sql
\i operations/06_order_filter_calculate.sql
```
