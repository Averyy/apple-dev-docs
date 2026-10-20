# Get All Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches all negative keywords in a campaign.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

To return all campaign negative keywords, use the associated `campaignId` in the URI. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [Using Apple Ads API Functionality](./using-apple-search-ads-api-functionality.md).

##### Payload example: Get all campaign negative keywords

**Request**:

```
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords
```

**Response**:

```json
[
        {
            "id": 542370642,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 1",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "modificationTime": "2024-04-08T17:48:31.979",
            "deleted": false
        },
        {
            "id": 542370643,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 2",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "modificationTime": "2024-04-08T17:48:31.984",
            "deleted": false
        },
        {
            "id": 542370644,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 3",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "modificationTime": "2024-04-08T20:52:59.050",
            "deleted": false
        },
        {
            "id": 542370645,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 4",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "modificationTime": "2024-04-08T20:52:59.054",
            "deleted": false
        }
    ]
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

### Query Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.

  **Default**: `20`
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

  **Default**: `0`

## Responses

- `200` OK (`NegativeKeywordListResponse`, `application/json`): If the call succeeds, the API returns a list of [`NegativeKeyword`](./negativekeyword.md) objects in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Campaign Negative Keywords Endpoints
- [Create Campaign Negative Keywords](./create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Find Campaign Negative Keywords](./find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](./get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Update Campaign Negative Keywords](./update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](./delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-campaign-negative-keywords)*