CREATE TABLE `Datapoint` (
  `id` int PRIMARY KEY,
  `ticker` varchar(255),
  `date` datetime,
  `sentiment` int,
  `text` varchar(255)
);
