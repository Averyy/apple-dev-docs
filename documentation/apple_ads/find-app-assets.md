# Find App Assets

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches app asset metadata by adam ID.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint with [`Selector`](selector.md) to find app asset metadata associated with an `adamId`. Use your `adamId` in the resource path. See the [`AppAsset`](appasset.md) object for parameter descriptions and selector condition operators.

This endpoint supports default and custom product page ads.

##### Payload Example Find App Assets

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Find Ad Creative Rejection Reasons](find-ad-creative-rejection-reasons.md)
  Fetches ad creative rejection reasons.
- [Get Ad Creative Rejection Reasons](gets-a-product-page-reason.md)
  Fetches ad creative rejection reasons by custom product page ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-app-assets)*