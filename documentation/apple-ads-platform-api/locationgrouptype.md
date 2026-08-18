# LocationGroupType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

How a location group’s membership is composed: dynamically via rules, or as a static, explicit list.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string LocationGroupType
```

#### Discussion

A group’s `groupType` is set to one of the following:

| Value | Description |
| --- | --- |
| `DYNAMIC` | Membership is determined by evaluating `rules` against location attributes. |
| `STATIC` | Membership is an explicit list of `locationIds` you supply. |

#### Discussion

The two types differ in how `systemStatus` behaves after creation or update. A `STATIC` group’s membership is already known at the moment you supply `locationIds`, so `systemStatus` is `VALID` immediately. A `DYNAMIC` group’s membership depends on evaluating `rules`, so `systemStatus` starts at `PENDING` and transitions to `VALID` once that evaluation completes. Wait for `systemStatus: VALID` before referencing a `DYNAMIC` group in campaign targeting.

## See Also

- [type EligibilityStatus](eligibilitystatus.md)
  Overall eligibility status for an entity’s policy evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/locationgrouptype)*