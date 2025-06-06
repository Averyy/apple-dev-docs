# Displaying text in visionOS

**Framework**: Visionos

Create styled text in a window using SwiftUI.

**Availability**:
- visionOS 2.0+
- Xcode 16.0+

#### Overview

This sample app uses SwiftUI views to display text in four distinct styles:

- Large title
- Subheadline
- Bold
- Regular with color

The following image shows how the scene renders in visionOS:

![A screenshot of a visionOS app in Simulator, displaying a translucent window with four lines of center-aligned text in a vertical arrangement. From top to bottom, the lines exhibit the following styles: large title, subheadline, bold, and regular with a green color.](https://docs-assets.developer.apple.com/published/b0b559a94b06c521fe5a19afaae2670e/sample-text-1-main-view.png)

The app’s main view displays four lines of text by creating a [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) instance for each line:

```swift
struct SwiftUIText: View {
    /// The amount of spacing between each text entry.
    let spacing: CGFloat = 30

    var body: some View {
        VStack(spacing: spacing) {
            // Set the style to large title.
            Text("This is a large title").font(.largeTitle)

            // Set the style to subheadline.
            Text("This is a subheadline text").font(.subheadline)

            // Format the text to bold.
            Text("This is a bold text").fontWeight(.bold)

            // Set the text's color to green.
            Text("This is a green text").foregroundStyle(.green)
        }
    }
}
```

SwiftUI provides the `Text` view and its modifiers, which the app uses to make each text appear unique.

## See Also

- [Adding a depth effect to text in visionOS](adding-a-depth-effect-to-text-in-visionos.md)
  Create text that expands out of a window using stacked SwiftUI text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/displaying-text-in-visionos)*