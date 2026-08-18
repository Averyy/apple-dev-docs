# Rule

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single filter rule for a dynamic location group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Rule
```

#### Discussion

`Rule` defines a filter for a `DYNAMIC` `LocationGroup`, specifying how the system selects locations at query time. Rules can mix different `field` values within the same group, and the system re-evaluates location membership whenever rules change, setting `LocationGroup.systemStatus` to `PENDING` until evaluation completes.

##### Example

```json
{
  "field": "adminArea",
  "operator": "IN",
  "value": ["California", "New York"]
}
```

## Topics

### Dictionaries
- [object Rule.Value](rule/value-data.dictionary.md)
  The comparison value for a targeting rule, as either a single string or an array of strings.

## Properties

- `field` (string) *(required)*: The location attribute to filter on. Values: `adminArea` (state or province name, e.g. `"California"`), `locality` (city or locality, formatted as `countryOrRegion|adminArea|locality`, e.g. `"US|New York|Brooklyn"`), `postalCode` (postal code, e.g. `"94107"`), `locationId` (location ID, e.g. `"7205759403792794"`). Cannot be `null`.
- `operator` (string) *(required)*: Comparison operator to apply against `field`. Cannot be `null`.
- `value` (Rule.Value) *(required)*: The value to match against. Pass a string for `EQUALS` and `NOT_EQUALS`. Pass an array of strings for `IN` and `NOT_IN`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/rule)*