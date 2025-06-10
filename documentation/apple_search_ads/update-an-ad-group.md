# Update an Ad Group

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Updates an ad group with an ad group identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update ad groups, use the associated `campaignId` and `adgroupId` in the resource path.

In the request, specify [`TargetingDimensions`](targetingdimensions.md) and apply it to ad groups. If you’re not updating [`TargetingDimensions`](targetingdimensions.md), don’t include them in the payload. Use partial updates as necessary. For more information, see the Use Partial Updates section of [`Using Apple Search Ads API Functionality`](using-apple-search-ads-api-functionality.md).

> **Note**:  You can’t create or update ad groups with geotargeting for campaigns with multiple countries or regions. Use [`UpdateCampaignRequest`](updatecampaignrequest.md) to clear your geotargeting parameters. Then apply [`TargetingDimensions`](targetingdimensions.md) in the request payload.

##### Payload Example Update an Ad Group with Targeting

##### Payload Example Update an Ad Group Without Targeting

##### Payload Example Update an Ad Group to Show a Cpa Goal

## Request Body

The request body that includes the details of the ad group and campaign.

## See Also

- [Create an Ad Group](create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](find-ad-groups-(org-level).md)
  Fetches ad groups within an organization.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/update-an-ad-group)*