# Create Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Creates negative keywords in a specific ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

Negative keywords prevent your ad from showing up in App Store searches. Negative keywords can belong to a campaign or an ad group.

To create ad group negative keywords, use the associated `campaignId` and `adgroupId` in the URI.

### Payload example: Create ad group negative keywords

**Request**:

```
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk

[  
 {
    "text": "ad group negative keyword 1",
    "matchType": "BROAD"
  },
  {
    "text": "ad group negative keyword 2",
    "matchType": "EXACT"
  }
]

```

**Response**:

```json
[
  {
    "id": 542370642,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "ad group negative keyword example 1",
    "status": "ACTIVE",
    "matchType": "BROAD",
    "modificationTime": "2024-04-08T22:02:07.514",
    "deleted": false
  },
  {
    "id": 542370643,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "Update campaign negative keyword example 2",
    "status": "ACTIVE",
    "matchType": "EXACT",
    "modificationTime": "2024-04-08T22:02:07.523",
    "deleted": false
  }
]
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `[NegativeKeyword]`

The request body that includes negative keyword details.

## Responses

- `200` OK (`NegativeKeywordListResponse`, `application/json`): If the call succeeds, the API returns a list of [`NegativeKeyword`](./negativekeyword.md) objects in the response payload with an HTTP status code of `200` `(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.

  > **Note**:  If you create duplicate keywords, the payload response indicates an error, but the call returns with a 200 status code.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Group Negative Keywords Endpoints
- [Find Ad Group Negative Keywords](./find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get an Ad Group Negative Keyword](./get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](./get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Update Ad Group Negative Keywords](./update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.
- [Delete Ad Group Negative Keywords](./delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-ad-group-negative-keywords)*