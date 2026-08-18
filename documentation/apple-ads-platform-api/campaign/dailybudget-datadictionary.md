# Campaign.DailyBudget

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Daily budget cap for a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Campaign.DailyBudget
```

#### Discussion

A `Money` object specifying the campaign’s daily spend cap. Once the daily budget is exhausted, the campaign stops delivering ads for the remainder of that day. `dailyBudget` is required on all campaigns. A shared budget assignment, if any, enforces a separate flight-period cap independently.

## Properties

- `value` (Money): The daily budget amount as a Money object with amount and ISO 4217 currency code. The currency must match the ad account’s currency. See [`Money`](money.md). Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/dailybudget-data.dictionary)*