# WidgetPreviewContext

**Framework**: WidgetKit  
**Kind**: struct

A specification for the context of a widget preview.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
struct WidgetPreviewContext
```

#### Overview

To create a preview for a widget in Xcode, use [`previewContext(_:)`](https://developer.apple.com/documentation/SwiftUI/View/previewContext(_:)) and pass `WidgetPreviewContext` initialized with the appropriate `WidgetFamily`.

```swift
struct Widget_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            MyWidgetView()
                .previewContext(WidgetPreviewContext(family: .systemSmall))
        }
    }
}
```

## Topics

### Creating a Preview Context
- [init(family: WidgetFamily)](widgetpreviewcontext/init(family:).md)
  Creates a context for previewing a widget or a widget’s view.

## Relationships

### Conforms To
- [PreviewContext](../SwiftUI/PreviewContext.md)

## See Also

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md)
  Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Debugging widgets](debugging-widgets.md)
  Set environment variables in Xcode to control your widget’s configuration in the debugger.
- [Preview macros](preview-macros.md)
  Use Swift macros to create widget previews in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpreviewcontext)*