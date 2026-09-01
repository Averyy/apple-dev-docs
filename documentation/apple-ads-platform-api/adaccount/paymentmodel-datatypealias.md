# AdAccount.PaymentModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The payment model for the ad account.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AdAccount.PaymentModel
```

#### Discussion

Choosing `LOC` here is a prerequisite for using budget orders on this ad account.

See also [`Budget Orders Endpoints`](budget-orders-endpoints.md).

##### Example

```json
{
  "paymentModel": "PAYG"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccount/paymentmodel-data.typealias)*