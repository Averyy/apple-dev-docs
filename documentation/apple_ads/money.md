# Money

**Framework**: Apple Ads  
**Kind**: dictionary

The response to requests for budget amounts in campaigns.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object Money
```

## Properties

- `amount` (string): The monetary value in the specified currency. The API uses `amount` whenever a currency value is necessary. The string can contain up to two decimal digits.
- `currency` (string): The organization’s default currency that is set up in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).

## Relationships

### Inherited By
- [ReportingAdGroup.CpaGoal](reportingadgroup/cpagoal-data.dictionary.md)
- [ReportingCampaign.TargetCpa](reportingcampaign/targetcpa-data.dictionary.md)

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
- [object LOCInvoiceDetails](locinvoicedetails.md)
  The response to a request to fetch details for  `LOC` invoicing details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/money)*