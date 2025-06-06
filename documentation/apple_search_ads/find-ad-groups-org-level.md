# Find Ad Groups (org-level)

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches ad groups within an organization.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Search Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to find ad groups within your organization. Use a [`Selector`](selector.md) [`Condition`](condition.md) to narrow results. If you don’t specify selector conditions, all of your ad groups return in the API response. See the [`AdGroup`](adgroup.md) object for field descriptions and selector condition operators.

##### Payload Example Find Ad Groups Org Level

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create an Ad Group](create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/find-ad-groups-(org-level))*