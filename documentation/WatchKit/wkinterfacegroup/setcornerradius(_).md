# setCornerRadius(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Changes the radius to use when drawing rounded corners for the group.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setCornerRadius(_ cornerRadius: CGFloat)
```

```objc
- (void) setCornerRadius:(CGFloat) cornerRadius;
```

#### Discussion

Setting the radius to a value greater than `0.0` causes the group to draw rounded corners on its background. When a corner radius is applied, the group’s background color or image are clipped accordingly.

The default corner radius for groups is 6 points.

## Parameters

- `cornerRadius`: The radius (in points) of the circle used to round the corners of the groups edges.

## See Also

### Setting the Layout Information
- [func setContentInset(UIEdgeInsets)](./setcontentinset%28_%29.md)
  Sets the distance between the edges of the group and any contained objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setcornerradius(_:))*