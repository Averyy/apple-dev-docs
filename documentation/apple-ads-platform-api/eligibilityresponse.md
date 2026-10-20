# EligibilityResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary  
**Role**: Object

The response object describing an app’s eligibility for a specific supply placement, supply source, country or region, and device class.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
object EligibilityResponse
```

## Properties

- `adamId` (int64): The Adam ID of the app. Read-only.
- `supplyPlacement` (string): The supply placement being checked. Read-only.
- `supplySource` (string): The supply source being checked. Read-only.

  **Allowed Values**: `APPSTORE`, `MAPS`
- `minAge` (number): The minimum age rating required to serve ads for this app in this market. Read-only.
- `state` (string): Eligibility state: `ELIGIBLE` or `INELIGIBLE`. Defaults to `ELIGIBLE`. Read-only.

  **Default**: `ELIGIBLE`; **Allowed Values**: `ELIGIBLE`, `INELIGIBLE`
- `countryOrRegion` (string): The country or region evaluated. Read-only.
- `deviceClass` (string): The device class evaluated. Read-only.

  **Allowed Values**: `IPHONE`, `IPAD`
- `creationTime` (date-time): The date and time this eligibility record was created. Read-only.
- `modificationTime` (date-time): The date and time this eligibility record was last modified. Read-only.

## See Also

- [object EligibilityQueryRequest](./eligibilityqueryrequest.md)
  The request body for querying app eligibility.
- [object EligibilityQueryResponse](./eligibilityqueryresponse.md)
  The paginated response object for an app eligibility query.
- [object RejectionReasonResponse](./rejectionreasonresponse.md)
  The response object for a rejection reason operation.
- [object AppDetailsResponse](./appdetailsresponse.md)
  The response object for a get app details operation.
- [object AppDetails](./appdetails.md)
  Application details and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/eligibilityresponse)*