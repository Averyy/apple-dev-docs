# SwiftUI views for widgets

**Framework**: WidgetKit

Present your app’s content in widgets with SwiftUI views.

#### Overview

Widgets can use many, but not all, SwiftUI views to present content. Use the views listed below to implement your widget’s view.

> **Note**: Widgets can’t use UIKit or AppKit views wrapped with [`UIViewRepresentable`](https://developer.apple.com/documentation/SwiftUI/UIViewRepresentable) or [`NSViewRepresentable`](https://developer.apple.com/documentation/SwiftUI/NSViewRepresentable).

## Topics

### Displaying text
- [Displaying dynamic dates in widgets](displaying-dynamic-dates.md)
  Show up-to-date, time-based information in your widget even when it isn’t running.
- [@frozen struct Text](../SwiftUI/Text.md)
  A view that displays one or more lines of read-only text.
### Showing images
- [@frozen struct Image](../SwiftUI/Image.md)
  A view that displays an image.
### Adding interaction
- [Adding interactivity to widgets and Live Activities](adding-interactivity-to-widgets-and-live-activities.md)
  Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [struct Button<Label> where Label : View](../SwiftUI/Button.md)
  A control that initiates an action.
- [struct Toggle<Label> where Label : View](../SwiftUI/Toggle.md)
  A control that toggles between on and off states.
### Adding labels and links
- [struct Label<Title, Icon> where Title : View, Icon : View](../SwiftUI/Label.md)
  A standard label for user interface items, consisting of an icon with a title.
- [@MainActor @preconcurrency struct Link<Label> where Label : View](../SwiftUI/Link.md)
  A control for navigating to a URL.
### Stacking views
- [@frozen struct HStack<Content> where Content : View](../SwiftUI/HStack.md)
  A view that arranges its subviews in a horizontal line.
- [@frozen struct VStack<Content> where Content : View](../SwiftUI/VStack.md)
  A view that arranges its subviews in a vertical line.
- [@frozen struct ZStack<Content> where Content : View](../SwiftUI/ZStack.md)
  A view that overlays its subviews, aligning them in both axes.
- [struct LazyHStack<Content> where Content : View](../SwiftUI/LazyHStack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct LazyVStack<Content> where Content : View](../SwiftUI/LazyVStack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.
### Arranging views in grids
- [struct LazyHGrid<Content> where Content : View](../SwiftUI/LazyHGrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct LazyVGrid<Content> where Content : View](../SwiftUI/LazyVGrid.md)
  A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
- [struct GridItem](../SwiftUI/GridItem.md)
  A description of a row or a column in a lazy grid.
### Enumerating lists
- [struct ForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable](../SwiftUI/ForEach.md)
  A structure that computes views on demand from an underlying collection of identified data.
### Grouping views
- [@frozen struct Group<Content>](../SwiftUI/Group.md)
  A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [struct GroupBox<Label, Content> where Label : View, Content : View](../SwiftUI/GroupBox.md)
  A stylized view, with an optional label, that visually collects a logical grouping of content.
- [struct Section<Parent, Content, Footer>](../SwiftUI/Section.md)
  A container view that you can use to add hierarchy within certain views.
### Representing hierarchies
- [struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable](../SwiftUI/OutlineGroup.md)
  A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
### Adding spacers and dividers
- [@frozen struct Spacer](../SwiftUI/Spacer.md)
  A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
- [struct Divider](../SwiftUI/Divider.md)
  A visual element that can be used to separate other content.
### Handling conditional views
- [@frozen struct EmptyView](../SwiftUI/EmptyView.md)
  A view that doesn’t contain any content.
- [@frozen struct EquatableView<Content> where Content : Equatable, Content : View](../SwiftUI/EquatableView.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
### Displaying shapes
- [@frozen struct Rectangle](../SwiftUI/Rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [@frozen struct RoundedRectangle](../SwiftUI/RoundedRectangle.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [@frozen struct Circle](../SwiftUI/Circle.md)
  A circle centered on the frame of the view containing it.
- [@frozen struct Ellipse](../SwiftUI/Ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [@frozen struct Capsule](../SwiftUI/Capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [@frozen struct Path](../SwiftUI/Path.md)
  The outline of a 2D shape.
### Transforming views
- [@frozen struct ScaledShape<Content> where Content : Shape](../SwiftUI/ScaledShape.md)
  A shape with a scale transform applied to it.
- [@frozen struct RotatedShape<Content> where Content : Shape](../SwiftUI/RotatedShape.md)
  A shape with a rotation transform applied to it.
- [@frozen struct OffsetShape<Content> where Content : Shape](../SwiftUI/OffsetShape.md)
  A shape with a translation offset transform applied to it.
- [@frozen struct TransformedShape<Content> where Content : Shape](../SwiftUI/TransformedShape.md)
  A shape with an affine transform applied to it.
- [@frozen struct ContainerRelativeShape](../SwiftUI/ContainerRelativeShape.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
### Styling views
- [@frozen struct Color](../SwiftUI/Color.md)
  A representation of a color that adapts to a given context.
- [@frozen struct ImagePaint](../SwiftUI/ImagePaint.md)
  A shape style that fills a shape by repeating a region of an image.
- [@frozen struct Gradient](../SwiftUI/Gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [@frozen struct LinearGradient](../SwiftUI/LinearGradient.md)
  A linear gradient.
- [@frozen struct AngularGradient](../SwiftUI/AngularGradient.md)
  An angular gradient.
- [@frozen struct RadialGradient](../SwiftUI/RadialGradient.md)
  A radial gradient.
- [@frozen struct ForegroundStyle](../SwiftUI/ForegroundStyle.md)
  The foreground style in the current context.
- [@frozen struct FillStyle](../SwiftUI/FillStyle.md)
  A style for rasterizing vector shapes.
- [@frozen struct BackgroundStyle](../SwiftUI/BackgroundStyle.md)
  The background style in the current context.
- [struct SelectionShapeStyle](../SwiftUI/SelectionShapeStyle.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [struct SeparatorShapeStyle](../SwiftUI/SeparatorShapeStyle.md)
  A style appropriate for foreground separator or border lines.
- [@frozen struct StrokeStyle](../SwiftUI/StrokeStyle.md)
  The characteristics of a stroke that traces a path.
### Creating 2D graphics
- [struct Canvas<Symbols> where Symbols : View](../SwiftUI/Canvas.md)
  A view type that supports immediate mode drawing.
### Managing view geometry
- [struct GeometryProxy](../SwiftUI/GeometryProxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [@frozen struct GeometryReader<Content> where Content : View](../SwiftUI/GeometryReader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [@frozen struct ProjectionTransform](../SwiftUI/ProjectionTransform.md)
### Substituting views
- [@frozen struct AnyView](../SwiftUI/AnyView.md)
  A type-erased view.
- [@frozen struct TupleView<T>](../SwiftUI/TupleView.md)
  A View created from a swift tuple of View values.

## See Also

- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [Displaying the right widget background](displaying-the-right-widget-background.md)
  Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md)
  Ensure that your small system family widget works well in StandBy and CarPlay.
- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct WidgetRenderingMode](widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/swiftui-views)*