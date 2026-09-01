# AppsReportingCampaign.BillingEvent

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The billing event of the campaign at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AppsReportingCampaign.BillingEvent
```

#### Discussion

This determines which report metrics are actionable for cost analysis: `TAPS` billing pairs with tap-based cost metrics, while `IMPRESSIONS` billing pairs with CPM-based ones.

##### Example

```json
{
  "billingEvent": "TAPS"
}
```

See [`ReportingBillingEvent`](reportingbillingevent.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingcampaign/billingevent-data.typealias)*