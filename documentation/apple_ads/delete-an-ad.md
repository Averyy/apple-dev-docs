# Delete an Ad

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes an ad from an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use this endpoint to delete an [`Ad`](./ad.md) assignment from an ad group. Use your `adId` in the resource path.

## Endpoint

`DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/ads/{adId}`

## Parameters

### Path Parameters

- `adId` (int64) *(required)*: A unique identifier representing the assignment relationship between an ad group and an [`Ad`](./ad.md).
- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Responses

- `200` OK (`VoidResponse`, `application/json`): If the call succeeds, the API returns the [`VoidResponse`](./voidresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
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
- [Get All Ads](./get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](./update-an-ad.md)
  Updates an ad in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-an-ad)*