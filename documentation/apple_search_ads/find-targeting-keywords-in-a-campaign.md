# Find Targeting Keywords in a Campaign

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches targeting keywords in a campaign’s ad groups.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Search Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to find targeting keywords in different ad groups within the same campaign. Use the associated `campaignId` in the URI. Find calls use [`Selector`](selector.md) [`Condition`](condition.md) operators to narrow results. If you don’t specify any selector conditions in the payload, the API returns all keywords across all ad groups of the campaign. For more information about available selection condition operators to use, see the [`Keyword`](keyword.md) object.

##### Payload Example Find Targeting Keywords in a Campaign

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create Targeting Keywords](create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/find-targeting-keywords-in-a-campaign)*