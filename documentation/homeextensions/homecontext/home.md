# home

**Framework**: HomeExtensions  
**Kind**: property  
**Role**: Instance Property

The home that a person selected in the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
final var home: HMHome? { get set }
```

## Discussion

This value is `nil` if the home isn’t available.

## See Also

### Getting context
- [var accessory: HMAccessory?](./accessory.md)
  The accessory that a person selected in the Home app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontext/home)*