# Rule.Value

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The comparison value for a targeting rule, as either a single string or an array of strings.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Rule.Value
```

#### Discussion

`Rule.value` accepts either a single string or an array of strings, depending on the rule’s `operator`. Pass a string for `EQUALS` and `NOT_EQUALS`. Pass an array of strings for `IN` and `NOT_IN`.

The expected string format also depends on `field`: a plain name for `adminArea` and `postalCode`, a pipe-delimited `countryOrRegion|adminArea|locality` string for `locality`, and a location ID string for `locationId`. See [`Rule`](rule.md) for the full list of supported `field` values.

##### Example

```json
{
  "field": "locality",
  "operator": "IN",
  "value": ["US|New York|Brooklyn", "US|California|San Francisco"]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/rule/value-data.dictionary)*