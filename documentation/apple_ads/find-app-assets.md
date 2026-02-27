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

**Request**:

```None
HTTP POST https://api.searchads.apple.com/api/v5/apps/{adamId}/assets/find

{
  “conditions”: [
    {
      “field”: “assetGenId”,
      “operator”: “equals”,
      “values”: [
        “368234568;en-US;9;0;4201c5a4bd4087cc82xdfetdc8141b94d0”
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
      "assetGenId": "368234568;en-US;9;0;4201c5a4bd4087cc82xdfetdc8141b94d0",
      "adamId": 835599320,
      "assetURL”: “https://is5-ssl.mzstatic.com/image/thumb/source113/v4/25/f5/70/25f57023-87bd-25f0-71dc-bf5f48525b4c/afcd3ec4-d7af-49c5-9d93-44084b0abea8_2208x1242iphone55_4.jpg/2208x1242.jpg",
      "assetVideoURL": null,
      "appPreviewDevice": “iphone_6_7”,
      "sourceHeight": 2208,
      "sourceWidth": 1242,
      "orientation": "PORTRAIT",
      "assetType": "SCREENSHOT"
    },
    {
      "assetGenId": "368234568;en-US;9;0;4201c5a4bd4087cc82xdfetdc8141b94d0",
      "adamId": 835599320,
      "assetURL”: “https://is5-ssl.mzstatic.com/image/thumb/PurpleSource122/v4/0b/d2/ea/0bd2ea96-744a-4341-2227-8aaa5c79ceef/84589e4f-d770-4444-9ade-e0806658f171_0.png/1290x2796.jpg",
      "assetVideoURL": null,
      "appPreviewDevice": "iphone_6_7",
      "sourceHeight": 1290,
      "sourceWidth": 2796,
      "orientation": “LANDSCAPE”,
      "assetType": “SCREENSHOT”
    }
 ],
  "pagination": {
    "totalResults": 2,
    "startIndex": 0,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/apps/{adamId}/assets/find`

## Parameters

- `adamId` (int64) *(required)*: Your unique App Store app identifier. Your `adamId` in the resource path needs to match the `adamId` in your campaign. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId` and correlate it to the correct campaign.

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Find Ad Creative Rejection Reasons](find-ad-creative-rejection-reasons.md)
  Fetches ad creative rejection reasons.
- [Get Ad Creative Rejection Reasons](gets-a-product-page-reason.md)
  Fetches ad creative rejection reasons by custom product page ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-app-assets)*