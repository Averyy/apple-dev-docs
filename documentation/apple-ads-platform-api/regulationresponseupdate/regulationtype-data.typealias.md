# RegulationResponseUpdate.RegulationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The category of regulatory disclosure being answered.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string RegulationResponseUpdate.RegulationType
```

#### Discussion

Each type maps to a different set of valid `responseValue` options, and applies at either the campaign level (`CAC`, `CAMPAIGN_SAPIN_LAW`) or the organization level (`ORG_SAPIN_LAW`).

##### Example

```json
{
  "regulationType": "CAMPAIGN_SAPIN_LAW",
  "responseValue": "AGENT"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponseupdate/regulationtype-data.typealias)*