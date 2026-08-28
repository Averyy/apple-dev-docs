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

The `LocationGroupCreate` object is the payload sent to [`Create Location Group`](create-location-group.md).

##### Grouptype Details

The `groupType` you choose determines how membership is defined and maintained:

| Type | How Membership Is Defined |
| --- | --- |
| `STATIC` | An explicit list of `locationIds` associated with the brand. Membership changes only when you update the `locationIds` array. |
| `DYNAMIC` | A set of `rules` evaluated against the brand’s full location catalog. Membership updates automatically as locations are added to or removed from the brand. |

The `STATIC` groups give precise control over which locations are targeted. The `DYNAMIC` groups reduce maintenance when the brand’s footprint changes frequently, for example always including every location in a given city without manually updating the group. Once evaluation completes, `groupTotal` reflects the number of matched locations.

Two fields set at creation are locked in permanently:

| Field | Notes |
| --- | --- |
| `brandId` | Scopes the group to a single brand. Cannot be changed after creation. |
| `adAccountId` | Determines which ad account owns and can access the group. |

Creating a group also requires satisfying the following constraints:

| Constraint | Detail |
| --- | --- |
| `locationIds` required for `STATIC` | At least one location ID must be provided when `groupType` is `STATIC`. |
| `rules` required for `DYNAMIC` | At least one rule must be provided when `groupType` is `DYNAMIC`. |
| `groupTotal` on creation | For `STATIC` groups, `groupTotal` equals the number of IDs supplied. For `DYNAMIC` groups, `groupTotal` is `0` until evaluation completes. |
| `locality` value format | A `rules` entry with `field: locality` must use the pipe-delimited format `countryOrRegion|adminArea|locality`, for example `"US|New York|Brooklyn"`, not a bare city name. |

##### Dynamic Rule Field Values

When `field` is `adminArea`, the `value` must be the full English name of the administrative area, such as `"Illinois"` rather than `"IL"` or `"California"` rather than `"CA"`.

> **Note**: **Important:** The API accepts abbreviated codes without returning an error, but the system creates the location group with `groupTotal: 0` because no locations match. There is no validation error to indicate the mismatch. Use the full name exactly as it appears in a location’s `adminArea` field (returned by [`Query for Locations`](query-locations.md) or [`Get a Location`](get-location-by-id.md)) to ensure rules evaluate correctly.

##### Status

After creation, a `DYNAMIC` group’s `systemStatus` is initially `PENDING` while Apple Ads evaluates the rules. The `STATIC` groups are `VALID` immediately, since membership is an explicit list rather than something to evaluate. Wait for `systemStatus: VALID` before using a `DYNAMIC` group in ad group targeting.

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
- `groupType` (LocationGroupType) *(required)*: Type of location grouping. Values: `STATIC`, `DYNAMIC`. See groupType Details in the Discussion section.
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