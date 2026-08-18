# AdGroupTargeting.Daypart

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Hour-of-day targeting, restricting delivery to specific one-hour slots in a 7-day week grid.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargeting.Daypart
```

#### Discussion

Used with App Store and Apple Maps campaigns. Uses the [`TargetingData`](targetingdata.md) `include`/`exclude` shape.

| Day | Slot Range | Example |
| --- | --- | --- |
| Sunday | 0–23 | 0 = Sunday 12:00 AM, 1 = Sunday 1:00 AM |
| Monday | 24–47 | 24 = Monday 12:00 AM |
| Tuesday | 48–71 | 48 = Tuesday 12:00 AM |
| Wednesday | 72–95 | 72 = Wednesday 12:00 AM |
| Thursday | 96–119 | 96 = Thursday 12:00 AM |
| Friday | 120–143 | 120 = Friday 12:00 AM |
| Saturday | 144–167 | 144 = Saturday 12:00 AM |

To convert any slot value: divide by 24 to get the day index (0 = Sunday), and take the remainder to get the hour. Slot values are evaluated in the ad account’s configured time zone.

## Properties

- `include` ([string]): Slot integers (0–167) restricting delivery to those one-hour windows in a 7-day week grid starting on Sunday. Mutable.
- `exclude` ([string]): Has no effect. `daypart` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargeting/daypart-data.dictionary)*