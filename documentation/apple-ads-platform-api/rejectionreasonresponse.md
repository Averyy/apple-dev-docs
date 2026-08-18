# RejectionReasonResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a rejection reason operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RejectionReasonResponse
```

#### Discussion

The API returns `RejectionReasonResponse` as the envelope when you retrieve rejection reason details for an app.

##### Example

```json
{
  "result": {
    "id": 14919,
    "adamId": 987654321,
    "creativeId": 456789,
    "productPageId": "9ea4bb81-5f18-401f-bfe1-101a6ee6d328",
    "assetId": "41a91e19-e021-45bb-ac5a-5faec02f9445",
    "supplySource": "APPSTORE",
    "supplyPlacement": "APPSTORE_TODAY_TAB",
    "countryOrRegion": "US",
    "languageCode": "en-US",
    "reasonType": "REJECTION_REASON",
    "reasonCode": "APP_NOT_ELIGIBLE",
    "comment": "Product page metadata does not meet App Store review guidelines.",
    "reasonLevel": "CUSTOM_PRODUCT_PAGE_LOCALE",
    "creationTime": "2026-02-05T08:30:00.000",
    "modificationTime": "2026-03-05T08:30:00.000"
  }
}
```

## Properties

- `error` (Error)
- `result` (CreativeRejectionReason): The rejection reason record describing why an ad creative was rejected during review. See [`CreativeRejectionReason`](creativerejectionreason.md) for the full field reference, including `creativeId` and `reasonLevel`. Read-only.

## See Also

- [App Eligibility Endpoints](app-eligibility-endpoints.md)
  Check whether apps qualify to run ads and look up rejection reasons for creatives.
- [object EligibilityQueryRequest](eligibilityqueryrequest.md)
  The request body for querying app eligibility.
- [object EligibilityQueryResponse](eligibilityqueryresponse.md)
  The paginated response object for an app eligibility query.
- [object AppDetailsResponse](appdetailsresponse.md)
  The response object for a get app details operation.
- [object AppDetails](appdetails.md)
  Application details and metadata.
- [object EligibilityResponse](eligibilityresponse.md)
  The response object describing an app’s eligibility for a specific supply placement, supply source, country or region, and device class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/rejectionreasonresponse)*