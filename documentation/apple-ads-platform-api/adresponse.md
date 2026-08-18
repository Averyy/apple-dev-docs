# AdResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for an Ad operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdResponse
```

#### Discussion

Ad create, read, update, and delete operations return `AdResponse`, the single-item response envelope.

##### Example

```json
{
  "result": {
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
    "displayStatus": "RUNNING",
    "deleted": false,
    "creationTime": "2025-09-01T08:00:00.000",
    "modificationTime": "2025-09-01T08:00:00.000"
  }
}
```

## Properties

- `result` (Ad): The full `Ad` object, populated on success. Absent on failure. See [`Ad`](ad.md). Read-only.
- `error` (Error): Describes the problem when the operation fails. Absent on success. See [`Error`](error.md). Read-only.

## See Also

- [object Ad](ad.md)
  Ad entity that links an ad creative to an ad group for serving.
- [object AdCreate](adcreate.md)
  The request body for creating a new Ad object.
- [object AdUpdate](adupdate.md)
  The request body for updating an existing Ad object.
- [object AdQueryResponse](adqueryresponse.md)
  The response object for an Ad query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adresponse)*