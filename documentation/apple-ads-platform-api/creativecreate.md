# CreativeCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for creating a new Creative object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeCreate
```

#### Discussion

Creating an ad creative defines the visual presentation and destination for an ad, before you ever attach it to an ad group. An ad creative isn’t tied to a campaign or ad group at creation, so you can reuse the same ad creative across multiple ads later.

Pick `creativeType` before filling in `creativeSpec` and `destination`, since it determines the required shape of both.

##### Example

```json
{
  "name": "AwayFinder - Summer Campaign Creative",
  "creativeType": "CUSTOM_PRODUCT_PAGE",
  "creativeSpec": {},
  "destination": {
    "destinationType": "APP_STORE_PRODUCT_PAGE",
    "parameters": {
      "adamId": "987654321",
      "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
    }
  }
}
```

## Topics

### Dictionaries
- [object CreativeCreate.CreativeSpec](creativecreate/creativespec-data.dictionary.md)
  The ad creative spec object matching the ad creative type being created.
- [object CreativeCreate.Destination](creativecreate/destination-data.dictionary.md)
  The post-tap landing experience specified when creating an ad creative.
### Type Aliases
- [type CreativeCreate.CreativeType](creativecreate/creativetype-data.typealias.md)
  Type of ad creative to create. Determines the shape of `creativeSpec`.

## Properties

- `name` (string) *(required)*: Name of the ad creative.
- `creativeType` (CreativeCreate.CreativeType) *(required)*: Type of ad creative. Determines the shape of `creativeSpec`. Immutable after creation. Possible values: `CUSTOM_PRODUCT_PAGE`, `DEFAULT_PRODUCT_PAGE`, `LOCAL_ADS_SEARCH_CREATIVE`. See [`CreativeCreate.CreativeType`](creativecreate/creativetype-data.typealias.md).
- `creativeSpec` (CreativeCreate.CreativeSpec): Provide the matching spec object for the ad creative type being created. Required when `creativeType` is `LOCAL_ADS_SEARCH_CREATIVE`. See [`CreativeCreate.CreativeSpec`](creativecreate/creativespec-data.dictionary.md).
- `destination` (CreativeCreate.Destination) *(required)*: The post-tap landing experience. For App Store placements, include `adamId` in `destination.parameters`. For Custom Product Page campaigns, also include `productPageId`. See [`DestinationCreate`](destinationcreate.md).

## See Also

- [object Creative](creative.md)
  Ad creative containing all data for visually rendering an ad.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativecreate)*