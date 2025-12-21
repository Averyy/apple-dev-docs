# Preview(_:as:using:widget:contentStates:)

**Framework**: WidgetKit  
**Kind**: macro

Preview a widget with an activity configuration, using the specified attributes and content states.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<Widget, Attributes>(_ name: String? = nil, as viewKind: ActivityPreviewViewKind, using attributes: Attributes, widget: @escaping () -> Widget, @PreviewActivityBuilder<Attributes> contentStates: @escaping @MainActor () async -> [Attributes.ContentState]) where Widget : Widget, Attributes : ActivityAttributes
```

## Mentions

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md)

#### Overview

Provide the preview with sample data and use it to step through the specified content states and test out the transitions between them.

> **Note**: The attributes must be of the type that the widget expects.

## Parameters

- `name`: An optional display name for the preview that appears in the preview canvas.
- `viewKind`: The kind of widget view to display.
- `attributes`: The attributes with which to configure the widget.
- `widget`: A closure producing the widget to be previewed.
- `contentStates`: A closure building the content states to be previewed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preview(_:as:using:widget:contentstates:))*