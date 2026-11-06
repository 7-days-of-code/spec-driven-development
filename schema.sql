CREATE TABLE IF NOT EXISTS habit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK (length(trim(name)) > 0),
    name_key TEXT NOT NULL UNIQUE,
    weekly_goal INTEGER NULL CHECK (weekly_goal IS NULL OR weekly_goal BETWEEN 1 AND 7)
);

CREATE TABLE IF NOT EXISTS habit_checkin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER NOT NULL,
    completed_on TEXT NOT NULL,
    UNIQUE(habit_id, completed_on),
    FOREIGN KEY (habit_id) REFERENCES habit(id)
);
