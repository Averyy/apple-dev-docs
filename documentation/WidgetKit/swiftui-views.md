# SwiftUI views for widgets

**Framework**: WidgetKit

Present your app’s content in widgets with SwiftUI views.

## Overview

Widgets can use many, but not all, SwiftUI views to present content. Use the views listed below to implement your widget’s view.

> **Note**: Widgets can’t use UIKit or AppKit views wrapped with [`UIViewRepresentable`](../SwiftUI/uiviewrepresentable.md) or [`NSViewRepresentable`](../SwiftUI/nsviewrepresentable.md).

## Topics

### Displaying text
- [Displaying dynamic dates in widgets](./displaying-dynamic-dates.md)
  Show up-to-date, time-based information in your widget even when it isn’t running.
- [struct Text](../SwiftUI/text.md)
  A view that displays one or more lines of read-only text.
### Showing images
- [struct Image](../SwiftUI/image.md)
  A view that displays an image.
### Adding interaction
- [Adding interactivity to widgets and Live Activities](./adding-interactivity-to-widgets-and-live-activities.md)
  Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [struct Button](../SwiftUI/button.md)
  A control that initiates an action.
- [struct Toggle](../SwiftUI/toggle.md)
  A control that toggles between on and off states.
### Adding labels and links
- [struct Label](../SwiftUI/label.md)
  A standard label for user interface items, consisting of an icon with a title.
- [struct Link](../SwiftUI/link.md)
  A control for navigating to a URL.
### Stacking views
- [struct HStack](../SwiftUI/hstack.md)
  A view that arranges its subviews in a horizontal line.
- [struct VStack](../SwiftUI/vstack.md)
  A view that arranges its subviews in a vertical line.
- [struct ZStack](../SwiftUI/zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [struct LazyHStack](../SwiftUI/lazyhstack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct LazyVStack](../SwiftUI/lazyvstack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.
### Arranging views in grids
- [struct LazyHGrid](../SwiftUI/lazyhgrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct LazyVGrid](../SwiftUI/lazyvgrid.md)
  A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
- [struct GridItem](../SwiftUI/griditem.md)
  A description of a row or a column in a lazy grid.
### Enumerating lists
- [struct ForEach](../SwiftUI/foreach.md)
  A structure that computes views on demand from an underlying collection of identified data.
### Grouping views
- [struct Group](../SwiftUI/group.md)
  A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [struct GroupBox](../SwiftUI/groupbox.md)
  A stylized view, with an optional label, that visually collects a logical grouping of content.
- [struct Section](../SwiftUI/section.md)
  A container view that you can use to add hierarchy within certain views.
### Representing hierarchies
- [struct OutlineGroup](../SwiftUI/outlinegroup.md)
  A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
### Adding spacers and dividers
- [struct Spacer](../SwiftUI/spacer.md)
  A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
- [struct Divider](../SwiftUI/divider.md)
  A visual element that can be used to separate other content.
### Handling conditional views
- [struct EmptyView](../SwiftUI/emptyview.md)
  A view that doesn’t contain any content.
- [struct EquatableView](../SwiftUI/equatableview.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
### Displaying shapes
- [struct Rectangle](../SwiftUI/rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [struct RoundedRectangle](../SwiftUI/roundedrectangle.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [struct Circle](../SwiftUI/circle.md)
  A circle centered on the frame of the view containing it.
- [struct Ellipse](../SwiftUI/ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [struct Capsule](../SwiftUI/capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [struct Path](../SwiftUI/path.md)
  The outline of a 2D shape.
### Transforming views
- [struct ScaledShape](../SwiftUI/scaledshape.md)
  A shape with a scale transform applied to it.
- [struct RotatedShape](../SwiftUI/rotatedshape.md)
  A shape with a rotation transform applied to it.
- [struct OffsetShape](../SwiftUI/offsetshape.md)
  A shape with a translation offset transform applied to it.
- [struct TransformedShape](../SwiftUI/transformedshape.md)
  A shape with an affine transform applied to it.
- [struct ContainerRelativeShape](../SwiftUI/containerrelativeshape.md)
  A shape whose dimensions the system calculates from an inset version of the current container shape.
### Styling views
- [struct Color](../SwiftUI/color.md)
  A representation of a color that adapts to a given context.
- [struct ImagePaint](../SwiftUI/imagepaint.md)
  A shape style that fills a shape by repeating a region of an image.
- [struct Gradient](../SwiftUI/gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct LinearGradient](../SwiftUI/lineargradient.md)
  A linear gradient.
- [struct AngularGradient](../SwiftUI/angulargradient.md)
  An angular gradient.
- [struct RadialGradient](../SwiftUI/radialgradient.md)
  A radial gradient.
- [struct ForegroundStyle](../SwiftUI/foregroundstyle.md)
  The foreground style in the current context.
- [struct FillStyle](../SwiftUI/fillstyle.md)
  A style for rasterizing vector shapes.
- [struct BackgroundStyle](../SwiftUI/backgroundstyle.md)
  The background style in the current context.
- [struct SelectionShapeStyle](../SwiftUI/selectionshapestyle.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [struct SeparatorShapeStyle](../SwiftUI/separatorshapestyle.md)
  A style appropriate for foreground separator or border lines.
- [struct StrokeStyle](../SwiftUI/strokestyle.md)
  The characteristics of a stroke that traces a path.
### Creating 2D graphics
- [struct Canvas](../SwiftUI/canvas.md)
  A view type that supports immediate mode drawing.
### Managing view geometry
- [struct GeometryProxy](../SwiftUI/geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct GeometryReader](../SwiftUI/geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct ProjectionTransform](../SwiftUI/projectiontransform.md)
  A 3x3 matrix that transforms points in a plane.
### Substituting views
- [struct AnyView](../SwiftUI/anyview.md)
  A type-erased view.
- [struct TupleView](../SwiftUI/tupleview.md)
  A View created from a swift tuple of View values.

## See Also

### Presentation
- [Creating views for widgets, Live Activities, and watch complications](./creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/swiftui-views)*