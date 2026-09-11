# value(at:)

**Framework**: USDKit  
**Kind**: method

Returns this attribute’s value at the given time, or `nil` if unauthored.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func value<T>(at time: USDStage.TimeCode = .default) -> T? where T : USDPrim.Attribute.Value
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/value(at:))*