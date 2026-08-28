# Org.Currency

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The currency used by the organization.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Org.Currency
```

#### Discussion

This currency is set once for the organization, including legacy organizations that still report amounts in `RMB` rather than its ISO 4217 equivalent `CNY`.

##### Example

```json
{
  "currency": "USD"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/org/currency-data.typealias)*