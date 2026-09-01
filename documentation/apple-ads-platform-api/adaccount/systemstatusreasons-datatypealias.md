# AdAccount.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Populated when `systemStatus` is not active.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AdAccount.SystemStatusReasons
```

#### Discussion

Reasons here can originate from the ad account’s own payment method or cascade down from the parent organization, as with `ORG_NO_PAYMENT_METHOD_ON_FILE`.

##### Example

```json
{
  "systemStatusReasons": ["PAYMENT_DECLINED"]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccount/systemstatusreasons-data.typealias)*