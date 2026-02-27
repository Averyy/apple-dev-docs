# Find Ad Groups (org-level)

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches ad groups within an organization.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to find ad groups within your organization. Use a [`Selector`](selector.md) [`Condition`](condition.md) to narrow results. If you don’t specify selector conditions, all of your ad groups return in the API response. See the [`AdGroup`](adgroup.md) object for field descriptions and selector condition operators.

##### Payload Example Find Ad Groups Org Level

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/adgroups/find

{
  "fields": null,
  "conditions": [
    {
      "field": "pricingModel",
      "operator": "EQUALS",
      "values": [
        "CPC"
      ]
    }
  ],
  "orderBy": [
    {
      "field": "id",
      "sortOrder": "ASCENDING"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 20
  }
}

```

**Response**:

```json
{
  "data": [
    {
      "id": 542370764,
      "campaignId": 56543219,
      "name": "Trip Trek ad group 5",
      "cpaGoal": null,
      "paymentModel": "PAYG",
      "startTime": "2024-10-20T20:37:21.146Z",
      "endTime": "2024-10-20T20:37:21.146Z",
      "automatedKeywordsOptIn": true,
      "defaultBidAmount": {
        "amount": "1",
        "currency": "USD"
      },
      "pricingModel": "CPC",
      "targetingDimensions": {
        "age": {
          "included": [
            {
              "minAge": 18,
              "maxAge": 55
            }
          ]
        },
        "gender": {
          "included": [
            "F"
          ]
        },
        "country": {
          "included": [
            "US"
          ]
        },
        "adminArea": {
          "included": [
            "CA"
          ]
        },
        "locality": {
          "included": [
            "Cupertino"
          ]
        },
        "deviceClass": {
          "included": [
            "IPHONE",
            "IPAD"
          ]
        },
        "daypart": {
          "userTime": {
            "included": [
              0
            ]
          }
        },
        "appDownloaders": {
          "included": [
            "654327167"
          ],
          "excluded": [
            "654325422"
          ]
        },
        "appCategories": {
          "included": [
            100
          ],
          "excluded": [
            100
          ]
        }
      },
      "orgId": 40669876,
      "modificationTime": "2024-10-20T20:37:21.146Z",
      "status": "ENABLED",
      "servingStatus": "RUNNING",
      "servingStateReasons": [
        "null"
      ],
      "displayStatus": "RUNNING",
      "deleted": false
    }
  ],
  "pagination": {
    "totalResults": 1,
    "startIndex": 1,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/adgroups/find`

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create an Ad Group](create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ad-groups-(org-level))*