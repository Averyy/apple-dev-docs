# Create Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Creates negative keywords for a campaign.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Overview

> **Note**:  If you create duplicate keywords, the payload response indicates an error, but the call returns with a 200 status code.

- 400: An invalid query or missing required parameters.
- 401: An unauthenticated call fails to get the requested response.
- 403: Insufficient rights to the resource.
- 404: The API can’t locate the resource.
- 429: The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- 500: The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## Discussion

Negative keywords prevent your ad from showing up in App Store searches. Negative keywords can belong to a campaign or an ad group.

To create campaign negative keywords, use the associated `campaignId` in the URI.

### Payload example: Create campaign negative keywords

**Request**:

```
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/bulk

[
    {
        "text": "create campaign negative keyword example 1",
        "matchType": "EXACT"
    },
    {
        "text": "create campaign negative keyword example 2",
        "matchType": "BROAD"
    }
]
```

**Response**:

```json
[
  {
    "id": 542370642,
    "campaignId": 542370539,
    "adGroupId": 542317095,
    "text": "create campaign negative keyword example 1",
    "status": "ACTIVE",
    "matchType": "EXACT",
    "modificationTime": "2024-04-08T20:52:59.050",
    "deleted": false
  },
  {
    "id": 542370643,
    "campaignId": 542370539,
    "adGroupId": 542317095,
    "text": "create campaign negative keyword example 2",
    "status": "ACTIVE",
    "matchType": "BROAD",
    "modificationTime": "2024-04-08T20:52:59.054",
    "deleted": false
  }
]
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/bulk`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `[NegativeKeyword]`

The request body that includes negative keyword details.

## Responses

- `200` OK (`NegativeKeywordListResponse`, `application/json`): If the call succeeds, the API returns a list of [`NegativeKeyword`](./negativekeyword.md) objects in the response payload with an HTTP status code of `200` `(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`)
- `401` Unauthorized (`ApiErrorResponse`, `application/json`)
- `403` Forbidden (`ApiErrorResponse`, `application/json`)
- `404` Not Found (`ApiErrorResponse`, `application/json`)
- `429` (`ApiErrorResponse`, `application/json`)
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`)

## See Also

### Campaign Negative Keywords Endpoints
- [Find Campaign Negative Keywords](./find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](./get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](./get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](./update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](./delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-campaign-negative-keywords)*