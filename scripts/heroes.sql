use dotanucleo;

CREATE TABLE heroes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO heroes (id, name) VALUES
(1, 'Anti-Mage'), (2, 'Axe'), (3, 'Bane'), (4, 'Bloodseeker'), (5, 'Crystal Maiden'),
(6, 'Drow Ranger'), (7, 'Earthshaker'), (8, 'Juggernaut'), (9, 'Mirana'), (10, 'Morphling'),
(11, 'Shadow Fiend'), (12, 'Phantom Lancer'), (13, 'Puck'), (14, 'Pudge'), (15, 'Razor'),
(16, 'Sand King'), (17, 'Storm Spirit'), (18, 'Sven'), (19, 'Tiny'), (20, 'Vengeful Spirit'),
(21, 'Windranger'), (22, 'Zeus'), (23, 'Kunkka'), (25, 'Lina'), (26, 'Lion'),
(27, 'Shadow Shaman'), (28, 'Slardar'), (29, 'Tidehunter'), (30, 'Witch Doctor'),
(31, 'Lich'), (32, 'Riki'), (33, 'Enigma'), (34, 'Tinker'), (35, 'Sniper'),
(36, 'Necrophos'), (37, 'Warlock'), (38, 'Beastmaster'), (39, 'Queen of Pain'),
(40, 'Venomancer'), (41, 'Faceless Void'), (42, 'Wraith King'), (43, 'Death Prophet'),
(44, 'Phantom Assassin'), (45, 'Pugna'), (46, 'Templar Assassin'), (47, 'Viper'),
(48, 'Luna'), (49, 'Dragon Knight'), (50, 'Dazzle'), (51, 'Clockwerk'), (52, 'Leshrac'),
(53, 'Nature''s Prophet'), (54, 'Lifestealer'), (55, 'Dark Seer'), (56, 'Clinkz'),
(57, 'Omniknight'), (58, 'Enchantress'), (59, 'Huskar'), (60, 'Night Stalker'),
(61, 'Broodmother'), (62, 'Bounty Hunter'), (63, 'Weaver'), (64, 'Jakiro'),
(65, 'Batrider'), (66, 'Chen'), (67, 'Spectre'), (68, 'Ancient Apparition'),
(69, 'Doom'), (70, 'Ursa'), (71, 'Spirit Breaker'), (72, 'Gyrocopter'), (73, 'Alchemist'),
(74, 'Invoker'), (75, 'Silencer'), (76, 'Outworld Destroyer'), (77, 'Lycan'),
(78, 'Brewmaster'), (79, 'Shadow Demon'), (80, 'Lone Druid'), (81, 'Chaos Knight'),
(82, 'Meepo'), (83, 'Treant Protector'), (84, 'Ogre Magi'), (85, 'Undying'),
(86, 'Rubick'), (87, 'Disruptor'), (88, 'Nyx Assassin'), (89, 'Naga Siren'),
(90, 'Keeper of the Light'), (91, 'Io'), (92, 'Visage'), (93, 'Slark'),
(94, 'Medusa'), (95, 'Troll Warlord'), (96, 'Centaur Warrunner'), (97, 'Magnus'),
(98, 'Timbersaw'), (99, 'Bristleback'), (100, 'Tusk'), (101, 'Skywrath Mage'),
(102, 'Abaddon'), (103, 'Elder Titan'), (104, 'Legion Commander'), (105, 'Techies'),
(106, 'Ember Spirit'), (107, 'Earth Spirit'), (108, 'Underlord'), (109, 'Terrorblade'),
(110, 'Phoenix'), (111, 'Oracle'), (112, 'Winter Wyvern'), (113, 'Arc Warden'),
(114, 'Monkey King'), (119, 'Dark Willow'), (120, 'Pangolier'), (121, 'Grimstroke'),
(123, 'Hoodwink'), (126, 'Void Spirit'), (128, 'Snapfire'), (129, 'Mars'),
(131, 'Ringmaster'), (135, 'Dawnbreaker'), (136, 'Marci'), (137, 'Primal Beast'),
(138, 'Muerta'), (145, 'Kez');
