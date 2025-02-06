use dotanucleo;

CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    discord_id BIGINT UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    position ENUM('1', '2', '3', '4', '5') NOT NULL,
    mmr INT DEFAULT 500,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    abandons INT DEFAULT 0
);