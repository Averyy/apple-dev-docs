# Get App Details

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches app metadata.

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to return app details using your adamId in the resource path. Related objects: [`MediaDetail`](mediadetail.md), [`MediaDetailResponse`](mediadetailresponse.md).

##### Get App Details Example

**Request**:

```console
GET https://api.searchads.apple.com/api/v5/apps/{adamId}
```

**Response**:

```json
{
  "data": {
    "id": 284815942,
    "adamId": 284815942,
    "appName": "Trip Trek",
    "artistName": "Trip Trek",
    "primaryLanguage": "en-US",
    "primaryGenre": ">Mobile Software Applications>Utilities",
    "secondaryGenre": ">Mobile Software Applications>Reference",
    "deviceClasses": [
      "IPHONE",
      "IPAD"
    ],
    "iconPictureUrl": "...",
    "isPreOrder": "false",
    "availableStorefronts": [
      "US"
    ]
  }
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/apps/{adamId}`

## Parameters

- `adamId` (int64) *(required)*: Your unique App Store app identifier.

## See Also

- [Get Localized App Details](get-localized-app-details.md)
  Fetches the localized default product page for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-app-details)*