# Get All Ads

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches all ads assigned to an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

Use this endpoint to fetch all `ads` assigned to an ad group.

### Payload example: Get all ads

**Request**:

```
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/ads
```

**Response**:

```json
{
    "id": 573408745,
    "orgId": 39872140,
    "campaignId": 570798765,
    "adGroupId": 570798765,
    "creativeId": 94895512,
    "name": "Trip Trek custom product page variation",
    "creativeType": "CUSTOM_PRODUCT_PAGE",
    "status": "PAUSED",
    "servingStatus": "NOT_RUNNING",
    "servingStateReasons": [
      "PAUSED_BY_USER"
      ],
    "deleted": false,
    "creationTime": "2024-10-08T00:18:37.606Z",
    "modificationTime": "2024-10-09T00:18:37.606Z"
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/ads`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Responses

- `200` OK (`AdListResponse`, `application/json`): If the call succeeds, the API returns the [`AdListResponse`](./adlistresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Endpoints
- [Create an Ad](./create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads](./find-ads.md)
  Finds ads within a campaign by selector criteria.
- [Find Ads (org-level)](./find-ads-%28org-level%29.md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](./get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Update an Ad](./update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](./delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-ads)*