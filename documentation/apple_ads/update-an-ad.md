# Update an Ad

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates an ad in an ad group.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to update or replace an [`Ad`](ad.md). Use your `adId` in the resource path. The follow-up step is to create an [`Ad`](ad.md) using your `creativeId`. See [`Create an Ad`](create-an-ad.md). You can assign one active custom product page to an ad group. For information about how to edit a subset of object properties without having to include all object properties in the payload, see the Use Partial Updates section in [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update an Ad

## Request Body

The request body that includes the details of the [`Creative`](creative.md).

## See Also

- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads](find-ads.md)
  Finds ads within a campaign by selector criteria.
- [Find Ads (org-level)](find-ads-(org-level).md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Delete an Ad](delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-an-ad)*