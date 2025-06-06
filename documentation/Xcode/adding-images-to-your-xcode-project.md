# Adding images to your Xcode project

**Framework**: Xcode

Import images into your project, manage their appearances and variations, and load them at runtime.

#### Overview

Xcode projects often contain many images, and need to manage multiple variations of each image to create a great visual experience for all the devices and platforms on which your app runs. For example, your app might display a different version of an image depending on the device screen size, resolution, language, appearance, gamut, and many other factors. If your app uses images, you can use asset catalogs to simplify managing those images through image sets.

##### Create a New Image Set

An  represents one image that you intend to load at runtime. Each image set contains multiple variations of a single image that you customize to support different device characteristics. If you have multiple images in your app, you need to create an image set for each image.

To create an image set, generate an image asset outside of Xcode, then import it into an asset catalog. The system converts the image format into the most appropriate representation when you build the project.

1. In the Project navigator, select an asset catalog: a file with a `.xcassets` file extension.
2. Drag an image from the Finder to the outline view. A new image set appears in the outline view, and the image asset appears in a well in the detail area.
3. Double-click the image set name in the outline view to rename the image set with a descriptive name, and press the Return key.

![Screenshot of an asset catalog in Xcode. An image set with the name Image contains a single picture of oranges in the 1x well in the detail area.](https://docs-assets.developer.apple.com/published/fde3f2c3641843d417853ca4df14f28c/adding-images-to-your-xcode-project-1%402x.png)

##### Select Supported Appearances and Variations for Images

By default, Xcode creates each image set with wells for @1x, @2x, and @3x resolutions. If the filename of the image you import ends in `@2x` or `@3x`, Xcode automatically places the image into the well with the corresponding resolution. Supply high-resolution images for all images in your app, for all devices your app supports.

In addition to resolution, your image assets might vary based on other device characteristics. Use the Attributes inspector to add, remove, and edit the image variations to include in your image set. You can accomplish this task in an asset catalog or in Interface Builder.

1. In the Project navigator, select the asset catalog.
2. In the outline view, select the image set.
3. In the inspector area, select the Attributes inspector.
4. In the Attributes inspector, add, remove, and edit the device characteristic settings to show additional image wells for the variations you want to customize.

![Screenshot of the Attributes inspector with the default Universal option selected.](https://docs-assets.developer.apple.com/published/039f3c8fc6decb8e7e250da05956b546/adding-images-to-your-xcode-project-2%402x.png)

For more information about image size and resolution, see [`Image Size and Resolution`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution) in the [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios).

##### Drag Images to the Variant Wells

After you select the desired characteristic settings for your image set, provide image variations by dragging additional images into the corresponding wells in the image set.

1. In the Project navigator, select the asset catalog.
2. In the outline view, select the image set.
3. In the Finder, drag other variations of the image to the wells in the detail area that match their resolutions or other characteristics.

##### Load the Image Asset From Your Code

To use the image from code, initialize an image with the name of the image set. Don’t include the file extension.

```swift
// SwiftUI
let image = Image("ImageName")

// UIKit
let image = UIImage(named: "ImageName")

// AppKit
let image = NSImage(named: "ImageName")
```

## See Also

- [Creating custom symbol images for your app](../UIKit/creating-custom-symbol-images-for-your-app.md)
  Create, organize, and annotate symbol images using SF Symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-images-to-your-xcode-project)*