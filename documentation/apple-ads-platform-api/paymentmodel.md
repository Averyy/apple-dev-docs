# PaymentModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Enumeration of billing models that determine payment method and budget availability for an ad account.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string PaymentModel
```

## Possible Values

- `PAYG`: Pay as You Go. The default billing model when no payment model is configured. Budget orders are not available with this model.
- `LOC`: Line of Credit. A monthly invoicing model required to use budget orders. Invoicing details are available in [`InvoiceDetail`](./invoicedetail.md).

## See Also

- [type BudgetSystemStatus](./budgetsystemstatus.md)
  The system-derived operational state of a budget order.
- [type BudgetSystemStatusReason](./budgetsystemstatusreason.md)
  A reason code that explains why a budget or budget order has its current system status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/paymentmodel)*