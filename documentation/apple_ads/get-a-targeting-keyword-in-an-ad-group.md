# Get a Targeting Keyword in an Ad Group

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches a specific targeting keyword in an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

To return a specific targeting keyword, use the associated `campaignId`, `adgroupId`, and `keywordId` in the URI. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [Using Apple Ads API Functionality](./using-apple-search-ads-api-functionality.md).

### Payload example: Get a targeting keyword in an ad group

**Request**:

```
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}
```

**Response**:

```json
{  
  "id": 542370642,
  "adGroupId": 427916203,
  "text": "targeting keyword example 1",
  "status": "ACTIVE",
  "matchType": "BROAD",
  "bidAmount": {
    "amount": "100",
    "currency": "USD"
  },
  "modificationTime": "2025-04-08T20:48:28.206",
  "deleted": false
}
```

### Payload example: Get a targeting keyword in an ad group in a Maximize Conversions campaign

**Request**:

```
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}
```

**Response**:

```json
{
  "id": 542370642,
  "campaignId": 585885088,
  "adGroupId": 542370539,
  "text": "food delivery",
  "status": "ACTIVE",
  "matchType": "BROAD",
  "bidAmount": {
    "amount": "0",
    "currency": "USD"
  }
  ...
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.
- `keywordId` (int64) *(required)*: The unique identifier for the keyword.

## Responses

- `200` OK (`KeywordResponse`, `application/json`): If the call succeeds, the API returns the [`Keyword`](./keyword.md) object in the response payload with an HTTP status code of `200` `(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Group Targeting Keywords Endpoints
- [Create Targeting Keywords](./create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
- [Find Targeting Keywords in a Campaign](./find-targeting-keywords-in-a-campaign.md)
  Fetches targeting keywords in a campaign’s ad groups.
- [Get All Targeting Keywords in an Ad Group](./get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Update Targeting Keywords](./update-targeting-keywords.md)
  Updates targeting keywords in ad groups.
- [Delete Targeting Keywords](./delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](./delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-targeting-keyword-in-an-ad-group)*