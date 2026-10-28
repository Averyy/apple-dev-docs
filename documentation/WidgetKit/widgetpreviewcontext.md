# WidgetPreviewContext

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

A specification for the context of a widget preview.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
struct WidgetPreviewContext
```

## Overview

To create a preview for a widget in Xcode, use [`previewContext(_:)`](../SwiftUI/view/previewcontext%28_%29.md) and pass `WidgetPreviewContext` initialized with the appropriate `WidgetFamily`.

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
- [init(family: WidgetFamily)](./widgetpreviewcontext/init%28family%29.md)
  Creates a context for previewing a widget or a widget’s view.

## Relationships

### Conforms To
- [PreviewContext](../SwiftUI/previewcontext.md)

## See Also

### Previews and debugging
- [Previewing widgets and Live Activities in Xcode](./previewing-widgets-and-live-activities-in-xcode.md)
  Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Preview macros](./preview-macros.md)
  Use Swift macros to create widget previews in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpreviewcontext)*