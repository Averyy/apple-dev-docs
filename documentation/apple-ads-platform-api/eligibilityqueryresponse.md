# EligibilityQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The paginated response object for an app eligibility query.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object EligibilityQueryResponse
```

#### Discussion

The eligibility query endpoint returns `EligibilityQueryResponse` as the paginated response.

To iterate through large result sets, use the `totalCount` and `offset` fields on the embedded `QueryPaginationResult` object.

##### Example

```json
{
  "result": [
    {
      "adamId": 10738622087,
      "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
      "supplySource": "APPSTORE",
      "minAge": 18,
      "state": "ELIGIBLE",
      "countryOrRegion": "US",
      "deviceClass": "IPHONE",
      "reasons": [
        "APP_LANGUAGE_INCOMPATIBLE"
      ],
      "creationTime": "2026-02-05T08:30:00.000",
      "modificationTime": "2026-03-05T08:30:00.000"
    },
    {
      "adamId": 10738622087,
      "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
      "supplySource": "APPSTORE",
      "minAge": 18,
      "state": "INELIGIBLE",
      "countryOrRegion": "BR",
      "deviceClass": "IPHONE",
      "reasons": [
        "APP_NOT_ELIGIBLE_SUPPLY",
        "APP_NOT_ELIGIBLE_IN_STOREFRONT"
      ],
      "creationTime": "2026-02-05T08:30:00.000",
      "modificationTime": "2026-03-05T08:30:00.000"
    }
  ],
  "pagination": {
    "pageSize": 20,
    "offset": 0,
    "totalCount": 2
  }
}
```

## Properties

- `result` ([EligibilityResponse]): Array of [`EligibilityResponse`](eligibilityresponse.md) records matching the supplied filter criteria. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the response, including `offset`, `pageSize`, and `totalCount`. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error information if the request encountered an error. See [`Error`](error.md). Read-only.

## See Also

- [object EligibilityQueryRequest](eligibilityqueryrequest.md)
  The request body for querying app eligibility.
- [object RejectionReasonResponse](rejectionreasonresponse.md)
  The response object for a rejection reason operation.
- [object AppDetailsResponse](appdetailsresponse.md)
  The response object for a get app details operation.
- [object AppDetails](appdetails.md)
  Application details and metadata.
- [object EligibilityResponse](eligibilityresponse.md)
  The response object describing an app’s eligibility for a specific supply placement, supply source, country or region, and device class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/eligibilityqueryresponse)*