# Get all Campaigns

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches all of an organization’s assigned campaigns.

**Availability**:
- Search Ads 5.0+

#### Discussion

This endpoint returns data for all of an organization’s assigned campaigns. You can also use a partial fetch as necessary. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns`

## Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

## See Also

- [Create a Campaign](create-a-campaign.md)
  Creates a campaign to promote an app.
- [Find Campaigns](find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get a Campaign](get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Update a Campaign](update-a-campaign.md)
  Updates a campaign with a campaign identifier.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-campaigns)*