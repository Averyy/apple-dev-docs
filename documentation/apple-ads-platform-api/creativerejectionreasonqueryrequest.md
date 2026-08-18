# CreativeRejectionReasonQueryRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for querying ad creative rejection reasons.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeRejectionReasonQueryRequest
```

#### Discussion

`CreativeRejectionReasonQueryRequest` is the request body for querying ad creative rejection reasons.

##### Example

```json
{
  "filters": [
    {
      "field": "adamId",
      "operator": "EQUALS",
      "value": 123456789
    }
  ],
  "sorting": [
    {
      "field": "creationTime",
      "order": "DESC"
    }
  ],
  "pagination": {
    "pageSize": 20,
    "offset": 0
  }
}
```

## Properties

- `filters` ([QueryFilter]): Scopes results to specific ad creatives or rejection reason types. Accepts `QueryFilter` objects targeting filterable fields such as `adamId`, to retrieve rejection reasons for a specific app. See [`QueryFilter`](queryfilter.md).
- `sorting` ([QuerySort]): Standard `QueryRequest` sorting for the result set. See [`QuerySort`](querysort.md).
- `pagination` (QueryPagination): Standard `QueryRequest` pagination for navigating large result sets. See [`QueryPagination`](querypagination.md).

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
- [object CreativeRejectionReasonQueryResponse](creativerejectionreasonqueryresponse.md)
  The response object for a creative rejection reason query, containing matched results and pagination metadata.
- [object LocaleInfo](localeinfo.md)
  Represents a specific language and its corresponding language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativerejectionreasonqueryrequest)*