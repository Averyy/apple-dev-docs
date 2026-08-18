# Brand

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A brand eligible for promotion through Apple Maps ads.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Brand
```

#### Discussion

`Brand` represents a business entity registered in Apple Ads. Use the `id` field as the `promotedObjectId` when creating a `BUSINESS_BRAND` campaign. You can actively promote only brands with `eligibility.status: ELIGIBLE`.

To understand the business type, use the `categories` field. The `countryOrRegion` field identifies the primary market for the brand. Use [`Query Brands`](query-brands.md) to list brands accessible to your ad account, and [`Get Brand by ID`](get-brand-by-id.md) to retrieve a specific brand by its identifier.

Query endpoint requests support fields marked **Filterable** in the properties as filter criteria. See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on constructing queries.

##### Example

```json
{
  "id": "123456789",
  "name": "AwayFinder",
  "countryOrRegion": "US",
  "categories": [
    "shopping.retail",
    "dining.restaurant"
  ],
  "eligibility": {
    "status": "ELIGIBLE",
    "blockedGroups": [],
    "allowedGroups": [],
    "modificationTime": "2025-01-10T08:00:00.000"
  },
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000"
}
```

## Properties

- `id` (string) *(required)*: ID of the brand. Filterable with `EQUALS`, `IN`.
- `name` (string): Primary display name for the brand.
- `countryOrRegion` (string): 2-character ISO 3166-1 alpha-2 country or region code.
- `categories` ([string]): Modern category taxonomy identifiers. The first entry is the primary category. See [`BusinessCategory`](businesscategory.md).
- `eligibility` (Eligibility): Ad serving eligibility for this brand. See [`Eligibility`](eligibility.md). Read-only.
- `creationTime` (date-time): ISO-8601 timestamp when the brand record was created. Read-only.
- `modificationTime` (date-time): ISO-8601 timestamp of the last modification. Read-only.

## See Also

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
- [object Eligibility](eligibility.md)
  Eligibility status and constraint details for a Business domain entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brand)*