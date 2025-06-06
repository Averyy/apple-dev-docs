# Ad Groups

**Framework**: Apple Search Ads

Create and manage ad groups.

#### Overview

An ad group is a collection of criteria that defines who sees your ad in App Store search results. A basic ad group includes a `startTime`, `endTime`, and `dailyBudgetAmount`. You can add bid amounts, [`TargetingDimensions`](targetingdimensions.md), and [`Targeting Keywords and Negative Keywords`](targeting-keywords-and-negative-keywords.md). Use the [`Search for Geolocations`](search-for-geolocations.md) endpoint to find localities to use for targeting dimensions within ad groups.

##### Build a Campaign Keywords Strategy

When building a campaign promotion strategy, you define keywords relevant to your app and bid on them. Relevant keywords increase the viability of your app to rank high in user searches. You can either automate your keyword and bid strategy by using the Search Match feature, or use your own keywords and bid strategy.

The Search Match feature is an algorithm that uses multiple resources to match your ad to relevant searches in the App Store. The resources include metadata from your App Store product page, information about similar apps in the same genre, and other available search data. Search Match is a good option if you don’t want to figure out all keyword possibilities and actively bid on them.

![Keyword app search example](https://docs-assets.developer.apple.com/published/fa3e1fc5987e946aefdab9346c4cf657/media-3341277%402x.png)

##### Enable and Disable Search Match

To enable Search Match, use [`Create an Ad Group`](create-an-ad-group.md) or [`Update an Ad Group`](update-an-ad-group.md) endpoints to perform the following steps:

1. Set `automatedKeywordsOptIn: true`.
2. Set the required field `defaultBidAmount`.

If you’re using your own keywords and bid strategy, disable Search Match using [`Create an Ad Group`](create-an-ad-group.md) or [`Update an Ad Group`](update-an-ad-group.md) endpoints using the following steps:

1. Set `automatedKeywordsOptIn: false`.
2. Set the required field `defaultBidAmount`.
3. Use the `bidAmount` field in `Create Targeting Keywords` and `Update Targeting Keywords` endpoints to set a threshold price for a keyword in a bidding auction.

> ❗ **Important**:  If you don’t provide a `bidAmount`, the `bidAmount` uses the `defaultBidamount` of the corresponding ad group.

 If you don’t provide a `bidAmount`, the `bidAmount` uses the `defaultBidamount` of the corresponding ad group.

## Topics

### Ad Group Endpoints
- [Create an Ad Group](create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](find-ad-groups-(org-level).md)
  Fetches ad groups within an organization.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.
### Ad Group Request and Response Objects
- [object AdGroup](adgroup.md)
  The response to ad group requests.
- [object AdGroupUpdate](adgroupupdate.md)
  The response to ad group update requests.
- [object AdGroupResponse](adgroupresponse.md)
  A container for the ad group response body.
- [object AdGroupListResponse](adgrouplistresponse.md)
  The response details of ad group requests.
### Audience Refinement
- [object TargetingDimensions](targetingdimensions.md)
  The optional criteria to use with ad groups to narrow the audience that views your ads.
- [object AppCategoryCriteria](appcategorycriteria.md)
  The defined target audience by app category.
- [object AppDownloaderCriteria](appdownloadercriteria.md)
  The defined targeted audience according to app downloads.
- [object AdminAreaCriteria](adminareacriteria.md)
  The defined targeted audience by administrative area.
- [object CountryCriteria](countrycriteria.md)
  The defined targeted audience by country or region.
- [object LocalityCriteria](localitycriteria.md)
  The defined targeted audience by locality.
- [object AgeCriteria](agecriteria.md)
  The defined targeted audience to include using the age demographic.
- [object AgeRange](agerange.md)
  The defined target audience to include using the age-range demographic.
- [object DaypartCriteria](daypartcriteria.md)
  The defined targeted audience to include for a specific time of day.
- [object DaypartDetail](daypartdetail.md)
  The defined targeted audience to include by a specific time of day.
- [object DeviceClassCriteria](deviceclasscriteria.md)
  The defined targeted audience to include by device type.
- [object GenderCriteria](gendercriteria.md)
  The defined targeted audience to include using the gender demographic.
### Data Types
- [type AdGroupDisplayStatus](adgroupdisplaystatus.md)
  The status of the ad group.
- [type AdGroupServingStateReasons](adgroupservingstatereasons.md)
  A list of reasons that displays when an ad group isn’t running.
- [type AdGroupServingStatus](adgroupservingstatus.md)
  The status of whether the ad group is serving.
- [type AdGroupStatus](adgroupstatus.md)
  The status of whether the ad group is enabled or not.
- [type DeviceClass](deviceclass.md)
  The defined targeted audience to include by device type.
- [type Gender](gender.md)
  The defined targeted audience in a campaign.
- [type PricingModel](pricingmodel.md)
  The type of pricing model for a bid.

## See Also

- [Campaigns](campaigns.md)
  Create and manage Search Ads campaigns.
- [Budget Orders](budget-orders.md)
  Manage your payment model.
- [Targeting Keywords and Negative Keywords](targeting-keywords-and-negative-keywords.md)
  Apply relevant words or phrases that make your campaigns findable.
- [Search Geolocations](search-geolocations.md)
  Search for apps and geocriteria for your campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/ad-groups)*