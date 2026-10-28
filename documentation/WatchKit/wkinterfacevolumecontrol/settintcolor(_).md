# setTintColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the volume control’s tint color.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func setTintColor(_ tintColor: UIColor?)
```

```objc
- (void) setTintColor:(UIColor *) tintColor;
```

## Discussion

The system only applies the tint color to the control’s default state (when the crown is not being used to adjust the volume).

## Parameters

- `tintColor`: The tint color for the volume control. If `nil`, the system uses the app’s tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/settintcolor(_:))*