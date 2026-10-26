# detectsPhoneNumbers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether telephone number detection is on.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`dataDetectorTypes`](./datadetectortypes.md) instead.

## Declaration

```objc
@property (nonatomic) BOOL detectsPhoneNumbers;
```

#### Discussion

If [`true`](../../Swift/true.md), telephone number detection is on; otherwise, [`false`](../../Swift/false.md). If a webpage contains numbers that can be interpreted as phone numbers, but are not phone numbers, you can turn off telephone number detection by setting this property to [`false`](../../Swift/false.md). The default value is [`true`](../../Swift/true.md) on devices that have phone capabilities.

##### Special considerations

The functionality provided by this property has been superseded by the [`dataDetectorTypes`](./datadetectortypes.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/detectsphonenumbers)*