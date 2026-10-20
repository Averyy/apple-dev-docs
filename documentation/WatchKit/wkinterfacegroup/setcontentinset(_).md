# setContentInset(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the distance between the edges of the group and any contained objects.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setContentInset(_ contentInset: UIEdgeInsets)
```

```objc
- (void) setContentInset:(UIEdgeInsets) contentInset;
```

#### Discussion

Use this method to change the default insets you set in Interface Builder. Changes to the content insets of a group are animatable.

## Parameters

- `contentInset`: The insets to apply to contained objects. All inset values are measured in points. Inset values must not be less than `0`.

## See Also

### Setting the Layout Information
- [func setCornerRadius(CGFloat)](./setcornerradius%28_%29.md)
  Changes the radius to use when drawing rounded corners for the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setcontentinset(_:))*