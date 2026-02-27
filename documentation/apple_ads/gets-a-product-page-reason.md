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

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/product-page-reasons/{productPageReasonId}
```

**Response**:

```json
{
  "data": {
    "id": "135366",
    "adamId": 735599345,
    "productPageId": "68e5948c-3726-4cfc-8915-6b09afb36d83",
    "assetGenId": "735599345;en-US;9;0;4201c5a4bd4087cc82xdfetdc8141b94d0",
    "supplySource": "APPSTORE_TODAY_TAB",
    "countryOrRegion": "US",
    "languageCode": “en-US”,
    "reasonType": "APP_NAME_LANGUAGE_CONFLICT",
    "reasonCode": "SUBTITLE_LANGUAGE_CONFLICT",
    "comment": null
  }
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/product-page-reasons/{productPageReasonId}`

## Parameters

- `productPageReasonId` (int64) *(required)*: A unique identifier for a custom product page with an associated ad creative rejection reason.

## See Also

- [Find Ad Creative Rejection Reasons](find-ad-creative-rejection-reasons.md)
  Fetches ad creative rejection reasons.
- [Find App Assets](find-app-assets.md)
  Fetches app asset metadata by adam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/gets-a-product-page-reason)*