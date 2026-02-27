# CampaignResponse

**Framework**: Apple Ads  
**Kind**: dictionary

A container for the campaign response body.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object CampaignResponse
```

## Properties

- `data` (Campaign): Response data that the API provides.
- `error` (ErrorResponseBody): Error response data that the API provides.
- `pagination` (PageDetail): Page detail information that the API provides.

## See Also

- [object Campaign](campaign.md)
  The response to a request to create and fetch campaigns.
- [object Campaign.CountryOrRegionServingStateReasons](campaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons why a campaign can’t run.
- [object CampaignListResponse](campaignlistresponse.md)
  The response details of campaign requests.
- [object CampaignUpdate](campaignupdate.md)
  The list of campaign fields that are updatable.
- [object UpdateCampaignRequest](updatecampaignrequest.md)
  The payload properties to clear geotargeting from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/campaignresponse)*