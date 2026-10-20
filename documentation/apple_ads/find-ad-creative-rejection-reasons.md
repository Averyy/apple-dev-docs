# Find Ad Creative Rejection Reasons

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches ad creative rejection reasons.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to find rejected approval reasons for ad creatives based on default or custom product page. See the [`ProductPageReason`](./productpagereason.md) object for rejection reason code enumerations, parameter descriptions, and [`Selector`](./selector.md) condition operators.

##### Payload example 1: Find ad creative rejection reasons

**Request**:

```
POST https://api.searchads.apple.com/api/v5/product-page-reasons/find

{
  "conditions": [
    {
      "field": "supplySources",
      "operator": "equals",
      "values": [
        "APPSTORE_TODAY_TAB"
      ]
    },
    {
      "field": "countriesOrRegions",
      "operator": "IN",
      "values": [
        "US"
      ]
    },
    {
      "field": "productPageId",
      "operator": "IN",
      "values": [
        "59f4948c-3726-4cfc-8915-6b09afb36d83",
        "0349277e-32f8-436b-980a-258c3aabf0ad"
      ]
    },
    {
      "orderBy": [
        {
          "field": "productPageId",
          "sortOrder": "ASCENDING"
        }
      ]
    }
  ]
}
```

**Response**:

```json
{
  "data": [
    {
      "id": 4567890421,
      "adamId": 144714574,
      "productPageId": "59f4948c-3726-4cfc-8915-6b09afb36d83",
      "assetGenId": "368234568;en-US;9;0;4201c5a4bd4087cc82xdfetdc8141b94d0",
      "supplySource": "APPSTORE_TODAY_TAB",
      "countryOrRegion": "US",
      "languageCode": "en-US",
      "reasonType": "REJECTION_REASON",
      "reasonCode": "SUBTITLE_LANGUAGE_CONFLICT",
      "reasonLevel": "CUSTOM_PRODUCT_PAGE_LOCALE",
      "comment": "Custom comment for rejection."
    },
    {
      "id": 4837240452,
      "adamId": 144714574,
      "productPageId": "0349277e-32f8-436b-980a-258c3aabf0ad",
      "assetGenId": "835599320;en-AU;9;0;dbac55b222a61e1939f19f2640e48dfa",
      "supplySource": "APPSTORE_TODAY_TAB",
      "countryOrRegion": "US",
      "languageCode": "en-US",
      "reasonType": "APP_NAME_LANGUAGE_CONFLICT",
      "reasonCode": "CUSTOM_PRODUCT_PAGE_LOCALE",
      "comment": "Custom comment for rejection."
    }
  ],
  "pagination": {
    "totalResults": 2,
    "startIndex": 0,
    "itemsPerPage": 10
  }
}

```

##### Payload example 2: Find ad creative rejection reasons

**Request**:

```
HTTP POST https://api.searchads.apple.com/api/v5/product-page-reasons/find

{
  "conditions": [
    {
      "field": "adamId",
      "operator": "equals",
      "values": [
        "735599345"
      ]
    },

      "orderBy": [
        {
          "field": "productPageId",
          "sortOrder": "ASCENDING"
        }
      ]
    }
  ]
}

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
    "languageCode": "en-US",
    "reasonType": "REJECTION_REASON",
    "reasonCode": "APP_NAME_LANGUAGE_CONFLICT",
    "reasonLevel": "CUSTOM_PRODUCT_PAGE_LOCALE",
    "comment”: "Custom comment for rejection."
  }
}

```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/product-page-reasons/find`

## Request Body

**Content-Type**: `application/json`  
**Type**: `Selector`

The request body that includes the selector [`Condition`](./condition.md). [`Selector`](./selector.md) objects define what data the API returns when fetching resources.

## Responses

- `200` OK (`ProductPageReasonListResponse`, `application/json`): If the call succeeds, the API returns the [`ProductPageReasonListResponse`](./productpagereasonlistresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Rejections
- [Get Ad Creative Rejection Reasons](./gets-a-product-page-reason.md)
  Fetches ad creative rejection reasons by custom product page ID.
- [Find App Assets](./find-app-assets.md)
  Fetches app asset metadata by adam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ad-creative-rejection-reasons)*