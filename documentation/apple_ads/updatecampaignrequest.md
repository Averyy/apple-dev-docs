# UpdateCampaignRequest

**Framework**: Apple Ads  
**Kind**: dictionary

The payload properties to clear geotargeting from a campaign.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object UpdateCampaignRequest
```

## Properties

- `campaign` (CampaignUpdate): The campaign properties to update.
- `clearGeoTargetingOnCountryOrRegionChange` (boolean): The parameter to clear geotargeting from all ad groups in the campaign. To modify `countriesOrRegions` in a campaign, set the value of `clearGeoTargetingOnCountryOrRegionChange` to `true`. See the Payload Example: Update a Campaign with Countries or Regions in [`Update a Campaign`](update-a-campaign.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/updatecampaignrequest)*