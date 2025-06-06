# Supporting multiple watch sizes

**Framework**: Watchos Apps

Customize the layout of your user interface to support all Apple Watch sizes.

#### Overview

With the addition of Apple Watch Series 10, watchOS apps now support seven watch sizes.

| Devices | Sizes |
| --- | --- |
| Apple Watch Series 4, 5, 6, and SE | 40 mm and 44 mm |
| Apple Watch Series 7, 8, and 9 | 41 mm and 45 mm |
| Apple Watch Series 10 | 42 mm and 46 mm |
| Apple Watch Ultra | 49 mm |

In addition to adding two new sizes, Apple Watch Series 10 also has a slightly different aspect ratio–gaining a bit more width. It also has rounder corners.

![A figure with the Series 9 screen placed over the Series 10 screen. This shows the difference in size, aspect, and shape between the two screens.](https://docs-assets.developer.apple.com/published/545a3f73364055658d64e3b965a4c97f/screen-comparison%402x.png)

When Apple Watch Series 10 runs an app compiled for watchOS 10 or earlier, the system letterboxes the interface, centering it on the screen. Additionally, the Series 10 clips the corners of the letter-boxed content; however, it doesn’t clip the safe area. To fully use the Series 10 sizes, build your app with the watchOS 11 SDK or later.

##### Create a Dynamic Layout

When designing your app, be sure to consider all available watch sizes. Where possible, use resizable objects to fill the available space. Resizable objects help create flexible layouts and minimize the amount of customization you need to support for the different sizes. If necessary, you can customize your layout for specific sizes; however, when creating the layout for larger screens, use the additional space to display larger controls and assets, rather than filling the screen with additional controls.

For additional design information, see [`Designing for watchOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-watchos).

##### Use Safe Areas and Scene Padding

Most watches have rounded corners that may clip scrolling content. Some also bend content around the bevel, which can affect the appearance of anything placed near the sides. Finally, each screen keeps a margin between the text in its status and notification bars, and the edge of the screen. When laying out your content, you typically align text with the leading edge of the navigation bar’s title or the back button, and the trailing edge of the status bar’s text.

The system provides the following tools to help you manage your content:

The following figures show the safe area and scene padding for all watch sizes. The  value at the top is the number of points from the top of the safe area to the bottom of the status bar. The  distance indicates the size of the text margin.

By default, SwiftUI views fill the safe area. Scrolling content, such as a list view, automatically settles within the safe areas. To disable the safe area, use the [`ignoresSafeArea(_:edges:)`](https://developer.apple.com/documentation/SwiftUI/View/ignoresSafeArea(_:edges:)) view modifier.

To align items with the status and navigation bar, call [`scenePadding(_:)`](https://developer.apple.com/documentation/SwiftUI/View/scenePadding(_:)) on the view. In general, align text with the status and navigation bar. In watchOS 11 and later, [`Button`](https://developer.apple.com/documentation/SwiftUI/Button)  automatically aligns to the text margins. The rounded rectangle for a [`List`](https://developer.apple.com/documentation/SwiftUI/List) horizontally fills the safe area, but its content aligns with the status and navigation bar.

```swift
@State var showing = true

var body: some View {
    Text("Hello World")
    // Displaying a sheet ensures that there are items on both sides
    // of the status bar.
        .sheet(isPresented: $showing) {
            VStack {
                
                Spacer()
                                    
                // Align the text with the status bar.
                Text("The quick brown fox jumps over the lazy dog.")
                    .scenePadding(.horizontal)
                
                Spacer()
                                    
                // The button automatically aligns with the status bar.
                Button("My Button") {
                    print("Button Pressed!")
                }
            }
        }
}
```

![An image of a watch face that displays the result of the code listing Both the text and the button align with the text margins.](https://docs-assets.developer.apple.com/published/4965427b195b15c102c781e3f64b03a7/scene-padding%402x.png) For additional design information, see [`Layout`](https://developer.apple.com/design/Human-Interface-Guidelines/layout).

##### Support Dynamic Type

Use dynamic type so the wearer can modify the size of text components in your app. Dynamic type helps users who need larger text for better readability. It also accommodates those who can read smaller text, allowing more information to appear on the screen. Apps that support Dynamic Type provide an experience that is consistent with the system apps. For more information, see [`Applying custom fonts to text`](https://developer.apple.com/documentation/SwiftUI/Applying-Custom-Fonts-to-Text).

Different watch sizes use different default dynamic type sizes.

| Device | Dynamic type size |
| --- | --- |
| 40 mm, 41 mm, and 42 mm | Large |
| 44 mm, 45 mm, 46 mm, and 49 mm | XLarge |

> **Note**: The wearer can change the dynamic type size, including using accessibility sizes. Always check your app’s appearance with all available type sizes.

The wearer can change the dynamic type size, including using accessibility sizes. Always check your app’s appearance with all available type sizes.

For additional design information, see [`Typography`](https://developer.apple.com/design/Human-Interface-Guidelines/typography).

##### Manage Assets

To provide an asset that adapts to all watch sizes, create a scalable PDF asset. Add a PDF to the asset catalog as a 2x image asset, then set its Auto Scaling attribute to Automatic.

![A screenshot of Xcode that shows Apple Watch Series 4 40 mm selected in the destination picker.](https://docs-assets.developer.apple.com/published/5ec86df7540a6ca7fbd09984655daa6a/screensize-preview%402x.png)

When you load the PDF, the system scales the image based on the current device’s size as listed in the table.

| Watch Size | Image Scale |
| --- | --- |
| 38 mm | 90% |
| 40 mm | 100% |
| 41 mm | 106% |
| 42 mm (Series 3) | 100% |
| 42 mm (Series 10) | 106% |
| 44 mm | 110% |
| 45 mm | 119% |
| 46 mm | 119% |
| 49 mm | 119% |

For more design information, see [`Images`](https://developer.apple.com/design/Human-Interface-Guidelines/images).

##### Preview Multiple Sizes

When designing a watchOS app, you can use Xcode previews to check your app’s layout. You can display one or more previews using the `#Preview` macro.

```swift
#Preview {
    ContentView()
}
```

You can then use the Preview destination picker to switch between different devices.

![A screenshot of Xcode that shows Apple Watch Series 4 40 mm selected in the destination picker.](https://docs-assets.developer.apple.com/published/5ec86df7540a6ca7fbd09984655daa6a/screensize-preview%402x.png)

You can also view all the dynamic type sizes for that device by selecting the Dynamic Type Variants option.

![A screenshot of Xcode that shows a preview of all the dynamic type variants.](https://docs-assets.developer.apple.com/published/7466437f47c55047cc34dc51ca0733fb/preview-dynamic-type%402x.png)

For more information, see [`Previewing your app’s interface in Xcode`](https://developer.apple.com/documentation/Xcode/previewing-your-apps-interface-in-xcode).

## See Also

- [Building a productivity app for Apple Watch](building-a-productivity-app-for-apple-watch.md)
  Create a watch app to manage and share a task list and visualize the status with a chart.
- [Designing your app for the Always On state](designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [Setting the app’s accent color](setting-the-app-s-accent-color.md)
  Set your app’s accent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/supporting-multiple-watch-sizes)*