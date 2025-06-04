# init(image:)

**Framework**: Watchkit  
**Kind**: init

Creates and returns an image object using the specified UIKit image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(image: UIImage)
```

## Overview

An initialized `WKImage` object.

## Parameters

- `image`: The image object. This parameter must not be  .

## Discussion

Use this method when you already have a UIKit image object and want to use it in your picker.

## See Also

- [convenience init(imageData: Data)](init(imagedata:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagedata:)))
- [convenience init(imageName: String)](init(imagename:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagename:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(image:))*