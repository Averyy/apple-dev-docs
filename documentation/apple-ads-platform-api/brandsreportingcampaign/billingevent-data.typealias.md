# BrandsReportingCampaign.BillingEvent

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The billing event of the campaign at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingCampaign.BillingEvent
```

## Possible Values

- `TAPS`: The campaign is charged per tap.
- `IMPRESSIONS`: The campaign is charged per thousand impressions (CPM).

## Discussion

Brands campaigns can use either billing model, so check this field before comparing cost-per-tap and cost-per-impression figures across rows.

### Example

```json
{
  "billingEvent": "TAPS"
}
```

See [`ReportingBillingEvent`](../reportingbillingevent.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign/billingevent-data.typealias)*