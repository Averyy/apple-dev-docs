# Get a Negative Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single negative keyword by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single negative keyword by its ID. The response indicates whether the record is a campaign-level or ad-group-level exclusion based on the presence of the `adGroupId` field. Campaign-level negatives do not include `adGroupId` in the response. Ad-group-level negatives include it.

The presence of `adGroupId` in the response distinguishes which level the negative keyword applies to.

| Condition | Level |
| --- | --- |
| `adGroupId` is absent from the response | Campaign-level negative keyword: applies to all ad groups in the campaign. |
| `adGroupId` is present in the response | Ad-group-level negative keyword: scoped to a single ad group. |

Deleted negative keywords remain retrievable by ID and never expose a `bid` field.

| Constraint | Detail |
| --- | --- |
| Deleted negative keywords are returned | A deleted negative keyword is returned with `deleted: true`. The record is not removed from GET by ID responses. |
| Use query endpoint for listing | `GET /negative-keywords/{id}` returns a single record. Use `POST /negative-keywords/query` to filter and list. |
| No `bid` field | Negative keywords never have a bid field in the response. |

#### Payload Examples

**Campaign-Level Response**:

##### Request

A campaign-level negative keyword. The `adGroupId` field is absent. This exclusion applies across all ad groups in the campaign.

```None
GET https://api.ads.apple.com/v1/negative-keywords/777888999
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

**Ad Group-Level Response**:

##### Request

An ad-group-level negative keyword. The `adGroupId` field is present. This exclusion is scoped to that ad group only.

```None
GET https://api.ads.apple.com/v1/negative-keywords/777888998
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

## Endpoint

`GET https://api.ads.apple.com/v1/negative-keywords/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Negative Keyword](post-negative-keywords.md)
  Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.
- [Query Negative Keywords](post-negative-keywords-query.md)
  Query negative keywords using structured filters, sorting, and pagination.
- [Update a Negative Keyword](put-negative-keywords-_id_.md)
  Update a negative keyword’s status to enable or pause its search term exclusion.
- [Delete a Negative Keyword](delete-negative-keywords-_id_.md)
  Soft-delete a negative keyword by ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-negative-keywords-_id_)*