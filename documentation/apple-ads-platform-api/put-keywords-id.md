# Update a Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Update a keyword’s bid amount or status to optimize spend and control delivery for that term.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint updates an existing keyword. Only fields included in the request body are modified. Omitted fields retain their current values. The `KeywordUpdate` schema is intentionally narrow. Only `bid` and `status` are accepted. Attempting to update a deleted keyword returns 404 Not Found. This differs from [`Get a Keyword`](get-keywords-_id_.md), which does not return 404 for a deleted keyword. It returns the keyword with `deleted: true` instead.

On update, `bid` must be a valid `Money` object. Passing `null` returns an error, unlike [`Create a Keyword`](post-keywords.md), where omitting `bid` or passing `null` defaults the keyword to the ad group’s bid strategy. See [`Managing Keywords and Negative Keywords`](keywords-and-negative-keywords.md) for the full explanation.

#### Payload Examples

**Update Bid**:

Increase the maximum cost-per-tap for a keyword. Send only the `bid` field.

##### Request

```json
PUT /v1/keywords/888999000

{
 "bid": {
   "amount": "3.75",
   "currency": "USD"
 }
}
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
     "amount": "3.75",
     "currency": "USD"
   },
   "status": "ENABLED",
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T10:00:00.000"
 }
}
```

**Pause Keyword**:

Pause a keyword to temporarily stop it from bidding. The keyword retains its bid amount and can be re-enabled at any time.

##### Request

```json
PUT /v1/keywords/888999000

{
 "status": "PAUSED"
}
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
   "status": "PAUSED",
   "displayStatus": "PAUSED",
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T11:00:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/keywords/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Keyword](post-keywords.md)
  Create a new keyword in an ad group, setting the match type and optional bid amount.
- [Query Keywords](post-keywords-query.md)
  Query keywords using structured filters, sorting, and pagination.
- [Get a Keyword](get-keywords-_id_.md)
  Retrieve a single keyword by its unique identifier.
- [Delete a Keyword](delete-keywords-_id_.md)
  Soft-delete a keyword by ID, setting its deleted field to true and stopping bids on that term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-keywords-_id_)*