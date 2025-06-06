# Find Ad Group Negative Keywords

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches negative keywords in a campaign’s ad groups.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find negative keywords in different ad groups within the same campaign. Use the associated `campaignId` in the URI. Find calls use [`Selector`](selector.md) [`Condition`](condition.md) operators to narrow results. If you don’t specify any selector conditions, the API returns all negative keywords across all ad groups of the campaign. See the [`NegativeKeyword`](negativekeyword.md) object for details about [`Selector`](selector.md) `condition` operators per field.

##### Payload Example Find Ad Group Negative Neywords

## Request Body

[`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create Ad Group Negative Keywords](create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Get an Ad Group Negative Keyword](get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Update Ad Group Negative Keywords](update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/find-ad-group-negative-keywords)*