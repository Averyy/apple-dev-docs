# AESendPriority

**Framework**: Core Services  
**Kind**: tdef

Specifies the processing priority for a sent Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AESendPriority = Int16
```

#### Discussion

When you call the `AESend(_:_:_:_:_:_:_:)` function, you pass a value of type `AESendPriority` for the `sendPriority` parameter. [`Priority Constants for the AESend Function (Deprecated in macOS)`](apple_events/1542840-priority_constants_for_the_aesen.md) lists the valid constant values for a variable or parameter of this type. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aesendpriority)*