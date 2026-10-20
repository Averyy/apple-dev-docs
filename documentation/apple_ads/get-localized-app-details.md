# Get Localized App Details

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches the localized default product page for an app.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to return localized app details using your `adamId` in the resource path. Related objects: [`MediaLocaleDetail`](./medialocaledetail.md), [`MediaLocaleDetailResponse`](./medialocaledetailresponse.md).

##### Query Parameters

- expand: Detailed app asset details of a device. Use `true` for expanded values in the API response.

##### Get localized app details example

**Request**:

```
GET https://api.searchads.apple.com/api/v5/apps/{adamId}/locale-details        
```

**Response**:

```json
{
  "data": [
    {
      "language": "en-US",
      "appName": "Trip Trek",
      "shortDescription": "Trip Trek app.",
      "isPrimaryLocale": true,
      "subTitle": "Search for trips.",
      "appPreviewDeviceWithAssets": {
        "ipadPro": {
          "appPreviewDeviceFallBackDevices": null,
          "screenshots": [
            {
              "assetGenId": "…",
              "assetToken": "…",
              "assetUrl": "…",
              "appPreviewDevice": "…",
              "sortPosition": 1,
              "sourceHeight": 2732,
              "sourceWidth": 2048,
              "orientation": "PORTRAIT",
              "assetType": "SCREENSHOT",
              "checksum": "…",
              "pictureUrl": "…",
              "videoUrl": null,
              "assetDuplicationType": null
            }
          ],
          "appPreviews": null
        }
      }
    }
  ]
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/apps/{adamId}/locale-details`

## Parameters

### Path Parameters

- `adamId` (int64) *(required)*: Your unique App Store app identifier.

## Responses

- `200` OK (`MediaLocaleDetailResponse`, `application/json`): If successful, the API returns a list of objects in the response payload with an HTTP status code of `200 (OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`)
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`)
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### App Details
- [Get App Details](./get-app-details.md)
  Fetches app metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-localized-app-details)*