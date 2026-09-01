# Campaign.SystemStatusLimitingReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code indicating that a campaign is running but delivering at reduced capacity.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Campaign.SystemStatusLimitingReasons
```

#### Discussion

Unlike [`Campaign.SystemStatusReasons`](campaign/systemstatusreasons-data.typealias.md), these codes describe conditions, such as pending app documentation or brand policy issues, that throttle delivery rather than stop it outright.

##### Example

```json
{
  "systemStatusLimitingReasons": ["AD_GROUPS_LIMITED"]
}
```

See [`CampaignSystemLimitedStatusReason`](campaignsystemlimitedstatusreason.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/systemstatuslimitingreasons-data.typealias)*