# RegulationResponse.ResponseValue

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The advertiser’s answer to the regulatory disclosure question.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string RegulationResponse.ResponseValue
```

## Possible Values

- `AGENT`: The advertiser is an agent, as defined under the Sapin Law regulation.
- `NOT_AGENT`: The advertiser is not an agent, as defined under the Sapin Law regulation.
- `FRENCH_BUSINESS`: The advertiser is a French business, as defined under the Sapin Law regulation.
- `NOT_FRENCH_BUSINESS`: The advertiser is not a French business, as defined under the Sapin Law regulation.
- `TRUE`: A generic affirmative response.
- `FALSE`: A generic negative response.
- `NOT_ANSWERED`: No response has been provided yet.

#### Discussion

Which values apply depends on the paired `regulationType`: Sapin Law questions expect `AGENT`/`NOT_AGENT` or `FRENCH_BUSINESS`/`NOT_FRENCH_BUSINESS`, while other regulation types may use the generic `TRUE`/`FALSE`.

##### Example

```json
{
  "regulationType": "CAMPAIGN_SAPIN_LAW",
  "responseValue": "AGENT"
}
```

See [`RegulationResponseValue`](../regulationresponsevalue.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponse/responsevalue-data.typealias)*