# Roadmap

## Next Milestones
- Add configurable reminder cadence (D+3, D+7, D+14)
- Add reconciliation scoring with fuzzy reference matching
- Add audit log for all generated recurring invoices
- Add retry + dead-letter handling for reminder send failures

## Known Limitations
- Statement matching currently relies primarily on exact amount
- Recurring invoice template is static in this version
- Reminder delivery currently uses email channel only
