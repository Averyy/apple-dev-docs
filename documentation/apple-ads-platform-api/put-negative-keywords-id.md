# Update a Negative Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Update a negative keyword’s status to enable or pause its search term exclusion.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint updates an existing negative keyword. The `NegativeKeywordUpdate` schema accepts only the `status` field. Negative keywords do not have a `bid` field, and `text` and `matchType` are immutable after creation. To change a negative keyword’s text or match type, delete it and create a new one.

#### Payload Examples

Pause a negative keyword to temporarily suspend its search term exclusion. The term can be re-enabled without recreating it.

##### Request

```json
PUT /v1/negative-keywords/{id}

{
 "status": "PAUSED"
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
   "status": "PAUSED",
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T10:00:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/negative-keywords/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Negative Keyword](post-negative-keywords.md)
  Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.
- [Query Negative Keywords](post-negative-keywords-query.md)
  Query negative keywords using structured filters, sorting, and pagination.
- [Get a Negative Keyword](get-negative-keywords-_id_.md)
  Retrieve a single negative keyword by its unique identifier.
- [Delete a Negative Keyword](delete-negative-keywords-_id_.md)
  Soft-delete a negative keyword by ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-negative-keywords-_id_)*