# setFinishedSelectedImage:withFinishedUnselectedImage:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the finished selected and unselected images.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`image`](../uibaritem/image.md) and [`selectedImage`](./selectedimage.md) with [`UIImage.RenderingMode.alwaysOriginal`](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) instead.

## Declaration

```objc
- (void) setFinishedSelectedImage:(UIImage *) selectedImage withFinishedUnselectedImage:(UIImage *) unselectedImage;
```

## Parameters

- `selectedImage`: The finished selected image.
- `unselectedImage`: The finished unselected image.

## See Also

### Deprecated
- [- finishedSelectedImage](./finishedselectedimage.md)
  Returns the finished selected image.
- [- finishedUnselectedImage](./finishedunselectedimage.md)
  Returns the finished unselected image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/setfinishedselectedimage:withfinishedunselectedimage:)*