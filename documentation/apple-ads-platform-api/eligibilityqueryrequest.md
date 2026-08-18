# EligibilityQueryRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for querying app eligibility.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object EligibilityQueryRequest
```

#### Discussion

`EligibilityQueryRequest` is the request body for the eligibility query endpoint. To filter, paginate, and sort the app eligibility records returned, use it.

The `filters` array accepts `QueryFilter` objects targeting filterable fields on the eligibility resource. Combine multiple filters to narrow results. For example, filter by `adamId` to check eligibility for a specific set of apps.

The `filters` array supports the following fields:

| Field | Description |
| --- | --- |
| `adamId` | The Adam ID of the app. |
| `supplyPlacement` | The supply placement being checked. |
| `supplySource` | The supply source being checked. |
| `countryOrRegion` | The country or region evaluated. |
| `deviceClass` | The device class evaluated. |
| `state` | Eligibility state: `ELIGIBLE` or `INELIGIBLE`. |

##### Example

```json
{
  "filters": [
    {
      "field": "adamId",
      "operator": "EQUALS",
      "value": 123456789
    }
  ],
  "sorting": [
    {
      "field": "countryOrRegion",
      "order": "ASC"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20
  }
}
```

## Properties

- `filters` ([QueryFilter]): See [`QueryFilter`](queryfilter.md) for details.
- `sorting` ([QuerySort]): See [`QuerySort`](querysort.md) for details.
- `pagination` (QueryPagination): See [`QueryPagination`](querypagination.md) for details.

## See Also

- [object EligibilityQueryResponse](eligibilityqueryresponse.md)
  The paginated response object for an app eligibility query.
- [object RejectionReasonResponse](rejectionreasonresponse.md)
  The response object for a rejection reason operation.
- [object AppDetailsResponse](appdetailsresponse.md)
  The response object for a get app details operation.
- [object AppDetails](appdetails.md)
  Application details and metadata.
- [object EligibilityResponse](eligibilityresponse.md)
  The response object describing an app’s eligibility for a specific supply placement, supply source, country or region, and device class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/eligibilityqueryrequest)*