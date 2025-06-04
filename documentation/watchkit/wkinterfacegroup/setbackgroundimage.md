# setBackgroundImage(_:)

**Framework**: WatchKit  
**Kind**: method

Changes the background image of the group container to the specified image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImage(_ image: UIImage?)
```

## Parameters

- `image`: The background image to be displayed behind all items in the group. Specifying   removes the existing image, causing the background color to show through. You may specify an image object that contains multiple images running as an animation.

## See Also

- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundcolor(_:)))
  Changes the background color for the group container.
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagedata(_:)))
  Changes the background image of the group container to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagenamed(_:)))
  Changes the background image of the group container to the image in the specified resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimage(_:))*