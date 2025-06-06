# WKInterfaceImage

**Framework**: Watchkit  
**Kind**: class

An image that can be displayed in the interface of your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceImage
```

#### Overview

The images you display in your watchOS app can be static or animated. You use [`WKInterfaceImage`](wkinterfaceimage.md) objects to specify the image data you want to display and to start and stop animations.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to an image object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed image objects and assigns them to their associated outlets. At that point, you can use those objects to make changes to the onscreen images.

The images you use in your interface can be embedded in your Watch app bundle, created dynamically, or downloaded from the Internet. Images in your Watch app bundle represent the images that are part of your app’s user interface. Images that you download or create dynamically exist either in memory or as files in your WatchKit extension’s container directory. The `WKInterfaceImage` class provides setter methods for getting your images onscreen regardless of their location.

##### Image Management

The images you use in your interface can come from many different locations, and you load and manage those images in different ways:

- Store images that are part of your standard interface in your Watch app bundle. Use asset catalogs to store your images and to customize those images for different device sizes as needed. Use the [`setImageNamed(_:)`](wkinterfaceimage/setimagenamed(_:).md) method of this class to display an image located in an asset catalog or in your Watch app bundle.

You can store animated image sequences in your Watch app bundle, but your image files must use specific naming conventions. For information about these conventions, see [`Animating a Series of Images`](wkinterfaceimage#Animating-a-Series-of-Images.md).

- Store downloaded image files in your WatchKit extension’s container directory. Image files must be stored locally in your extension’s container directory and loaded into memory at runtime. When loading an image file that you want to display without modification, load the raw image data into an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object and use the [`setImageData(_:)`](wkinterfaceimage/setimagedata(_:).md) method to display it in your interface. Raw image data is typically compressed and can be sent more quickly than a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object.
- Set dynamically created images directly. For content that you draw programmatically, create a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) of the final results and display it using the [`setImage(_:)`](wkinterfaceimage/setimage(_:).md) method. You also use this technique for animated images sequences you create dynamically using the [`animatedImageNamed(_:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImageNamed(_:duration:)) or [`animatedImage(with:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImage(with:duration:)) method.

When creating your images, always create them at a size that is appropriate for the underlying device. Whenever possible, try to use the same size image regardless of the underlying device. In cases where you need different images for different device sizes, use asset catalogs to store the different versions of the image using the same image name. If the image you specify is too large or too small, WatchKit uses the mode attribute you set in Interface Builder to determine how to render the image.

##### Supported Image Formats

You can specify images using any image formats supported by iOS, but it is recommended that you use JPEG and PNG images whenever possible. Specifying images in formats other than JPEG and PNG can introduce a performance penalty when rendering those images. All images should be designed for Retina displays, and image filenames you provide yourself should include the `@2x` modifier in the filename.

For more information about the supported image formats, see [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage).

##### Animating a Series of Images

Animated images are an easy and fast way to make your interface more dynamic and engaging for users. You create animated images from existing images in your asset catalog or by creating a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object using the images you want.

For animations based on images in your asset catalogs, name your image resources using the convention , where the  string is the same for all images and the  value indicates the position of the image in the animation sequence. The number of the first image in the sequence must be `0` or `1`. For example, an animation with three images could have the file names `image1`, `image2`, and `image3`. If you store image resource files in your Watch app bundle without using asset catalogs, the naming convention for your image files is the same except your files should also have the appropriate filename extension.

Whenever possible, place image resources in an asset catalog in your Watch app bundle (not in your WatchKit extension’s bundle). Placing them in the Watch app bundle lets you use the [`setImageNamed(_:)`](wkinterfaceimage/setimagenamed(_:).md) method to load the animated image at runtime, which simplifies the loading process. For animations you generate dynamically, use the [`animatedImage(with:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImage(with:duration:)) method of [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) to assemble your animation in your WatchKit extension, and then set that animation using the [`setImage(_:)`](wkinterfaceimage/setimage(_:).md) method.

> **Note**:  You cannot use the [`animatedImageNamed(_:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImageNamed(_:duration:)) method of [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) to create an animated image based on images in your Watch app’s bundle. That method looks for images in the bundle of the active process, which is your WatchKit extension’s bundle. To load an animated image sequence from images in your Watch app bundle, you must name your image resources appropriately and use the [`setImageNamed(_:)`](wkinterfaceimage/setimagenamed(_:).md) method of this class.

 You cannot use the [`animatedImageNamed(_:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImageNamed(_:duration:)) method of [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) to create an animated image based on images in your Watch app’s bundle. That method looks for images in the bundle of the active process, which is your WatchKit extension’s bundle. To load an animated image sequence from images in your Watch app bundle, you must name your image resources appropriately and use the [`setImageNamed(_:)`](wkinterfaceimage/setimagenamed(_:).md) method of this class.

For more information on how to create animated images, see the discussions of the [`animatedImageNamed(_:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImageNamed(_:duration:)) and [`animatedImage(with:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImage(with:duration:)) methods in [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage).

##### Interface Builder Configuration Options

Xcode lets you configure information about your image interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Image | The name of the image to be displayed. This image must be in the Watch app’s bundle. If you do not set the image in your storyboard, set it programmatically using the methods of this class. |
| Mode | The content mode for the image. The mode defines how the image fills the available space. Some modes let you scale the image with or without maintaining the current aspect ratio. Other modes position the image relative to a fixed point in the image interface object’s bounds. |
| Tint | The color applied to a template image. You can change the tint color programmatically by calling the [`setTintColor(_:)`](wkinterfaceimage/settintcolor(_:).md) method. The color you specify has no affect on animated images or non template images. |
| Animate | A Boolean value indicating whether the image is animatable. Set the value to Yes to configure the animation parameters, including its duration (in seconds) and whether it starts immediately when the parent interface controller appears onscreen. Animations started at load time run continuously in a loop. |

## Topics

### Configuring the Image
- [func setImage(UIImage?)](wkinterfaceimage/setimage(_:).md)
  Sets the displayed image using the specified image object.
- [func setImageData(Data?)](wkinterfaceimage/setimagedata(_:).md)
  Sets the displayed image using a formatted data object.
- [func setImageNamed(String?)](wkinterfaceimage/setimagenamed(_:).md)
  Sets the displayed image using a named image resource file.
- [func setTintColor(UIColor?)](wkinterfaceimage/settintcolor(_:).md)
  Changes the color applied to a template image.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [WKImageAnimatable](wkimageanimatable.md)

## See Also

- [class WKImage](wkimage.md)
  A wrapper for images you use with a picker interface.
- [protocol WKImageAnimatable](wkimageanimatable.md)
  A collection of methods you can use to control the playback of animated images.
- [class WKInterfaceMovie](wkinterfacemovie.md)
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md)
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md)
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.
- [enum WKVideoGravity](wkvideogravity.md)
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage)*