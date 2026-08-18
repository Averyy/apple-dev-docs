# AdGroupTargeting.AppCategory

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

App category targeting based on App Store categories, with include and exclude support.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargeting.AppCategory
```

#### Discussion

`appCategory` is one of only two `AdGroupTargeting` dimensions that support both `include` and `exclude`. Used with App Store campaigns. Uses the [`TargetingData`](targetingdata.md) `include`/`exclude` shape.

```json
"appCategory": {
  "include": ["100"]
}
```

```json
"appCategory": {
  "exclude": ["100"]
}
```

## Properties

- `include` ([string]): App Store category IDs to target. `100` targets the same category as the promoted app. Mutable.
- `exclude` ([string]): App Store category IDs to exclude. `100` excludes the same category as the promoted app. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargeting/appcategory-data.dictionary)*