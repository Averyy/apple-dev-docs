# setField(_:to:)

**Framework**: USDKit  
**Kind**: method

Typed field setter.

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
func setField<T>(_ name: USDToken, to value: T) -> Bool where T : USDValueProtocol
```

#### Return Value

`true` on success.

## Parameters

- `name`: The field name to author.
- `value`: The typed value to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec/fieldcollection/setfield(_:to:)-4lcqw)*