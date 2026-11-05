# Phantom Lake Club — unofficial preview

A mock-up of [phantomlakeclub.org](https://phantomlakeclub.org) (Home, Hours, Water Polo, Swim Team) in the look of the club's
Squarespace site, with the pool schedule on live [Pool Relay](https://www.poolrelay.com) calendars. Not operated by, endorsed by or
affiliated with Phantom Lake Club. No logo or photos are used.

No schedule is typed into the pages: `finder.js` fills every `data-live` element from the Pool Relay views; `check.py` fails the build
on any time, weekday or date outside a script or a labeled quote. Build with `python3 build.py && python3 check.py`.

- Pool Relay views: `92it6ldSSl4pteiXEFcD7Y` (pool, lane by lane) and `NW5jUspT0J4R0HAbaQkeaC` (pool, week; feeds the live text).
- Data (read 2026-11-05): the club's public Google Calendars on /hours (PLC Pool Calendar; Lessons and programs) from Sept 1 to closing
  day, and Northwest Water Polo Club's fall practices (the off-season renter). Six lanes, 25 yards (club's About page). Lanes are estimates.
