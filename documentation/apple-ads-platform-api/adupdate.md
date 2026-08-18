# AdUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating an existing Ad object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdUpdate
```

#### Discussion

To modify an existing ad, use `AdUpdate` with `PUT /v1/ads/{id}`. You can change only `name` and `status` after creation. The system locks in the ad’s creative, ad group, campaign, and ad account at creation. Omit any field you don’t want to update.

Setting `status` to `PAUSED` immediately stops the ad from entering auctions. Switching it back to `ENABLED` resumes participation.

##### Example

```json
{
  "name": "AwayFinder Summer Sale Ad",
  "status": "PAUSED"
}
```

## Topics

### Type Aliases
- [type AdUpdate.Status](adupdate/status-data.typealias.md)
  Advertiser-configurable status set when updating an ad.

## Properties

- `name` (string): Must be at least 1 character long if provided. Mutable.
- `status` (AdUpdate.Status): See [`AdStatus`](adstatus.md). Mutable.

## See Also

- [object Ad](ad.md)
  Ad entity that links an ad creative to an ad group for serving.
- [object AdCreate](adcreate.md)
  The request body for creating a new Ad object.
- [object AdResponse](adresponse.md)
  The response object for an Ad operation.
- [object AdQueryResponse](adqueryresponse.md)
  The response object for an Ad query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adupdate)*