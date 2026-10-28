# setImageData(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the displayed image using a formatted data object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setImageData(_ imageData: Data?)
```

```objc
- (void) setImageData:(NSData *) imageData;
```

## Discussion

This method changes the image being displayed.

When setting images, always try to use images that are sized to fit the available space. Images are rendered according to the mode and size attributes you set for the image interface object.

## Parameters

- `imageData`: A data object containing the image data in its native format. Specifying `nil` removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image.

## See Also

### Configuring the Image
- [func setImage(UIImage?)](./setimage%28_%29.md)
  Sets the displayed image using the specified image object.
- [func setImageNamed(String?)](./setimagenamed%28_%29.md)
  Sets the displayed image using a named image resource file.
- [func setTintColor(UIColor?)](./settintcolor%28_%29.md)
  Changes the color applied to a template image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimagedata(_:))*