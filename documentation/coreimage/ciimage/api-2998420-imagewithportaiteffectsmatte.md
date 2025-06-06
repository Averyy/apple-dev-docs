# imageWithPortaitEffectsMatte:options:

**Framework**: Core Image  
**Kind**: clm

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
+ (instancetype)imageWithPortaitEffectsMatte:(AVPortraitEffectsMatte *)matte options:(NSDictionary<CIImageOption, id> *)options;
```

## See Also

- [+ emptyImage](ciimage/1438023-emptyimage.md)
  Creates and returns an empty image object.
- [- initWithImage:](ciimage/1624119-initwithimage.md)
  Initializes an image object with the specified UIKit image object.
- [- initWithImage:options:](ciimage/1624098-initwithimage.md)
  Initializes an image object with the specified UIKit image object, using the specified options.
- [- initWithContentsOfURL:](ciimage/1437908-initwithcontentsofurl.md)
  Initializes an image object by reading an image from a URL.
- [+ imageWithContentsOfURL:](ciimage/1547027-imagewithcontentsofurl.md)
  Creates and returns an image object from the contents of a file.
- [- initWithContentsOfURL:options:](ciimage/1437867-initwithcontentsofurl.md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [+ imageWithContentsOfURL:options:](ciimage/1546997-imagewithcontentsofurl.md)
  Creates and returns an image object from the contents of a file, using the specified options.
- [+ imageWithCGImage:](ciimage/1547025-imagewithcgimage.md)
  Creates and returns an image object from a Quartz 2D image.
- [- initWithCGImage:](ciimage/1437986-initwithcgimage.md)
  Initializes an image object with a Quartz 2D image.
- [+ imageWithCGImage:options:](ciimage/1547021-imagewithcgimage.md)
  Creates and returns an image object from a Quartz 2D image using the specified options.
- [- initWithCGImage:options:](ciimage/1437764-initwithcgimage.md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [+ imageWithCGImageSource:index:options:](ciimage/3152398-imagewithcgimagesource.md)
- [- initWithCGImageSource:index:options:](ciimage/3152399-initwithcgimagesource.md)
- [+ imageWithData:](ciimage/1547029-imagewithdata.md)
  Creates and returns an image object initialized with the supplied image data.
- [- initWithData:](ciimage/1437925-initwithdata.md)
  Initializes an image object with the supplied image data.
- [+ imageWithData:options:](ciimage/1547016-imagewithdata.md)
  Creates and returns an image object initialized with the supplied image data, using the specified options.
- [- initWithData:options:](ciimage/1438032-initwithdata.md)
  Initializes an image object with the supplied image data, using the specified options.
- [+ imageWithBitmapData:bytesPerRow:size:format:colorSpace:](ciimage/1547023-imagewithbitmapdata.md)
  Creates and returns an image object from bitmap data.
- [- initWithBitmapData:bytesPerRow:size:format:colorSpace:](ciimage/1437857-initwithbitmapdata.md)
  Initializes an image object with bitmap data. 
- [- initWithBitmapImageRep:](ciimage/1535335-initwithbitmapimagerep.md)
  Initializes an image object with the specified bitmap image representation.
- [+ imageWithImageProvider:size::format:colorSpace:options:](ciimage/1579115-imagewithimageprovider.md)
  Creates and returns an image object initialized with data provided by an image provider.
- [- initWithImageProvider:size::format:colorSpace:options:](ciimage/1437868-initwithimageprovider.md)
  Initializes an image object with  data provided by an image provider, using the specified options. 
- [+ imageWithDepthData:](ciimage/2998417-imagewithdepthdata.md)
- [- initWithDepthData:](ciimage/2998421-initwithdepthdata.md)
- [+ imageWithDepthData:options:](ciimage/2998418-imagewithdepthdata.md)
- [- initWithDepthData:options:](ciimage/2998422-initwithdepthdata.md)
- [+ imageWithPortaitEffectsMatte:](ciimage/2998419-imagewithportaiteffectsmatte.md)
- [- initWithPortaitEffectsMatte:](ciimage/2998423-initwithportaiteffectsmatte.md)
- [- initWithPortaitEffectsMatte:options:](ciimage/2998424-initwithportaiteffectsmatte.md)
- [+ imageWithSemanticSegmentationMatte:](ciimage/3242777-imagewithsemanticsegmentationmat.md)
- [- initWithSemanticSegmentationMatte:](ciimage/3242779-initwithsemanticsegmentationmatt.md)
- [+ imageWithSemanticSegmentationMatte:options:](ciimage/3242778-imagewithsemanticsegmentationmat.md)
- [- initWithSemanticSegmentationMatte:options:](ciimage/3242780-initwithsemanticsegmentationmatt.md)
- [+ imageWithCVImageBuffer:](ciimage/1547007-imagewithcvimagebuffer.md)
  Creates and returns an image object from the contents of  `CVImageBuffer` object.
- [- initWithCVImageBuffer:](ciimage/1438012-initwithcvimagebuffer.md)
  Initializes an image object from the contents of a Core Video image buffer.
- [+ imageWithCVImageBuffer:options:](ciimage/1547028-imagewithcvimagebuffer.md)
  Creates and returns an image object from the contents of  `CVImageBuffer` object, using the specified options.
- [- initWithCVImageBuffer:options:](ciimage/1437617-initwithcvimagebuffer.md)
  Initializes an image object from the contents of a Core Video image buffer, using the specified options.
- [+ imageWithCVPixelBuffer:](ciimage/1547005-imagewithcvpixelbuffer.md)
  Creates and returns an image object from the contents of  `CVPixelBuffer` object.
- [- initWithCVPixelBuffer:](ciimage/1438072-initwithcvpixelbuffer.md)
  Initializes an image object from the contents of a Core Video pixel buffer.
- [+ imageWithCVPixelBuffer:options:](ciimage/1547003-imagewithcvpixelbuffer.md)
  Creates and returns an image object from the contents of  `CVPixelBuffer` object, using the specified options.
- [- initWithCVPixelBuffer:options:](ciimage/1438209-initwithcvpixelbuffer.md)
  Initializes an image object from the contents of a Core Video pixel buffer using the specified options.
- [+ imageWithMTLTexture:options:](ciimage/1546999-imagewithmtltexture.md)
  Creates and returns an image object with data supplied by a Metal texture.
- [- initWithMTLTexture:options:](ciimage/1437890-initwithmtltexture.md)
  Initializes an image object with data supplied by a Metal texture.
- [+ imageWithIOSurface:](ciimage/1547024-imagewithiosurface.md)
  Creates and returns an image from the contents of an IOSurface.
- [- initWithIOSurface:](ciimage/1438030-initwithiosurface.md)
  Initializes an image with the contents of an IOSurface.
- [- initWithIOSurface:options:](ciimage/1438181-initwithiosurface.md)
  Initializes, using the specified options, an image with the contents of an IOSurface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/2998420-imagewithportaiteffectsmatte)*