# setBackgroundImage(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Changes the background image of the group container to the specified image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImage(_ image: UIImage?)
```

```objc
- (void) setBackgroundImage:(UIImage *) image;
```

## Parameters

- `image`: The background image to be displayed behind all items in the group. Specifying `nil` removes the existing image, causing the background color to show through. You may specify an image object that contains multiple images running as an animation.

## See Also

### Setting the Group’s Content
- [func setBackgroundColor(UIColor?)](./setbackgroundcolor%28_%29.md)
  Changes the background color for the group container.
- [func setBackgroundImageData(Data?)](./setbackgroundimagedata%28_%29.md)
  Changes the background image of the group container to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](./setbackgroundimagenamed%28_%29.md)
  Changes the background image of the group container to the image in the specified resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimage(_:))*