# setValue(_:)

**Framework**: Watchkit  
**Kind**: method

Changes the value of the slider.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setValue(_ value: Float)
```

## Parameters

- `value`: The new value for the slider. If the new value is outside of the slider’s acceptable range, this method clamps the new value to the minimum or maximum value.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setColor(UIColor?)](setcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setcolor(_:)))
- [func setNumberOfSteps(Int)](setnumberofsteps(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setnumberofsteps(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setvalue(_:))*