# PolicyAssignmentQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response returned by the Query Rejection Reasons endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object PolicyAssignmentQueryResponse
```

#### Discussion

`PolicyAssignmentQueryResponse` extends the standard [`QueryResponse`](queryresponse.md) envelope. The `result` array contains [`BrandRejectionReasonResponse`](brandrejectionreasonresponse.md) objects, each describing a policy assignment with rejection reason details for a brand entity.

##### Example

```json
{
  "result": [
    {
      "id": 555666777,
      "promotedObjectId": "123456789",
      "promotedObjectType": "BUSINESS_BRAND",
      "entityId": "987654321",
      "entityType": "BUSINESS_BRAND",
      "componentType": "ENTITY_ASSET",
      "component": "3135832a-0645-5b84-a030-36394cbdbcf6",
      "code": "PERSONAL_INFORMATION",
      "title": "Personal Information",
      "body": "Content containing personally identifiable information is not allowed."
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

- `result` ([BrandRejectionReasonResponse]): The list of policy assignment records with rejection reason details. See [`BrandRejectionReasonResponse`](brandrejectionreasonresponse.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata including `totalCount`, `offset`, and `pageSize`. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error information if the request encountered an error. See [`Error`](error.md). Read-only.

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
- [object LocationGroupQueryResponse](locationgroupqueryresponse.md)
  The response object returned by the Query Location Groups endpoint.
- [object LocationQueryResponse](locationqueryresponse.md)
  The paginated response envelope returned by the Query Locations endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/policyassignmentqueryresponse)*