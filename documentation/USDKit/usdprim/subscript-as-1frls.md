# subscript(_:as:)

**Framework**: USDKit  
**Kind**: subscript

Access or modify the value of a named attribute on this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript<T>(attributeName: USDToken, as type: T.Type) -> T? where T : USDPrim.Attribute.Value { get nonmutating set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/subscript(_:as:)-1frls)*