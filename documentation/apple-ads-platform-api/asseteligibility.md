# AssetEligibility

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Eligibility status and constraint details for an asset.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AssetEligibility
```

#### Discussion

`AssetEligibility` captures the policy evaluation result for an asset. `Asset` responses always include it (unless excluded via the `fields` parameter), and it describes whether and where the asset can be used for ad serving.

Check `AssetEligibility` before including an asset in a creative. You cannot use assets with `INELIGIBLE` or `PENDING` status in any ad unit. Assets with `LIMITED` status can serve in some placements or markets. See [`AssetEligibilityStatus`](asseteligibilitystatus.md) for the full list of status values.

##### Example

```json
{
  "status": "LIMITED",
  "blockedGroups": [
    {
      "supplyPlacement": ["SEARCH_TAB"],
      "countryOrRegion": ["CN"]
    }
  ],
  "allowedGroups": [
    {
      "supplyPlacement": ["SEARCH_TAB", "TODAY_TAB", "SEARCH_RESULTS"],
      "countryOrRegion": ["US", "GB"]
    }
  ]
}
```

## Properties

- `status` (AssetEligibilityStatus): Overall eligibility status. Read-only.
- `blockedGroups` ([AssetConstraintGroup]): Constraint groups where the asset is blocked from serving. See [`AssetConstraintGroup`](assetconstraintgroup.md). Read-only.
- `allowedGroups` ([AssetConstraintGroup]): Constraint groups where the asset is explicitly allowed to serve. See [`AssetConstraintGroup`](assetconstraintgroup.md). Read-only.

## See Also

- [object Asset](asset.md)
  Unified asset entity containing product-agnostic asset metadata and references.
- [object AssetResponse](assetresponse.md)
  The Get Asset and Upload Asset endpoints return this response object.
- [object AssetQueryResponse](assetqueryresponse.md)
  Paginated response object for asset queries.
- [object AssetConstraintGroup](assetconstraintgroup.md)
  A constraint group defining the supply placements and countries or regions where an asset is blocked or allowed to serve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/asseteligibility)*