# Get App Details

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches app metadata.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to return app details using your adamId in the resource path. Related objects: [`MediaDetail`](./mediadetail.md), [`MediaDetailResponse`](./mediadetailresponse.md).

##### Get app details example

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

### Path Parameters

- `adamId` (int64) *(required)*: Your unique App Store app identifier.

## Responses

- `200` OK (`MediaDetailResponse`, `application/json`): If the call succeeds, the API returns a response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`)
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### App Details
- [Get Localized App Details](./get-localized-app-details.md)
  Fetches the localized default product page for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-app-details)*