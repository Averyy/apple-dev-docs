# tap(withNumberOfTaps:numberOfTouches:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends one or more taps with one or more touch points.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- watchOS
- Xcode 16.3+

## Declaration

```swift
func tap(withNumberOfTaps numberOfTaps: Int, numberOfTouches: Int)
```

```objc
- (void) tapWithNumberOfTaps:(NSUInteger) numberOfTaps numberOfTouches:(NSUInteger) numberOfTouches;
```

## Parameters

- `numberOfTaps`: The number of taps.
- `numberOfTouches`: The number of touch points.

## See Also

### Tapping multiple times
- [func twoFingerTap()](./twofingertap%28%29.md)
  Sends a two-finger tap event to a hittable point the system computes for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/tap(withnumberoftaps:numberoftouches:))*