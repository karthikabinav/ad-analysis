# Advertising Analysis: Dorohedoro Premiere

## Summary

**Question**: Find the average amount spent on advertisements that started only the day after the date the anime Dorohedoro premiered.

## Key Dates
- **Dorohedoro Premiere Date**: January 12, 2020
- **Target Date (Day After Premiere)**: January 13, 2020

## Data Source
- **Database**: Notion Advertising Database
- **Database ID**: 21b97551-844e-8068-b387-fe7a56b04348
- **Query**: Filtered for StartDate between 2020-01-12 and 2020-01-14

## Findings

### Advertisements in the Query Range:
1. **CAMP3818**: Started 2020-01-12, Spent $1,017 (Search Engine)
2. **CAMP3335**: Started 2020-01-14, Spent $10,846 (Banner)
3. **CAMP4976**: Started 2020-01-14, Spent $10,035 (Social Media)

### Critical Finding:
**NO advertisements started on 2020-01-13** (the exact day after Dorohedoro premiered).

## Conclusion

Since there are **zero advertisements** that started on January 13, 2020:
- **Average amount spent**: **$0.00** (or undefined)

The database contains:
- 1 advertisement from the actual premiere date (2020-01-12)
- 2 advertisements from two days after the premiere (2020-01-14)
- No advertisements from the day after the premiere (2020-01-13)

## Analysis Script

See `query_ads.py` for the code used to analyze this data.
