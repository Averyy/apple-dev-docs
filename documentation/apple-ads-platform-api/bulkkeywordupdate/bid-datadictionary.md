# BulkKeywordUpdate.Bid

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The updated keyword-level bid amount for a bulk keyword update item.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BulkKeywordUpdate.Bid
```

#### Discussion

The updated keyword-level bid amount for a bulk keyword update item, expressed as a `Money` object with `amount` and `currency`. It overrides the ad group’s default bid for this keyword. This bid is not used with Maximize Conversions bid strategy campaigns.

See [`BulkKeywordUpdate`](bulkkeywordupdate.md) for the full field reference.

## Properties

- `currency` (string): The ISO 4217 currency code (for example, `"USD"`, `"EUR"`). Must match the ad account’s currency.
- `amount` (string) *(required)*: The monetary amount as a decimal string (for example, `"10.00"`), represented as a string to preserve decimal precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkkeywordupdate/bid-data.dictionary)*