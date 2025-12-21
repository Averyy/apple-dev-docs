# Supporting multiple watch sizes

**Framework**: watchOS apps

Customize the layout of your user interface to support all Apple Watch sizes.

#### Overview

When designing your app, be sure to support all available Apple Watch sizes to ensure a consistent experience for everyone who uses your app. For more information on Apple Watch screen dimensions, refer to [`watchOS device screen dimensions`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/layout#watchOS-device-screen-dimensions) in the Human Interface Guidelines. For information about adopting Liquid Glass in watchOS, refer to [`Adopting Liquid Glass`](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass).

| Devices | Sizes |
| --- | --- |
| Apple Watch Series 4, 5, 6, and SE (all generations) | 40mm and 44mm |
| Apple Watch Series 7, 8, and 9 | 41mm and 45mm |
| Apple Watch Series 10 and 11 | 42mm and 46mm |
| Apple Watch Ultra (all generations) | 49mm |

Where possible, use resizable objects to fill the available space. Resizable objects help you create flexible layouts and minimize the amount of customization you need to support for the different sizes. If necessary, you can customize your layout for specific sizes; however, when creating the layout for larger screens, use the additional space to display larger controls and assets, rather than filling the screen with additional controls. For additional design information, refer to [`Designing for watchOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-watchos).

##### Use Safe Areas and Scene Padding

Most watches have rounded corners that may clip scrolling content. Some also bend content around the bevel, which can affect the appearance of anything placed near the sides. Each screen keeps a margin between the text in its status and navigation bars, and the edge of the screen. When you lay out content, align text with the leading edge of the navigation bar’s title or Back button, and with the trailing edge of the status bar’s text.

The system provides the following tools to help you manage your content:

Apple Watch uses system-defined safe areas to keep content from getting too close to the edge of the screen. By default, SwiftUI views fill the safe area: scrolling content, such as list views, automatically settle within the safe areas. Override the safe area only when necessary, such as when you need content like background images or colors to extend to the screen edges. To disable the safe area, use the [`ignoresSafeArea(_:edges:)`](https://developer.apple.com/documentation/SwiftUI/View/ignoresSafeArea(_:edges:)) view modifier. However, keep most interactive content within the safe area for optimal usability.

The following example demonstrates extending a background image to fill the entire screen while keeping text readable within the safe area:

```swift
struct ContentView: View {
    var body: some View {
        
        ZStack {
            // Background image extends to all edges.
            Image("watchBackground")
                .resizable()
                .aspectRatio(contentMode: .fill)
                .ignoresSafeArea(.all) // Fills entire screen including corners.
            
            VStack {
                Text("12:34")
                    .font(.largeTitle)
                    .foregroundColor(.white)
                Text("Monday, Sep 15")
                    .font(.caption)
                    .foregroundColor(.white.opacity(0.8))
            }
            // Text content stays within safe area automatically.
        }
        
    }
}
```

To align items with the status and navigation bar, call [`scenePadding(_:)`](https://developer.apple.com/documentation/SwiftUI/View/scenePadding(_:)) on your view. Apply scene padding when you want your text and interactive elements to align with the system’s standard margins. This is particularly important for text heavy content where it can enhance readability. The following example shows text alignment using scene padding:

```swift
struct ContentView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 12) {
                Text("Activity Summary")
                    .font(.headline)
                
                Text("Your move goal is 300 calories. You've burned 287 calories so far today.")
                    .font(.body)
                
                Text("Keep going to complete your goal!")
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
        }
        .scenePadding(.horizontal) // Aligns text with the navigation bar margins.
    }
}
```

Use [`Button`](https://developer.apple.com/documentation/SwiftUI/Button)  to automatically align with the text margins. The rounded rectangle for a [`List`](https://developer.apple.com/documentation/SwiftUI/List) horizontally fills the safe area, but its content aligns with the status and navigation bar. For additional design information, refer to [`Layout`](https://developer.apple.com/design/Human-Interface-Guidelines/layout).

> **Note**: When Apple Watch Series 10 or 11 runs an app compiled for watchOS 10 or earlier, the system letterboxes the interface, centering it on the screen. Additionally, the Series 10 clips the corners of the letterboxed content; however, it doesn’t clip the safe area. To ensure your app’s interface appears as you expect on Series 10 and 11 sizes, build your app with the watchOS 11 SDK or later.

##### Support Dynamic Type

Use Dynamic Type so the wearer can modify the size of text components in your app. Dynamic Type helps people who need larger text for better readability. It also accommodates those who can read smaller text, allowing more information to appear on the screen. Apps that support Dynamic Type provide an experience that’s consistent with the system apps. For more information, refer to [`Applying custom fonts to text`](https://developer.apple.com/documentation/SwiftUI/Applying-Custom-Fonts-to-Text).

Different watch sizes use different default Dynamic Type sizes:

| Device | Dynamic Type size |
| --- | --- |
| 40mm, 41mm, and 42mm | Large |
| 44mm, 45mm, 46mm, and 49mm | XLarge |

> **Note**: The wearer can change the Dynamic Type size, including using accessibility sizes. Always check your app’s appearance with all available type sizes. For additional design information, refer to [`Typography`](https://developer.apple.com/design/Human-Interface-Guidelines/typography).

##### Manage Assets

To provide an asset that adapts to all watch sizes, create a scalable PDF asset. Add a PDF to the asset catalog as a 2x image asset, then set its Auto Scaling attribute to Automatic.

![A screenshot that shows the 2x image drop target and the auto scaling attribute.](https://docs-assets.developer.apple.com/published/3afcd8c2d6e6fce5dc7fd94e60d1e276/supporting-multiple-watch-sizes-6%402x.png)

When you load the PDF, the system scales the image based on the current device’s size as listed in the table below.

| Watch size | Image scale |
| --- | --- |
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm (Series 3) | 100% |
| 42mm (Series 10) | 106% |
| 44mm | 110% |
| 45mm | 119% |
| 46mm | 119% |
| 49mm | 119% |

For more design information, refer to [`Images`](https://developer.apple.com/design/Human-Interface-Guidelines/images).

##### Preview Multiple Sizes

When designing a watchOS app, you can use Xcode previews to check your app’s layout. You can display one or more previews using the `#Preview` macro.

```swift
#Preview {
    ContentView()
}
```

You can then use the Preview destination picker to switch between different devices.

![A screenshot of Xcode that shows Apple Watch Series 4 40mm selected in the destination picker.](https://docs-assets.developer.apple.com/published/5ec86df7540a6ca7fbd09984655daa6a/screensize-preview%402x.png)

You can also view all the Dynamic Type sizes for that device by selecting the Dynamic Type Variants option in Xcode. For more information, refer to [`Previewing your app’s interface in Xcode`](https://developer.apple.com/documentation/Xcode/previewing-your-apps-interface-in-xcode).

![A screenshot of Xcode that shows a preview of all the Dynamic Type variants.](https://docs-assets.developer.apple.com/published/5407a33e8d0f3255d743e289d78ebd5d/preview-dynamic-type%402x.png)

## See Also

- [Building a productivity app for Apple Watch](building-a-productivity-app-for-apple-watch.md)
  Create a watch app to manage and share a task list and visualize the status with a chart.
- [Designing your app for the Always On state](designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [Setting the app’s accent color](setting-the-app-s-accent-color.md)
  Set your app’s accent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/supporting-multiple-watch-sizes)*