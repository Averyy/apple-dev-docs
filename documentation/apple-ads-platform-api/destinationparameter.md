# DestinationParameter

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Destination-specific identifiers used when linking an ad creative to an App Store product page.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DestinationParameter
```

#### Discussion

[`Destination`](destination.md) and [`DestinationCreate`](destinationcreate.md) embed `DestinationParameter`. It supplies the app and product page identifiers needed to route a tapped ad to the correct App Store listing. For non-App Store destination types (such as `LOCAL_ADS_PLACECARD`), omit this object.

##### Example

```json
{
  "adamId": "987654321",
  "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
}
```

## Properties

- `adamId` (string): The App Store app identifier. This is the `promotedObjectId` on the campaign for App Store campaigns. Required for `APP_STORE_PRODUCT_PAGE` destinations.
- `productPageId` (string): The UUID of a Custom Product Page created in App Store Connect. Omit to use the default product page.

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
- [object CreativeRejectionReason](creativerejectionreason.md)
  Detailed rejection reason for an ad creative that failed Apple review.
- [object CreativeRejectionReasonQueryRequest](creativerejectionreasonqueryrequest.md)
  The request body for querying ad creative rejection reasons.
- [object CreativeRejectionReasonQueryResponse](creativerejectionreasonqueryresponse.md)
  The response object for a creative rejection reason query, containing matched results and pagination metadata.
- [object LocaleInfo](localeinfo.md)
  Represents a specific language and its corresponding language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationparameter)*