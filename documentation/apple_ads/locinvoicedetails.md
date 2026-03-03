# LOCInvoiceDetails

**Framework**: Apple Ads  
**Kind**: dictionary

The response to a request to fetch details for `LOC` invoicing details.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object LOCInvoiceDetails
```

## Properties

- `billingContactEmail` (string): A valid email address for the LOC billing contact.
- `buyerEmail` (string): A valid email address for the LOC buyer.
- `buyerName` (string): A valid LOC buyer name.
- `clientName` (string): An advertiser or product. Required for agency-type accounts.
- `orderNumber` (string): A purchase order number. Required for agency-type accounts.

## See Also

- [object BudgetOrder](budgetorder.md)
  The response to requests for budget order details.
- [object BudgetOrderInfo](budgetorderinfo.md)
  The parent object response to a request for budget order details.
- [object BudgetOrderCreate](budgetordercreate.md)
  The parent object response to a request to create a budget order.
- [object BudgetOrderUpdate](budgetorderupdate.md)
  The parent object response to a request to update a budget order.
- [object BudgetOrderInfoResponse](budgetorderinforesponse.md)
  A container for the budget order response body.
- [object BudgetOrderInfoListResponse](budgetorderinfolistresponse.md)
  The response details to budget order requests.
- [object Money](money.md)
  The response to requests for budget amounts in campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/locinvoicedetails)*