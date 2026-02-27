# Get an Ad Group

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a specific ad group with a campaign and ad group identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

To return a specific ad group, use the associated `campaignId` and `adgroupId` in the URI path. You can also use a partial fetch. For more information, see the Use a Partial Fetch subsection of  [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get an Ad Group

**Request**:

```http
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}
```

**Response**:

```json
{
    "id": 542370539,
    "campaignId": 56543219,
    "name": " ad group name example",
    "cpaGoal": {
      "amount": "100",
      "currency": "USD"
    },
    "startTime": "2025-04-08T12:00:22.788",
    "endTime": "2025-04-09T12:00:22.788",
    "automatedKeywordsOptIn": false,
    "defaultBidAmount": {
      "amount": "100",
      "currency": "USD"
    },
   "pricingModel": "CPC",    
   "targetingDimensions": {
      "age": {
        "included": [
          {
            "minAge": 20,
            "maxAge": 25
          },
          {
            "minAge": 25,
            "maxAge": 55
          }
        ]
      },
      "gender": {
        "included": [
          "M",
          "F"
        ]
      },
      "country": null,
      "adminArea": null,
      "locality": null,
      "deviceClass": {
        "included": [
          "IPAD",
          "IPHONE"
        ]
      },
      "daypart": {
        "userTime": {
          "included": [
            1,
            3,
            22
          ]
        }
      },
      "appDownloaders": null
    },
    "orgId": 40669820,
    "modificationTime": "2025-04-08T19:00:24.105",
    "status": "ENABLED",
    "servingStatus": "RUNNING",
    "servingStateReasons": null,
    "displayStatus": "RUNNING",
    "deleted": false
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## See Also

- [Create an Ad Group](create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](find-ad-groups-(org-level).md)
  Fetches ad groups within an organization.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-an-ad-group)*