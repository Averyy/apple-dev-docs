# stop()

**Framework**: WatchKit  
**Kind**: method

Stops updates to the timer’s display.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func stop()
```

#### Discussion

Use this method to stop updates to the timer object’s label. This method does not stop the timer from counting. The timer continues counting to or from its target value even when updates to the label are not occurring.

## See Also

- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/start()))
  Begins updates to the timer’s display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/stop())*