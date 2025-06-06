# Create Targeting Keywords

**Framework**: Apple_Search_Ads  
**Kind**: httpRequest

Creates targeting keywords in ad groups.

**Availability**:
- Search Ads 5.0+

#### Overview

> **Note**:  If you create duplicate keywords, the payload response indicates an error, but the call returns with a 200 status code.

- 400: An invalid query or missing required parameters.
- 401: An unauthenticated call fails to get the requested response.
- 403: Insufficient rights to the resource.
- 404: The API can’t locate the resource.
- 429: The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [`Calling the Apple Search Ads API`](calling-the-apple-search-ads-api.md).
- 500: The Apple Search Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

#### Discussion

Keywords must belong to a specific ad group, unlike negative keywords, which can belong to a campaign or an ad group.

To create targeting keywords, use the associated `campaignId` and `adgroupId` in the URI.

> **Note**:  The limit is 5000 targeting keywords per campaign and per ad group.

##### Payload Example Create Ad Group Targeting Keywords

## Request Body

The request body that includes keyword targeting details.

## See Also

- [Find Targeting Keywords in a Campaign](find-targeting-keywords-in-a-campaign.md)
  Fetches targeting keywords in a campaign’s ad groups.
- [Get a Targeting Keyword in an Ad Group](get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Get All Targeting Keywords in an Ad Group](get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Update Targeting Keywords](update-targeting-keywords.md)
  Updates targeting keywords in ad groups.
- [Delete Targeting Keywords](delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/create-targeting-keywords)*