# Find Campaigns

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches campaigns with selector operators.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find campaigns using a [`Selector`](selector.md) [`Condition`](condition.md) to narrow results. If you don’t specify selector conditions, all campaign objects return in the response. See the [`Campaign`](campaign.md) object for parameter descriptions and selector condition operators.

##### Payload Example Find Campaigns

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create a Campaign](create-a-campaign.md)
  Creates a campaign to promote an app.
- [Get a Campaign](get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Get all Campaigns](get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Update a Campaign](update-a-campaign.md)
  Updates a campaign with a campaign identifier.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/find-campaigns)*