# setBackgroundImageNamed(_:)

**Framework**: WatchKit  
**Kind**: method

Changes the background image of the group container to the image in the specified resource file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImageNamed(_ imageName: String?)
```

#### Discussion

This method looks for an image with the specified name in the Watch app’s bundle and uses it as the background image for the group. If the specified image cannot be found, the group displays no background image.

## Parameters

- `imageName`: The name of the image to be loaded from the WatchKit app’s bundle. For images in the bundle, specify the filename of the image and include the filename extension in the name. You may specify an image file that contains multiple images running as an animation.

## See Also

- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundcolor(_:)))
  Changes the background color for the group container.
- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimage(_:)))
  Changes the background image of the group container to the specified image.
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagedata(_:)))
  Changes the background image of the group container to the image in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagenamed(_:))*