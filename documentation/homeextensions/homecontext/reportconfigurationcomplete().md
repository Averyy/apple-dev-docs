# reportConfigurationComplete()

**Framework**: HomeExtensions  
**Kind**: method  
**Role**: Instance Method

Tells the Home app that the accessory’s configuration is complete.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final func reportConfigurationComplete() async
```

#### Discussion

Call this method from your [`HomeAccessoryConfiguration`](../homeaccessoryconfiguration.md) content when a person finishes setting up the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontext/reportconfigurationcomplete())*