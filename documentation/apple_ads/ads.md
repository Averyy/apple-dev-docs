# Ads

**Framework**: Apple Ads

Assign an ad creative to an ad group.

#### Overview

You use an [`Ad`](ad.md) object to assign an ad creative to an ad group. You can assign one active ad per ad group. See also [`Ad Rejection Reasons`](ad-rejection-reasons.md).

## Topics

### Ad Endpoints
- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads](find-ads.md)
  Finds ads within a campaign by selector criteria.
- [Find Ads (org-level)](find-ads-(org-level).md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](delete-an-ad.md)
  Deletes an ad from an ad group.
### Ad Request and Response Objects
- [object Ad](ad.md)
  The assignment of a creative to an ad group.
- [object AdCreate](adcreate.md)
  The request to create an ad, and assign a creative to an ad group.
- [object AdUpdate](adupdate.md)
  The request to update an ad.
- [object AdResponse](adresponse.md)
  The response to an ad request.
- [object AdListResponse](adlistresponse.md)
  The response to a request that returns a list of ads.
### Data Types
- [type AdServingStateReasons](adservingstatereasons.md)
  Reasons the system provides when an ad isn’t running.
- [type AdStatus](adstatus.md)
  The user-controlled status of the ad.
- [type AdServingStatus](adservingstatus.md)
  The status of whether the ad is serving.

## See Also

- [Ad Rejection Reasons](ad-rejection-reasons.md)
  Review reasons for an ad rejection.
- [Creatives](creatives.md)
  Create and manage ad creatives within your organization.
- [Custom Product Pages](custom-product-pages.md)
  View Custom Product Page details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/ads)*