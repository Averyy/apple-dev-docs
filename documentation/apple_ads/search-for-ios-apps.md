# Search for iOS apps

**Framework**: Apple Ads  
**Kind**: httpRequest

Searches for iOS apps to promote in a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to search for iOS apps that you can promote in a campaign. You can use query parameters to fetch data. For more information, see the Use Query Parameters section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

An app search returns your `adamId`, which you can use in [`Create a Campaign`](create-a-campaign.md) in addition to the `AppDownloaderCriteria` in the [`TargetingDimensions`](targetingdimensions.md) payload. You can apply targeting dimensions to ad groups using [`Create an Ad Group`](create-an-ad-group.md) or [`Update an Ad Group`](update-an-ad-group.md) endpoints.

![Search for iOS apps workflow. The first box on the left in the flow diagram is the get call URL. The second box is the AppDownloaderCriteria targeting dimension. The third box in the flow diagram specifies to create or update an ad group.](/images/com.apple.appleads/media-4452999@2x.png)

##### Payload Example Search for Ios Apps

**Request**:

```None
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

- `limit` (int32): The number of items to return per request. The maximum is 1000. ```console
GET https://api.searchads.apple.com/api/v5/search/apps?limit=100
```
- `offset` (int32): The offset pagination that limits the number of records returned. The start of each page is offset by the number specified. You can apply `offset` to most API calls, but not all GET endpoints support it. ```console
GET https://api.searchads.apple.com/api/v5/search/apps?limit=<LIMIT>&offset=<OFFSET>
```
- `query` (string) *(required)*: The query for a list of iOS apps using a matching prefix. ```console
GET https://api.searchads.apple.com/api/v5/search/apps?query=Run%20Ke
``` The query search pattern uses a prefix-matching algorithm. You can use spaces in search patterns. Prefixes require a minimum of three characters. If you’re sending a quoted search string, use HTML encoding.
- `returnOwnedApps` (boolean): The list of apps belonging to your organization. ```console
GET https://api.searchads.apple.com/api/v5/search/apps?query=appexample&returnOwnedApps=true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/search-for-ios-apps)*