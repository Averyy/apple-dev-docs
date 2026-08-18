# CreativeQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a Creative query, containing matched results and pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeQueryResponse
```

#### Discussion

`CreativeQueryResponse` is returned by the ad creatives query endpoint and contains the filtered, sorted, and paginated set of `Creative` objects matching the request.

To scope results by `adAccountId`, `creativeType`, `systemStatus`, or other filterable fields, use the `QueryRequest` body with `filters`.

##### Example

```json
{
  "result": [
    {
      "id": 666777888,
      "adAccountId": 123456789,
      "name": "AwayFinder - Summer Campaign Creative",
      "creativeType": "CUSTOM_PRODUCT_PAGE",
      "systemStatus": "VALID",
      "deleted": false,
      "creationTime": "2025-06-01T10:00:00.000",
      "modificationTime": "2025-06-01T10:00:00.000"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` ([Creative]): The matching `Creative` records. See [`Creative`](creative.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the response, including `offset`, `pageSize`, and `totalCount`. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error information if the request encountered an error. See [`Error`](error.md). Read-only.

## See Also

- [object Creative](creative.md)
  Ad creative containing all data for visually rendering an ad.
- [object CreativeCreate](creativecreate.md)
  The request body for creating a new Creative object.
- [object CreativeUpdate](creativeupdate.md)
  The request body for updating an existing Creative object.
- [object CreativeResponse](creativeresponse.md)
  The response object for an ad creative operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativequeryresponse)*