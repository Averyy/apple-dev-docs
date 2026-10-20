# BudgetOrderCreate

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The parent object response to a request to create a budget order.

**Availability**:
- Search Ads 4.11+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object BudgetOrderCreate
```

## Topics

### Objects
- [object BudgetOrderCreate.Bo](./budgetordercreate/bo-data.dictionary.md)
  The response to a request to create a budget order.

## Properties

- `bo` (BudgetOrderCreate.Bo): Contains the details of the budget order.
- `orgIds` ([int64]): The identifier of the organization that owns the campaign. Currently, only one `orgId` is supported.

## See Also

### Budget Order Request and Response Objects
- [object BudgetOrder](./budgetorder.md)
  The response to requests for budget order details.
- [object BudgetOrderInfo](./budgetorderinfo.md)
  The parent object response to a request for budget order details.
- [object BudgetOrderUpdate](./budgetorderupdate.md)
  The parent object response to a request to update a budget order.
- [object BudgetOrderInfoResponse](./budgetorderinforesponse.md)
  A container for the budget order response body.
- [object BudgetOrderInfoListResponse](./budgetorderinfolistresponse.md)
  The response details to budget order requests.
- [object LOCInvoiceDetails](./locinvoicedetails.md)
  The response to a request to fetch details for `LOC` invoicing details.
- [object Money](./money.md)
  The response to requests for budget amounts in campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/budgetordercreate)*