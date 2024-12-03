CREATE TABLE IF NOT EXISTS wikilinks (
    name TEXT PRIMARY_KEY,
    outlinks TEXT
);

CREATE INDEX IF NOT EXISTS idx_name ON wikilinks(name);