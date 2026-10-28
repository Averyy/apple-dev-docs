# Get all Ad Groups

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches all ad groups with a campaign identifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

To return all ad groups, use the associated `campaignId` and `adgroupId` in the URI path. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [Using Apple Ads API Functionality](./using-apple-search-ads-api-functionality.md).

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

### Query Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.

  **Default**: `20`
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

  **Default**: `0`

## Responses

- `200` OK (`AdGroupListResponse`, `application/json`): If the call succeeds, the API returns the [`AdGroup`](./adgroup.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
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
- [Update an Ad Group](./update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](./delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-ad-groups)*