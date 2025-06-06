# Get a Budget Order

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches a specific budget order using a budget order identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

This call retrieves a specific assigned budget order for your organization. It also returns completed and canceled orders. Budget orders also return when you use the [`Create a Campaign`](create-a-campaign.md) or [`Update a Campaign`](update-a-campaign.md) endpoints.

You can’t set budget order invoicing through the API. You can only fetch a budget order using Get a Budget Order or [`Get All Budget Orders`](get-all-budget-orders.md).

##### Payload Example Get a Budget Order

## See Also

- [Create a Budget Order](create-a-budget-order.md)
  Creates a budget order in the context of your org ID.
- [Update a Budget Order](update-a-budget-order.md)
  Updates an existing budget order.
- [Get All Budget Orders](get-all-budget-orders.md)
  Fetches all assigned budget orders for an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/get-a-budget-order)*