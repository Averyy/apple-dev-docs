# start()

**Framework**: Watchkit  
**Kind**: method

Begins updates to the timer’s display.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func start()
```

#### Discussion

After setting the target date for the timer, call this method to begin updating the timer object’s displayed text. Further updates to the timer occur automatically on the user’s Apple Watch, without the need for you to do anything else.

This method does not actually affect the actual timer value. The timer begins counting when you set the target date using the [`setDate(_:)`](wkinterfacetimer/setdate(_:).md) method. This method tells WatchKit to start updating the label containing the timer’s value.

## See Also

- [func stop()](wkinterfacetimer/stop.md)
  Stops updates to the timer’s display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/start())*