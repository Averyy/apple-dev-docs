# AdGroupTargetingUpdate.MinAge

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Minimum age targeting, setting the lower bound of the target age range.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.MinAge
```

#### Discussion

Applies to App Store campaigns. Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"minAge": {
  "include": ["18"]
}
```

## Properties

- `include` ([string]): The lower bound of the target age range (18–64). Mutable.
- `exclude` ([string]): Has no effect. `minAge` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/minage-data.dictionary)*