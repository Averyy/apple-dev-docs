# setNumberOfSteps(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the number of steps for the slider.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setNumberOfSteps(_ numberOfSteps: Int)
```

## Overview

Each tap on the slider’s increment or decrement areas changes the slider value by one step. The value of each step is equal to the difference between the minimum and maximum values divided by the number of steps. For example, if the minimum value is `0`, the maximum value is `1`, and the number of steps is `10`, each step increments or decrements the value by `0.1`.

## Parameters

- `numberOfSteps`: The number of steps between the minimum and maximum value. If the slider’s value is continuous, calling this method has no effect.

## See Also

- [func setValue(Float)](setvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setvalue(_:)))
- [func setColor(UIColor?)](setcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setcolor(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setnumberofsteps(_:))*