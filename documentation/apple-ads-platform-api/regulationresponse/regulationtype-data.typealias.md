# RegulationResponse.RegulationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The category of regulatory disclosure this response answers.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string RegulationResponse.RegulationType
```

## Possible Values

- `CAC`: Disclosure required under CAC regulation, at the campaign level.
- `CAMPAIGN_SAPIN_LAW`: Disclosure required under Sapin Law regulation, at the campaign level.
- `ORG_SAPIN_LAW`: Disclosure required under Sapin Law regulation, at the organization level.

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