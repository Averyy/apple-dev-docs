# Update a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates a campaign with a campaign identifier.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to update countries or regions (App Store geolocations) where you promote your app, and to set your campaign budget. Use the associated `campaignId` as a resource.

To edit a subset of object properties without having to include all object properties in the payload, use partial updates. Use a campaign object JSON envelope in your campaign update request payloads. Other objects don’t require a JSON envelope. See the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Switch From a Manual to a Maximize Conversions Bid Strategy Campaign

Ad group and keyword bid values are hidden (returned as `0`) in Maximize Conversions campaigns. If you switch back to the manual strategy later, your bids will be restored.

The `TargetCpa` must be must be provided.

The campaign requires an automated ad group to run. See [`Create an Ad Group`](create-an-ad-group.md).

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}

{
  "clearGeoTargetingOnCountryOrRegionChange": false,
  "campaign": {
    "biddingStrategy": "MAX_CONVERSIONS",
    "targetCpa": {
      "amount": "10",
      "currency": "USD"
    }
  }
}
```

**Response**:

```json
{
  "id": 542370642,
  "orgId": 40669820,
  "name": "TripTrek campaign 7",
  "dailyBudgetAmount": {
    "amount": "500",
    "currency": "USD"
  },
  "adamId": 427916203,
  "paymentModel": "PAYG",
  "locInvoiceDetails": null,
  "budgetOrders": [],
  "billingEvent": "TAPS",
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "biddingStrategy": "MAX_CONVERSIONS",
  "targetCpa": {
    "amount": "12",
    "currency": "USD"
  },
  "adChannelType": "SEARCH",
  "displayStatus": "RUNNING",
  "startTime": "2025-05-18T00:00:00.000",
  "endTime": "2025-05-22T00:00:00.000",
  "status": "ENABLED",
  "servingStatus": "PAUSED_BY_SYSTEM",
  "servingStateReasons": null,
  "modificationTime": "2025-05-08T18:27:56.380",
  "deleted": false,
  "sapinLawResponse": "NOT_ANSWERED",
  "countriesOrRegions": [
    "AU",
    "CA",
    "GB",
    "US"
  ],
  "countryOrRegionServingStateReasons": {}
}
```

##### Payload Example Switch From a Maximize Conversions to a Manual Bid Strategy Campaign

Bid values on ad groups and keywords are visible in Maximize Conversions campaigns.

The `TargetCpa` must be set to null.

Bids will be added based on recommended bids for the campaign. If the campaign previously used a manual strategy, your previous bids will be restored. It is recommended to review all keywords and bids before running a campaign to ensure that they align with your business goals.

For reports with a Maximize Conversions bidding strategy, see campaign and ad group [`Get Campaign-Level Reports`](get-campaign-level-reports.md) and [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md).

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}

{
  "clearGeoTargetingOnCountryOrRegionChange": false,
  "campaign": {
    "biddingStrategy": "MANUAL_CPT",
    "targetCpa": null
  }
}
```

**Response**:

```json
{
  "id": 542370642,
  "orgId": 40669820,
  "name": "TripTrek campaign 2",
  "dailyBudgetAmount": {
    "amount": "500",
    "currency": "USD"
  },
  "adamId": 427916203,
  "paymentModel": "PAYG",
  "locInvoiceDetails": null,
  "budgetOrders": [],
  "billingEvent": "TAPS",
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "biddingStrategy": "MANUAL_CPT",
  "targetCpa": null,
  "adChannelType": "SEARCH",
  "displayStatus": "RUNNING",
  "startTime": "2025-05-18T00:00:00.000",
  "endTime": "2025-05-22T00:00:00.000",
  "status": "ENABLED",
  "servingStatus": "RUNNING",
  "servingStateReasons": null,
  "modificationTime": "2025-05-08T18:27:56.380",
  "deleted": false,
  "sapinLawResponse": "NOT_ANSWERED",
  "countriesOrRegions": [
    "AU",
    "CA",
    "GB",
    "US"
  ],
  "countryOrRegionServingStateReasons": {}
}
```

##### Payload Example Update a Campaign

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}

{
  "clearGeoTargetingOnCountryOrRegionChange": true,
  "campaign": {
    “name”: “TripTrek campaign 1”,
    “dailyBudgetAmount”: {
      "amount": "250",
      "currency": "USD"
    },
    "budgetOrders": [
      0
    ],
    "locInvoiceDetails": {
      "clientName": "client name",
      "orderNumber": "7565239",
      "primaryBuyerName": "buyer name",
      "primaryBuyerEmail": "buyer email",
      "billingContactEmail": "billing email"
    },
    "status": "ENABLED",
    "countriesOrRegions": [
      "US",
      "CA",
      "GB",
      "AU"
    ]
  }
}
```

**Response**:

```json
{
  "id": 542370539,
  "orgId": 40669820,
  "name": "TripTrek campaign 1",
  "dailyBudgetAmount": {
    "amount": "250",
    "currency": "USD"
  },
  "adamId": 422689480,
  "paymentModel": “PAYG”,
  "billingEvent": "TAPS",
  "locInvoiceDetails": {
    "clientName": "client name",
    "orderNumber": "7565239",
    "buyerName": "buyer name",
    "buyerEmail": "buyer email",
    "billingContactEmail": "billing e-mail"
  },
  "budgetOrders": [
    34562211,
    34562212
  ],
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "biddingStrategy": "MANUAL_CPT",
  "targetCpa": null,
  },
  "adChannelType": "SEARCH",
  "displayStatus": "RUNNING",
  "startTime": "2025-05-18T12:00:00.000Z",
  "endTime": "2025-05-22T12:00:00.000Z",
  "status": "ENABLED",
  "servingStatus": "RUNNING",
  "servingStateReasons": [
    [
      "null"
    ]
  ],
  "modificationTime": "2025-05-09T17:20:33.919Z",
  "deleted": false,
  "countriesOrRegions": [
    "AU",
    "CA",
    "GB",
    "US"
  ],
  "countryOrRegionServingStateReasons": {
  }
}
```

##### Payload Example Update a Target Cpa of a Maximize Conversions Bid Strategy

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}

{
  "clearGeoTargetingOnCountryOrRegionChange": false,
  "campaign": {
    "targetCpa": {
      "amount": "12",
      "currency": "USD"
    }
  }
}
```

**Response**:

```json
{
  "id": 542370642,
  "orgId": 40669820,
  "name": "TripTrek campaign 2",
  "dailyBudgetAmount": {
    "amount": "500",
    "currency": "USD"
  },
  "adamId": 427916203,
  "paymentModel": "PAYG",
  "locInvoiceDetails": null,
  "budgetOrders": [],
  "billingEvent": "TAPS",
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "biddingStrategy": "MAX_CONVERSIONS",
  "targetCpa": {
    "amount": "12",
    "currency": "USD"
  },
  "adChannelType": "DISPLAY",
  "displayStatus": "RUNNING",
  "startTime": "2026-05-18T00:00:00.000",
  "endTime": "2026-05-22T00:00:00.000",
  "status": "ENABLED",
  "servingStatus": "RUNNING",
  "servingStateReasons": null,
  "modificationTime": "2026-05-08T18:27:56.380",
  "deleted": false,
  "sapinLawResponse": "NOT_ANSWERED",
  "countriesOrRegions": [
    "AU",
    "CA",
    "GB",
    "US"
  ],
  "countryOrRegionServingStateReasons": {}
}
```

##### Payload Example Update a Campaign Daily Budget Amount

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}

{
  "campaign": {
    "dailyBudgetAmount": {
      "amount": "300",
      "currency": "USD"
    }
  }
}
```

**Response**:

```json
{
  "data": {
    "id": 586640439,
    "orgId": 39879640,
    "name": "TripTrek campaign",
    "dailyBudgetAmount": {
      "amount": "300",
      "currency": "USD"
    },
    "adamId": 1004806037,
    "paymentModel": "PAYG",
    "locInvoiceDetails": null,
    "budgetOrders": [],
    "startTime": "2025-05-18T17:00:00.000",
    "endTime": "2025-05-22T17:00:00.000",
    "status": "ENABLED",
    "servingStatus": "NOT_RUNNING",
    "creationTime": "2025-05-11T19:59:51.484",
    "servingStateReasons": [
      "CAMPAIGN_START_DATE_IN_FUTURE",
      "AD_GROUP_MISSING"
    ],
    "modificationTime": "2025-05-11T20:08:40.809",
    "deleted": false,
    "sapinLawResponse": "NOT_ANSWERED",
    "countriesOrRegions": [
      "US"
    ],
    "supplySources": [
      "APPSTORE_SEARCH_TAB"
    ],
    "adChannelType": "DISPLAY",
    "billingEvent": "TAPS",
    "displayStatus": "ON_HOLD"
  },
  "pagination": null,
  "error": null
}
```

##### Payload Example Update a Campaign with Countries or Regions

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}

{
  "clearGeoTargetingOnCountryOrRegionChange": true,
  "campaign": {
    "countriesOrRegions": [
      "US",
      "CA",
      "GB",
      "AU"
    ]
  }
}
```

**Response**:

```json
{
  "id": 542370642,
  "orgId": 40669820,
  "name": "TripTrek campaign 2",
  "dailyBudgetAmount": {
    "amount": "500",
    "currency": "USD"
  },
  "adamId": 427916203,
  "paymentModel": "PAYG",
  "locInvoiceDetails": null,
  "budgetOrders": [],
  "billingEvent": "TAPS",
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "adChannelType": "SEARCH",
  "displayStatus": "RUNNING",
  "startTime": "2025-05-18T00:00:00.000",
  "endTime": "2025-05-22T00:00:00.000",
  "status": "ENABLED",
  "servingStatus": "RUNNING",
  "servingStateReasons": null,
  "modificationTime": "2025-05-08T18:27:56.380",
  "deleted": false,
  "sapinLawResponse": "NOT_ANSWERED",
  "countriesOrRegions": [
    "AU",
    "CA",
    "GB",
    "US"
  ],
  "countryOrRegionServingStateReasons": {}
}
```

## Endpoint

`PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes the details of the campaign.

## See Also

- [Create a Campaign](create-a-campaign.md)
  Creates a campaign to promote an app.
- [Find Campaigns](find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get a Campaign](get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Get all Campaigns](get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-a-campaign)*