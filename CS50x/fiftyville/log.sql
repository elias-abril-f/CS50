-- Keep a log of any SQL queries you execute as you solve the mystery.
-- To read the report
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND street = "Humphrey Street";

-- To find the interviews from the crime at the bakery
SELECT * FROM interviews
 WHERE day = 28
   AND month = 7
   AND year = 2021
   AND transcript
  LIKE "%bakery%";

-- People who were at the atm, bakery and made a phonecall less than <60s and left the bakery within 10 min of the theft
SELECT name
  FROM atm_transactions
       JOIN bank_accounts
       ON bank_accounts.account_number = atm_transactions.account_number
       JOIN people
       ON people.id = bank_accounts.person_id
 WHERE person_id IN
       (SELECT people.id
          FROM bakery_security_logs
               JOIN people
               ON bakery_security_logs.license_plate = people.license_plate
               JOIN phone_calls
               ON phone_calls.caller = people.phone_number
         WHERE bakery_security_logs.day = 28
           AND bakery_security_logs.month = 7
           AND bakery_security_logs.year = 2021
           AND bakery_security_logs.hour = 10
           AND minute
       BETWEEN 15 AND 25
           AND phone_calls.duration <= 60
           AND phone_calls.day = 28
           AND phone_calls.month = 7
           AND phone_calls.year = 2021
       )

-- Find out the destination of the escape by finding the first flight that leaves Fiftyville (by ordering by hour and limit of 1) and then returning the city of destination
SELECT city FROM flights
       JOIN airports
       ON  airports.id = destination_airport_id
 WHERE flights.year = 2021
   AND flights.month = 7
   AND flights.day = 29
   AND origin_airport_id = (SELECT id
                              FROM airports
                             WHERE city = "Fiftyville"
                           )
  ORDER BY hour
  LIMIT 1;

 -- Get the name of the culprit by checking who was at the atm, left the bakery and placed a phonecall less than 60s long at the right time and is in
 -- the list of passengers of the first flight leaving fiftyville airport on the 29th.
SELECT name FROM passengers
       JOIN people
       ON people.passport_number = passengers.passport_number
 WHERE flight_id IN
       (SELECT id FROM flights
         WHERE year = 2021
           AND month = 7
           AND day = 29
           AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")
           AND  destination_airport_id = (SELECT destination_airport_id FROM flights
                                                 JOIN airports
                                                 ON  airports.id = destination_airport_id
                                           WHERE flights.year = 2021
                                             AND flights.month = 7
                                             AND flights.day = 29
                                             AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")
                                           ORDER BY hour
                                           LIMIT 1)
           AND people.passport_number IN
               (SELECT passport_number
                  FROM atm_transactions
                       JOIN bank_accounts
                       ON bank_accounts.account_number = atm_transactions.account_number
                       JOIN people
                       ON people.id = bank_accounts.person_id
                 WHERE person_id IN
                       (SELECT people.id
                          FROM bakery_security_logs
                               JOIN people
                               ON bakery_security_logs.license_plate = people.license_plate
                               JOIN phone_calls
                               ON phone_calls.caller = people.phone_number
                         WHERE bakery_security_logs.day = 28
                           AND bakery_security_logs.month = 7
                           AND bakery_security_logs.year = 2021
                           AND bakery_security_logs.hour = 10
                           AND minute
                               BETWEEN 15 AND 25
                           AND phone_calls.duration <= 60
                           AND phone_calls.day = 28
                           AND phone_calls.month = 7
                           AND phone_calls.year = 2021
                       )
               )
       );


-- Get the name of the accomplice by getting the name of the receiver of a phonecall placed by the person who was in the atm, left the bakery at the right time,
-- placed a phonecall less than 60s while leaving and is in the list of passengers of the first flight leaving on the 29th

SELECT name FROM people
       JOIN phone_calls
       ON phone_calls.receiver = people.phone_number
 WHERE day = 28
   AND month = 7
   AND year = 2021
   AND duration <= 60
   AND caller = (SELECT phone_number FROM passengers
                        JOIN people
                        ON people.passport_number = passengers.passport_number
                  WHERE flight_id IN
                        (SELECT id FROM flights
                          WHERE year = 2021
                            AND month = 7
                            AND day = 29
                            AND origin_airport_id = (SELECT id FROM airports
                                                      WHERE city = "Fiftyville")
                            AND destination_airport_id = (SELECT destination_airport_id FROM flights
                                                                 JOIN airports
                                                                 ON  airports.id = destination_airport_id
                                                           WHERE flights.year = 2021
                                                             AND flights.month = 7
                                                             AND flights.day = 29
                                                             AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")
                                                           ORDER BY hour
                                                           LIMIT 1)
                            AND people.passport_number IN
                                (SELECT passport_number
                                   FROM atm_transactions
                                        JOIN bank_accounts
                                        ON bank_accounts.account_number = atm_transactions.account_number
                                        JOIN people
                                        ON people.id = bank_accounts.person_id
                                  WHERE person_id IN
                                        (SELECT people.id
                                           FROM bakery_security_logs
                                                JOIN people
                                                ON bakery_security_logs.license_plate = people.license_plate
                                                JOIN phone_calls
                                                ON phone_calls.caller = people.phone_number
                                          WHERE bakery_security_logs.day = 28
                                            AND bakery_security_logs.month = 7
                                            AND bakery_security_logs.year = 2021
                                            AND bakery_security_logs.hour = 10
                                            AND minute
                                        BETWEEN 15 AND 25
                                            AND phone_calls.duration <= 60
                                            AND phone_calls.day = 28
                                            AND phone_calls.month = 7
                                            AND phone_calls.year = 2021
                                        )
                                )
                        )
                );