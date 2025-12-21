# Create a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates a campaign to promote an app.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Essential points for creating campaigns are:

- Use [`Search for iOS apps`](search-for-ios-apps.md) to retrieve your `adamId` to use in the request payload.
- Use [`Find App Eligibility Records`](find-app-eligibility-records.md) to determine your app eligibility to run in campaigns.
- A `dailyBudgetAmount` is a required field to manage the daily budget of your campaigns. Use an optional `budgetAmount` to manage your campaign’s total budget. You can only add a `budgetAmount` using the Create a Campaign endpoint. You can’t update a campaign to use a `budgetAmount`.
- Use the `countriesOrRegions` attribute to assign App Store locations. To advertise in multiple markets, group countries and regions into a single campaign using ISO alpha-2 country code values.
- See the [`Campaign`](campaign.md) object and [`SupplySource`](supplysource.md) for descriptions of attributes.

After creating a campaign, set up [`Ad Groups`](ad-groups.md).

##### Payload Example Create a Campaign

## Request Body

The request body that includes the details of the campaign.

## See Also

- [Find Campaigns](find-campaigns.md)
  Fetches campaigns with selector operators.
- [Get a Campaign](get-a-campaign.md)
  Fetches a specific campaign by campaign identifier.
- [Get all Campaigns](get-all-campaigns.md)
  Fetches all of an organization’s assigned campaigns.
- [Update a Campaign](update-a-campaign.md)
  Updates a campaign with a campaign identifier.
- [Delete a Campaign](delete-a-campaign.md)
  Deletes a specific campaign by campaign identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-a-campaign)*