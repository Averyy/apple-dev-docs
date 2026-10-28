# AdAccount.Currency

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The currency for the ad account.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdAccount.Currency
```

## Possible Values

- `USD`: United States Dollar.
- `RMB`: Renminbi. A legacy alias for `CNY`, not an ISO 4217 code. Prefer `CNY`.
- `AUD`: Australian Dollar.
- `CAD`: Canadian Dollar.
- `EUR`: Euro.
- `GBP`: British Pound Sterling.
- `JPY`: Japanese Yen.
- `MXN`: Mexican Peso.
- `NZD`: New Zealand Dollar.
- `RUB`: Russian Ruble.
- `CNY`: Chinese Yuan. The ISO 4217 code for the same currency as `RMB`.
- `INR`: Indian Rupee.
- `BRL`: Brazilian Real.
- `IDR`: Indonesian Rupiah.

## Discussion

The `AdAccount` currency is inherited from the parent org at creation.

### Example

```json
{
  "currency": "USD"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccount/currency-data.typealias)*