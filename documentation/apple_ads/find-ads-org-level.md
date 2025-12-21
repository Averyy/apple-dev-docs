# Find Ads (org-level)

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches ads within an organization by selector criteria.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to find `ads` within your organization using a [`Selector`](selector.md) [`Condition`](condition.md) to narrow results. If you don’t specify selector conditions, all [`Ad`](ad.md) objects return in the response. See the [`Ad`](ad.md) object for parameter descriptions and selector condition operators.

##### Payload Example Find Ads Org Level

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads](find-ads.md)
  Finds ads within a campaign by selector criteria.
- [Get an Ad](get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ads-(org-level))*