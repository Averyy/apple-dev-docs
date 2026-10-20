# Delete a Targeting Keyword

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes a targeting keyword in an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

To delete targeting keywords, include the associated `campaignId` and `adgroupId` in the URI with the `keywordId`. This is a soft deletion.

##### Payload example: Delete a targeting keyword

**Request**:

```
DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}
```

**Response**:

```json
{
    "data": 1,
    "pagination": null,
    "error": null
}

```

## Endpoint

`DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.
- `keywordId` (int64) *(required)*: The unique identifier for the keyword.

## Responses

- `200` OK (`VoidResponse`, `application/json`): If the call succeeds, the API returns a [`VoidResponse`](./voidresponse.md) payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
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
- [Get a Targeting Keyword in an Ad Group](./get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Get All Targeting Keywords in an Ad Group](./get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Update Targeting Keywords](./update-targeting-keywords.md)
  Updates targeting keywords in ad groups.
- [Delete Targeting Keywords](./delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-a-targeting-keyword)*