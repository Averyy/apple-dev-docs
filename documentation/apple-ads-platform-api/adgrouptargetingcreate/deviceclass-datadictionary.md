# AdGroupTargetingCreate.DeviceClass

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Device class targeting (for example, `IPHONE` or `IPAD`).

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingCreate.DeviceClass
```

#### Discussion

Used with App Store campaigns. Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

```json
"deviceClass": {
  "include": ["IPHONE"]
}
```

## Properties

- `include` ([string]): Device class values (`IPHONE` or `IPAD`) restricting delivery to those devices. Mutable.
- `exclude` ([string]): Has no effect. `deviceClass` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingcreate/deviceclass-data.dictionary)*