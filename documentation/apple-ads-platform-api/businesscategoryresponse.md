# BusinessCategoryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The Get Business Category endpoint returns this response object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BusinessCategoryResponse
```

#### Discussion

[`Get Business Category`](get-category-by-id.md) returns `BusinessCategoryResponse` as the top-level envelope. On success, `result` contains a single [`BusinessCategory`](businesscategory.md) object. On failure (for example, 404 Not Found), the response contains only the `error` object. The response omits the `result` key entirely rather than setting it to `null`.

##### Example

```json
{
  "result": {
    "id": "cat-din-001",
    "name": "Restaurant",
    "qualifiedId": "dining.restaurant",
    "description": "Establishments that serve prepared food and beverages for on-site consumption.",
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-01-10T08:00:00.000",
    "eligibility": {
      "status": "ELIGIBLE",
      "blockedGroups": [],
      "allowedGroups": []
    }
  }
}
```

## Properties

- `result` (BusinessCategory): The retrieved business category. Omitted from the response entirely if not found (see the 404 case above), rather than being present as `null`. See [`BusinessCategory`](businesscategory.md). Read-only.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/businesscategoryresponse)*