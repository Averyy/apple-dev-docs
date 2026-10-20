# BudgetOrder

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The response to requests for budget order details.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object BudgetOrder
```

## Properties

- `billingEmail` (string): The billing email.

  This field is updatable.
- `budget` (Money): The total budget amount available for the budget order.

  This field is updatable.
- `clientName` (string): The advertiser or product. This is a requirement for agency-type accounts.

  This field is updatable only before the startDate of a campaign.
- `endDate` (date-time): The scheduled end date and time for the budget order in the format of `yyyy-mm-dd'T'HH:MM:SS.SSS`.

  This field is updatable.
- `id` (int64): A unique identifier for the budget order.

  When you create a budget order through [Apple Ads Advanced](https://ads.apple.com), the system returns a budget order ID (`boId`) that you can use with [`Get a Budget Order`](./get-a-budget-order.md) to return details of a specific budget order for an organization or campaign group.
- `name` (string): The name of the budget order, which is unique within an organization. This field is updatable only before the `startDate` of a campaign.
- `orderNumber` (string): A purchase order number. This is a requirement for agency-type accounts.

  This field is updatable only before the startDate of a campaign.
- `parentOrgId` (int64): The unique identifier of the organization that owns the budget order.
- `primaryBuyerEmail` (string): The primary buyer’s email address.

  This field is updatable.
- `primaryBuyerName` (string): The primary buyer’s name.

  This field is updatable.
- `startDate` (date-time): The scheduled start date and time for the budget order in the format of `yyyy-mm-dd'T'HH:MM:SS.SSS`.

  This field is updatable only before the `startDate` of a campaign and is only editable if there are no campaigns assigned to the budget order.
- `status` (string): The system-controlled status indicator for the budget order.

  - **`ACTIVE`**: This status occurs when the budget order reaches its start date.
  - **`CANCELED`**: This status occurs when you cancel the budget order.
  - **`COMPLETED`**: This status occurs when the budget order reaches its end date.
  - **`EXHAUSTED`**: This status occurs when you exhaust the budget for the budget order before it reaches its end date.
  - **`INACTIVE`**: This status occurs after you create the budget order and before it reaches its start date.

  **Allowed Values**: `ACTIVE`, `CANCELED`, `INACTIVE`, `COMPLETED`, `EXHAUSTED`
- `supplySources` ([string]): The supply source of ads to use in a budget order and a campaign. As of [Apple Ads Campaign Management API version 5.3](./apple-search-ads-campaign-management-api-5.md#53), the [`Create a Budget Order`](./create-a-budget-order.md) endpoint does not support a single placement type. In all responses, the `supplySources` field contains all possible values.

  **Allowed Values**: `APPSTORE_PRODUCT_PAGES_BROWSE`, `APPSTORE_SEARCH_RESULTS`, `APPSTORE_SEARCH_TAB`, `APPSTORE_TODAY_TAB`

## See Also

### Budget Order Request and Response Objects
- [object BudgetOrderInfo](./budgetorderinfo.md)
  The parent object response to a request for budget order details.
- [object BudgetOrderCreate](./budgetordercreate.md)
  The parent object response to a request to create a budget order.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/budgetorder)*