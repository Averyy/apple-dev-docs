# CreativeRejectionReason

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Detailed rejection reason for an ad creative that failed Apple review.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeRejectionReason
```

#### Discussion

`CreativeRejectionReason` records are returned by the rejection reasons endpoint and describe why a specific ad creative was rejected. Each record includes the scope of rejection (by `adamId`, `productPageId`, or `assetId`) and the policy categories that were violated. To diagnose and remediate rejected ad creatives, use these records alongside `systemStatusReasons` on the [`Creative`](creative.md).

The endpoints that query and fetch `CreativeRejectionReason` records, `POST /v1/rejection-reasons/apps/query` and `GET /v1/rejection-reasons/apps/{rejectionReasonId}`, are documented under Apps > App Eligibility. See [`Query Rejection Reasons`](find-rejection-reasons.md) and [`Get Rejection Reasons`](gets-rejection-reasons-by-id.md).

##### Example

```json
{
  "id": 555666777,
  "adamId": 123456789,
  "creativeId": 666777888,
  "productPageId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "assetId": null,
  "supplySource": "APPSTORE",
  "supplyPlacement": "APPSTORE_SEARCH_TAB",
  "countryOrRegion": "US",
  "languageCode": "en-US",
  "reasonType": "REJECTION_REASON",
  "reasonCode": "SCREENSHOT_NOT_REPRESENTATIVE",
  "comment": "Screenshot does not accurately represent the AwayFinder app experience.",
  "reasonLevel": "CUSTOM_PRODUCT_PAGE_LOCALE",
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000"
}
```

## Properties

- `id` (int64) *(required)*: System-assigned identifier for this rejection reason record. Read-only.
- `adamId` (int64): The Adam ID of the app whose product page triggered the rejection, if applicable. Read-only.
- `productPageId` (string): The product page ID associated with the rejection, if applicable. Read-only.
- `assetId` (string): The UUID of the asset that triggered the rejection, if applicable. Read-only.
- `supplySource` (string): Supply source for the rejection. Read-only.
- `supplyPlacement` (string): Supply placement for the rejection. Read-only.
- `countryOrRegion` (string): Country or region code. Read-only.
- `languageCode` (string): Language code. Read-only.
- `reasonType` (string): Type of rejection reason. Read-only.
- `reasonCode` (string): Code for the specific rejection reason. Read-only.
- `comment` (string): Additional context for the rejection. Nullable. Read-only.
- `reasonLevel` (string): The level at which the rejection applies. Possible values: `DEFAULT_PRODUCT_PAGE`, `DEFAULT_PRODUCT_PAGE_LOCALE`, `CUSTOM_PRODUCT_PAGE`, `CUSTOM_PRODUCT_PAGE_LOCALE`. Read-only.

## See Also

- [object Creative](creative.md)
  Ad creative containing all data for visually rendering an ad.
- [object CreativeCreate](creativecreate.md)
  The request body for creating a new Creative object.
- [object CreativeUpdate](creativeupdate.md)
  The request body for updating an existing Creative object.
- [object CreativeResponse](creativeresponse.md)
  The response object for an ad creative operation.
- [object CreativeQueryResponse](creativequeryresponse.md)
  The response object for a Creative query, containing matched results and pagination metadata.
- [object CreativeEligibility](creativeeligibility.md)
  Eligibility state for an ad creative across supply sources and placements.
- [object AssetReference](assetreference.md)
  A reference to an asset by its UUID.
- [object AssetImage](assetimage.md)
  Image-specific asset detail fields.
- [object Destination](destination.md)
  Post-tap destination entity embedded in a Creative.
- [object DestinationCreate](destinationcreate.md)
  Request payload for specifying the post-tap destination when creating an ad creative.
- [object DestinationParameter](destinationparameter.md)
  Destination-specific identifiers used when linking an ad creative to an App Store product page.
- [object CreativeRejectionReasonQueryRequest](creativerejectionreasonqueryrequest.md)
  The request body for querying ad creative rejection reasons.
- [object CreativeRejectionReasonQueryResponse](creativerejectionreasonqueryresponse.md)
  The response object for a creative rejection reason query, containing matched results and pagination metadata.
- [object LocaleInfo](localeinfo.md)
  Represents a specific language and its corresponding language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativerejectionreason)*