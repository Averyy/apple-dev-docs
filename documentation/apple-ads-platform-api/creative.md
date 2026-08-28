# Creative

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad creative containing all data for visually rendering an ad.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Creative
```

#### Discussion

A `Creative` is the unit of visual presentation for an ad, composed of a pre-tap `creativeSpec` and a post-tap `destination`.

The `creativeType` field governs which `creativeSpec` variant applies:

- The `CUSTOM_PRODUCT_PAGE` and `DEFAULT_PRODUCT_PAGE` types use App Store product pages.
- The `LOCAL_ADS_SEARCH_CREATIVE` type is for Ads on Apple Maps.

The `systemStatus` field reflects the ad creative’s validation state:

- `VALID`: the ad creative can serve on an ad, though it may still be subject to additional review.
- `INVALID`: the ad creative has failed validation. For App Ads (`CUSTOM_PRODUCT_PAGE`, `DEFAULT_PRODUCT_PAGE`), you must create a new ad creative. For Apple Maps (`LOCAL_ADS_SEARCH_CREATIVE`), the ad creative may be recoverable by editing it (for example, adding a missing asset). Inspect `systemStatusReasons` to identify the cause.
- `PENDING`: the ad creative is undergoing system validation, policy determination, or waiting for asset CDN availability.

The system always returns the `eligibility` field unless you exclude it with the `fields` parameter. It summarizes whether the ad creative meets the requirements to serve ads on each supported ad placement.

Fields you can filter and sort on when querying ad creatives are listed in [`Query Ad Creatives`](post-creatives-query.md).

##### Example

```json
{
  "id": 666777888,
  "adAccountId": 123456789,
  "name": "AwayFinder - Summer Campaign Creative",
  "creativeType": "CUSTOM_PRODUCT_PAGE",
  "creativeSpec": {},
  "destination": {
    "destinationType": "APP_STORE_PRODUCT_PAGE",
    "parameters": {
      "adamId": "987654321",
      "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
    },
    "url": "https://apps.apple.com/us/app/id/987654321"
  },
  "systemStatus": "VALID",
  "systemStatusReasons": [],
  "creationTime": "2025-06-01T10:00:00.000",
  "modificationTime": "2025-06-01T10:00:00.000",
  "eligibility": {
    "status": "ELIGIBLE",
    "allowedGroups": [
      {
        "supplyPlacement": ["APPSTORE_SEARCH_RESULTS"],
        "countryOrRegion": ["US"]
      }
    ],
    "blockedGroups": []
  }
}
```

## Topics

### Dictionaries
- [object Creative.CreativeSpec](creative/creativespec-data.dictionary.md)
  Pre-tap ad experience specification with customizable attributes and assets.
- [object Creative.Destination](creative/destination-data.dictionary.md)
  Post-tap destination entity defining where users go after tapping the ad.
- [object Creative.Eligibility](creative/eligibility-data.dictionary.md)
  Eligibility data summarizing whether the ad creative meets requirements to serve ads.
### Type Aliases
- [type Creative.CreativeType](creative/creativetype-data.typealias.md)
  Type of ad creative, determining which ad placements it can serve on.
- [type Creative.SystemStatus](creative/systemstatus-data.typealias.md)
  System validation status reflecting whether the ad creative can serve.
- [type Creative.SystemStatusReasons](creative/systemstatusreasons-data.typealias.md)
  Reason codes explaining the ad creative’s current system status.

## Properties

- `id` (int64): Primary identifier. Read-only.
- `adAccountId` (int64): Reference to the Ad Account. System-assigned. Read-only.
- `name` (string): Name of the ad creative. Mutable.
- `creativeType` (Creative.CreativeType): Type of ad creative. Possible values: `CUSTOM_PRODUCT_PAGE`, `DEFAULT_PRODUCT_PAGE`, `LOCAL_ADS_SEARCH_CREATIVE`. See [`Creative.CreativeType`](creative/creativetype-data.typealias.md). Immutable after creation.
- `creativeSpec` (Creative.CreativeSpec): Pre-tap ad experience specification with customizable attributes and assets. Contains data used to render the ad before user interaction. Empty for Product Page ad creatives (`CUSTOM_PRODUCT_PAGE` or `DEFAULT_PRODUCT_PAGE`) since pre-tap isn’t customizable. For `LOCAL_ADS_SEARCH_CREATIVE` the `creativeSpec` carries the Apple Maps ad creative spec (brand ID, asset references, and localized text). Not every sub-field within `creativeSpec` is mutable. Partially mutable.
- `destination` (Creative.Destination): Post-tap destination entity (embedded). Defines where users go after tapping the ad (for example, App Store product page). See [`Creative.Destination`](creative/destination-data.dictionary.md). Immutable after creation.
- `systemStatus` (Creative.SystemStatus): System validation status. Possible values: `VALID`, `INVALID`, `PENDING`. Read-only.
- `systemStatusReasons` ([Creative.SystemStatusReasons]): Reasons for system status. Read-only.
- `creationTime` (date-time): Creation timestamp. Read-only.
- `modificationTime` (date-time): Last modification timestamp. Read-only.
- `deleted` (boolean): Whether the ad creative has been deleted. Excluded from query results by default unless explicitly filtered to `true`. Read-only.
- `eligibility` (Creative.Eligibility): Eligibility data. Always returned unless excluded via `fields` parameter. See [`CreativeEligibility`](creativeeligibility.md). Read-only.

## See Also

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
- [object CreativeRejectionReason](creativerejectionreason.md)
  Detailed rejection reason for an ad creative that failed Apple review.
- [object CreativeRejectionReasonQueryRequest](creativerejectionreasonqueryrequest.md)
  The request body for querying ad creative rejection reasons.
- [object CreativeRejectionReasonQueryResponse](creativerejectionreasonqueryresponse.md)
  The response object for a creative rejection reason query, containing matched results and pagination metadata.
- [object LocaleInfo](localeinfo.md)
  Represents a specific language and its corresponding language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative)*