# AssetEligibilityStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Overall eligibility status for an asset’s policy evaluation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AssetEligibilityStatus
```

#### Discussion

`status` on [`AssetEligibility`](asseteligibility.md) is always one of these values. Treat it as the first check before inspecting `blockedGroups` or `allowedGroups`.

`INELIGIBLE` and `PENDING` mean you should not use the asset in a creative, regardless of what the constraint groups contain. `LIMITED` is the only value where you need to consult those groups for placement- and market-specific detail.

## See Also

- [type AssetType](assettype.md)
  The media type of an asset.
- [type ImageType](imagetype.md)
  Image format type for an uploaded asset.
- [type Orientation](orientation.md)
  Asset orientation and aspect ratio classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/asseteligibilitystatus)*