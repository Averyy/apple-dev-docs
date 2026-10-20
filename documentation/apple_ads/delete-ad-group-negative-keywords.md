# Delete Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes negative keywords from an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

To delete ad group negative keywords, include the associated `campaignId` and `adgroupId` in the URI. This is a soft deletion.

##### Payload example: Delete ad group negative keywords

**Request**:

```
POST https://api.searchads.apple.com/api/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/delete/bulk

[
    578054687,
    578054686,
    578054685
]
```

**Response**:

```json
{
    "data": 3,
    "pagination": null,
    "error": null
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/delete/bulk`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `[int64]`

The request body with negative jkeyword IDs.

## Responses

- `200` OK (`IntegerResponse`, `application/json`): If the call succeeds, the API returns the [`IntegerResponse`](./integerresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
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
- [Update Ad Group Negative Keywords](./update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-ad-group-negative-keywords)*