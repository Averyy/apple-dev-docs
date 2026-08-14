# SwiftUI views for widgets

**Framework**: WidgetKit

Present your app’s content in widgets with SwiftUI views.

#### Overview

Widgets can use many, but not all, SwiftUI views to present content. Use the views listed below to implement your widget’s view.

> **Note**: Widgets can’t use UIKit or AppKit views wrapped with [`UIViewRepresentable`](https://developer.apple.com/documentation/swiftui/uiviewrepresentable) or [`NSViewRepresentable`](https://developer.apple.com/documentation/swiftui/nsviewrepresentable).

## Topics

### Displaying text
- [Displaying dynamic dates in widgets](displaying-dynamic-dates.md)
  Show up-to-date, time-based information in your widget even when it isn’t running.
- [struct Text](../swiftui/text.md)
  A view that displays one or more lines of read-only text.
### Showing images
- [struct Image](../swiftui/image.md)
  A view that displays an image.
### Adding interaction
- [Adding interactivity to widgets and Live Activities](adding-interactivity-to-widgets-and-live-activities.md)
  Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [struct Button](../swiftui/button.md)
  A control that initiates an action.
- [struct Toggle](../swiftui/toggle.md)
  A control that toggles between on and off states.
### Adding labels and links
- [struct Label](../swiftui/label.md)
  A standard label for user interface items, consisting of an icon with a title.
- [struct Link](../swiftui/link.md)
  A control for navigating to a URL.
### Stacking views
- [struct HStack](../swiftui/hstack.md)
  A view that arranges its subviews in a horizontal line.
- [struct VStack](../swiftui/vstack.md)
  A view that arranges its subviews in a vertical line.
- [struct ZStack](../swiftui/zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [struct LazyHStack](../swiftui/lazyhstack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct LazyVStack](../swiftui/lazyvstack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.
### Arranging views in grids
- [struct LazyHGrid](../swiftui/lazyhgrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct LazyVGrid](../swiftui/lazyvgrid.md)
  A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
- [struct GridItem](../swiftui/griditem.md)
  A description of a row or a column in a lazy grid.
### Enumerating lists
- [struct ForEach](../swiftui/foreach.md)
  A structure that computes views on demand from an underlying collection of identified data.
### Grouping views
- [struct Group](../swiftui/group.md)
  A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [struct GroupBox](../swiftui/groupbox.md)
  A stylized view, with an optional label, that visually collects a logical grouping of content.
- [struct Section](../swiftui/section.md)
  A container view that you can use to add hierarchy within certain views.
### Representing hierarchies
- [struct OutlineGroup](../swiftui/outlinegroup.md)
  A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
### Adding spacers and dividers
- [struct Spacer](../swiftui/spacer.md)
  A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
- [struct Divider](../swiftui/divider.md)
  A visual element that can be used to separate other content.
### Handling conditional views
- [struct EmptyView](../swiftui/emptyview.md)
  A view that doesn’t contain any content.
- [struct EquatableView](../swiftui/equatableview.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
### Displaying shapes
- [struct Rectangle](../swiftui/rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [struct RoundedRectangle](../swiftui/roundedrectangle.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [struct Circle](../swiftui/circle.md)
  A circle centered on the frame of the view containing it.
- [struct Ellipse](../swiftui/ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [struct Capsule](../swiftui/capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [struct Path](../swiftui/path.md)
  The outline of a 2D shape.
### Transforming views
- [struct ScaledShape](../swiftui/scaledshape.md)
  A shape with a scale transform applied to it.
- [struct RotatedShape](../swiftui/rotatedshape.md)
  A shape with a rotation transform applied to it.
- [struct OffsetShape](../swiftui/offsetshape.md)
  A shape with a translation offset transform applied to it.
- [struct TransformedShape](../swiftui/transformedshape.md)
  A shape with an affine transform applied to it.
- [struct ContainerRelativeShape](../swiftui/containerrelativeshape.md)
  A shape whose dimensions the system calculates from an inset version of the current container shape.
### Styling views
- [struct Color](../swiftui/color.md)
  A representation of a color that adapts to a given context.
- [struct ImagePaint](../swiftui/imagepaint.md)
  A shape style that fills a shape by repeating a region of an image.
- [struct Gradient](../swiftui/gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct LinearGradient](../swiftui/lineargradient.md)
  A linear gradient.
- [struct AngularGradient](../swiftui/angulargradient.md)
  An angular gradient.
- [struct RadialGradient](../swiftui/radialgradient.md)
  A radial gradient.
- [struct ForegroundStyle](../swiftui/foregroundstyle.md)
  The foreground style in the current context.
- [struct FillStyle](../swiftui/fillstyle.md)
  A style for rasterizing vector shapes.
- [struct BackgroundStyle](../swiftui/backgroundstyle.md)
  The background style in the current context.
- [struct SelectionShapeStyle](../swiftui/selectionshapestyle.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [struct SeparatorShapeStyle](../swiftui/separatorshapestyle.md)
  A style appropriate for foreground separator or border lines.
- [struct StrokeStyle](../swiftui/strokestyle.md)
  The characteristics of a stroke that traces a path.
### Creating 2D graphics
- [struct Canvas](../swiftui/canvas.md)
  A view type that supports immediate mode drawing.
### Managing view geometry
- [struct GeometryProxy](../swiftui/geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct GeometryReader](../swiftui/geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct ProjectionTransform](../swiftui/projectiontransform.md)
### Substituting views
- [struct AnyView](../swiftui/anyview.md)
  A type-erased view.
- [struct TupleView](../swiftui/tupleview.md)
  A View created from a swift tuple of View values.

## See Also

- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/swiftui-views)*