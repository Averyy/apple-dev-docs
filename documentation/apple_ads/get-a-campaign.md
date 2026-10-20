# Get a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches a specific campaign by campaign identifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use this endpoint to return data for a specific campaign. You can also use a partial fetch as necessary. For more information, see the Use a Partial Fetch section of [Using Apple Ads API Functionality](./using-apple-search-ads-api-functionality.md).

##### Payload example: Get a campaign

**Request**:

```http
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}
```

**Response**:

```json
{
  "id": 542370642,
  "orgId": 40669820,
  "name": "TripTrek campaign 1",
  "dailyBudgetAmount": {
    "amount": "500",
    "currency": "USD"
  },
  "adamId": 427916203,
  "paymentModel": "PAYG",
  "locInvoiceDetails": null,
  "budgetOrders": [],
  "biddingStrategy": "MANUAL_CPT",
  "targetCpa": null,
  "displayStatus": "ON_HOLD",
  "startTime": "2024-04-08T10:33:31.650",
  "endTime": "2024-04-09T10:33:31.650",
  "status": "ENABLED",
  "servingStatus": "NOT_RUNNING",
  "servingStateReasons": [
    "CAMPAIGN_END_DATE_REACHED"
  ],
  "modificationTime": "2024-04-08T11:00:06.513",
  "deleted": false,
  "sapinLawResponse": "NOT_ANSWERED",
  "countriesOrRegions": [
    "AU",
    "CA",
    "GB",
    "US"
  ],
  "countryOrRegionServingStateReasons": {},
  "billingEvent": "TAPS",
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "adChannelType": "SEARCH"
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Responses

- `200` OK (`CampaignResponse`, `application/json`): If the call succeeds, the API returns the [`Campaign`](./campaign.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Campaign Endpoints
- [Create a Campaign](./create-a-campaign.md)
  Creates a campaign to promote an app.
- [Find Campaigns](./find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get all Campaigns](./get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Update a Campaign](./update-a-campaign.md)
  Updates a campaign with a campaign identifier.
- [Delete a Campaign](./delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-campaign)*