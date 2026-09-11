# setValue(_:at:)

**Framework**: USDKit  
**Kind**: method

Sets this attribute’s value at the given time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
func setValue<T>(_ value: T, at time: USDStage.TimeCode = .default) -> Bool where T : USDPrim.Attribute.Value
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/setvalue(_:at:))*