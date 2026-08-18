# CreativeUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating an existing Creative object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeUpdate
```

#### Discussion

To change an existing ad creative’s `name` or `creativeSpec`, use `CreativeUpdate` with `PUT /v1/creatives/{id}`. `creativeType` and `destination` are locked in at creation and can’t be changed later.

##### Example

```json
{
  "name": "AwayFinder - Summer Campaign Creative - Revised",
  "creativeSpec": {
    "localizedText": {
      "en-US": {
        "promoText": "New summer deals - shop now!"
      }
    },
    "brandId": "111222",
    "defaultLocale": "en-US"
  }
}
```

## Topics

### Dictionaries
- [object CreativeUpdate.CreativeSpec](creativeupdate/creativespec-data.dictionary.md)
  The creative spec fields that can be updated after creation.

## Properties

- `name` (string): Name of the ad creative. Omit if you do not intend to update. Mutable, Optional.
- `creativeSpec` (CreativeUpdate.CreativeSpec): The creative spec. Updating this may trigger re-review. `systemStatus` transitions back to `PENDING`. Omit if you do not intend to update. Mutable, Optional.

## See Also

- [object Creative](creative.md)
  Ad creative containing all data for visually rendering an ad.
- [object CreativeCreate](creativecreate.md)
  The request body for creating a new Creative object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativeupdate)*