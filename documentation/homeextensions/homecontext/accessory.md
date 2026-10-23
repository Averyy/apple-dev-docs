# accessory

**Framework**: HomeExtensions  
**Kind**: property  
**Role**: Instance Property

The accessory that a person selected in the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final var accessory: HMAccessory? { get set }
```

#### Discussion

This value is `nil` if the accessory isn’t available.

## See Also

### Getting context
- [var home: HMHome?](./home.md)
  The home that a person selected in the Home app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontext/accessory)*