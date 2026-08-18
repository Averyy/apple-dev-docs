# AdGroupTargetingUpdate.AppDownloader

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting based on whether users have downloaded specific apps, identified by Adam ID.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.AppDownloader
```

#### Discussion

`appDownloader` is one of only two `AdGroupTargeting` dimensions that support both `include` and `exclude`. Look up Adam IDs via [`Search for Apps`](searches-for-a-list-of-apps.md). Used with App Store campaigns. Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"appDownloader": {
  "include": ["11111"]
}
```

```json
"appDownloader": {
  "exclude": ["111111"]
}
```

## Properties

- `include` ([string]): Adam IDs of apps whose downloaders to target. Mutable.
- `exclude` ([string]): Adam IDs of apps whose downloaders to exclude, typically to suppress existing users of your app (acquisition targeting). Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/appdownloader-data.dictionary)*