# AssetConstraintGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A constraint group defining the supply placements and countries or regions where an asset is blocked or allowed to serve.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AssetConstraintGroup
```

#### Discussion

`AssetConstraintGroup` defines a pairing of supply placements and geographic markets that collectively describe where an asset eligibility rule applies. [`AssetEligibility`](asseteligibility.md) objects embed it to specify the exact scope of a blocking or allowing rule for an asset.

When both `supplyPlacement` and `countryOrRegion` are populated, the constraint applies to the intersection of those placements and markets.

##### Example

```json
{
  "supplyPlacement": [
    "SEARCH_TAB",
    "TODAY_TAB"
  ],
  "countryOrRegion": [
    "US",
    "GB"
  ]
}
```

## Properties

- `supplyPlacement` ([string]): Supply placement identifiers scoped by this constraint. Example values: `SEARCH_TAB`, `TODAY_TAB`, `SEARCH_RESULTS`.
- `countryOrRegion` ([string]): ISO 3166-1 alpha-2 country or region codes scoped by this constraint. Example values: `US`, `GB`, `CN`.

## See Also

- [object Asset](asset.md)
  Unified asset entity containing product-agnostic asset metadata and references.
- [object AssetResponse](assetresponse.md)
  The Get Asset and Upload Asset endpoints return this response object.
- [object AssetQueryResponse](assetqueryresponse.md)
  Paginated response object for asset queries.
- [object AssetEligibility](asseteligibility.md)
  Eligibility status and constraint details for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/assetconstraintgroup)*