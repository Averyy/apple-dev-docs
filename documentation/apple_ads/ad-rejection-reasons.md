# Ad Rejection Reasons

**Framework**: Apple Ads

Review reasons for an ad rejection.

#### Overview

Ads require approval by Apple. While in review, your [`Ad`](ad.md) is on hold. After approval, the [`AdServingStatus`](adservingstatus.md) changes to `RUNNING` unless you schedule it to start on a specific date or [`Update an Ad`](update-an-ad.md) status to `PAUSED` while in review.

> **Note**:  In [`4.9`](apple-search-ads-campaign-management-api-4#49.md) release, all previously rejected Today tab ad creatives were `PAUSED` and resubmitted for re-review. You need to update the status to `ENABLED` after the re-review. See [`Update an Ad`](update-an-ad.md).

Use [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md) or [`Get Ad Creative Rejection Reasons`](gets-a-product-page-reason.md) to look up rejection reasons. See [`ProductPageReason`](productpagereason.md) for rejection reason descriptions.

## Topics

### Ad Rejections
- [Find Ad Creative Rejection Reasons](find-ad-creative-rejection-reasons.md)
  Fetches ad creative rejection reasons.
- [Get Ad Creative Rejection Reasons](gets-a-product-page-reason.md)
  Fetches ad creative rejection reasons by custom product page ID.
- [Find App Assets](find-app-assets.md)
  Fetches app asset metadata by adam ID.
### Ad Rejection Reason Objects
- [object AppAsset](appasset.md)
  The app assets associated with an adam ID.
- [object AppAssetListResponse](appassetlistresponse.md)
  The response to a request that returns a list of app assets.
- [object ProductPageReason](productpagereason.md)
  The ad creative rejection reason based on a product page.
- [object ProductPageReasonListResponse](productpagereasonlistresponse.md)
  The response to a request that returns a list of product page rejection reasons.
- [object ProductPageReasonResponse](productpagereasonresponse.md)
  A container for product page reasons.
### Data Types
- [type ReasonLevel](reasonlevel.md)
  The level at which the system applies an ad rejection reason.

## See Also

- [Ads](ads.md)
  Assign an ad creative to an ad group.
- [Creatives](creatives.md)
  Create and manage ad creatives within your organization.
- [Custom Product Pages](custom-product-pages.md)
  View Custom Product Page details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/ad-rejection-reasons)*