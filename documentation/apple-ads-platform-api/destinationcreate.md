# DestinationCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request payload for specifying the post-tap destination when creating an ad creative.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DestinationCreate
```

#### Discussion

[`CreativeCreate`](creativecreate.md) embeds `DestinationCreate` to define where users go after tapping the ad.

##### Example

```json
{
  "destinationType": "APP_STORE_PRODUCT_PAGE",
  "parameters": {
    "adamId": "123456789",
    "productPageId": "987654321"
  }
}
```

## Topics

### Dictionaries
- [object DestinationCreate.Parameters](destinationcreate/parameters-data.dictionary.md)
  Destination-specific parameters supplied when creating an ad creative.
### Type Aliases
- [type DestinationCreate.DestinationType](destinationcreate/destinationtype-data.typealias.md)
  The type of post-tap destination to create.

## Properties

- `destinationType` (DestinationCreate.DestinationType) *(required)*: The type of post-tap destination. See [`DestinationCreate.DestinationType`](destinationcreate/destinationtype-data.typealias.md). Immutable after creation.
- `parameters` (DestinationCreate.Parameters): Destination-specific parameters. For App Store destinations, provide `adamId` and optionally `productPageId` to link to a Custom Product Page. See [`DestinationParameter`](destinationparameter.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationcreate)*