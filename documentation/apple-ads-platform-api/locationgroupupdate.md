# LocationGroupUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body object for updating an existing location group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object LocationGroupUpdate
```

#### Discussion

`LocationGroupUpdate` is the partial-update payload sent to [`Update Location Group`](update-location-group.md). All fields are optional. The system changes only the fields you provide. Omitted fields retain their current values.

##### Example

```json
{
  "name": "West Coast Stores (Updated)",
  "description": "All AwayFinder retail stores on the West Coast, including new Pacific Northwest locations"
}
```

## Properties

- `name` (string): Updated display name for the location group.
- `groupType` (LocationGroupType): Type of location grouping. Values: `STATIC`, `DYNAMIC`. Immutable after creation. To switch a group between types, delete the group and recreate it.
- `rules` ([Rule]): Updated array of [`Rule`](rule.md) objects for `DYNAMIC` groups. Replaces the existing rules and transitions `systemStatus` to `PENDING`. Wait for `systemStatus: VALID` before relying on the updated membership in active targeting.
- `locationIds` ([string]): Updated array of location IDs for `STATIC` groups. Replaces the existing list and may briefly set `systemStatus` to `PENDING`.
- `description` (string): Updated description of the location group.

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
- [object LocationGroupResponse](locationgroupresponse.md)
  The response object returned by the Get Location Group endpoint.
- [object LocationGroupQueryResponse](locationgroupqueryresponse.md)
  The response object returned by the Query Location Groups endpoint.
- [object LocationQueryResponse](locationqueryresponse.md)
  The paginated response envelope returned by the Query Locations endpoint.
- [object Eligibility](eligibility.md)
  Eligibility status and constraint details for a Business domain entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/locationgroupupdate)*