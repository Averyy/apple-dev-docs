# Campaign.PaymentModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The payment model that determines payment method and budget availability for the ad account running this campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Campaign.PaymentModel
```

## Possible Values

- `PAYG`: Pay as You Go. The default billing model when no payment model is configured. Budget orders are not available with this model.
- `LOC`: Line of Credit. A monthly invoicing model required to use budget orders. Invoicing details are available in [`InvoiceDetail`](../invoicedetail.md).

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