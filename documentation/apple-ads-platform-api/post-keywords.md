# Create a Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a new keyword in an ad group, setting the match type and optional bid amount.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates one keyword per request. To create many keywords in a single call, use [`Bulk Create Keywords`](post-keywords-bulk-create.md).

Creates a keyword in an ad group. Each keyword belongs to an ad group via `adGroupId`, which is required at creation and immutable afterward. The `text` field is the search term itself and is also immutable after creation. To change a keyword’s text, delete it and create a new one.

Omitting `bid` or passing `null` on create defaults the keyword to the ad group’s bid strategy. This differs from [`Update a Keyword`](put-keywords-_id_.md), where `null` is not accepted for `bid`. See [`Managing Keywords and Negative Keywords`](keywords-and-negative-keywords.md) for the full explanation.

#### Payload Examples

**App Store - Exact Match**:

Create an exact match keyword with an explicit bid. The ad shows only when users search for “photo editor” with no additional words.

##### Request

```json
POST /v1/keywords

{
 "adGroupId": 555666777,
 "text": "photo editor",
 "matchType": "EXACT",
 "bid": {
   "amount": "2.50",
   "currency": "USD"
 },
 "status": "ENABLED"
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
   "status": "ENABLED",
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**App Store - Broad Match**:

Create a broad match keyword without specifying a bid. The keyword inherits the ad group’s default bid and matches variations and related terms.

##### Request

```json
POST /v1/keywords

{
 "adGroupId": 555666777,
 "text": "productivity app",
 "matchType": "BROAD",
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 888999001,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "text": "productivity app",
   "matchType": "BROAD",
   "bid": {
     "amount": "1.50",
     "currency": "USD"
   },
   "status": "ENABLED",
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-01-10T08:05:00.000",
   "modificationTime": "2025-01-10T08:05:00.000"
 }
}
```

**Apple Maps - Phrase Match**:

Create a phrase match keyword for an Apple Maps ad group. The ad shows for the keyword and close variants within Maps search.

##### Request

```json
POST /v1/keywords

{
 "adGroupId": 555666780,
 "text": "coffee shop near me",
 "matchType": "PHRASE",
 "bid": {
   "amount": "3.00",
   "currency": "USD"
 },
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 888999002,
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "adGroupId": 555666780,
   "text": "coffee shop near me",
   "matchType": "PHRASE",
   "bid": {
     "amount": "3.00",
     "currency": "USD"
   },
   "status": "ENABLED",
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-01-10T08:10:00.000",
   "modificationTime": "2025-01-10T08:10:00.000"
 }
}
```

**Apple Maps - Category Match**:

Create a category match keyword for an Apple Maps ad group. The `text` must be a Maps business category identifier from the [`Query Business Categories`](query-categories.md) endpoint.

##### Request

```json
POST /v1/keywords

{
 "adGroupId": 555666780,
 "text": "dining.restaurant",
 "matchType": "CATEGORY",
 "bid": {
   "amount": "3.50",
   "currency": "USD"
 },
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 888999003,
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "adGroupId": 555666780,
   "text": "dining.restaurant",
   "matchType": "CATEGORY",
   "bid": {
     "amount": "3.50",
     "currency": "USD"
   },
   "status": "ENABLED",
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-01-10T08:15:00.000",
   "modificationTime": "2025-01-10T08:15:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/keywords`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Keywords](post-keywords-query.md)
  Query keywords using structured filters, sorting, and pagination.
- [Get a Keyword](get-keywords-_id_.md)
  Retrieve a single keyword by its unique identifier.
- [Update a Keyword](put-keywords-_id_.md)
  Update a keyword’s bid amount or status to optimize spend and control delivery for that term.
- [Delete a Keyword](delete-keywords-_id_.md)
  Soft-delete a keyword by ID, setting its deleted field to true and stopping bids on that term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-keywords)*