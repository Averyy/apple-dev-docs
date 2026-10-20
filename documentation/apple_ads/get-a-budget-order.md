# Get a Budget Order

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches a specific budget order using a budget order identifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

When you create a budget order through [Apple Ads Advanced](https://ads.apple.com), the system returns a budget order ID (`boId`) that you can use with to return details of a specific budget order for an organization or campaign group. Through the API, you can only fetch a budget order using Get a Budget Order or [`Get all Budget Orders`](./get-all-budget-orders.md).

This call retrieves a specific assigned budget order for your organization. It also returns completed and canceled orders. Budget orders also return when you use the [`Create a Campaign`](./create-a-campaign.md) or [`Update a Campaign`](./update-a-campaign.md) endpoints.

##### Payload example: Get a budget order

**Request**:

```
GET https://api.searchads.apple.com/api/v5/budgetorders/{boId}
```

**Response**:

```json
{
  "data": {
    "orgIds": [
      3761812
    ],
    "bo": {
      "id": 542370539,
      "name": "get a budget order example",
      "startDate": "2024-04-08T00:00:00.000",
      "endDate": "2024-04-09T23:59:59.999",
      "budget": {
        "amount": "2000",
        "currency": "USD"
      },
      "orderNumber": "2376542",
      "clientName": "Trip Trek",
      "primaryBuyerName": "Trip Trek",
      "primaryBuyerEmail": "buyer@triptrek.com",
      "billingEmail": "billing@triptrek.com",
      "status": "COMPLETED",
      "parentOrgId": 27154130,
      "supplySources": [
        "APPSTORE_PRODUCT_PAGES_BROWSE", 
        "APPSTORE_SEARCH_RESULTS",
        "APPSTORE_SEARCH_TAB", 
        "APPSTORE_TODAY_TAB"
      ]
    }
  },
  "pagination": null,
  "error": null
}

```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/budgetorders/{boId}`

## Parameters

### Path Parameters

- `boId` (int64) *(required)*: The unique identifier for the budget order. You set the `boID` when creating a budget order through the Apple Ads UI.

## Responses

- `200` OK (`BudgetOrderInfoResponse`, `application/json`): If the call succeeds, the API returns the [`BudgetOrderInfoResponse`](./budgetorderinforesponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Budget Order Endpoints
- [Create a Budget Order](./create-a-budget-order.md)
  Creates a budget order in the context of your org ID.
- [Update a Budget Order](./update-a-budget-order.md)
  Updates an existing budget order.
- [Get all Budget Orders](./get-all-budget-orders.md)
  Fetches all assigned budget orders for an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-budget-order)*