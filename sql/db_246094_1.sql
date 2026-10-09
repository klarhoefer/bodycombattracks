-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: klarhoefer.lima-db.de:3306
-- Erstellungszeit: 09. Okt 2026 um 23:06
-- Server-Version: 8.4.10-10
-- PHP-Version: 8.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `db_246094_1`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `durations`
--

CREATE TABLE `durations` (
  `releaseID` int NOT NULL DEFAULT '0',
  `trackID` int NOT NULL DEFAULT '0',
  `seconds` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tracks`
--

CREATE TABLE `tracks` (
  `releaseID` tinyint UNSIGNED NOT NULL,
  `trackID` tinyint UNSIGNED NOT NULL,
  `title` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `artist` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin2;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `durations`
--
ALTER TABLE `durations`
  ADD PRIMARY KEY (`releaseID`,`trackID`);

--
-- Indizes für die Tabelle `tracks`
--
ALTER TABLE `tracks`
  ADD PRIMARY KEY (`releaseID`,`trackID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
