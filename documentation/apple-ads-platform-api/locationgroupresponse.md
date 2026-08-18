# LocationGroupResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object returned by the Get Location Group endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object LocationGroupResponse
```

#### Discussion

`LocationGroupResponse` is the top-level envelope returned by [`Get Location Group`](get-location-group-by-id.md). On success, `result` contains a single [`LocationGroup`](locationgroup.md). On failure (for example, 404 Not Found), the response contains only the `error` object. The response omits the `result` key entirely rather than setting it to `null`.

##### Example

```json
{
  "result": {
    "id": "5764607523034238976",
    "name": "AwayFinder West Coast Stores",
    "brandId": "9151314442816847872",
    "adAccountId": "293897290",
    "groupType": "DYNAMIC",
    "systemStatus": "VALID",
    "rules": [
      {
        "field": "adminArea",
        "operator": "IN",
        "value": [
          "California",
          "Oregon",
          "Washington"
        ]
      }
    ],
    "groupTotal": 42,
    "isAllLocationsGroup": false,
    "description": "All AwayFinder locations on the West Coast",
    "creationTime": "2026-02-01T09:00:00Z",
    "modificationTime": "2026-03-25T16:00:00Z",
    "eligibility": {
      "status": "ELIGIBLE"
    }
  }
}
```

## Properties

- `result` (LocationGroup): The retrieved [`LocationGroup`](locationgroup.md) object. Omitted from the response entirely if no location group was found (see the 404 case above), rather than being present as `null`. Read-only.
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
- [object LocationGroupQueryResponse](locationgroupqueryresponse.md)
  The response object returned by the Query Location Groups endpoint.
- [object LocationQueryResponse](locationqueryresponse.md)
  The paginated response envelope returned by the Query Locations endpoint.
- [object Eligibility](eligibility.md)
  Eligibility status and constraint details for a Business domain entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/locationgroupresponse)*