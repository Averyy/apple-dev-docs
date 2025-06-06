# setCornerRadius(_:)

**Framework**: Watchkit  
**Kind**: method

Changes the radius to use when drawing rounded corners for the group.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setCornerRadius(_ cornerRadius: CGFloat)
```

#### Discussion

Setting the radius to a value greater than `0.0` causes the group to draw rounded corners on its background. When a corner radius is applied, the group’s background color or image are clipped accordingly.

The default corner radius for groups is 6 points.

## Parameters

- `cornerRadius`: The radius (in points) of the circle used to round the corners of the groups edges.

## See Also

- [func setContentInset(UIEdgeInsets)](wkinterfacegroup/setcontentinset(_:).md)
  Sets the distance between the edges of the group and any contained objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setcornerradius(_:))*