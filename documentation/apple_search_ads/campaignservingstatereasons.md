# CampaignServingStateReasons

**Framework**: Apple Search Ads  
**Kind**: typealias

Reasons the system provides when a campaign can’t run.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
string CampaignServingStateReasons
```

#### Discussion

Ad creatives in campaigns with an `APPSTORE_TODAY_TAB` [`SupplySource`](supplysource.md) receive a review from Apple for compliance.  Ads that are pending review are on hold until Apple completes the review. The system doesn’t serve rejected ads.

## See Also

- [type AdChannelType](adchanneltype.md)
  The channel type of an ad in a campaign.
- [type BillingEventType](billingeventtype.md)
  The type of billing event for a campaign.
- [type CampaignCountryOrRegionsServingStateReasons](campaigncountryorregionsservingstatereasons.md)
  Reasons that displays when a campaign can’t run.
- [type CampaignDisplayStatus](campaigndisplaystatus.md)
  The status of the campaign.
- [type CampaignServingStatus](campaignservingstatus.md)
  The status of the campaign.
- [type CampaignStatus](campaignstatus.md)
  The status of the campaign.
- [type PaymentModel](paymentmodel.md)
  The payment model that you set.
- [type SupplySource](supplysource.md)
  The ad placements for a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/campaignservingstatereasons)*