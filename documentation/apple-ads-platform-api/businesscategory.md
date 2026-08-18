# BusinessCategory

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A category in the Apple Maps business taxonomy used to classify brands and locations.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BusinessCategory
```

#### Discussion

`BusinessCategory` represents a leaf or branch node in the Apple Maps category taxonomy. Categories classify brands and locations and scope which businesses Apple Maps campaigns can reach.

You can associate active Apple Maps campaigns only with categories that have `eligibility.status: ELIGIBLE`. Check eligibility before using a category in a production campaign.

##### Example

```json
{
  "id": "cat-restaurant-042",
  "name": "Restaurant",
  "qualifiedId": "dining.restaurant",
  "description": "Establishments that prepare and serve food and beverages to customers.",
  "eligibility": {
    "status": "ELIGIBLE",
    "blockedGroups": [],
    "allowedGroups": [
      {
        "supplyPlacement": ["SEARCH_TAB", "SEARCH_RESULTS"],
        "countryOrRegion": ["US", "GB"]
      }
    ],
    "modificationTime": "2025-01-10T08:00:00.000"
  },
  "creationTime": "2024-11-02T09:15:00.000",
  "modificationTime": "2025-01-10T08:00:00.000"
}
```

## Properties

- `id` (string) *(required)*: MUID (Maps Unique Identifier) for this category. Read-only.
- `name` (string): English locale display name of the category. Example: `"Association or Organization"`. Read-only.
- `qualifiedId` (string): Dot-delimited taxonomy path encoding the category hierarchy. A dot always marks a hierarchy boundary, but an individual level’s name can itself contain underscores (for example, `association_or_organization`). Example: `"dining.restaurant"`. Use this value as the `text` on a `CATEGORY` match-type Keyword. Read-only.
- `description` (string): Human-readable description of the category. Example: `"Sporting venues where animals are involved."` Read-only.
- `eligibility` (Eligibility): Ad serving eligibility for this category. See [`Eligibility`](eligibility.md). Read-only.
- `creationTime` (date-time): ISO-8601 timestamp when the category record was created. Read-only.
- `modificationTime` (date-time): ISO-8601 timestamp of the last modification. Read-only.

## See Also

- [object Brand](brand.md)
  A brand eligible for promotion through Apple Maps ads.
- [object BrandResponse](brandresponse.md)
  The Get Brand by ID endpoint returns this response object.
- [object BrandQueryResponse](brandqueryresponse.md)
  The Query Brands endpoint returns this response object.
- [object BrandRejectionReasonResponse](brandrejectionreasonresponse.md)
  A single policy assignment with rejection reason details for a brand entity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/businesscategory)*