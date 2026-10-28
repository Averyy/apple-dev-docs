# Update Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Updates negative keywords in an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

To update negative keywords, use the associated `campaignId` and `adgroupId` in the URI. The `id` in the payload must belong to a negative keyword that exists inside the ad group in the URI. Use `PAUSED` or `ACTIVE` values to update the `status` field. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [Using Apple Ads API Functionality](./using-apple-search-ads-api-functionality.md).

### Payload example: Update ad group negative keywords

**Request**:

```
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk

[
  {
    "id": "12345678",
    "status": "PAUSED"
  },
  {
    "id": "12345679",
    "status": "PAUSED"
  }
]

```

**Response**:

```json
[
  {
    "id": 12345678,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "Update ad group negative keyword example 1",
    "status": "PAUSED",
    "matchType": "BROAD",
    "modificationTime": "2024-04-08T22:08:42.618",
    "deleted": false
  },
  {
    "id": 12345679,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "Update ad group negative keyword example 2",
    "status": "PAUSED",
    "matchType": "EXACT",
    "modificationTime": "2024-04-08T22:08:42.618",
    "deleted": false
  }
]
```

## Endpoint

`PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `[NegativeKeyword]`

The request body that includes negative keyword details.

## Responses

- `200` OK (`NegativeKeywordListResponse`, `application/json`): If the call succeeds, the API returns a list of [`NegativeKeyword`](./negativekeyword.md) objects in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Group Negative Keywords Endpoints
- [Create Ad Group Negative Keywords](./create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Find Ad Group Negative Keywords](./find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get an Ad Group Negative Keyword](./get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](./get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Delete Ad Group Negative Keywords](./delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-ad-group-negative-keywords)*