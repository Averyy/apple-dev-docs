# Create a Negative Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates one negative keyword per request. To create many negative keywords in a single call, use [`Bulk Create Negative Keywords`](post-negative-keywords-bulk-create.md).

Negative keywords prevent your ads from showing when a user’s search query contains a term you want to exclude. They block traffic rather than compete for it. Negative keywords can be created at two levels, campaign or ad group, each with distinct field requirements and scope.

#### Use Campaign Level Negative Keywords

Campaign-level negative keywords block ads from appearing for excluded search terms across all ad groups in the campaign. Use campaign-level negatives when you want broad exclusions that apply uniformly throughout an entire campaign.

A campaign-level negative keyword requires `campaignId` and leaves `adGroupId` unset.

| Field | Requirement |
| --- | --- |
| `campaignId` | Required |
| `adGroupId` | Must not be set |

#### Use Ad Group Level Negative Keywords

Ad group-level negative keywords are scoped to a single ad group. Use ad group-level negatives when you need finer control over exclusions for a specific ad group within a campaign.

An ad-group-level negative keyword requires `adGroupId` and leaves `campaignId` unset.

| Field | Requirement |
| --- | --- |
| `campaignId` | Must not be set. |
| `adGroupId` | Required |

#### Payload Examples

**Campaign-Level Negative**:

Create a campaign-level negative keyword by omitting `adGroupId`. The exclusion applies to all ad groups in the campaign.

##### Request

```json
POST /v1/negative-keywords

{
 "campaignId": 444555666,
 "text": "free app",
 "matchType": "BROAD",
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 777888999,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "text": "free app",
   "matchType": "BROAD",
   "status": "ENABLED",
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Ad Group-Level Negative**:

Create an ad-group-level negative keyword by providing `adGroupId`. The exclusion is scoped to that single ad group.

##### Request

```json
POST /v1/negative-keywords

{
 "adGroupId": 555666777,
 "text": "cheap downloads",
 "matchType": "EXACT",
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 777888998,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "text": "cheap downloads",
   "matchType": "EXACT",
   "status": "ENABLED",
   "deleted": false,
   "creationTime": "2025-01-10T08:05:00.000",
   "modificationTime": "2025-01-10T08:05:00.000"
 }
}
```

**Maps - Phrase Negative**:

Create a phrase-match negative keyword for an Apple Maps ad group. Blocks queries containing the phrase within Maps search. `CATEGORY` is not supported for negative keywords.

##### Request

```json
POST /v1/negative-keywords

{
 "adGroupId": 555666780,
 "text": "fast food",
 "matchType": "PHRASE",
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 777888997,
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "adGroupId": 555666780,
   "text": "fast food",
   "matchType": "PHRASE",
   "status": "ENABLED",
   "deleted": false,
   "creationTime": "2025-01-10T08:10:00.000",
   "modificationTime": "2025-01-10T08:10:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/negative-keywords`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Negative Keywords](post-negative-keywords-query.md)
  Query negative keywords using structured filters, sorting, and pagination.
- [Get a Negative Keyword](get-negative-keywords-_id_.md)
  Retrieve a single negative keyword by its unique identifier.
- [Update a Negative Keyword](put-negative-keywords-_id_.md)
  Update a negative keyword’s status to enable or pause its search term exclusion.
- [Delete a Negative Keyword](delete-negative-keywords-_id_.md)
  Soft-delete a negative keyword by ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-negative-keywords)*