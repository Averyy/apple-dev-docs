# UIView

**Framework**: UIKit  
**Kind**: class

An object that manages the content for a rectangular area on the screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIView
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
- [About App Development with UIKit](about-app-development-with-uikit.md)
- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)
- [Customizing drawings](customizing-drawings.md)
- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md)
- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Overview

Views are the fundamental building blocks of your app’s user interface, and the [`UIView`](uiview.md) class defines the behaviors that are common to all views. A view object renders content within its bounds rectangle, and handles any interactions with that content. The [`UIView`](uiview.md) class is a concrete class that you can instantiate and use to display a fixed background color. You can also subclass it to draw more sophisticated content. To display labels, images, buttons, and other interface elements commonly found in apps, use the view subclasses that the UIKit framework provides rather than trying to define your own.

Because view objects are the main way your application interacts with the user, they have a number of responsibilities. Here are just a few:

- Drawing and animation - Views draw content in their rectangular area using UIKit or Core Graphics.
- You can animate some view properties to new values.
- Layout and subview management - Views may contain zero or more subviews.
- Views can adjust the size and position of their subviews.
- Use Auto Layout to define the rules for resizing and repositioning your views in response to changes in the view hierarchy.
- Event handling - A view is a subclass of [`UIResponder`](uiresponder.md) and can respond to touches and other types of events.
- Views can install gesture recognizers to handle common gestures.

Views can nest inside other views to create view hierarchies, which offer a convenient way to organize related content. Nesting a view creates a parent-child relationship between the nested child view (known as the ) and the parent (known as the ). A parent view may contain any number of subviews, but each subview has only one superview. By default, when a subview’s visible area extends outside of the bounds of its superview, no clipping of the subview’s content occurs. Use the [`clipsToBounds`](uiview/clipstobounds.md) property to change that behavior.

The [`frame`](uiview/frame.md) and [`bounds`](uiview/bounds.md) properties define the geometry of each view. The [`frame`](uiview/frame.md) property defines the origin and dimensions of the view in the coordinate system of its superview. The [`bounds`](uiview/bounds.md) property defines the internal dimensions of the view as it sees them, and its use is almost exclusive to custom drawing code. The center property provides a convenient way to reposition a view without changing its [`frame`](uiview/frame.md) or [`bounds`](uiview/bounds.md) properties directly.

##### Create a View

Normally, you create views in your storyboards by dragging them from the library to your canvas. You can also create views programmatically. When creating a view, you typically specify its initial size and position relative to its future superview. For example, the following example creates a view and places its top-left corner at the point (10, 10) in the superview’s coordinate system (once it is added to that superview).

To add a subview to another view, call the [`addSubview(_:)`](uiview/addsubview(_:).md) method on the superview. You may add any number of subviews to a view, and sibling views may overlap each other without any issues in iOS. Each call to the [`addSubview(_:)`](uiview/addsubview(_:).md) method places the new view on top of all other siblings. You can specify the relative z-order of subview by adding it using the [`insertSubview(_:aboveSubview:)`](uiview/insertsubview(_:abovesubview:).md) and [`insertSubview(_:belowSubview:)`](uiview/insertsubview(_:belowsubview:).md) methods. You can also exchange the position of already added subviews using the [`exchangeSubview(at:withSubviewAt:)`](uiview/exchangesubview(at:withsubviewat:).md) method.

After creating a view, create Auto Layout rules to govern how the size and position of the view change in response to changes in the rest of the view hierarchy.

##### Draw Views

View drawing occurs on an as-needed basis. When a view is first shown, or when all or part of it becomes visible due to layout changes, the system asks the view to draw its contents. For views that contain custom content using UIKit or Core Graphics, the system calls the view’s [`draw(_:)`](uiview/draw(_:).md) method. Your implementation of this method is responsible for drawing the view’s content into the current graphics context, which is set up by the system automatically prior to calling this method. This creates a static visual representation of your view’s content that can then be displayed on the screen.

When the actual content of your view changes, it’s your responsibility to notify the system that your view needs to be redrawn. You do this by calling your view’s [`setNeedsDisplay()`](uiview/setneedsdisplay().md) or [`setNeedsDisplay(_:)`](uiview/setneedsdisplay(_:).md) method of the view. These methods let the system know that it should update the view during the next drawing cycle. Because it waits until the next drawing cycle to update the view, you can call these methods on multiple views to update them at the same time.

##### Animate Views

Changes to several view properties can be animated — that is, changing the property creates an animation starting at the current value and ending at the new value that you specify. The following properties of the [`UIView`](uiview.md) class are animatable:

- [`frame`](uiview/frame.md)
- [`bounds`](uiview/bounds.md)
- [`center`](uiview/center.md)
- [`transform`](uiview/transform.md)
- [`alpha`](uiview/alpha.md)
- [`backgroundColor`](uiview/backgroundcolor.md)

To animate your changes, create a [`UIViewPropertyAnimator`](uiviewpropertyanimator.md) object and use its handler block to change the values of your view’s properties. The [`UIViewPropertyAnimator`](uiviewpropertyanimator.md) class lets you specify the duration and timing of your animations, but it performs the actual animations. You can pause a property-based animator that’s currently running to interrupt the animation and drive it interactively. For more information, see [`UIViewPropertyAnimator`](uiviewpropertyanimator.md).

##### Threading Considerations

Manipulations to your app’s user interface must occur on the main thread. Thus, you should always call the methods of the [`UIView`](uiview.md) class from code running in the main thread of your app. The only time this may not be strictly necessary is when creating the view object itself, but all other manipulations should occur on the main thread.

##### Subclassing Notes

The [`UIView`](uiview.md) class is a key subclassing point for visual content that also requires user interactions. Although there are many good reasons to subclass [`UIView`](uiview.md), it is recommended that you do so only when the basic [`UIView`](uiview.md) class or the standard system views do not provide the capabilities that you need. Subclassing requires more work on your part to implement the view and to tune its performance.

For information about ways to avoid subclassing, see [`Alternatives to subclassing`](uiview#Alternatives-to-subclassing.md).

###### Methods to Override

When subclassing [`UIView`](uiview.md), there are only a handful of methods you should override and many methods that you might override depending on your needs. Because [`UIView`](uiview.md) is a highly configurable class, there are also many ways to implement sophisticated view behaviors without overriding custom methods, which are discussed in the Alternatives to Subclassing section. In the meantime, the following list includes the methods you might consider overriding in your [`UIView`](uiview.md) subclasses:

- Initialization: - [`init(frame:)`](uiview/init(frame:).md) - It is recommended that you implement this method. You can also implement custom initialization methods in addition to, or instead of, this method.
- [`init(coder:)`](uiview/init(coder:).md) - Implement this method if you load your view from storyboards or nib files and your view requires custom initialization.
- [`layerClass`](uiview/layerclass.md) Use this property only if you want your view to use a different Core Animation layer for its backing store. For example, if your view uses tiling to display a large scrollable area, you might want to set the property to the [`CATiledLayer`](https://developer.apple.com/documentation/QuartzCore/CATiledLayer) class.
- Drawing and printing: - [`draw(_:)`](uiview/draw(_:).md) - Implement this method if your view draws custom content. If your view does not do any custom drawing, avoid overriding this method.
- [`draw(_:for:)`](uiview/draw(_:for:).md) - Implement this method only if you want to draw your view’s content differently during printing.
- Layout and Constraints: - [`requiresConstraintBasedLayout`](uiview/requiresconstraintbasedlayout.md) Use this property if your view class requires constraints to work properly.
- [`updateConstraints()`](uiview/updateconstraints().md) - Implement this method if your view needs to create custom constraints between your subviews.
- [`alignmentRect(forFrame:)`](uiview/alignmentrect(forframe:).md), [`frame(forAlignmentRect:)`](uiview/frame(foralignmentrect:).md) - Implement these methods to override how your views are aligned to other views.
- [`didAddSubview(_:)`](uiview/didaddsubview(_:).md), [`willRemoveSubview(_:)`](uiview/willremovesubview(_:).md) - Implement these methods as needed to track the additions and removals of subviews.
- [`willMove(toSuperview:)`](uiview/willmove(tosuperview:).md), [`didMoveToSuperview()`](uiview/didmovetosuperview().md) - Implement these methods as needed to track the movement of the current view in your view hierarchy.
- Event Handling: - [`gestureRecognizerShouldBegin(_:)`](uiview/gesturerecognizershouldbegin(_:).md) - Implement this method if your view handles touch events directly and might want to prevent attached gesture recognizers from triggering additional actions.
- [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md), [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md), [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md), [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) - Implement these methods if you need to handle touch events directly. (For gesture-based input, use gesture recognizers.)

###### Alternatives to Subclassing

Many view behaviors can be configured without the need for subclassing. Before you start overriding methods, consider whether modifying the following properties or behaviors would provide the behavior you need.

- [`addConstraint(_:)`](uiview/addconstraint(_:).md) - Define automatic layout behavior for the view and its subviews.
- [`autoresizingMask`](uiview/autoresizingmask-swift.property.md) - Provides automatic layout behavior when the superview’s frame changes. These behaviors can be combined with constraints.
- [`contentMode`](uiview/contentmode-swift.property.md) - Provides layout behavior for the view’s content, as opposed to the [`frame`](uiview/frame.md) of the view. This property also affects how the content is scaled to fit the view and whether it is cached or redrawn.
- [`isHidden`](uiview/ishidden.md) or [`alpha`](uiview/alpha.md) - Change the transparency of the view as a whole rather than hiding or applying alpha to your view’s rendered content.
- [`backgroundColor`](uiview/backgroundcolor.md) - Set the view’s color rather than drawing that color yourself.
- Subviews - Rather than draw your content using a [`draw(_:)`](uiview/draw(_:).md) method, embed image and label subviews with the content you want to present.
- Gesture recognizers - Rather than subclass to intercept and handle touch events yourself, you can use gesture recognizers to send an action to a target object.
- Animations - Use the built-in animation support rather than trying to animate changes yourself. The animation support provided by Core Animation is fast and easy to use.
- Image-based backgrounds - For views that display relatively static content, consider using a [`UIImageView`](uiimageview.md) object with gesture recognizers instead of subclassing and drawing the image yourself. Alternatively, you can also use a generic [`UIView`](uiview.md) object and assign your image as the content of the view’s [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) object.

Animations are another way to make visible changes to a view without requiring you to subclass and implement complex drawing code. Many properties of the [`UIView`](uiview.md) class are animatable, which means changes to those properties can trigger system-generated animations. Starting animations requires as little as one line of code to indicate that any changes that follow should be animated. For more information about animation support for views, see [`Animate views`](uiview#Animate-views.md).

## Topics

### Creating a view object
- [init(frame: CGRect)](uiview/init(frame:).md)
  Creates a view with the specified frame rectangle.
- [init?(coder: NSCoder)](uiview/init(coder:).md)
  Creates a view from data in an unarchiver.
### Configuring a view’s visual appearance
- [var backgroundColor: UIColor?](uiview/backgroundcolor.md)
  The view’s background color.
- [var isHidden: Bool](uiview/ishidden.md)
  A Boolean value that determines whether the view is hidden.
- [var alpha: CGFloat](uiview/alpha.md)
  The view’s alpha value.
- [var isOpaque: Bool](uiview/isopaque.md)
  A Boolean value that determines whether the view is opaque.
- [var tintColor: UIColor!](uiview/tintcolor.md)
  The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [var tintAdjustmentMode: UIView.TintAdjustmentMode](uiview/tintadjustmentmode-swift.property.md)
  The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [var clipsToBounds: Bool](uiview/clipstobounds.md)
  A Boolean value that determines whether subviews are confined to the bounds of the view.
- [var clearsContextBeforeDrawing: Bool](uiview/clearscontextbeforedrawing.md)
  A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [var mask: UIView?](uiview/mask.md)
  An optional view whose alpha channel is used to mask a view’s content.
- [class var layerClass: AnyClass](uiview/layerclass.md)
  Returns the class used to create the layer for instances of this class.
- [var layer: CALayer](uiview/layer.md)
  The view’s Core Animation layer to use for rendering.
### Configuring a view’s corners
- [var cornerConfiguration: UICornerConfiguration](uiview/cornerconfiguration-7l0ja.md)
  A configuration that defines the corners of the view.
- [struct UICornerConfiguration](uicornerconfiguration-swift.struct.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [struct UICornerRadius](uicornerradius-swift.struct.md)
  A type that represents the radius the system uses to round a corner.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](uiview/effectiveradius(corner:).md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.
### Configuring the event-related behavior
- [var isUserInteractionEnabled: Bool](uiview/isuserinteractionenabled.md)
  A Boolean value that determines whether user events are ignored and removed from the event queue.
- [var isMultipleTouchEnabled: Bool](uiview/ismultipletouchenabled.md)
  A Boolean value that indicates whether the view receives more than one touch at a time.
- [var isExclusiveTouch: Bool](uiview/isexclusivetouch.md)
  A Boolean value that indicates whether the receiver handles touch events exclusively.
### Configuring the bounds and frame rectangles
- [var frame: CGRect](uiview/frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](uiview/bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var center: CGPoint](uiview/center.md)
  The center point of the view’s frame rectangle.
- [var transform: CGAffineTransform](uiview/transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var transform3D: CATransform3D](uiview/transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](uiview/anchorpoint.md)
  The anchor point of the view’s bounds rectangle.
### Managing the view hierarchy
- [var superview: UIView?](uiview/superview.md)
  The receiver’s superview, or `nil` if it has none.
- [var subviews: [UIView]](uiview/subviews.md)
  The receiver’s immediate subviews.
- [var window: UIWindow?](uiview/window.md)
  The receiver’s window object, or `nil` if it has none.
- [func addSubview(UIView)](uiview/addsubview(_:).md)
  Adds a view to the end of the receiver’s list of subviews.
- [func bringSubviewToFront(UIView)](uiview/bringsubviewtofront(_:).md)
  Moves the specified subview so that it appears on top of its siblings.
- [func sendSubviewToBack(UIView)](uiview/sendsubviewtoback(_:).md)
  Moves the specified subview so that it appears behind its siblings.
- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [func insertSubview(UIView, at: Int)](uiview/insertsubview(_:at:).md)
  Inserts a subview at the specified index.
- [func insertSubview(UIView, aboveSubview: UIView)](uiview/insertsubview(_:abovesubview:).md)
  Inserts a view above another view in the view hierarchy.
- [func insertSubview(UIView, belowSubview: UIView)](uiview/insertsubview(_:belowsubview:).md)
  Inserts a view below another view in the view hierarchy.
- [func exchangeSubview(at: Int, withSubviewAt: Int)](uiview/exchangesubview(at:withsubviewat:).md)
  Exchanges the subviews at the specified indices.
- [func isDescendant(of: UIView) -> Bool](uiview/isdescendant(of:).md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.
### Observing view-related changes
- [func didAddSubview(UIView)](uiview/didaddsubview(_:).md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](uiview/willremovesubview(_:).md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](uiview/willmove(tosuperview:).md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](uiview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](uiview/willmove(towindow:).md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](uiview/didmovetowindow.md)
  Tells the view that its window object changed.
### Observing trait changes
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
### Requesting trait updates
- [func updateTraitsIfNeeded()](uiview/updatetraitsifneeded.md)
### Overriding trait values
- [var traitOverrides: UITraitOverrides](uiview/traitoverrides-fd9z.md)
- [struct UITraitOverrides](uitraitoverrides-swift.struct.md)
  A mutable container of traits you use to set trait changes for an object and its descendants.
### Configuring content margins
- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uiview/directionallayoutmargins.md)
  The default spacing to use when laying out content in a view, taking into account the current language direction.
- [var layoutMargins: UIEdgeInsets](uiview/layoutmargins.md)
  The default spacing to use when laying out content in the view.
- [var preservesSuperviewLayoutMargins: Bool](uiview/preservessuperviewlayoutmargins.md)
  A Boolean value indicating whether the current view also respects the margins of its superview.
- [func layoutMarginsDidChange()](uiview/layoutmarginsdidchange.md)
  Notifies the view that the layout margins changed.
### Getting the safe area
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var safeAreaInsets: UIEdgeInsets](uiview/safeareainsets.md)
  The insets that you use to determine the safe area for this view.
- [var safeAreaLayoutGuide: UILayoutGuide](uiview/safearealayoutguide.md)
  The layout guide representing the portion of your view that is unobscured by bars and other content.
- [func safeAreaInsetsDidChange()](uiview/safeareainsetsdidchange.md)
  Called when the safe area of the view changes.
- [var insetsLayoutMarginsFromSafeArea: Bool](uiview/insetslayoutmarginsfromsafearea.md)
  A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.
### Managing the view’s constraints
- [var constraints: [NSLayoutConstraint]](uiview/constraints.md)
  The constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](uiview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](uiview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](uiview/removeconstraint(_:).md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](uiview/removeconstraints(_:).md)
  Removes the specified constraints from the view.
### Creating constraints using layout anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](uiview/bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](uiview/centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](uiview/centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var firstBaselineAnchor: NSLayoutYAxisAnchor](uiview/firstbaselineanchor.md)
  A layout anchor representing the baseline for the topmost line of text in the view.
- [var heightAnchor: NSLayoutDimension](uiview/heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var lastBaselineAnchor: NSLayoutYAxisAnchor](uiview/lastbaselineanchor.md)
  A layout anchor representing the baseline for the bottommost line of text in the view.
- [var leadingAnchor: NSLayoutXAxisAnchor](uiview/leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](uiview/leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](uiview/rightanchor.md)
  A layout anchor representing the right edge of the view’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](uiview/topanchor.md)
  A layout anchor representing the top edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](uiview/trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.
- [var widthAnchor: NSLayoutDimension](uiview/widthanchor.md)
  A layout anchor representing the width of the view’s frame.
### Working with layout guides
- [func addLayoutGuide(UILayoutGuide)](uiview/addlayoutguide(_:).md)
  Adds the specified layout guide to the view.
- [var layoutGuides: [UILayoutGuide]](uiview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: UILayoutGuide](uiview/layoutmarginsguide.md)
  A layout guide representing the view’s margins.
- [var readableContentGuide: UILayoutGuide](uiview/readablecontentguide.md)
  A layout guide representing an area with a readable width within the view.
- [func removeLayoutGuide(UILayoutGuide)](uiview/removelayoutguide(_:).md)
  Removes the specified layout guide from the view.
### Measuring in Auto Layout
- [func systemLayoutSizeFitting(CGSize) -> CGSize](uiview/systemlayoutsizefitting(_:).md)
  Returns the optimal size of the view based on its current constraints.
- [func systemLayoutSizeFitting(CGSize, withHorizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize](uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:).md)
  Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [var intrinsicContentSize: CGSize](uiview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](uiview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](uiview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](uiview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.
### Aligning views in Auto Layout
- [func alignmentRect(forFrame: CGRect) -> CGRect](uiview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: CGRect) -> CGRect](uiview/frame(foralignmentrect:).md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: UIEdgeInsets](uiview/alignmentrectinsets.md)
  The insets from the view’s frame that define its alignment rectangle.
- [var forFirstBaselineLayout: UIView](uiview/forfirstbaselinelayout.md)
  Returns a view used to satisfy first baseline constraints.
- [var forLastBaselineLayout: UIView](uiview/forlastbaselinelayout.md)
  Returns a view used to satisfy last baseline constraints.
### Triggering Auto Layout
- [func needsUpdateConstraints() -> Bool](uiview/needsupdateconstraints.md)
  A Boolean value that determines whether the view’s constraints need updating.
- [func setNeedsUpdateConstraints()](uiview/setneedsupdateconstraints.md)
  Controls whether the view’s constraints need updating.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func updateConstraintsIfNeeded()](uiview/updateconstraintsifneeded.md)
  Updates the constraints for the receiving view and its subviews.
### Debugging Auto Layout
- [func constraintsAffectingLayout(for: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]](uiview/constraintsaffectinglayout(for:).md)
  Returns the constraints impacting the layout of the view for a given axis.
- [var hasAmbiguousLayout: Bool](uiview/hasambiguouslayout.md)
  A Boolean value that determines whether the constraints impacting the layout of the view incompletely specify the location of the view.
- [func exerciseAmbiguityInLayout()](uiview/exerciseambiguityinlayout.md)
  Randomly changes the frame of a view with an ambiguous layout between the different valid values.
### Configuring the resizing behavior
- [var contentMode: UIView.ContentMode](uiview/contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [UIView.ContentMode](uiview/contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeThatFits(CGSize) -> CGSize](uiview/sizethatfits(_:).md)
  Asks the view to calculate and return the size that best fits the specified size.
- [func sizeToFit()](uiview/sizetofit.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizesSubviews: Bool](uiview/autoresizessubviews.md)
  A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [var autoresizingMask: UIView.AutoresizingMask](uiview/autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.
### Laying out subviews
- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func setNeedsLayout()](uiview/setneedslayout.md)
  Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [func layoutIfNeeded()](uiview/layoutifneeded.md)
  Lays out the subviews immediately, if layout updates are pending.
- [class var requiresConstraintBasedLayout: Bool](uiview/requiresconstraintbasedlayout.md)
  A Boolean value that indicates whether the receiver depends on the constraint-based layout system.
- [var translatesAutoresizingMaskIntoConstraints: Bool](uiview/translatesautoresizingmaskintoconstraints.md)
  A Boolean value that determines whether the view’s autoresizing mask is translated into Auto Layout constraints.
### Accessing insets and layout guides
- [UIView.LayoutRegion](uiview/layoutregion.md)
- [func directionalEdgeInsets(for: UIView.LayoutRegion) -> NSDirectionalEdgeInsets](uiview/directionaledgeinsets(for:).md)
- [func edgeInsets(for: UIView.LayoutRegion) -> UIEdgeInsets](uiview/edgeinsets(for:).md)
- [func layoutGuide(for: UIView.LayoutRegion) -> UILayoutGuide](uiview/layoutguide(for:).md)
### Adjusting the user interface
- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiview/overrideuserinterfacestyle.md)
  The user interface style adopted by the view and all of its subviews.
- [var semanticContentAttribute: UISemanticContentAttribute](uiview/semanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [var effectiveUserInterfaceLayoutDirection: UIUserInterfaceLayoutDirection](uiview/effectiveuserinterfacelayoutdirection.md)
  The user interface layout direction appropriate for arranging the immediate content of the view.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection](uiview/userinterfacelayoutdirection(for:).md)
  Returns the user interface direction for the given semantic content attribute.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute, relativeTo: UIUserInterfaceLayoutDirection) -> UIUserInterfaceLayoutDirection](uiview/userinterfacelayoutdirection(for:relativeto:).md)
  Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.
### Constraining views to the keyboard
- [var keyboardLayoutGuide: UIKeyboardLayoutGuide](uiview/keyboardlayoutguide.md)
  A layout guide that tracks the keyboard’s position in your app’s layout.
### Adding and removing interactions
- [func addInteraction(any UIInteraction)](uiview/addinteraction(_:).md)
  Adds an interaction to the view.
- [func removeInteraction(any UIInteraction)](uiview/removeinteraction(_:).md)
  Removes an interaction from the view.
- [var interactions: [any UIInteraction]](uiview/interactions.md)
  The array of interactions for the view.
- [protocol UIInteraction](uiinteraction.md)
  The protocol that an interaction implements to access the view that owns it.
### Drawing and updating the view
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
- [func setNeedsDisplay()](uiview/setneedsdisplay.md)
  Marks the receiver’s entire bounds rectangle as needing to be redrawn.
- [func setNeedsDisplay(CGRect)](uiview/setneedsdisplay(_:).md)
  Marks the specified rectangle of the receiver as needing to be redrawn.
- [var contentScaleFactor: CGFloat](uiview/contentscalefactor.md)
  The scale factor applied to the view.
- [func tintColorDidChange()](uiview/tintcolordidchange.md)
  Called by the system when the tint color property changes.
### Updating the view when property values change
- [UIView.Invalidating](uiview/invalidating.md)
  A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.
- [protocol UIViewInvalidating](uiviewinvalidating.md)
  Implements a type of invalidation that can occur on a view that requires an update.
### Formatting printed view content
- [func viewPrintFormatter() -> UIViewPrintFormatter](uiview/viewprintformatter.md)
  Returns a print formatter for the receiving view.
- [func draw(CGRect, for: UIViewPrintFormatter)](uiview/draw(_:for:).md)
  Implemented to draw the view’s content for printing.
### Managing gesture recognizers
- [func addGestureRecognizer(UIGestureRecognizer)](uiview/addgesturerecognizer(_:).md)
  Attaches a gesture recognizer to the view.
- [func removeGestureRecognizer(UIGestureRecognizer)](uiview/removegesturerecognizer(_:).md)
  Detaches a gesture recognizer from the receiving view.
- [var gestureRecognizers: [UIGestureRecognizer]?](uiview/gesturerecognizers.md)
  The gesture-recognizer objects currently attached to the view.
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uiview/gesturerecognizershouldbegin(_:).md)
  Asks the view if the gesture recognizer should continue tracking touch events.
### Working with focus
- [var canBecomeFocused: Bool](uiview/canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [class var inheritedAnimationDuration: TimeInterval](uiview/inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var isFocused: Bool](uiview/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](uiview/focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](uiview/focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](uiview/focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
### Using motion effects
- [func addMotionEffect(UIMotionEffect)](uiview/addmotioneffect(_:).md)
  Begins applying a motion effect to the view.
- [var motionEffects: [UIMotionEffect]](uiview/motioneffects.md)
  The array of motion effects for the view.
- [func removeMotionEffect(UIMotionEffect)](uiview/removemotioneffect(_:).md)
  Stops applying a motion effect to the view.
### Managing the hover appearance
- [var hoverStyle: UIHoverStyle?](uiview/hoverstyle.md)
  The hover style for the view.
- [class UIHoverStyle](uihoverstyle.md)
  The hover style to apply to a view, including an effect and a shape to use for displaying that effect.
- [class UIHoverEffectLayer](uihovereffectlayer.md)
### Managing font-sizing preferences
- [var minimumContentSizeCategory: UIContentSizeCategory?](uiview/minimumcontentsizecategory.md)
  The minimum content size category for the view and its subviews.
- [var maximumContentSizeCategory: UIContentSizeCategory?](uiview/maximumcontentsizecategory.md)
  The maximum content size category for the view and its subviews.
- [var appliedContentSizeCategoryLimitsDescription: String](uiview/appliedcontentsizecategorylimitsdescription.md)
  A string that lists each of the view’s superviews, its content size category, and whether that view has content size category limits.
### Preserving and restoring state
- [var restorationIdentifier: String?](uiview/restorationidentifier.md)
  The identifier that determines whether the view supports state restoration.
- [func encodeRestorableState(with: NSCoder)](uiview/encoderestorablestate(with:).md)
  Encodes state-related information for the view.
- [func decodeRestorableState(with: NSCoder)](uiview/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view.
### Capturing a view snapshot
- [func snapshotView(afterScreenUpdates: Bool) -> UIView?](uiview/snapshotview(afterscreenupdates:).md)
  Returns a snapshot view based on the contents of the current view.
- [func resizableSnapshotView(from: CGRect, afterScreenUpdates: Bool, withCapInsets: UIEdgeInsets) -> UIView?](uiview/resizablesnapshotview(from:afterscreenupdates:withcapinsets:).md)
  Returns a snapshot view based on the specified contents of the current view, with stretchable insets.
- [func drawHierarchy(in: CGRect, afterScreenUpdates: Bool) -> Bool](uiview/drawhierarchy(in:afterscreenupdates:).md)
  Renders a snapshot of the complete view hierarchy as visible onscreen into the current context.
### Identifying the view at runtime
- [var tag: Int](uiview/tag.md)
  An integer that you can use to identify view objects in your application.
- [func viewWithTag(Int) -> UIView?](uiview/viewwithtag(_:).md)
  Returns the view whose tag matches the specified value.
### Converting between view coordinate systems
- [func convert(CGPoint, to: UIView?) -> CGPoint](uiview/convert(_:to:)-1xizt.md)
  Converts a point from the receiver’s coordinate system to that of the specified view.
- [func convert(CGPoint, from: UIView?) -> CGPoint](uiview/convert(_:from:)-8neo1.md)
  Converts a point from the coordinate system of a given view to that of the receiver.
- [func convert(CGRect, to: UIView?) -> CGRect](uiview/convert(_:to:)-2kf3d.md)
  Converts a rectangle from the receiver’s coordinate system to that of another view.
- [func convert(CGRect, from: UIView?) -> CGRect](uiview/convert(_:from:)-7irzk.md)
  Converts a rectangle from the coordinate system of another view to that of the receiver.
### Hit-testing in a view
- [func hitTest(CGPoint, with: UIEvent?) -> UIView?](uiview/hittest(_:with:).md)
  Returns the farthest descendant in the view hierarchy of the current view, including itself, that contains the specified point.
- [func point(inside: CGPoint, with: UIEvent?) -> Bool](uiview/point(inside:with:).md)
  Returns a Boolean value indicating whether the receiver contains the specified point.
### Ending a view-editing session
- [func endEditing(Bool) -> Bool](uiview/endediting(_:).md)
  Causes the view (or one of its embedded text fields) to resign the first responder status.
### Modifying the accessibility behavior
- [var accessibilityIgnoresInvertColors: Bool](uiview/accessibilityignoresinvertcolors.md)
  A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [var largeContentImage: UIImage?](uiview/largecontentimage.md)
  An image that represents the view in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uiview/largecontentimageinsets.md)
  Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [var largeContentTitle: String?](uiview/largecontenttitle.md)
  A string that describes the view in the large content viewer.
- [var scalesLargeContentImage: Bool](uiview/scaleslargecontentimage.md)
  A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [var showsLargeContentViewer: Bool](uiview/showslargecontentviewer.md)
  A Boolean value that indicates whether to show the view in the large content viewer.
### Animating views
- [static func animate(Animation, changes: () -> Void, completion: (() -> Void)?)](uiview/animate(_:changes:completion:).md)
- [class func animate(springDuration: TimeInterval, bounce: CGFloat, initialSpringVelocity: CGFloat, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(springduration:bounce:initialspringvelocity:delay:options:animations:completion:).md)
  Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:delay:options:animations:completion:).md)
  Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [class func animate(withDuration: TimeInterval, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:animations:completion:).md)
  Animate changes to one or more views using the specified duration and completion handler.
- [class func animate(withDuration: TimeInterval, animations: () -> Void)](uiview/animate(withduration:animations:).md)
  Animate changes to one or more views using the specified duration.
- [class func transition(with: UIView, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiview/transition(with:duration:options:animations:completion:).md)
  Creates a transition animation for the specified container view.
- [class func transition(from: UIView, to: UIView, duration: TimeInterval, options: UIView.AnimationOptions, completion: ((Bool) -> Void)?)](uiview/transition(from:to:duration:options:completion:).md)
  Creates a transition animation between the specified views using the given parameters.
- [class func animateKeyframes(withDuration: TimeInterval, delay: TimeInterval, options: UIView.KeyframeAnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animatekeyframes(withduration:delay:options:animations:completion:).md)
  Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [class func addKeyframe(withRelativeStartTime: Double, relativeDuration: Double, animations: () -> Void)](uiview/addkeyframe(withrelativestarttime:relativeduration:animations:).md)
  Specifies the timing and animation values for a single frame of a keyframe animation.
- [class func perform(UIView.SystemAnimation, on: [UIView], options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiview/perform(_:on:options:animations:completion:).md)
  Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, usingSpringWithDamping: CGFloat, initialSpringVelocity: CGFloat, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:delay:usingspringwithdamping:initialspringvelocity:options:animations:completion:).md)
  Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [class func performWithoutAnimation(() -> Void)](uiview/performwithoutanimation(_:).md)
  Disables a view transition animation.
- [class func modifyAnimations(withRepeatCount: CGFloat, autoreverses: Bool, animations: () -> Void)](uiview/modifyanimations(withrepeatcount:autoreverses:animations:).md)
  Repeats the specified animations a specific number of times, optionally running the animation forward and backward.
### Constants
- [UIView.AnimationCurve](uiview/animationcurve.md)
  Specifies the supported animation curves.
- [UIView.AnimationOptions](uiview/animationoptions.md)
  Options for animating views using block objects.
- [UIView.AnimationTransition](uiview/animationtransition.md)
  Animation transition options for use in an animation block object.
- [UIView.SystemAnimation](uiview/systemanimation.md)
  Option to remove the views from the hierarchy when animation is complete.
- [UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions.md)
  Options for configuring keyframe-based animations.
- [NSLayoutConstraint.Axis](nslayoutconstraint/axis.md)
  Keys that specify a horizontal or vertical layout constraint between objects.
- [UIView.TintAdjustmentMode](uiview/tintadjustmentmode-swift.enum.md)
  The tint adjustment mode for the view.
- [class let layoutFittingCompressedSize: CGSize](uiview/layoutfittingcompressedsize.md)
  The option to use the smallest possible size.
- [class let layoutFittingExpandedSize: CGSize](uiview/layoutfittingexpandedsize.md)
  The option to use the largest possible size.
- [class let noIntrinsicMetric: CGFloat](uiview/nointrinsicmetric.md)
  The absence of an intrinsic metric for a given numeric view property.
- [UIView.AutoresizingMask](uiview/autoresizingmask-swift.struct.md)
  Options for automatic view resizing.
- [enum UISemanticContentAttribute](uisemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
### Deprecated
- [Deprecated symbols](uiview-deprecated-symbols.md)
  Symbols that views no longer support.
### Initializers
- [convenience init()](uiview/init.md)
### Instance Methods
- [func setNeedsUpdateProperties()](uiview/setneedsupdateproperties.md)
  Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updateProperties()](uiview/updateproperties.md)
  Configures the view’s content and styling properties before layout.
- [func updatePropertiesIfNeeded()](uiview/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
### Enumerations
- [UIView.Invalidations](uiview/invalidations.md)
  Changes that cause an aspect of a view to be invalid and require an update.

## Relationships

### Inherits From
- [UIResponder](uiresponder.md)
### Inherited By
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIAlertView](uialertview.md)
- [UIBackgroundExtensionView](uibackgroundextensionview.md)
- [UICalendarView](uicalendarview.md)
- [UICollectionReusableView](uicollectionreusableview.md)
- [UIContentUnavailableView](uicontentunavailableview.md)
- [UIControl](uicontrol.md)
- [UIEventAttributionView](uieventattributionview.md)
- [UIImageView](uiimageview.md)
- [UIInputView](uiinputview.md)
- [UILabel](uilabel.md)
- [UIListContentView](uilistcontentview.md)
- [UINavigationBar](uinavigationbar.md)
- [UIPickerView](uipickerview.md)
- [UIPopoverBackgroundView](uipopoverbackgroundview.md)
- [UIProgressView](uiprogressview.md)
- [UIScrollView](uiscrollview.md)
- [UISearchBar](uisearchbar.md)
- [UIStackView](uistackview.md)
- [UIStandardTextCursorView](uistandardtextcursorview.md)
- [UITabBar](uitabbar.md)
- [UITableViewCell](uitableviewcell.md)
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
- [UIToolbar](uitoolbar.md)
- [UIVisualEffectView](uivisualeffectview.md)
- [UIWebView](uiwebview.md)
- [UIWindow](uiwindow.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md)
  Customize your app’s user interface with views and controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview)*