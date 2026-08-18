# PromotedObject

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Promoted object details.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object PromotedObject
```

#### Discussion

`PromotedObject` provides a lightweight summary of the entity being promoted in an ad.

This object appears in report rows and response contexts where the full promoted object identity (id, type) is captured elsewhere, and only the human-readable name is needed for display or logging purposes.

##### Example

```json
{
  "name": "AwayFinder Downtown"
}
```

## Properties

- `name` (string): The name of the promoted object. For `BRANDS` campaigns this is the brand or location name as it appears in Maps. Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/promotedobject)*