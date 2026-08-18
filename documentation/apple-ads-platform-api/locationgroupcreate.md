# LocationGroupCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body object for creating a new location group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object LocationGroupCreate
```

#### Discussion

`LocationGroupCreate` is the payload sent to [`Create Location Group`](create-location-group.md). The `groupType` field determines which membership fields are required: `rules` for `DYNAMIC` groups, or `locationIds` for `STATIC` groups.

After creation, a `DYNAMIC` group’s `systemStatus` is initially `PENDING` while Apple Ads evaluates the rules. `STATIC` groups are `VALID` immediately, since membership is an explicit list rather than something to evaluate. Wait for `systemStatus: VALID` before using a `DYNAMIC` group in ad group targeting.

##### Example

```json
{
  "name": "West Coast Stores",
  "brandId": "9151314442816847872",
  "adAccountId": "293897290",
  "groupType": "DYNAMIC",
  "rules": [
    {
      "field": "adminArea",
      "operator": "IN",
      "value": [
        "California",
        "New York"
      ]
    }
  ],
  "description": "All AwayFinder retail stores on the West Coast"
}
```

## Properties

- `name` (string) *(required)*: Display name for the location group.
- `brandId` (string) *(required)*: Associated brand identifier.
- `adAccountId` (string) *(required)*: Ad account ID that will own this location group.
- `groupType` (LocationGroupType) *(required)*: Type of location grouping. Values: `STATIC`, `DYNAMIC`.
- `rules` ([Rule]): Array of [`Rule`](rule.md) objects for `DYNAMIC` groups. Provide when `groupType` is `DYNAMIC`.
- `locationIds` ([string]): Array of location IDs for `STATIC` groups. Provide when `groupType` is `STATIC`.
- `description` (string): Optional description of the location group.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/locationgroupcreate)*