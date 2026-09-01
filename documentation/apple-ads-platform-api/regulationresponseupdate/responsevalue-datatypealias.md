# RegulationResponseUpdate.ResponseValue

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The advertiser’s answer to the regulatory disclosure question.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string RegulationResponseUpdate.ResponseValue
```

#### Discussion

Updating this value only makes sense when the campaign’s `regulationType` still requires the disclosure it answers.

##### Example

```json
{
  "regulationType": "CAMPAIGN_SAPIN_LAW",
  "responseValue": "AGENT"
}
```

See [`RegulationResponseValue`](regulationresponsevalue.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponseupdate/responsevalue-data.typealias)*