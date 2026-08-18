# BrandQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The Query Brands endpoint returns this response object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandQueryResponse
```

#### Discussion

[`Query Brands`](query-brands.md) returns `BrandQueryResponse` as the top-level envelope. The `result` array contains all [`Brand`](brand.md) objects that match the supplied filters, subject to pagination. To page through large result sets, use `pagination.totalCount` and `pagination.offset`.

##### Example

```json
{
  "result": [
    {
      "id": "123456789",
      "name": "AwayFinder",
      "countryOrRegion": "US",
      "categories": [
        "shopping.retail",
        "dining.restaurant"
      ],
      "eligibility": {
        "status": "ELIGIBLE",
        "blockedGroups": [],
        "allowedGroups": [],
        "modificationTime": "2025-01-10T08:00:00.000"
      },
      "creationTime": "2025-01-10T08:00:00.000",
      "modificationTime": "2025-01-10T08:00:00.000"
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

- `result` ([Brand]): Array of [`Brand`](brand.md) objects matching the query. Empty array if no brands match. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error details if the request failed. Absent on success. See [`Error`](error.md). Read-only.

## See Also

- [object Brand](brand.md)
  A brand eligible for promotion through Apple Maps ads.
- [object BrandResponse](brandresponse.md)
  The Get Brand by ID endpoint returns this response object.
- [object BrandRejectionReasonResponse](brandrejectionreasonresponse.md)
  A single policy assignment with rejection reason details for a brand entity.
- [object BusinessCategory](businesscategory.md)
  A category in the Apple Maps business taxonomy used to classify brands and locations.
- [object BusinessCategoryResponse](businesscategoryresponse.md)
  The Get Business Category endpoint returns this response object.
- [object BusinessCategoryQueryResponse](businesscategoryqueryresponse.md)
  The Query Business Categories endpoint returns this response object.
- [object Location](location.md)
  The brand location object.
- [object LocationResponse](locationresponse.md)
  The response object returned by the Get a Location endpoint.
- [object LocationGroup](locationgroup.md)
  A collection of business locations associated with a brand, used to target geos in Apple Maps campaigns.
- [object LocationGroupCreate](locationgroupcreate.md)
  The request body object for creating a new location group.
- [object LocationGroupUpdate](locationgroupupdate.md)
  The request body object for updating an existing location group.
- [object LocationGroupResponse](locationgroupresponse.md)
  The response object returned by the Get Location Group endpoint.
- [object LocationGroupQueryResponse](locationgroupqueryresponse.md)
  The response object returned by the Query Location Groups endpoint.
- [object LocationQueryResponse](locationqueryresponse.md)
  The paginated response envelope returned by the Query Locations endpoint.
- [object Eligibility](eligibility.md)
  Eligibility status and constraint details for a Business domain entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandqueryresponse)*