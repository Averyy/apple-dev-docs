# subscript(_:as:)

**Framework**: USDKit  
**Kind**: subscript

Access or modify the value of a named attribute on this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
subscript<T>(attributeName: USDToken, as type: T.Type) -> T? where T : USDPrim.Attribute.Value { get nonmutating set }
```

#### Overview

If the attribute has time samples, this subscript operates at the [`default`](usdstage/timecode/default.md) time code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/subscript(_:as:)-1frls)*