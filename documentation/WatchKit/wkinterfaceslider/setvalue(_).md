# setValue(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Changes the value of the slider.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setValue(_ value: Float)
```

```objc
- (void) setValue:(float) value;
```

## Parameters

- `value`: The new value for the slider. If the new value is outside of the slider’s acceptable range, this method clamps the new value to the minimum or maximum value.

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Setting the Slider Value
- [func setColor(UIColor?)](./setcolor%28_%29.md)
  Sets the color of the slider bar.
- [func setNumberOfSteps(Int)](./setnumberofsteps%28_%29.md)
  Sets the number of steps for the slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setvalue(_:))*