# Create a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates a campaign to promote an app.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)
- [Apple Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Essential points for creating campaigns are:

- Use [`Search for iOS apps`](search-for-ios-apps.md) to retrieve your `adamId` to use in the request payload.
- Use [`Find App Eligibility Records`](find-app-eligibility-records.md) to determine your app eligibility to run in campaigns.
- A `dailyBudgetAmount` is a required field to manage the daily budget of your campaigns.
- Use the `countriesOrRegions` attribute to assign App Store locations. To advertise in multiple markets, group countries and regions into a single campaign using ISO alpha-2 country code values.
- See the [`Campaign`](campaign.md) object and [`SupplySource`](supplysource.md) for descriptions of attributes.

After creating a campaign, see [`Create an Ad Group`](create-an-ad-group.md).

##### Payload Example Create a Campaign with a Manual Bid Strategy

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/campaigns

{
    "orgId": 48394480,
    "name": "Example Manual Campaign 1",
    "startTime": "2026-11-08T17:00:00.000",
    "endTime": "2026-11-09T17:00:00.000",
    "billingEvent": "TAPS",
    "dailyBudgetAmount": {
        "amount": "250.00",
        "currency": "MXN"
    },
    "adamId": 535500008,
    "countriesOrRegions": ["US","CA"],
    "status": "ENABLED",
    "supplySources": ["APPSTORE_SEARCH_RESULTS"],
    "adChannelType": "SEARCH"
}
```

**Response**:

```json
{
  "data": {
    "id": 886873328,
    "orgId": 19173940,
    "name": "Manual campaign example",
    "dailyBudgetAmount": {
      "amount": "250",
      "currency": "MXN"
    },
    "adamId": 535500008,
    "paymentModel": "PAYG",
    "locInvoiceDetails": null,
    "budgetOrders": [],
    "startTime": "2026-11-08T17:00:00.000",
    "endTime": "2026-11-09T17:00:00.000",
    "status": "ENABLED",
    "servingStatus": "NOT_RUNNING",
    "creationTime": "2026-02-03T21:17:01.891",
    "servingStateReasons": [
      "APP_NOT_CATEGORIZED",
      "CAMPAIGN_START_DATE_IN_FUTURE",
      "AD_GROUP_MISSING"
    ],
    "modificationTime": "2026-02-03T21:17:02.366",
    "deleted": false,
    "sapinLawResponse": "NOT_ANSWERED",
    "countriesOrRegions": [
      "CA",
      "US"
    ],
    "countryOrRegionServingStateReasons": {},
    "supplySources": [
      "APPSTORE_SEARCH_RESULTS"
    ],
    "adChannelType": "SEARCH",
    "billingEvent": "TAPS",
    "biddingStrategy": "MANUAL_CPT",
    "targetCpa": null,
    "displayStatus": "ON_HOLD"
  },
  "pagination": null,
  "error": null
}
```

##### Payload Example Create a Campaign with a Maximize Conversions Bid Strategy

- Set the `biddingStrategy` value to `MAX_CONVERSIONS`. If not specified, `biddingStrategy` defaults to `MANUAL_CPT`.
- A `targetCpa` is required.
- Only the `APPSTORE_SEARCH_RESULTS` `supplySources` placement is supported.

After creating a Maximize Conversions bid strategy, see the automated ad group payload example in [`Create an Ad Group`](create-an-ad-group.md).

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/campaigns

{
  "orgId": 39879640,
  "name": "Max Conversions bid strategy example",
  "startTime": "2025-05-08T17:00:00.000",
  "endTime": "2025-05-09T17:00:00.000",
  "billingEvent": "TAPS",
  "dailyBudgetAmount": {
    "amount": "250.00",
    "currency": "USD"
  },
  "adamId": 1004806037,
  "countriesOrRegions": [
    "US",
    "CA"
  ],
  "status": "ENABLED",
  "supplySources": [
    "APPSTORE_SEARCH_RESULTS"
  ],
  "biddingStrategy": "MAX_CONVERSIONS",
  "targetCpa": {
    "amount": "10",
    "currency": "USD"
  },
  "adChannelType": "DISPLAY"
}
```

**Response**:

```json
{
  "data": {
    "id": 585885088,
    "orgId": 39879640,
    "name": "TripTrek Campaign",
    "dailyBudgetAmount": {
      "amount": "250",
      "currency": "USD"
    },
    "adamId": 1004806037,
    "paymentModel": "PAYG",
    "locInvoiceDetails": null,
    "budgetOrders": [],
    "startTime": "2025-05-08T17:00:00.000",
    "endTime": "2025-05-09T17:00:00.000",
    "status": "ENABLED",
    "servingStatus": "NOT_RUNNING",
    "creationTime": "2026-05-04T20:15:04.382",
    "servingStateReasons": [
      "APP_NOT_PUBLISHED_YET",
      "CAMPAIGN_START_DATE_IN_FUTURE",
      "AD_GROUP_MISSING"
    ],
    "modificationTime": "2026-05-04T20:15:04.747",
    "deleted": false,
    "sapinLawResponse": "NOT_ANSWERED",
    "countriesOrRegions": [
      "CA",
      "US"
    ],
    "countryOrRegionServingStateReasons": {
      "CA": [
        "APP_NOT_PUBLISHED_YET"
      ],
      "US": [
        "APP_NOT_PUBLISHED_YET"
      ]
    },
    "supplySources": [
      "APPSTORE_SEARCH_RESULTS"
    ],
    "biddingStrategy": "MAX_CONVERSIONS",
    "targetCpa": {
      "amount": "10.00",
      "currency": "USD"
    },
    "adChannelType": "DISPLAY",
    "billingEvent": "TAPS",
    "displayStatus": "ON_HOLD"
  },
  "pagination": null,
  "error": null
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns`

## Request Body

The request body that includes the details of the campaign.

## See Also

- [Find Campaigns](find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get a Campaign](get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Get all Campaigns](get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Update a Campaign](update-a-campaign.md)
  Updates a campaign with a campaign identifier.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-a-campaign)*