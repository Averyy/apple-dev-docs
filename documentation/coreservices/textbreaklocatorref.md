# TextBreakLocatorRef

**Framework**: Core Services  
**Kind**: tdef

Refers to an opaque object that encapsulates locale and text-break information for the purpose of finding boundaries in Unicode text.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias TextBreakLocatorRef = OpaquePointer
```

#### Discussion

You can obtain a `TextBreakLocatorRef` value from the function  [`UCCreateTextBreakLocator`](1390362-uccreatetextbreaklocator.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/textbreaklocatorref)*