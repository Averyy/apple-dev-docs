# AdGroup.CpaCap

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A deprecated cost-per-acquisition goal value. Use `bidStrategy` with `MAX_CONVERSIONS` instead.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroup.CpaCap
```

#### Discussion

##### Example

```json
{
  "cpaCap": {
    "value": {
      "amount": "50.00",
      "currency": "USD"
    }
  }
}
```

See [`CPAGoal`](cpagoal.md) for the full field reference.

## Properties

- `value` (Money): The target CPA monetary value. Object with `amount` (string) and `currency` (string) properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/cpacap-data.dictionary)*