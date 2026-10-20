# setTextColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the color of the timer’s text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

```objc
- (void) setTextColor:(UIColor *) color;
```

## Parameters

- `color`: The custom color to apply to the timer string. Specifying `nil` removes the custom color and returns the text to the color specified in the storyboard file. The default text color is white.

## See Also

### Configuring the Timer Attributes
- [func setDate(Date)](./setdate%28_%29.md)
  Changes the start time for the timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/settextcolor(_:))*