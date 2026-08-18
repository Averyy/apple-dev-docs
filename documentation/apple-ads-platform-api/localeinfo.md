# LocaleInfo

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Represents a specific language and its corresponding language code.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object LocaleInfo
```

#### Discussion

`LocaleInfo` pairs a two-letter language identifier with its full BCP-47 locale code. Use it when you need to communicate both the base language (`language`) and the regional variant (`languageCode`) together, for example when enumerating the locales supported by a product page or brand creative.

The `language` field corresponds to the ISO 639-1 language code (e.g., `en`, `fr`, `ja`), while `languageCode` includes the region subtag as required by BCP-47 (e.g., `en-US`, `fr-FR`, `ja-JP`). When building locale-aware creative specs, use `languageCode` as the map key in `localizedText` structures.

##### Example

```json
{
  "language": "en",
  "languageCode": "en-US"
}
```

## Properties

- `language` (string): Language identifier (e.g., “en”, “es”). Read-only.
- `languageCode` (string): BCP-47 language code (e.g., “en-US”, “es-MX”). Read-only.

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
- [object CreativeRejectionReason](creativerejectionreason.md)
  Detailed rejection reason for an ad creative that failed Apple review.
- [object CreativeRejectionReasonQueryRequest](creativerejectionreasonqueryrequest.md)
  The request body for querying ad creative rejection reasons.
- [object CreativeRejectionReasonQueryResponse](creativerejectionreasonqueryresponse.md)
  The response object for a creative rejection reason query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/localeinfo)*