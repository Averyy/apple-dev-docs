# Delete a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes a specific campaign by campaign identifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Endpoint

`DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Responses

- `200` OK (`VoidResponse`, `application/json`): If the call succeeds, the API returns the [`Campaign`](./campaign.md) objects in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Campaign Endpoints
- [Create a Campaign](./create-a-campaign.md)
  Creates a campaign to promote an app.
- [Find Campaigns](./find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get a Campaign](./get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Get all Campaigns](./get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Update a Campaign](./update-a-campaign.md)
  Updates a campaign with a campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-a-campaign)*