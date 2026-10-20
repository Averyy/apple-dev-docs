# CampaignCountryOrRegionsServingStateReasons

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

Reasons that displays when a campaign can’t run.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string CampaignCountryOrRegionsServingStateReasons
```

## Possible Values

- `APP_NOT_ELIGIBLE`: The app is not eligible in [App Store Connect](https://appstoreconnect.apple.com).
- `APP_NOT_ELIGIBLE_SEARCHADS`: The app is not eligible for Apple Ads.
- `APP_NOT_PUBLISHED_YET`: The app has not been published on the App Store.
- `SAPIN_LAW_AGENT_UNKNOWN`: An agency has not identified as an agency through their Apple Ads account.
- `SAPIN_LAW_FRENCH_BIZ_UNKNOWN`: An app is owned by a business that is headquartered or has a branch in France but has not self-identified as an agency in their Apple Ads account.
- `SAPIN_LAW_FRENCH_BIZ`: An app is owned by a business that is headquartered or has a branch in France and has self-identified as an agency in their Apple Ads account.
- `ACCOUNT_DOC_APPROVAL_EXPIRED`: The account’s business documents have expired.
- `ACCOUNT_DOC_APPROVAL_INFECTED`: The account’s business documents have been removed.
- `ACCOUNT_DOC_APPROVAL_NOT_SUBMITTED`: The account’s business documents have not been submitted.
- `ACCOUNT_DOC_APPROVAL_PENDING`: The account’s business documents approval is pending.
- `ACCOUNT_DOC_APPROVAL_REJECTED`: The account’s business documents approval has been rejected.
- `APP_CONTENT_REJECTED`: The app content approval has been rejected.
- `APP_CONTENT_REVIEW_PENDING`: The app’s content review is successful.
- `APP_DOC_APPROVAL_EXPIRED`: The app’s business documents expired.
- `APP_DOC_APPROVAL_INFECTED`: The app’s business documents have been removed.
- `APP_DOC_APPROVAL_NOT_SUBMITTED`: The app’s business documents require approval.
- `APP_DOC_APPROVAL_PENDING`: The app’s business documents approval is pending.
- `APP_DOC_APPROVAL_REJECTED`: The app’s business documents approval has been rejected.
- `APP_NOT_ELIGIBLE_SUPPLY_SOURCE`: The app is not eligible for promotion with the [`SupplySource`](./supplysource.md).
- `FEATURE_NOT_AVAILABLE_IN_COUNTRY_OR_REGION`: A feature is not available in a [`CountryOrRegion`](./countryorregion.md).

## See Also

### Data Types
- [type AdChannelType](./adchanneltype.md)
  The channel type of an ad in a campaign.
- [type BillingEventType](./billingeventtype.md)
  The type of billing event for a campaign.
- [type CampaignDisplayStatus](./campaigndisplaystatus.md)
  The status of the campaign.
- [type CampaignServingStateReasons](./campaignservingstatereasons.md)
  Reasons the system provides when a campaign can’t run.
- [type CampaignServingStatus](./campaignservingstatus.md)
  The status of the campaign.
- [type CampaignStatus](./campaignstatus.md)
  The status of the campaign.
- [type PaymentModel](./paymentmodel.md)
  The payment model that you set.
- [type SupplySource](./supplysource.md)
  The ad placements for a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/campaigncountryorregionsservingstatereasons)*