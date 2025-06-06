# Find Campaign Negative Keywords

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches negative keywords for campaigns.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find campaign negative keywords. Use the associated `campaignId` in the URI. Find calls use [`Selector`](selector.md) [`Condition`](condition.md) operators to narrow results. If you don’t specify any selector conditions, all negative keywords in the campaign return in the response. See the [`NegativeKeyword`](negativekeyword.md) object for details about selector [`Condition`](condition.md) operators per field.

##### Payload Example Find Campaign Negative Keywords

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/find-campaign-negative-keywords)*