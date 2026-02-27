# Get Localized App Details

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches the localized default product page for an app.

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to return localized app details using your `adamId` in the resource path. Related objects: [`MediaLocaleDetail`](medialocaledetail.md), [`MediaLocaleDetailResponse`](medialocaledetailresponse.md).

##### Query Parameters

- expand: Detailed app asset details of a device. Use `true` for expanded values in the API response.

##### Get Localized App Details Example

**Request**:

```None
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

- `adamId` (int64) *(required)*: Your unique App Store app identifier.

## See Also

- [Get App Details](get-app-details.md)
  Fetches app metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-localized-app-details)*