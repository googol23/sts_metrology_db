# STS metrology database

`sts_metrology_db` is the workspace utility for storing STS metrology measurement
files and structured measurement records. It is intentionally independent of the
other STS workspace packages.

## Current contents

- SQLAlchemy models for operators, markers, units, uncertainty models, raw files,
  and measurements.
- A local SQLite schema prototype under `data/`.
- An unfinished measurement-file ingestion prototype.
- A FastAPI file upload/list/download/delete prototype retained for future work.

The analysis and fitting of ladder fiducial measurements belongs to the separate
`sts_ladder_metrology` project. PostgreSQL detector-construction access belongs to
`sts_db_api`.

## Local paths

By default, the SQLite database and uploaded files are kept in this project’s
`data/` directory. Override the database with `METROLOGY_DB_PATH`, uploaded-file
storage with `STORAGE_PATH`, and temporary uploads with `TEMP_PATH`.

This project currently has no dependencies on sibling workspace packages. Its
third-party runtime dependencies and packaging metadata still need to be formalized
before release.
