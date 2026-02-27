# Get a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a specific campaign by campaign identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to return data for a specific campaign. You can also use a partial fetch as necessary. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get a Campaign

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
  "budgetAmount": {
    "amount": "2000",
    "currency": "USD"
  },
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

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## See Also

- [Create a Campaign](create-a-campaign.md)
  Creates a campaign to promote an app.
- [Find Campaigns](find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get all Campaigns](get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Update a Campaign](update-a-campaign.md)
  Updates a campaign with a campaign identifier.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-campaign)*