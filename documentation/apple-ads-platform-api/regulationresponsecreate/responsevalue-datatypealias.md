# RegulationResponseCreate.ResponseValue

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The advertiser’s answer to the regulatory disclosure question.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string RegulationResponseCreate.ResponseValue
```

#### Discussion

Set this alongside `regulationType` when creating the response, since the valid options depend on which disclosure category you’re answering.

##### Example

```json
{
  "regulationType": "CAMPAIGN_SAPIN_LAW",
  "responseValue": "AGENT"
}
```

See [`RegulationResponseValue`](regulationresponsevalue.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponsecreate/responsevalue-data.typealias)*