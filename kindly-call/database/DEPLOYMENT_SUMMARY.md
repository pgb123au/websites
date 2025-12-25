# Kindly Call Database Schema - Deployment Summary

**Date:** 2025-12-25
**Status:** ✅ DEPLOYED AND VERIFIED
**Database:** retellai_prod (PostgreSQL 17.6)
**Server:** AWS EC2 52.13.124.171 (Docker: n8n-postgres-1)

---

## Deployment Results

### ✅ Tables Created: 8/8

| # | Table Name | Columns | Purpose |
|---|------------|---------|---------|
| 1 | `kindlycall_users` | 8 | Family members managing accounts |
| 2 | `kindlycall_recipients` | 14 | Elderly individuals receiving calls |
| 3 | `kindlycall_recipient_access` | 5 | Multi-user access control |
| 4 | `kindlycall_calls` | 14 | Call records and transcripts |
| 5 | `kindlycall_health_metrics` | 11 | Health tracking from conversations |
| 6 | `kindlycall_alerts` | 9 | Emergency notifications |
| 7 | `kindlycall_subscriptions` | 12 | Stripe billing management |
| 8 | `kindlycall_medications` | 7 | Medication reminders |

### ✅ Indexes Created: 24/24

- **Primary Keys:** 8 (one per table)
- **Unique Indexes:** 2 (email, recipient_access combo)
- **Performance Indexes:** 12 (optimized for common queries)
- **Partial Indexes:** 2 (unacknowledged alerts, active medications)

### ✅ Foreign Keys: 11/11

All referential integrity constraints properly configured with CASCADE or SET NULL behaviors.

### ✅ Check Constraints: 5/5

- `mood_score`: 1-5 range validation
- `sleep_quality`: 1-5 range validation
- `pain_level`: 0-10 range validation
- `appetite`: enum validation ('good', 'poor', 'normal')
- `severity`: enum validation ('low', 'medium', 'high', 'critical')

---

## Verification

### Connection Test
```bash
ssh -i "C:\Users\peter\.ssh\metabase-aws" ubuntu@52.13.124.171 \
  "docker exec n8n-postgres-1 bash -c 'PGPASSWORD=\"280.Army.po\" psql -U n8n -d retellai_prod -c \"SELECT version();\"'"
```

**Result:** PostgreSQL 17.6 (Debian) confirmed

### Schema Verification
```sql
-- All checks passed:
TABLES:            8/8 ✅
INDEXES:          24/24 ✅
FOREIGN KEYS:     11/11 ✅
CHECK CONSTRAINTS: 5/5 ✅
```

---

## Files Created

| File | Purpose | Location |
|------|---------|----------|
| `schema.sql` | Complete schema DDL (idempotent) | `C:\Users\peter\Downloads\CC\websites\kindly-call\database\schema.sql` |
| `SCHEMA_DOCUMENTATION.md` | Detailed documentation | `C:\Users\peter\Downloads\CC\websites\kindly-call\database\SCHEMA_DOCUMENTATION.md` |
| `verify_schema.sql` | Verification queries | `C:\Users\peter\Downloads\CC\websites\kindly-call\database\verify_schema.sql` |
| `DEPLOYMENT_SUMMARY.md` | This file | `C:\Users\peter\Downloads\CC\websites\kindly-call\database\DEPLOYMENT_SUMMARY.md` |

---

## Key Features

### Multi-Tenant Architecture
- Multiple family members can access one recipient's dashboard
- Role-based permissions (owner, admin, viewer)
- Secure data isolation via foreign keys

### JSONB Flexibility
- Health notes, interests, emergency contacts use JSONB
- No migrations needed for profile field changes
- Queryable with PostgreSQL JSON operators

### Performance Optimization
- Composite indexes for common queries (e.g., recent calls by recipient)
- Partial indexes reduce index size (only active/unacknowledged records)
- Foreign key indexes for JOIN performance

### Data Integrity
- Cascade deletes prevent orphaned records
- Check constraints enforce valid ranges
- NOT NULL constraints on critical fields

---

## Next Steps

1. **Row Level Security (RLS)**
   - Add Supabase RLS policies for multi-tenant isolation
   - Ensure users can only access their recipients

2. **Seed Data**
   - Create test users for development
   - Sample recipients, calls, and health metrics
   - Test subscription states

3. **API Integration**
   - Next.js API routes for CRUD operations
   - Authentication middleware (Clerk)
   - Rate limiting

4. **RetellAI Webhooks**
   - Connect to populate `kindlycall_calls` table
   - Extract health metrics from transcripts
   - Generate alerts on concerns

5. **Stripe Webhooks**
   - Handle subscription lifecycle events
   - Update `kindlycall_subscriptions` table
   - Trial expiration notifications

---

## Database Connection Details

**SSH Access:**
```bash
ssh -i "C:\Users\peter\.ssh\metabase-aws" ubuntu@52.13.124.171
```

**Docker Container:**
```bash
docker exec -it n8n-postgres-1 bash
```

**PostgreSQL Connection:**
```bash
PGPASSWORD="280.Army.po" psql -U n8n -d retellai_prod
```

**Environment Variables (for Next.js):**
```env
DATABASE_URL=postgresql://n8n:280.Army.po@52.13.124.171:5432/retellai_prod
```

---

## Maintenance Commands

### Backup Schema
```bash
ssh -i "C:\Users\peter\.ssh\metabase-aws" ubuntu@52.13.124.171 \
  "docker exec n8n-postgres-1 pg_dump -U n8n -d retellai_prod \
  --schema-only --table='kindlycall_*' > /tmp/kindlycall_backup.sql"
```

### Drop All Tables (DANGEROUS)
```sql
DROP TABLE IF EXISTS kindlycall_medications CASCADE;
DROP TABLE IF EXISTS kindlycall_subscriptions CASCADE;
DROP TABLE IF EXISTS kindlycall_alerts CASCADE;
DROP TABLE IF EXISTS kindlycall_health_metrics CASCADE;
DROP TABLE IF EXISTS kindlycall_calls CASCADE;
DROP TABLE IF EXISTS kindlycall_recipient_access CASCADE;
DROP TABLE IF EXISTS kindlycall_recipients CASCADE;
DROP TABLE IF EXISTS kindlycall_users CASCADE;
```

### Re-run Schema
```bash
cd /c/Users/peter/Downloads/CC/websites/kindly-call/database
scp -i "C:\Users\peter\.ssh\metabase-aws" schema.sql ubuntu@52.13.124.171:/tmp/schema.sql
ssh -i "C:\Users\peter\.ssh\metabase-aws" ubuntu@52.13.124.171 \
  "docker cp /tmp/schema.sql n8n-postgres-1:/tmp/ && \
   docker exec n8n-postgres-1 bash -c 'PGPASSWORD=\"280.Army.po\" psql -U n8n -d retellai_prod -f /tmp/schema.sql'"
```

---

## Git Commit

**Repository:** github.com/pgb123au/websites
**Commit:** 0c415cc
**Branch:** master
**Status:** Pushed to remote

---

**Deployment completed successfully on 2025-12-25**
**All schema components verified and documented**
