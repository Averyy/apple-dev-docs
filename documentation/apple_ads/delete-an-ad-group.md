# Delete an Ad Group

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes an ad group with a campaign and ad group identifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Endpoint

`DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Responses

- `200` OK (`VoidResponse`, `application/json`): If the call succeeds, the API returns the [`AdGroup`](./adgroup.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
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
- [Find Ad Groups](./find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](./find-ad-groups-%28org-level%29.md)
  Fetches ad groups within an organization.
- [Get an Ad Group](./get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](./get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](./update-an-ad-group.md)
  Updates an ad group with an ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-an-ad-group)*