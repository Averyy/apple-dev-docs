# BrandsReportingCampaign.AdChannelType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The advertising channel type of the campaign at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BrandsReportingCampaign.AdChannelType
```

#### Discussion

Since Brands campaigns only run on Apple Maps, this field distinguishes `SEARCH` results placements from `DISPLAY` placements like the Search tab or Today tab.

##### Example

```json
{
  "adChannelType": "SEARCH"
}
```

See [`ReportingAdChannelType`](reportingadchanneltype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign/adchanneltype-data.typealias)*