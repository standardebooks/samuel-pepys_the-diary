- Volumes 9 and 10 (appendix and Pepysiana) of the original series have been omitted from the production due to time constraints.

- Each diary entry has a `<time>` element to start. The datetime attribute is ISO8601 compliant (Gregorian), but the actual dates Pepys uses are Julian, which in that time period had diverged by ten days. This discrepancy between Pepys’ recorded dates and the datetime attributes is correct.

- This date is copied into the `entry-x` id attribute for each diary entry. Unfortunately, this causes linting to fail with leading 0 errors, so we remove those for the id.

- "Compleat" was not modernized, as it is likely a pun on "The Compleat Angler"
