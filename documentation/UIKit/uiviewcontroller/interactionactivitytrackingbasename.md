# interactionActivityTrackingBaseName

**Framework**: UIKit  
**Kind**: property

The base name the view controller uses for logging signposts that annotate user interactions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var interactionActivityTrackingBaseName: String? { get set }
```

#### Discussion

To help you investigate perfomance issues in your app, UIKit annotates significant user interactions with signpost messages. It creates activities that span the duration of the interaction and sets one of the [`ProcessInfo.ActivityOptions`](https://developer.apple.com/documentation/Foundation/ProcessInfo/ActivityOptions) for tracking: doc://com.apple.documentation/documentation/foundation/processinfo/activityoptions/3967425-animationtrackingenabled or doc://com.apple.documentation/documentation/foundation/processinfo/activityoptions/3967426-trackingenabled.

Use this property to customize the tracking name the activity uses in the signpost messages. Scroll views that can derive their enclosing view controller also use the tracking name to annotate interactive dragging and programmatic scrolling events.

In many cases, you can set the tracking name once in `init`, `viewDidLoad,` or `awakeFromNib`. You can, however, change the tracking name in response to different configurations. In this example, the tracking name updates in response to toggling a switch.

When not explicitly set, custom subclasses use their class name as the base name, while base classes may use the [`accessibilityIdentifier`](uiaccessibilityidentification/accessibilityidentifier.md) of the controller’s managed view.

If the view controller is a prominent child view controller of a [`UINavigationController`](uinavigationcontroller.md), [`UITabBarController`](uitabbarcontroller.md), or [`UISplitViewController`](uisplitviewcontroller.md), the parent may derive a name by applying a prefix:

- `UINC-` for a navigation controller
- `UITBC-` for a tab bar controller
- `UISVC-` for a split view controller

The system applies a suffix to the base name to denote the type of user interaction:

- `-Appearing` when presenting the view controller
- `-Disappearing` when dismising the view controller
- `-Scrolling` when scrolling the view controller’s managed `UIScrollView`
- `-Dragging` when dragging the view controller’s managed `UIScrollView`

For example, UIKit uses the tracking name `UINC-MyListTableViewController-Appearing` in a signpost when presenting a navigation controler with a `MyListTableViewController` prominent child controller.

## See Also

- [Recording Performance Data](../os/recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [Improving app responsiveness](../Xcode/improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/interactionactivitytrackingbasename)*