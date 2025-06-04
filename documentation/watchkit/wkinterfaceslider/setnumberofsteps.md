# setNumberOfSteps(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the number of steps for the slider.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setNumberOfSteps(_ numberOfSteps: Int)
```

#### Discussion

Each tap on the slider’s increment or decrement areas changes the slider value by one step. The value of each step is equal to the difference between the minimum and maximum values divided by the number of steps. For example, if the minimum value is `0`, the maximum value is `1`, and the number of steps is `10`, each step increments or decrements the value by `0.1`.

## Parameters

- `numberOfSteps`: The number of steps between the minimum and maximum value. If the slider’s value is continuous, calling this method has no effect.

## See Also

- [func setValue(Float)](wkinterfaceslider/setvalue(_:).md)
  Changes the value of the slider.
- [func setColor(UIColor?)](wkinterfaceslider/setcolor(_:).md)
  Sets the color of the slider bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setnumberofsteps(_:))*