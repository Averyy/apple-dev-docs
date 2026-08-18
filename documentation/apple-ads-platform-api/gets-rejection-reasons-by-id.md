# Get Rejection Reasons

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve the details of an ad creative rejection reason by ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves the details of a specific ad creative rejection reason by its identifier, including the reason code and description. See [`CreativeRejectionReason`](creativerejectionreason.md) for the full field reference, including `creativeId` and the `reasonLevel` values.

#### Payload Examples

##### Request

Retrieves the details of a specific ad creative rejection reason by its identifier, including the reason code and description.

```None
GET https://api.ads.apple.com/v1/rejection-reasons/apps/112233445
```

##### Response

```json
{
 "result": {
   "id": 112233445,
   "adamId": 123456789,
   "creativeId": 456789,
   "productPageId": "1a2b3c4d-0001",
   "assetId": null,
   "supplySource": "APPSTORE",
   "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
   "countryOrRegion": "US",
   "languageCode": "en-US",
   "reasonType": "REJECTION_REASON",
   "reasonCode": "APP_NOT_ELIGIBLE",
   "comment": null,
   "reasonLevel": "CUSTOM_PRODUCT_PAGE_LOCALE",
   "creationTime": "2026-02-05T08:30:00.000",
   "modificationTime": "2026-03-05T08:30:00.000"
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/rejection-reasons/apps/{rejectionReasonId}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [App Eligibility Endpoints](app-eligibility-endpoints.md)
  Check whether apps qualify to run ads and look up rejection reasons for creatives.
- [Check App Eligibility](find-apps-eligibilities.md)
  Check whether apps are eligible to run on certain Apple Ads placements and in specific countries or regions.
- [Query Rejection Reasons](find-rejection-reasons.md)
  Query ad creative rejection reasons for apps and return why each ad creative failed approval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/gets-rejection-reasons-by-id)*