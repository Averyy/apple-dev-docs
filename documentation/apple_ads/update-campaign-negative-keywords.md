# Update Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates negative keywords in a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update campaign negative keywords, use the associated `campaignId` in the URI. The `id` in the payload must belong to a negative keyword that exists inside the campaign in the URI. Use `PAUSED` or `ACTIVE` values to update the `status` field. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update Campaign Negative Keywords

## Request Body

The request body that includes negative keyword details.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Find Campaign Negative Keywords](find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-campaign-negative-keywords)*