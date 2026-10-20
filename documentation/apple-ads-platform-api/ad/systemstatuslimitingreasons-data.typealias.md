# Ad.SystemStatusLimitingReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reasons that limit an ad’s delivery capacity without fully stopping it.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Ad.SystemStatusLimitingReasons
```

## Possible Values

- `CREATIVE_POLICY_ISSUES`: The ad creative associated with this ad has policy violations that limit but do not fully stop delivery.

#### Discussion

Unlike [`Ad.SystemStatusReasons`](./systemstatusreasons-data.typealias.md), these codes flag conditions, such as creative policy issues, that reduce delivery rather than stop it outright.

##### Example

```json
{
  "systemStatusLimitingReasons": ["CREATIVE_POLICY_ISSUES"]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/systemstatuslimitingreasons-data.typealias)*