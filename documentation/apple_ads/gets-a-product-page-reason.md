# Get Ad Creative Rejection Reasons

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches ad creative rejection reasons by custom product page ID.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to fetch rejected ad creative approval reason details. Use the `id` that returns in `ProductPageReason` in the resource path as your `productPageReasonId`. See the [`ProductPageReason`](productpagereason.md) object for rejection reason code enumerations, parameter descriptions, and selector condition operators.

##### Payload Example Get Rejection Reasons

## See Also

- [Find Ad Creative Rejection Reasons](find-ad-creative-rejection-reasons.md)
  Fetches ad creative rejection reasons.
- [Find App Assets](find-app-assets.md)
  Fetches app asset metadata by adam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/gets-a-product-page-reason)*