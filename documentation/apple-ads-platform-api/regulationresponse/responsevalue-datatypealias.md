# RegulationResponse.ResponseValue

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The advertiser’s answer to the regulatory disclosure question.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string RegulationResponse.ResponseValue
```

#### Discussion

Which values apply depends on the paired `regulationType`: Sapin Law questions expect `AGENT`/`NOT_AGENT` or `FRENCH_BUSINESS`/`NOT_FRENCH_BUSINESS`, while other regulation types may use the generic `TRUE`/`FALSE`.

##### Example

```json
{
  "regulationType": "CAMPAIGN_SAPIN_LAW",
  "responseValue": "AGENT"
}
```

See [`RegulationResponseValue`](regulationresponsevalue.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponse/responsevalue-data.typealias)*