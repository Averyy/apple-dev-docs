# Destination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Post-tap destination entity embedded in a Creative.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Destination
```

#### Discussion

`Destination` specifies where a tap on the ad sends users. The `destinationType` field is immutable after creation, so changing the destination type requires creating a new ad creative.

For Ads on Apple Maps, `LOCAL_ADS_PLACECARD` is the supported `destinationType`, directing users to the brand’s Maps place card.

##### Example

```json
{
  "destinationType": "APP_STORE_PRODUCT_PAGE",
  "parameters": {
    "adamId": "987654321",
    "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
  },
  "url": "https://apps.apple.com/us/app/id/987654321"
}
```

## Topics

### Dictionaries
- [object Destination.Parameters](destination/parameters-data.dictionary.md)
  Destination-specific parameters for the post-tap experience.
### Type Aliases
- [type Destination.DestinationType](destination/destinationtype-data.typealias.md)
  The type of post-tap destination.

## Properties

- `destinationType` (Destination.DestinationType): The type of post-tap destination. See [`Destination.DestinationType`](destination/destinationtype-data.typealias.md). Immutable after creation.
- `parameters` (Destination.Parameters): Destination-specific parameters. Sub-fields: adamId (App Store app identifier, required), productPageId (UUID of a Custom Product Page created in App Store Connect, nullable string UUID, omit to use the default product page). Immutable after creation.
- `url` (string): The resolved destination URL. Read-only, computed by the system from `destinationType` and `parameters`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destination)*