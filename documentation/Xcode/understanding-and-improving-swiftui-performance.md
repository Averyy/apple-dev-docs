# Understanding and improving SwiftUI performance

**Framework**: Xcode

Identify and address long-running view updates, and reduce the frequency of updates.

#### Overview

[`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) implements a declarative approach to constructing a user interface. You describe your app’s UI and how it depends on the app’s data and environment. SwiftUI calculates the views that represent the UI, and updates the UI in response to people’s actions and to changes in the view’s dependencies, such as:

- The view’s state
- The environment
- [`Observable`](https://developer.apple.com/documentation/Observation/Observable) model data

Your app needs to compute its view bodies quickly to maintain a responsive experience for people who use the app. View bodies that take too long to run, or views that update too frequently, reduce overall system efficiency as they consume resources that the system could use elsewhere. The system requires views to update before the system renders the next display frame on the screen. If the views don’t complete their updates in time, they cause hitches in your app’s UI, giving someone a poor experience of using your app. For more information, see [`Improving app responsiveness`](improving-app-responsiveness.md).

Use Instruments to detect long-running view body calculations and frequent view updates in your app, and to identify the code in your app that causes these issues. Use common SwiftUI patterns to address the problems you discover.

##### Understand How Your App Uses Swiftui

Follow these steps to trace your app’s SwiftUI use:

1. In Xcode, choose Product > Profile to build and open your app in Instruments.
2. Choose the SwiftUI template.
3. Click Record (red D) to start a deferred recording.
4. Interact with the features of your app you want to test.
5. In Instruments, press Stop Recording.

The Instruments timeline shows a time profile of the code in your app, in parallel with a SwiftUI track.

The SwiftUI track contains lanes which show events related to SwiftUI work that your app causes:

The Hitches timeline reports situations in which your app didn’t prepare a view update in time for the system to render its updated UI to the screen.

When you select the SwiftUI timeline, the detail view shows a summary of all SwiftUI updates in your app. Instruments organizes the updates by module, view name, and category. Use this information to understand how views in your app and in system frameworks spend time updating as you exercise your app’s features.

##### Improve Long Running View Body Computations

Expand the SwiftUI timeline track by clicking the disclosure triangle in the SwiftUI instrument’s timeline. The tracks for View Body Updates, Platform View Updates, and Other Updates show distinct timelines for each module in your app, so that you can identify whether the view that takes a long time to update is part of your app’s code, a third-party SDK, or the system.

Control-click on a long view body update in the timeline and choose Set Inspection Range and Zoom to focus on that update in the timeline and the detail view. Use the Time Profiler instrument to identify what code your app runs during the long update. Click in the Time Profiler track in the timeline to see a call tree of the functions that run during the long update. Switch to the Flame Graph view for an alternative visualization.

A single instance of a long-running update might not contain enough samples in the Time Profiler instrument to help you determine the code in your app that’s running. In this case, repeat the long-running update while you record your app in Instruments, and use multiple examples of the update to identify the code in your app that causes the update to run for a long time. Filter the call tree or flame graph to all instances of the same update by following these steps:

1. Click in the timeline in the Time Profile track, but outside the selected range, to clear the selected range.
2. In the detail view, control-click on `MySwiftUIView.body` and choose Show Calls Made by `MySwiftUIView.body`.

To reset the filter, click Callers/Callees in the Instruments bottom bar, and choose Clear Selection.

A common cause of long view body updates is performing expensive calculations in the view’s  [`body`](https://developer.apple.com/documentation/SwiftUI/View/body-8kl5o) property. Instead, perform the calculation asynchronously, and cache the result to avoid repeating the work every time the view needs to use the result of the calculation.

##### Reduce the Frequency of View Updates

Not all performance problems are caused by long updates. Sometimes, an app generates a sequence of updates in which each update is short, but the large number of updates in the sequence causes SwiftUI to do a lot of work and to be active for a long time. Use the Update Groups timeline to identify groups that are active for a long time, but not associated with long updates.

Control-click on an update group and choose Set Inspection Range to focus on that group in the detail group. Use the information in the Summary: All Updates view to identify which views update as part of the group, and the count of updates.

> **Note**:  You might need to manually adjust the start of the inspection range to include events that cause the update and occur before the update group starts.

Hold the pointer over an update, and then click the arrow that appears and choose Show Causes. The detail view shows a list of updates in the group, and a graphical representation of the events that caused each update, and the effects that each update caused. Nodes in the graph represent objects that generate or receive updates; for example, view bodies, environment objects, and transactions. Edges in the graph represent causal links between nodes; for example, the connection from an [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) object to a view that reads one of the object’s properties in its `body`.

Click on a node to see more information about that node in the inspector. Blue nodes represent objects defined by code in your app. Gray nodes represent objects defined by the system.

Click on an edge to see more information about the update the edge represents in the inspector. The inspector displays additional information Instruments captures about the update, for example, changes to your view’s properties.

> 💡 **Tip**:  To simplify the presentation of the cause graph, Instruments sometimes represents the same nodes and edges in multiple places on the graph. When you click on a node or edge to view more information in the inspector, Instruments highlights all nodes and edges that represent the same object or update.

Compare the events that occur in the cause-and-effect graph with your understanding of the purpose of your views to identify unnecessary updates, or updates that are needed but happen too frequently. Examples of causes for too-frequent updates include:

- Your view observes properties on an object that has other observable properties, and updates when one of the other properties changes. Migrate your observable objects to use the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro, which tracks the properties that a view reads and only emits change events when those properties update. For more information, see [`Migrating from the Observable Object protocol to the Observable macro`](https://developer.apple.com/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro).
- The view that responds to an update causes the views it contains to update in ways that don’t contribute to meaningful changes in the UI; for example, a custom layout using a [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader) that recalculates scroll geometry for the views it contains, including for updates that don’t result in any scroll changes. Identify a different view in your app’s view hierarchy that can receive the update and make only relevant changes to the views it contains.

For views that need to update in response to frequent updates, follow the steps in [`Improve long-running view body computations`](https://developer.apple.com#Improve-long-running-view-body-computations) above, to improve the efficiency of these updates.

The cause-and-effect graph in Instruments only shows one changing property for each edge. After you make a change to reduce the frequency of view updates, capture a new recording in Instruments to determine whether the update frequency is reduced, or a different property update or event also causes the same views to update.

Identify the type of event that most frequently causes your view to update, and prioritize your performance-engineering work to reduce that event’s frequency first.

##### Remove Unnecessary Updates

A cause-and-effect graph that starts with a node that represents code in your app (a blue node), generates events that affect framework code (gray nodes), and ends with a node in your app (another blue node), signifies a situation where your app creates an event that your app needs to respond to itself, but that the SwiftUI framework mediates.

Change your code to reduce the frequency of updates that it causes, by reducing the frequency of the causing events. For example, if you use [`onGeometryChange(for:of:action:)`](https://developer.apple.com/documentation/SwiftUI/View/onGeometryChange(for:of:action:)) to update the layout of subviews whenever a view’s size changes, test whether the magnitude of the change is bigger than a threshold value before updating the layout.

##### Adopt Efficient Swiftui Design Patterns

Keep your view bodies fast. The code in a view body needs to be efficient and rely on limited dependencies, including state and environment objects.

Move business logic and other non-UI work out of views to model types because SwiftUI recreates views, and recalculates view bodies, frequently. So, avoid performing complex, long-running tasks in your [`View`](https://developer.apple.com/documentation/SwiftUI/View) initializer and these methods:

- [`body`](https://developer.apple.com/documentation/SwiftUI/View/body-8kl5o)
- [`onAppear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onAppear(perform:))
- [`onChanged(_:)`](https://developer.apple.com/documentation/SwiftUI/Gesture/onChanged(_:))
- Any other modifiers that can modify view state

Consider the performance impact of complex layouts. Layout readers, for example, [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader) and [`ScrollViewReader`](https://developer.apple.com/documentation/SwiftUI/ScrollViewReader), observe layout changes in their parent views to recalculate their layouts. Reduce the scope of simultaneous layout and state updates by moving views with state dependencies that don’t affect the layout into a separate view hierarchy.

Avoid storing closures in views. Closures can capture additional state from your parent view that make the view update more often. Whenever any of the closure’s captured state changes, SwiftUI needs to recalculate the closure’s result. If the closure captures `self`, whether explicitly or because it references one of the view’s properties, then SwiftUI recalculates the closure’s result whenever any of the view’s properties changes. When accepting a closure passed to your view’s initializer that builds a child view for your view, call the closure in the initializer so you only store its return value. Don’t mark the closure [`@escaping`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/#Escaping-Closures).

You don’t need to do this for action closures, like the closure you pass to [`Button`](https://developer.apple.com/documentation/SwiftUI/Button), or closures that require a parameter, like the closure you pass to [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach). However, such closures could still cause excessive updates, so follow the steps in [`Reduce the frequency of view updates`](https://developer.apple.com#Reduce-the-frequency-of-view-updates) above, to ensure that your app calls its closures efficiently.

## See Also

- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md)
  Make your app more responsive by examining the event-handling and rendering loop.
- [Understanding hangs in your app](understanding-hangs-in-your-app.md)
  Determine the cause for delays in user interactions by examining the main thread and the main run loop.
- [Understanding hitches in your app](understanding-hitches-in-your-app.md)
  Determine the cause of interruptions in motion by examining the render loop.
- [Diagnosing performance issues early](diagnosing-performance-issues-early.md)
  Diagnose potential performance issues in your app during testing with the Thread Performance Checker tool in Xcode.
- [Reducing your app’s launch time](reducing-your-app-s-launch-time.md)
  Create a more responsive experience with your app by minimizing time spent in startup.
- [Reducing terminations in your app](reduce-terminations-in-your-app.md)
  Minimize how frequently the system stops your app by addressing common termination reasons.
- [Reducing disk writes](reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance)*