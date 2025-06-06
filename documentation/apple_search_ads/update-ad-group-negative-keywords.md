# Update Ad Group Negative Keywords

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Updates negative keywords in an ad group.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update negative keywords, use the associated `campaignId` and `adgroupId` in the URI. The `id` in the payload must belong to a negative keyword that exists inside the ad group in the URI. Use `PAUSED` or `ACTIVE` values to update the `status` field. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [`Using Apple Search Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update Ad Group Negative Keywords

## Request Body

The request body that includes negative keyword details.

## See Also

- [Create Ad Group Negative Keywords](create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Find Ad Group Negative Keywords](find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get an Ad Group Negative Keyword](get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/update-ad-group-negative-keywords)*