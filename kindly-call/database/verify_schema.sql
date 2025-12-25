-- Kindly Call Schema Verification Script
-- Run this to verify all tables, indexes, and constraints are properly configured

-- ============================================================================
-- 1. VERIFY ALL TABLES EXIST
-- ============================================================================
SELECT 'TABLES' as check_type, COUNT(*) as count, 8 as expected
FROM pg_tables
WHERE schemaname = 'public'
  AND tablename LIKE 'kindlycall_%'
UNION ALL

-- ============================================================================
-- 2. VERIFY ALL INDEXES EXIST
-- ============================================================================
SELECT 'INDEXES', COUNT(*), 24
FROM pg_indexes
WHERE schemaname = 'public'
  AND tablename LIKE 'kindlycall_%'
UNION ALL

-- ============================================================================
-- 3. VERIFY ALL FOREIGN KEYS EXIST
-- ============================================================================
SELECT 'FOREIGN KEYS', COUNT(*), 11
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY'
  AND table_name LIKE 'kindlycall_%'
UNION ALL

-- ============================================================================
-- 4. VERIFY ALL CHECK CONSTRAINTS EXIST
-- ============================================================================
SELECT 'CHECK CONSTRAINTS', COUNT(*), 5
FROM pg_constraint
WHERE conrelid::regclass::text LIKE 'kindlycall_%'
  AND contype = 'c';

-- ============================================================================
-- 5. TABLE DETAILS
-- ============================================================================
SELECT
    t.tablename,
    (SELECT COUNT(*) FROM information_schema.columns WHERE table_name = t.tablename) as columns,
    (SELECT COUNT(*) FROM pg_indexes WHERE tablename = t.tablename) as indexes,
    obj_description((t.schemaname || '.' || t.tablename)::regclass) as description
FROM pg_tables t
WHERE t.schemaname = 'public'
  AND t.tablename LIKE 'kindlycall_%'
ORDER BY t.tablename;

-- ============================================================================
-- 6. INDEX DETAILS
-- ============================================================================
SELECT
    schemaname,
    tablename,
    indexname,
    CASE
        WHEN indexname LIKE '%pkey' THEN 'PRIMARY KEY'
        WHEN indexname LIKE '%key' THEN 'UNIQUE'
        WHEN indexdef LIKE '%WHERE%' THEN 'PARTIAL INDEX'
        ELSE 'INDEX'
    END as index_type
FROM pg_indexes
WHERE schemaname = 'public'
  AND tablename LIKE 'kindlycall_%'
ORDER BY tablename, indexname;

-- ============================================================================
-- 7. FOREIGN KEY RELATIONSHIPS
-- ============================================================================
SELECT
    tc.table_name as "table",
    kcu.column_name as "column",
    ccu.table_name as "references_table",
    ccu.column_name as "references_column"
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_name LIKE 'kindlycall_%'
ORDER BY tc.table_name, kcu.column_name;

-- ============================================================================
-- 8. DATA TYPE SUMMARY
-- ============================================================================
SELECT
    table_name,
    column_name,
    data_type,
    CASE
        WHEN is_nullable = 'NO' THEN 'NOT NULL'
        ELSE 'NULLABLE'
    END as nullable,
    column_default
FROM information_schema.columns
WHERE table_name LIKE 'kindlycall_%'
  AND table_schema = 'public'
ORDER BY table_name, ordinal_position;
