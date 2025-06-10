# Create an Ad Group

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Creates an ad group as part of a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

To create ad groups, use the associated `campaignId` as a resource in the URI. In the request, specify [`TargetingDimensions`](targetingdimensions.md) and apply it to ad groups.

> **Note**:  You can’t create or update ad groups with geotargeting for campaigns with multiple `countriesOrRegions`.

##### Payload Example Create an Ad Group with Targeting

##### Payload Example Create an Ad Group Without Targeting

## Request Body

The request body that includes the details of the ad group and campaign.

## See Also

- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](find-ad-groups-(org-level).md)
  Fetches ad groups within an organization.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/create-an-ad-group)*