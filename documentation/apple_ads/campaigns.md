# Campaigns

**Framework**: Apple Ads

Create and manage Apple Ads campaigns.

#### Overview

You use campaigns to promote your apps in the App Store. For an app to be eligible for Apple Ads in a particular market, it must be available for purchase, download, or preorder in the App Store, and Apple Ads must be available in the countries and regions you want to promote to. There may be some restrictions that make your app ineligible for Apple Ads advertising in some markets. Use [`Find App Eligibility Records`](find-app-eligibility-records.md) to determine your app eligibility to run in campaigns.

You must have an `adamId` for each app you’re promoting, a valid email address, and an Apple ID. Apple IDs that only use phone numbers aren’t acceptable. All advertisers must comply with [`Apple Ads Advertising Content Policies`](https://developer.apple.comhttps://ads.apple.com/policies).

## Topics

### Campaign Endpoints
- [Create a Campaign](create-a-campaign.md)
  Creates a campaign to promote an app.
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
### Campaign Request and Response Objects
- [object Campaign](campaign.md)
  The response to a request to create and fetch campaigns.
- [object CampaignResponse](campaignresponse.md)
  A container for the campaign response body.
- [object Campaign.CountryOrRegionServingStateReasons](campaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons why a campaign can’t run.
- [object CampaignListResponse](campaignlistresponse.md)
  The response details of campaign requests.
- [object CampaignUpdate](campaignupdate.md)
  The list of campaign fields that are updatable.
- [object UpdateCampaignRequest](updatecampaignrequest.md)
  The payload properties to clear geotargeting from a campaign.
### Data Types
- [type AdChannelType](adchanneltype.md)
  The channel type of an ad in a campaign.
- [type BillingEventType](billingeventtype.md)
  The type of billing event for a campaign.
- [type CampaignCountryOrRegionsServingStateReasons](campaigncountryorregionsservingstatereasons.md)
  Reasons that displays when a campaign can’t run.
- [type CampaignDisplayStatus](campaigndisplaystatus.md)
  The status of the campaign.
- [type CampaignServingStateReasons](campaignservingstatereasons.md)
  Reasons the system provides when a campaign can’t run.
- [type CampaignServingStatus](campaignservingstatus.md)
  The status of the campaign.
- [type CampaignStatus](campaignstatus.md)
  The status of the campaign.
- [type PaymentModel](paymentmodel.md)
  The payment model that you set.
- [type SupplySource](supplysource.md)
  The ad placements for a campaign.

## See Also

- [Budget Orders](budget-orders.md)
  Manage your payment model.
- [Ad Groups](ad-groups.md)
  Create and manage ad groups.
- [Targeting Keywords and Negative Keywords](targeting-keywords-and-negative-keywords.md)
  Apply relevant words or phrases that make your campaigns findable.
- [Search Geolocations](search-geolocations.md)
  Search for apps and geocriteria for your campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/campaigns)*