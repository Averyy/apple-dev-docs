# Find Ads

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Finds ads within a campaign by selector criteria.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find `ads` within campaigns using a [`Selector`](selector.md) [`Condition`](condition.md) to filter results. If you don’t specify selector conditions, all [`Ad`](ad.md) objects return in the response. See the [`Ad`](ad.md) object for parameter descriptions and selector condition operators.

##### Payload Example Find Ads

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads (org-level)](find-ads-(org-level).md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/find-ads)*