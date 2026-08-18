# BulkKeywordCreate.Bid

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The keyword-level bid amount for a bulk keyword create item.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BulkKeywordCreate.Bid
```

#### Discussion

The keyword-level bid amount for a bulk keyword create item, expressed as a `Money` object with `amount` and `currency`. It overrides the ad group’s default bid for this keyword. Omit the field or pass `null` to default to the ad group’s `BidStrategy` bid instead. This bid is not used with Maximize Conversions bid strategy campaigns.

See [`BulkKeywordCreate`](bulkkeywordcreate.md) for the full field reference.

See also [`Money`](money.md) for the amount and currency structure.

## Properties

- `currency` (string): The ISO 4217 currency code (for example, `"USD"`, `"EUR"`). Must match the ad account’s currency.
- `amount` (string) *(required)*: The monetary amount as a decimal string (for example, `"10.00"`), represented as a string to preserve decimal precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkkeywordcreate/bid-data.dictionary)*