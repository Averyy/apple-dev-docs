# Update a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates a campaign with a campaign identifier.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to update countries or regions (App Store geolocations) where you promote your app, and to set your campaign budget. Use the associated `campaignId` in the URI.

To edit a subset of object properties without having to include all object properties in the payload, use partial updates. Use a campaign object envelope in your campaign update request payloads. Other objects don’t require a JSON envelope. See the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update a Campaign

##### Payload Example Update a Campaign Budget Amount or Daily Budget Amount

##### Payload Example Update a Campaign with Countries or Regions

## Request Body

The request body that includes the details of the  campaign.

## See Also

- [Create a Campaign](create-a-campaign.md)
  Creates a campaign to promote an app.
- [Find Campaigns](find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get a Campaign](get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Get all Campaigns](get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-a-campaign)*