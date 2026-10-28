# Find Ad Groups

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches ad groups within a campaign.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

## Discussion

Use this endpoint to find ad groups within campaigns using the associated `campaignId` in the resource path. Use  a [`Selector`](./selector.md) [`Condition`](./condition.md) to narrow results. If you don’t specify selector conditions, all ad groups in campaigns return. See the [`AdGroup`](./adgroup.md) object for field descriptions and selector condition operators.

### Payload example: Find ad groups

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/campaigns/<campaignid>/adgroups/find

{
  "pagination": {
    "offset": 0,
    "limit": 20
  },
  "fields": null,
  "orderBy": [
    {
      "field": "id",
      "sortOrder": "ASCENDING"
    }
  ],
  "conditions": [
    {
      "field": "pricingModel",
      "operator": "EQUALS",
      "values": [
        "CPC"
      ]
    }
  ]
}
```

**Response**:

```json
{
  "data": [
    {
      "id": 542370642,
      "campaignId": 56543219,
      "name": "Trip Trek ad group 1",
      "cpaGoal": null,
      "startTime": "2026-04-08T07:00:00.000",
      "endTime": null,
      "automatedKeywordsOptIn": true,
      "defaultBidAmount": {
        "amount": "1",
        "currency": "USD"
      },
      "pricingModel": "CPC",
      "targetingDimensions": {
        "age": null,
        "gender": null,
        "country": null,
        "adminArea": null,
        "locality": null,
        "deviceClass": {
          "included": [
            "IPHONE",
            "IPAD"
          ]
        },
        "daypart": null,
        "appDownloaders": {
          "included": [],
          "excluded": []
        }
      },
      "orgId": 40669820,
      "modificationTime": "2026-04-08T23:30:17.280",
      "status": "ENABLED",
      "servingStatus": "RUNNING",
      "servingStateReasons": null,
      "displayStatus": "RUNNING",
      "deleted": false
    },
    {
      "id": 542370643,
      "campaignId": 56543219,
      "name": "Trip Trek ad group 2",
      "cpaGoal": null,
      "startTime": "2026-04-08T23:46:00.000",
      "endTime": "2026-04-09T05:00:00.000",
      "automatedKeywordsOptIn": true,
      "defaultCpcBid": {
        "amount": "1",
        "currency": "USD"
      },
      "pricingModel": "CPC",
      "targetingDimensions": {
        "age": null,
        "gender": null,
        "country": null,
        "adminArea": null,
        "locality": null,
        "deviceClass": {
          "included": [
            "IPHONE",
            "IPAD"
          ]
        },
        "daypart": null,
        "appDownloaders": {
          "included": [],
          "excluded": []
        }
      },
      "orgId": 40669820,
      "modificationTime": "2026-04-08T05:15:36.518",
      "status": "ENABLED",
      "servingStatus": "RUNNING",
      "servingStateReasons": [
        "null"
      ],
      "displayStatus": "RUNNING",
      "deleted": false
    },
    {
      "id": 542370644,
      "campaignId": 56543219,
      "name": "Trip Trek ad group 3",
      "cpaGoal": null,
      "startTime": "2026-04-08T23:45:00.000",
      "endTime": "2026-04-09T06:59:00.000",
      "automatedKeywordsOptIn": true,
      "defaultBidAmount": {
        "amount": "100",
        "currency": "USD"
      },
      "pricingModel": "CPC",
      "targetingDimensions": {
        "age": null,
        "gender": null,
        "country": null,
        "adminArea": null,
        "locality": null,
        "deviceClass": {
          "included": [
            "IPHONE",
            "IPAD"
          ]
        },
        "daypart": null,
        "appDownloaders": {
          "included": [],
          "excluded": []
        }
      },
      "orgId": 40669820,
      "modificationTime": "2026-04-08T07:15:21.110",
      "status": "ENABLED",
      "servingStatus": "NOT_RUNNING",
      "servingStateReasons": [
        "ADGROUP_END_DATE_REACHED"
      ],
      "displayStatus": "ON_HOLD",
      "deleted": false
    },
    {
      "id": 542370645,
      "campaignId": 56543219,
      "name": "Trip Trek ad group 4",
      "cpaGoal": {
        "amount": "100",
        "currency": "USD"
      },
      "startTime": "2026-04-08T19:10:31.650",
      "endTime": "2026-04-09T19:33:31.650",
      "automatedKeywordsOptIn": false,
      "defaultBidAmount": {
        "amount": "1",
        "currency": "USD"
      },
      "pricingModel": "CPC",
      "targetingDimensions": {
        "age": {
          "included": [
            {
              "minAge": 20,
              "maxAge": 25
            }
          ]
        },
        "gender": {
          "included": [
            "M"
          ]
        },
        "country": null,
        "adminArea": null,
        "locality": null,
        "deviceClass": {
          "included": [
            "IPAD",
            "IPHONE"
          ]
        },
        "daypart": {
          "userTime": {
            "included": [
              1,
              3,
              22,
              24
            ]
          }
        },
        "appDownloaders": null
      },
      "orgId": 40669820,
      "modificationTime": "2026-04-08T18:06:20.305",
      "status": "ENABLED",
      "servingStatus": "RUNNING",
      "servingStateReasons": null,
      "displayStatus": "RUNNING",
      "deleted": false
    }
  ],
  "pagination": {
    "totalResults": 4,
    "startIndex": 1,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/find`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `Selector`

The request body that includes the selector [`Condition`](./condition.md). [`Selector`](./selector.md) objects define what data the API returns when fetching resources.

## Responses

- `200` OK (`AdGroupListResponse`, `application/json`): If the call succeeds, the API returns the [`AdGroup`](./adgroup.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Group Endpoints
- [Create an Ad Group](./create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups (org-level)](./find-ad-groups-%28org-level%29.md)
  Fetches ad groups within an organization.
- [Get an Ad Group](./get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](./get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](./update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](./delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ad-groups)*