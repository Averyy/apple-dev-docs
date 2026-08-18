# LocationGroupQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object returned by the Query Location Groups endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object LocationGroupQueryResponse
```

#### Discussion

`LocationGroupQueryResponse` is the top-level envelope returned by [`Query Location Groups`](query-location-groups.md). The `result` array contains all [`LocationGroup`](locationgroup.md) objects that match the supplied filters, subject to pagination. Use `pagination.totalCount` and `pagination.offset` to page through large result sets.

##### Example

```json
{
  "result": [
    {
      "id": "5764607523034238976",
      "name": "AwayFinder West Coast Stores",
      "brandId": "9151314442816847872",
      "groupType": "DYNAMIC",
      "systemStatus": "VALID",
      "groupTotal": 42,
      "isAllLocationsGroup": false,
      "eligibility": {
        "status": "ELIGIBLE"
      },
      "creationTime": "2025-02-01T09:00:00.000",
      "modificationTime": "2025-03-25T16:00:00.000"
    }
  ],
  "pagination": {
    "totalCount": 1,
    "offset": 0,
    "pageSize": 100
  }
}
```

## Properties

- `result` ([LocationGroup]): Array of [`LocationGroup`](locationgroup.md) objects matching the query. Empty array if none match. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error details if the request failed. Absent on success. See [`Error`](error.md). Read-only.

## See Also

- [object Brand](brand.md)
  A brand eligible for promotion through Apple Maps ads.
- [object BrandResponse](brandresponse.md)
  The Get Brand by ID endpoint returns this response object.
- [object BrandQueryResponse](brandqueryresponse.md)
  The Query Brands endpoint returns this response object.
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
- [object LocationQueryResponse](locationqueryresponse.md)
  The paginated response envelope returned by the Query Locations endpoint.
- [object Eligibility](eligibility.md)
  Eligibility status and constraint details for a Business domain entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/locationgroupqueryresponse)*