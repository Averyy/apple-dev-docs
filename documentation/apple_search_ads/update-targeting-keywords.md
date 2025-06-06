# Update Targeting Keywords

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Updates targeting keywords in ad groups.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update targeting keywords, use the associated `campaignId` and `adgroupId` in the URI. The `id` in the payload must belong to a keyword that exists inside the ad group in the URI. The `status` and `bidAmount` fields are modifiable in the payload. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [`Using Apple Search Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update Ad Group Targeting Keywords

## Request Body

The request body that includes keyword targeting details.

## See Also

- [Create Targeting Keywords](create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
- [Find Targeting Keywords in a Campaign](find-targeting-keywords-in-a-campaign.md)
  Fetches targeting keywords in a campaign’s ad groups.
- [Get a Targeting Keyword in an Ad Group](get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Get All Targeting Keywords in an Ad Group](get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Delete Targeting Keywords](delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/update-targeting-keywords)*