# CampaignCreate.DailyBudget

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request wrapper for setting a campaign’s daily budget at creation time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignCreate.DailyBudget
```

#### Discussion

Sets the daily spend cap for a new campaign at creation time, using a `Money` object.

See [`DailyBudgetCreate`](dailybudgetcreate.md) for the full field reference and behavior.

## Properties

- `value` (Money): The daily budget amount as a Money object with `amount` (decimal string) and ISO 4217 `currency` code. See [`Money`](money.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/dailybudget-data.dictionary)*