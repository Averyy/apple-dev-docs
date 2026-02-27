# BudgetOrderUpdate.Bo

**Framework**: Apple Ads  
**Kind**: dictionary

The response to a  request to update a budget order.

**Availability**:
- Search Ads 4.11+

## Declaration

```swift
object BudgetOrderUpdate.Bo
```

## Properties

- `billingEmail` (string): The billing email. This field is updatable.
- `budget` (Money): The total budget amount available for the budget order. This field is updatable.
- `clientName` (string): The advertiser or product. This is a requirement for agency-type accounts. This field is updatable only before the startDate of a campaign.
- `endDate` (date-time): The scheduled end date and time for the budget order in the format of `yyyy-mm-dd’T’HH:MM:SS.SSS`. This field is updatable.
- `name` (string): The name of the budget order, which is unique within an organization. This field is updatable only before the startDate of a campaign.
- `orderNumber` (string): A purchase order number. This is a requirement for agency-type accounts. This field is updatable only before the startDate of a campaign.
- `primaryBuyerEmail` (string): The primary buyer’s email address. This field is updatable.
- `primaryBuyerName` (string): The primary buyer’s name. This field is updatable.
- `startDate` (date-time): The scheduled start date and time for the budget order in the format of `yyyy-mm-dd’T’HH:MM:SS.SSS`. This field is updatable only before the startDate of a campaign and is only editable if there are no campaigns assigned to the budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/budgetorderupdate/bo-data.dictionary)*