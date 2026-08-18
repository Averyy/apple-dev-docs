# AdQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for an Ad query, containing matched results and pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdQueryResponse
```

#### Discussion

The ads query endpoint returns `AdQueryResponse`, which contains the filtered, sorted, and paginated set of `Ad` objects matching the request.

To scope results by `adGroupId`, `campaignId`, `status`, or other filterable fields, use the `QueryRequest` body with `filters`.

##### Example

```json
{
  "result": [
    {
      "id": 777888999,
      "adAccountId": 123456789,
      "campaignId": 444555666,
      "adGroupId": 555666777,
      "creativeId": 666777888,
      "name": "AwayFinder - Default Product Page",
      "status": "ENABLED",
      "systemStatus": "RUNNING",
      "systemStatusReasons": [],
      "systemStatusLimitingReasons": [],
      "deleted": false,
      "creationTime": "2025-09-01T08:00:00.000",
      "modificationTime": "2025-09-01T08:00:00.000"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` ([Ad]): Array of [`Ad`](ad.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the response, including `offset`, `pageSize`, and `totalCount`. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error information if the request encountered an error. See [`Error`](error.md). Read-only.

## See Also

- [object Ad](ad.md)
  Ad entity that links an ad creative to an ad group for serving.
- [object AdCreate](adcreate.md)
  The request body for creating a new Ad object.
- [object AdUpdate](adupdate.md)
  The request body for updating an existing Ad object.
- [object AdResponse](adresponse.md)
  The response object for an Ad operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adqueryresponse)*