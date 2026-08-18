# AdGroupTargetingUpdate.Gender

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Gender targeting for the audience.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.Gender
```

#### Discussion

Applies to App Store campaigns. Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"gender": {
  "include": ["M"]
}
```

## Properties

- `include` ([string]): Gender values (`M` or `F`) restricting delivery to that audience. Mutable.
- `exclude` ([string]): Has no effect. `gender` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/gender-data.dictionary)*