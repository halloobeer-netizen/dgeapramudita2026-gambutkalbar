# PROJECT HANDOVER — PEATLAND INTELLIGENCE PLATFORM

## Repository
- Repository: `halloobeer-netizen/peatland-intelligence-platform`
- Branch: `main`
- Type: Static web application for peat ecosystem field survey, environmental data, mapping, and spatial information management
- Primary context: Kapuas Hulu, West Kalimantan

## Source of Truth
This handover is based on the current GitHub repository. The latest repository, Firebase Realtime Database data, and Firebase Database Rules are the source of truth.

This is an existing working project. Do not rebuild it from scratch.

## Verified Current Stack
- HTML5
- CSS3
- Vanilla JavaScript
- Leaflet 1.9.4
- OpenStreetMap
- Firebase Authentication
- Google Sign-In
- Firebase Realtime Database
- Firebase compat SDK 10.12.2
- SheetJS / XLSX 0.18.5
- Static web application architecture

Do not migrate to React, Next.js, Vue, Angular, or another framework unless explicitly requested.

## Current Repository Structure
Important root items:

```text
.github/
README.md
database.rules.json
firebase.json
index.html
scripts/
```

Inside `scripts/`:

```text
refresh_ui.py
```

The current application is centered primarily in `index.html`, which contains substantial HTML, CSS, UI logic, Firebase logic, mapping logic, import logic, and survey functionality.

## Product Direction
README defines Peatland Intelligence Platform as an environmental survey, mapping, and spatial data management system.

Core capabilities include:
- peat ecosystem survey dashboard
- survey progress monitoring
- KHG / peat hydrological unit management
- survey-point records
- coordinates and elevation
- interactive map visualization
- hydrology and environmental records
- pH, EC, and TDS data
- Excel import
- Google authentication
- responsive desktop/mobile interface

Keep development aligned with this environmental/spatial product direction.

## Data Root and Hierarchy
Firebase data is organized under:

```text
survei/
```

Important structures include:

```text
survei/
├── roles/
└── khgs/
```

Conceptually:

```text
KHG
  ↓
Survey Points
  ↓
Environmental / Spatial Data
```

Survey points are stored under KHG nodes similar to:

```text
survei/khgs/{khgId}/points/{pointIndex}
```

Do not change Firebase paths or point indexing without first auditing existing data and all read/write code.

## Survey Data
Existing application logic requires at minimum:
- Surveyor
- Nama Titik
- Tanggal

The platform also handles or is designed around:
- latitude / longitude
- elevation
- hydrology
- pH
- EC
- TDS
- peat/environment observations
- photos
- supporting documents

Never fabricate environmental measurements.

Do not silently replace missing/null scientific values with zero.

## Coordinate Standard
Spatial data should use:

```text
WGS84 / EPSG:4326
```

Convention:

```text
Latitude = Y
Longitude = X
```

Validate:
- latitude: -90 to 90
- longitude: -180 to 180

Do not swap latitude and longitude or invent coordinates.

## Mapping
Mapping is implemented with:
- Leaflet
- OpenStreetMap

Preserve existing survey-point compatibility and mobile rendering.

Do not introduce paid map providers unnecessarily.

## Dashboard and Survey Progress
The dashboard is intended to show field-survey operational progress, including:
- surveyed points
- remaining targets
- recent records
- overall completion percentage
- KHG summaries

Any progress-calculation change must be tested against real KHG/point data.

## Excel Import
The application uses SheetJS/XLSX.

Expected flow:

```text
Excel File
→ Parse Workbook
→ Parse Rows
→ Validate / Preview
→ Import
→ Firebase
```

Rules:
- do not blindly overwrite existing survey data
- validate required fields
- validate coordinates
- preserve currently supported field-column mapping
- keep import restricted according to role permissions

## Photos and Documents
The UI includes photo and document support associated with survey records.

When editing:
- preserve point-to-photo relationship
- do not lose existing attachments during unrelated edits
- Viewer must remain unable to modify attachments
- Editor/Admin permissions must remain aligned with Firebase rules

Before migrating attachments to Firebase Storage or another object-storage system, audit the current storage format and migration impact.

# ROLE-BASED ACCESS CONTROL — CRITICAL

## Roles
The project currently defines:

```text
admin
editor
viewer
```

Unknown/no-role authenticated users default to:

```text
viewer
```

This behavior must be preserved unless explicitly changed.

## Client Permission Model
### Admin
- manage KHG
- import data
- add point
- edit point
- delete point

### Editor
- cannot manage KHG
- cannot import Excel
- can add point
- can edit point
- cannot delete point

### Viewer
- view only
- cannot add/edit/delete data

Do not weaken these permissions accidentally.

## Firebase Server-Side Rules
Security does not rely only on hidden UI buttons.

`database.rules.json` currently starts from a restrictive global model:

```text
.read = false
.write = false
```

Access is then granted according to authentication and role.

This is critical and must remain secure.

Never set global database read/write to true.

## Role Management
Roles live at:

```text
survei/roles/{uid}
```

Current behavior:
- a user can read their own role
- Admin can read roles
- only Admin can write role assignments
- valid values are only `admin`, `editor`, `viewer`

Do not allow users to promote themselves to Admin.

## KHG Permissions
Authenticated Admin/Editor/Viewer can read KHG data according to current rules.

KHG-level management/write is Admin-only.

Do not give Editor KHG management rights without explicit approval.

## Point Write Permissions
The current design distinguishes Admin full privileged write behavior from Editor point-level writes.

This is important: a careless refactor that makes Editor persist the entire KHG node may violate Firebase rules or create a security issue.

Prefer minimum-node writes for Editor operations.

## Google Authentication
Authentication uses Google Sign-In through Firebase Authentication.

Before changing login:
1. inspect Firebase configuration
2. inspect authorized domains
3. inspect Google provider configuration
4. inspect auth-state handling
5. inspect `survei/roles/{uid}`

Do not replace it with custom password authentication unless explicitly requested.

## Firebase Configuration
`firebase.json` wires Firebase database rules to:

```text
database.rules.json
```

Do not remove this configuration.

When changing rules, test Admin, Editor, and Viewer separately before deployment.

## Firebase Data Safety
Never perform without explicit approval:
- delete `/survei`
- delete all KHGs
- delete all survey points
- overwrite all production data
- disable database rules
- open global `.read` or `.write`

Field data may be difficult or impossible to recreate.

## `index.html` Architecture
`index.html` is currently monolithic and contains a large portion of the application.

This is technical debt, but not justification for a full rewrite.

If modularization is requested, do it gradually:
1. preserve behavior
2. separate CSS/JS incrementally
3. preserve Firebase paths
4. preserve roles and permissions
5. verify mobile layout
6. verify map
7. verify import
8. verify CRUD

Do not do a big-bang framework migration.

## `scripts/refresh_ui.py`
The repository contains `scripts/refresh_ui.py`.

This script was used as a maintenance/patch script for role-based access-control changes inside `index.html`.

Rules:
- inspect current `index.html` before running it
- do not run it blindly
- its string-replacement anchors may fail after code changes
- it is not normal production runtime code

## UI Direction
Current visual direction is:
- green / environmental identity
- clean
- professional
- responsive
- mobile friendly
- field-operator friendly

The UI includes cards, progress indicators, KHG cards, forms, tabs, modals, toast messages, maps, and mobile navigation/action behavior.

Do not redesign the whole application for unrelated fixes.

## Mobile Requirements
Test at minimum around:
- 360px
- 390px
- 430px
- tablet
- desktop

Verify:
- forms remain usable
- buttons remain reachable
- maps render correctly
- tab scrolling works
- fixed/bottom controls do not cover content
- page remains scrollable

## Language
Current application UI uses Indonesian.

Keep Indonesian UI terminology unless explicitly asked to localize.

## External Browser Dependencies
Known versions currently referenced include:
- SheetJS/XLSX 0.18.5
- Leaflet 1.9.4
- Firebase compat 10.12.2

Do not casually perform major-version upgrades.

Firebase compat-to-modular migration should be treated as a deliberate refactor, not a routine cleanup.

## Recent Development Context
Recent GitHub history includes work around:
- login/dashboard UI modernization
- Admin/Editor/Viewer access control
- Firebase role-based rules
- Firebase rules deployment configuration
- security finalization
- professional README

Security and access control should therefore be considered recently stabilized and must not be casually overwritten.

# Mandatory Takeover Audit
Before coding, the next AI/developer must report:

1. Current repository structure
2. Frontend architecture
3. External library versions
4. Firebase Auth implementation
5. Firebase Realtime Database configuration
6. Firebase data structure
7. Admin/Editor/Viewer implementation
8. Database security rules
9. KHG CRUD implementation
10. Survey-point CRUD implementation
11. Excel import implementation
12. Leaflet/map implementation
13. Photo/document implementation
14. Dashboard/progress calculations
15. Responsive/mobile status
16. Existing bugs
17. Security risks
18. Data-integrity risks
19. Technical debt
20. Recommended smallest safe next task

Do not immediately start a major refactor.

# Development Priority
1. Data safety
2. Authentication and permissions
3. Survey-point CRUD
4. KHG management
5. Excel import
6. Mapping
7. Dashboard/progress
8. Responsive/mobile stability
9. Refactoring only after behavior is stable

# Role Test Matrix
## Admin must be able to
- view
- manage KHG
- import Excel
- add point
- edit point
- delete point

## Editor must be able to
- view
- add point
- edit point

Editor must NOT be able to
- manage KHG
- import Excel
- delete point
- change roles

## Viewer must only be able to
- view

Viewer must not be able to write even through browser developer tools. Firebase Rules must enforce this.

# Security Principle
Correct access control is:

```text
UI permissions
+
Firebase Database Rules
=
Access Control
```

Never rely on hidden buttons alone.

# Data Change Principle
For any field-data modification:

```text
READ EXISTING DATA
→ UNDERSTAND SCHEMA
→ CHANGE MINIMUM REQUIRED NODE
→ VERIFY WRITE
→ VERIFY OTHER DATA REMAINS
```

Avoid full-node overwrites when narrow writes are sufficient.

# Future Options — Only When Requested
Potential future features include:
- offline/PWA field mode
- GPS capture
- stronger Excel validation
- CSV export
- GeoJSON export
- QGIS-friendly export
- audit log
- QC workflow
- survey approval status
- Firebase Storage
- better error logging
- configurable field targets
- map filtering
- KHG polygons
- administrative boundaries
- environmental analytics

Do not implement everything at once.

# GIS Compatibility
When adding GIS/export features, prefer compatibility with:
- QGIS
- CSV
- Excel
- GeoJSON
- GeoPackage workflows

Default CRS remains EPSG:4326 unless there is a clear reason otherwise.

# Environmental Data Principles
This project may contain actual field observations.

Therefore:
- never invent missing measurements
- preserve raw values
- keep units clear
- preserve source coordinates
- avoid silent transformations
- show explicit validation errors

# Error Handling
### Firebase unavailable
- show error
- keep form state where possible
- never pretend save succeeded

### Excel parse failure
- reject invalid import safely
- explain invalid rows
- do not overwrite unrelated KHG data

### Permission denied
- show clear permission message
- do not bypass rules

# Git Workflow
Before editing:

```bash
git status
git log --oneline
```

Use clear commits such as:
- `fix: preserve editor point writes under firebase rules`
- `fix: validate coordinates before survey save`
- `feat: add survey point map filter`
- `security: tighten firebase survey point validation`

# Deployment Checklist
Before releasing changes, verify:
- application loads
- Google login works
- role loads correctly
- Admin access works
- Editor access works
- Viewer remains read-only
- KHG list loads
- survey points load
- authorized add/edit works
- delete restrictions work
- Excel import works for Admin
- map loads
- mobile page scrolls
- no console-breaking errors
- Firebase rules remain secure

# Locked / Preserved Decisions
Do not change without explicit approval:
- Project remains Peatland Intelligence Platform
- Domain remains peat ecosystem/environmental survey management
- Current stack is static HTML/CSS/JavaScript
- Leaflet + OpenStreetMap remains current mapping solution
- Firebase Authentication remains current auth
- Google Sign-In remains current login
- Firebase Realtime Database remains current database
- SheetJS/XLSX remains current Excel import mechanism
- Data root remains `survei`
- Existing KHG structure must be preserved unless deliberately migrated
- Roles remain `admin`, `editor`, `viewer`
- Unknown role defaults to Viewer
- Viewer is read-only
- Editor cannot delete points
- Editor cannot manage KHG
- Editor cannot import Excel
- Admin controls KHG and roles
- Firebase rules are part of the security model
- Global database read/write must stay closed
- Environmental data must never be fabricated
- Existing working functionality should not be rebuilt unnecessarily

# Correct Continuation Workflow

```text
READ README
→ AUDIT REPOSITORY
→ READ INDEX.HTML
→ READ FIREBASE RULES
→ UNDERSTAND DATA STRUCTURE
→ VERIFY AUTH + ROLES
→ VERIFY CURRENT FEATURES
→ IDENTIFY SMALLEST ISSUE
→ FIX
→ TEST ADMIN / EDITOR / VIEWER
→ TEST SURVEY DATA
→ TEST MAP / IMPORT
→ COMMIT
→ DEPLOY
```

Do not:

```text
REWRITE EVERYTHING
→ BREAK FIREBASE PATHS
→ LOSE SURVEY DATA
```

# Final Instruction
You are taking over an existing environmental survey platform.

Do not assume a framework migration is necessary.

Do not weaken authentication or database rules.

Do not change Firebase paths until existing production data is fully understood.

Do not fabricate peatland survey values.

Preserve Admin / Editor / Viewer permissions.

The first objective is to understand and stabilize the existing system. Improve architecture, UX, GIS, offline support, or analytics only after the existing implementation is verified.

**Repository + Firebase production data + Firebase rules are the source of truth.**
