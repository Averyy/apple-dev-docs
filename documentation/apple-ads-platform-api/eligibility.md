# Eligibility

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Eligibility status and constraint details for a Business domain entity.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Eligibility
```

#### Discussion

`Eligibility` captures the serving eligibility state for a Business domain entity, such as a brand or location, across supply sources and geographic markets.

Geo and brand eligibility lookup responses typically include this object, so you can use it to understand which supply placements and markets are accessible before configuring ad group targeting.

##### Example

```json
{
  "status": "LIMITED",
  "blockedGroups": [
    {
      "supplyPlacement": ["SEARCH_TAB", "TODAY_TAB"],
      "countryOrRegion": ["CN"]
    }
  ],
  "allowedGroups": [
    {
      "supplyPlacement": ["SEARCH_TAB", "SEARCH_RESULTS"],
      "countryOrRegion": ["US", "GB"]
    }
  ],
  "modificationTime": "2025-01-10T08:00:00.000"
}
```

## Properties

- `status` (EligibilityStatus): Overall eligibility status (`ELIGIBLE`, `INELIGIBLE`, `LIMITED`, `PENDING`, or `UNDEFINED`). See [`EligibilityStatus`](eligibilitystatus.md). Read-only.
- `blockedGroups` ([ConstraintGroup]): Constraint groups where the entity is blocked from serving. See [`ConstraintGroup`](constraintgroup.md). Read-only.
- `allowedGroups` ([ConstraintGroup]): Constraint groups where the entity is allowed to serve. See [`ConstraintGroup`](constraintgroup.md). Read-only.
- `modificationTime` (date-time): Timestamp of the last eligibility evaluation. Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/eligibility)*