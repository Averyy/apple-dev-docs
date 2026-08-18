# AssetReference

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A reference to an asset by its UUID.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AssetReference
```

#### Discussion

`AssetReference` is a pointer to an `Asset` by its system-generated UUID, used in ad creative specs and other contexts where only the asset identifier is required. To reference specific image or video assets without embedding the full `Asset` record, use it in ad creative spec objects, such as the `creativeAssets` array within an Apple Maps ad creative’s `creativeSpec`. The `assetId` must match an asset that already exists in the system.

##### Example

```json
{
  "assetId": "550e8400-e29b-41d4-a716-446655440000"
}
```

## Properties

- `assetId` (uuid): The ads-generated UUID for the unified asset. Example: `550e8400-e29b-41d4-a716-446655440000`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/assetreference)*