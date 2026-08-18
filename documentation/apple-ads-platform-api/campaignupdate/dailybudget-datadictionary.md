# CampaignUpdate.DailyBudget

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request wrapper for updating a campaign’s daily budget amount.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignUpdate.DailyBudget
```

#### Discussion

To change a campaign’s daily spend cap, use this object. Submitting a new value replaces the current daily budget outright and does not affect `sharedBudgets`, which are managed independently.

See [`DailyBudgetUpdate`](dailybudgetupdate.md) for the full field reference.

## Properties

- `value` (Money): The new daily budget amount as a Money object with `amount` (decimal string) and ISO 4217 `currency` code. See [`Money`](money.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/dailybudget-data.dictionary)*