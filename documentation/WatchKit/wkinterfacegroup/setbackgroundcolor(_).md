# setBackgroundColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Changes the background color for the group container.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundColor(_ color: UIColor?)
```

```objc
- (void) setBackgroundColor:(UIColor *) color;
```

## Discussion

If you do not specify a custom background color or if you set the custom color to `nil`, the group uses the color assigned to the group object in your storyboard file. The default background color is clear.

If you set a custom background image for the group, the image is displayed on top of the background color. If the image contains any transparency, the background color shows through the transparent portions of the image.

Changes to the background color of a group are animatable.

## Parameters

- `color`: The solid background color to be displayed behind all items in the group. Specify `nil` to remove the custom color you previously set using this method.

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Setting the Group’s Content
- [func setBackgroundImage(UIImage?)](./setbackgroundimage%28_%29.md)
  Changes the background image of the group container to the specified image.
- [func setBackgroundImageData(Data?)](./setbackgroundimagedata%28_%29.md)
  Changes the background image of the group container to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](./setbackgroundimagenamed%28_%29.md)
  Changes the background image of the group container to the image in the specified resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundcolor(_:))*