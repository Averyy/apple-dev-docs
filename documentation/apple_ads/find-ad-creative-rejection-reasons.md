# Find Ad Creative Rejection Reasons

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches ad creative rejection reasons.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to find rejected approval reasons for ad creatives based on default or custom product page. See the [`ProductPageReason`](productpagereason.md) object for rejection reason code enumerations, parameter descriptions, and [`Selector`](selector.md) condition operators.

##### Payload Example 1 Find Ad Creative Rejection Reasons

##### Payload Example 2 Find Ad Creative Rejection Reasons

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Get Ad Creative Rejection Reasons](gets-a-product-page-reason.md)
  Fetches ad creative rejection reasons by custom product page ID.
- [Find App Assets](find-app-assets.md)
  Fetches app asset metadata by adam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ad-creative-rejection-reasons)*