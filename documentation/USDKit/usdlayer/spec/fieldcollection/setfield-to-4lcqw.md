# setField(_:to:)

**Framework**: USDKit  
**Kind**: method

Typed field setter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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