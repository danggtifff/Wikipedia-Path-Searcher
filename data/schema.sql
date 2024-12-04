CREATE TABLE IF NOT EXISTS wikilinks (
    name TEXT PRIMARY_KEY,
    outlinks TEXT
);

CREATE INDEX IF NOT EXISTS idx_name ON wikilinks(name);

CREATE TABLE IF NOT EXISTS id_title (
    name TEXT PRIMARY_KEY,
    id TEXT
);

CREATE INDEX IF NOT EXISTS idx_this_name ON id_title(name);