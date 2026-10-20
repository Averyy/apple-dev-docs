# Search for iOS apps

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Searches for iOS apps to promote in a campaign.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use this endpoint to search for iOS apps that you can promote in a campaign. You can use query parameters to fetch data. For more information, see the Use Query Parameters section of [Using Apple Ads API Functionality](./using-apple-search-ads-api-functionality.md).

An app search returns your `adamId`, which you can use in [`Create a Campaign`](./create-a-campaign.md) in addition to the `AppDownloaderCriteria` in the [`TargetingDimensions`](./targetingdimensions.md) payload. You can apply targeting dimensions to ad groups using [`Create an Ad Group`](./create-an-ad-group.md) or [`Update an Ad Group`](./update-an-ad-group.md) endpoints.

![Search for iOS apps workflow. The first box on the left in the flow diagram is the get call URL. The second box is the AppDownloaderCriteria targeting dimension. The third box in the flow diagram specifies to create or update an ad group.](https://developer.apple.com/tutorials/images/com.apple.appleads/media-4452999@2x.png)

##### Payload Example: Search for iOS apps

**Request**:

```
GET https://api.searchads.apple.com/api/v5/search/apps?query=apple&limit=1
```

**Response**:

```json
[
  {
    "adamId": 427916203,
    "appName": "Trip Trek example app",
    "developerName": "example Apple developer",
    "countryOrRegionCodes": [
      "FR",
      "DE",
      "US",
      "NO",
      "MX",
      "GB",
      "CA",
      "SE",
      "AU"
    ]
  }
]
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/search/apps`

## Parameters

### Query Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/apps?limit=100
  ```

  **Default**: `20`
- `offset` (int32): The offset pagination that limits the number of records returned. The start of each page is offset by the number specified. You can apply `offset` to most API calls, but not all GET endpoints support it.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/apps?limit=<LIMIT>&offset=<OFFSET>
  ```

  **Default**: `0`
- `query` (string) *(required)*: The query for a list of iOS apps using a matching prefix.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/apps?query=Run%20Ke
  ```

  The query search pattern uses a prefix-matching algorithm. You can use spaces in search patterns. Prefixes require a minimum of three characters. If you’re sending a quoted search string, use HTML encoding.
- `returnOwnedApps` (boolean): The list of apps belonging to your organization.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/apps?query=appexample&returnOwnedApps=true
  ```

  **Default**: `false`

## Responses

- `200` OK (`AppInfoListResponse`, `application/json`): If the call succeeds, the API returns the [`AppInfo`](./appinfo.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/search-for-ios-apps)*