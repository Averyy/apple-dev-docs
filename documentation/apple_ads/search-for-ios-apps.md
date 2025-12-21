# Search for iOS apps

**Framework**: Apple Ads  
**Kind**: httpRequest

Searches for iOS apps to promote in a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to search for iOS apps that you can promote in a campaign. You can use query parameters to fetch data. For more information, see the Use Query Parameters section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

An app search returns your `adamId`, which you can use in [`Create a Campaign`](create-a-campaign.md) in addition to the `AppDownloaderCriteria` in the [`TargetingDimensions`](targetingdimensions.md) payload. You can apply targeting dimensions to ad groups using [`Create an Ad Group`](create-an-ad-group.md) or [`Update an Ad Group`](update-an-ad-group.md) endpoints.

![Search for iOS apps workflow. The first box on the left in the flow diagram is the get call URL. The second box is the AppDownloaderCriteria targeting dimension. The third box in the flow diagram specifies to create or update an ad group.](https://docs-assets.developer.apple.com/published/b06241f90357f928e68361bbf3a80703/media-4452999%402x.png)

##### Payload Example Search for Ios Apps


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/search-for-ios-apps)*