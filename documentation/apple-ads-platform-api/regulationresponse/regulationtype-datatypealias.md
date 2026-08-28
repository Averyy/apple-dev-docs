# RegulationResponse.RegulationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The category of regulatory disclosure this response answers.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string RegulationResponse.RegulationType
```

#### Discussion

This mirrors the `regulationType` set when the response was created, and continues to determine which `responseValue` options are valid.

##### Example

```json
{
  "regulationType": "CAMPAIGN_SAPIN_LAW",
  "responseValue": "AGENT"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponse/regulationtype-data.typealias)*