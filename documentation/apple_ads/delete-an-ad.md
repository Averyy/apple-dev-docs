# Delete an Ad

**Framework**: Apple Ads  
**Kind**: httpRequest

Deletes an ad from an ad group.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to delete an [`Ad`](ad.md) assignment from an ad group. Use your `adId` in the resource path.

## Endpoint

`DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/ads/{adId}`

## Parameters

- `adId` (int64) *(required)*: A unique identifier representing the assignment relationship between an ad group and an [`Ad`](ad.md).
- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## See Also

- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads](find-ads.md)
  Finds ads within a campaign by selector criteria.
- [Find Ads (org-level)](find-ads-(org-level).md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](update-an-ad.md)
  Updates an ad in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-an-ad)*