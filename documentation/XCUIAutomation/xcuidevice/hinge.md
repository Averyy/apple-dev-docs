# hinge

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The device’s hinge, if it has one.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
nonisolated
var hinge: XCUIHinge? { get }
```

```objc
@property (strong, readonly, nullable) XCUIHinge * hinge;
```

## Discussion

This property is `nil` on devices that do not have a hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/hinge)*