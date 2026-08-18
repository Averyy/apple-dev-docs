# Get a Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single keyword by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single keyword by its ID. The response includes all keyword fields plus `displayStatus`, which reflects the combined delivery state of the keyword, its ad group, and its campaign.

Deleted keywords remain retrievable and only the query endpoint supports listing multiple records.

| Constraint | Detail |
| --- | --- |
| Deleted keywords are returned | A deleted keyword is returned with `deleted: true`. The record is not removed from GET by ID responses. |
| Deleted keywords excluded from query results | `POST /keywords/query` omits deleted keywords by default. Add a `deleted EQUALS true` filter to retrieve deleted records. |
| Use query endpoint for listing | `GET /keywords/{id}` returns a single record. Use `POST /keywords/query` to filter and list multiple keywords. |
| `adGroupId` and `campaignId` always returned | The parent hierarchy IDs are always present in the response. |

#### Payload Examples

##### Request

Retrieves a single keyword by its unique identifier.

```None
GET https://api.ads.apple.com/v1/keywords/888999000
```

##### Response

```json
{
 "result": {
   "id": 888999000,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "text": "photo editor",
   "matchType": "EXACT",
   "bid": {
     "amount": "2.50",
     "currency": "USD"
   },
   "status": "ENABLED",
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/keywords/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Keyword](post-keywords.md)
  Create a new keyword in an ad group, setting the match type and optional bid amount.
- [Query Keywords](post-keywords-query.md)
  Query keywords using structured filters, sorting, and pagination.
- [Update a Keyword](put-keywords-_id_.md)
  Update a keyword’s bid amount or status to optimize spend and control delivery for that term.
- [Delete a Keyword](delete-keywords-_id_.md)
  Soft-delete a keyword by ID, setting its deleted field to true and stopping bids on that term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-keywords-_id_)*