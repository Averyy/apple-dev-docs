# AdGroupTargetingUpdate.MaxAge

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Maximum age targeting, setting the upper bound of the target age range.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.MaxAge
```

#### Discussion

Applies to App Store campaigns. Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"maxAge": {
  "include": ["64"]
}
```

To target 65+:

```json
"maxAge": {
  "include": null
}
```

## Properties

- `include` ([string]): The upper bound of the target age range (18–64), or `null`/omitted to target users 65 and older. Mutable.
- `exclude` ([string]): Has no effect. `maxAge` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/maxage-data.dictionary)*