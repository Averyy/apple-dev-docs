# Campaign.PaymentModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The payment model that determines payment method and budget availability for the ad account running this campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Campaign.PaymentModel
```

#### Discussion

Because this reflects the ad account’s payment model rather than a campaign-level setting, every campaign under the same ad account reports the same value.

##### Example

```json
{
  "paymentModel": "PAYG"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/paymentmodel-data.typealias)*