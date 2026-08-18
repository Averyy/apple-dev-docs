# AdGroupTargetingCreate.Gender

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Gender targeting for the audience.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingCreate.Gender
```

#### Discussion

Used with App Store campaigns. Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

```json
"gender": {
  "include": ["M"]
}
```

## Properties

- `include` ([string]): Gender values (`M` or `F`) restricting delivery to that audience. Mutable.
- `exclude` ([string]): Has no effect. `gender` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingcreate/gender-data.dictionary)*