# AdGroup.SystemStatusLimitingReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Reasons that limit delivery for an ad group without fully stopping it.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdGroup.SystemStatusLimitingReasons
```

#### Discussion

These reasons can stem from the ad group’s own location targeting or cascade up from limited ads within it, as with `ADS_LIMITED`.

##### Example

```json
{
  "systemStatusLimitingReasons": [
    "ADS_LIMITED"
  ]
}
```

See [`AdGroupSystemLimitedStatusReason`](adgroupsystemlimitedstatusreason.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/systemstatuslimitingreasons-data.typealias)*