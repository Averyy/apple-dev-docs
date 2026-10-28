# Org.PaymentModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The payment model set through Apple Ads.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Org.PaymentModel
```

## Possible Values

- `PAYG`: Pay as you go. The default billing model when no payment model is configured, charged per campaign spend. Budget orders aren’t available with this model.
- `LOC`: Line of credit. A monthly invoicing model required to use budget orders. Invoicing details are available in [`InvoiceDetail`](../invoicedetail.md).

## Discussion

Setting this to `LOC` at the organization level is what makes budget orders available to the ad accounts beneath it.

### Example

```json
{
  "paymentModel": "PAYG"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/org/paymentmodel-data.typealias)*