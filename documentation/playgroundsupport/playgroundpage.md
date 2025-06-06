# PlaygroundPage

**Framework**: Playground Support  
**Kind**: cl

An object you use to configure the state of a playground page and its live view.

**Availability**:
- macOS 11.0+
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
final class PlaygroundPage
```

#### Overview

You access the current playground page by using this class's static [`current`](playgroundpage/1964509-current.md) property; no more than one page is ever active at the same time. Playground pages in Swift Playgrounds have different capabilities than playground pages in Xcode. For example, control over the execution mode is available only in Swift Playgrounds, while the Touch Bar is accessible only to playgrounds in Xcode. 

Both playground environments can set a live view, which you use to show the visual results of running the code on the playground page.

```swift
PlaygroundPage.current.setLiveView(
    List(0..<42) { number in
        Text("My favorite number is \(number).")
    }
)
```

You also use the current page to configure the , a special live view that runs in a separate process from the code on a playground page and is available only in Swift Playgrounds. The always-on live view can display results that persist across multiple runs of the code on a page, or that you need for one-time setup tasks that take time to run. For example, you might use the always-on live view to display multiple stages of progress through a playground page that has multiple steps to reach the solution. 

Because the always-on live view is hosted outside of the process that runs the code on a playground page, you communicate with it indirectly. For more information, see [`Messaging Between a Playground Page and the Always-On Live View`](messaging_between_a_playground_page_and_the_always-on_live_view.md). 

## Topics

### Configuring Live Views
- [static let current: PlaygroundPage](playgroundpage/1964509-current.md)
  The current playground page.
- [func setLiveView<IncomingView>(IncomingView)](playgroundpage/3375751-setliveview.md)
  Displays a SwiftUI view that shows the result of running the code that’s on the current page.
- [func setLiveView<IncomingView>(IncomingView)](playgroundpage/3375752-setliveview.md)
  Displays a view that shows the result of running the code that’s on the current page.
- [var liveView: (any PlaygroundLiveViewable)?](playgroundpage/1964506-liveview.md)
  A live view that shows the result of running the code that’s on the current page.
### Configuring Execution
- [var executionMode: PlaygroundPage.ExecutionMode](playgroundpage/3029561-executionmode.md)
  The currently selected speed for executing the code on this playground page.
- [enum PlaygroundPage.ExecutionMode](playgroundpage/executionmode.md)
  The available speeds for executing the code on a playground page.
- [var needsIndefiniteExecution: Bool](playgroundpage/1964501-needsindefiniteexecution.md)
  A Boolean value that indicates whether indefinite execution is enabled.
- [func finishExecution() -> Never](playgroundpage/1964505-finishexecution.md)
  Terminates execution of the current playground page.
### Assessing Progress
- [var assessmentStatus: PlaygroundPage.AssessmentStatus?](playgroundpage/3029560-assessmentstatus.md)
  A value that indicates whether a learner has passed, failed, or not yet finished the task on a page.
- [enum PlaygroundPage.AssessmentStatus](playgroundpage/assessmentstatus.md)
  The values you use to communicate whether a learner has passed, failed, or not yet finished the task on a page.
### Inspecting Page Data
- [var text: String](playgroundpage/3029563-text.md)
  The current contents of the playground page, including any user-entered text.
- [var keyValueStore: PlaygroundKeyValueStore](playgroundpage/3029562-keyvaluestore.md)
  An object that persists data on a page between multiple sessions.
### Displaying Touch Bar Items
- [var liveTouchBar: NSTouchBar?](playgroundpage/2919769-livetouchbar.md)
  An object you use to add items to the Touch Bar of supported MacBook Pro models.
### Instance Properties
- [var userModuleNames: [String]](playgroundpage/3919480-usermodulenames.md)
- [var wantsFullScreenLiveView: Bool](playgroundpage/3074093-wantsfullscreenliveview.md)
### Instance Methods
- [func getText(forSourceFile: String, inUserModule: String) -> String?](playgroundpage/3919478-gettext.md)
- [func listSourceFiles(inUserModule: String) -> [String]](playgroundpage/3919479-listsourcefiles.md)
- [func navigateTo(page: PlaygroundPage.PageNavigation)](playgroundpage/3239065-navigateto.md)
- [func openApplication(withBundleIdentifier: String, iTunesItemIdentifier: Int?)](playgroundpage/3239066-openapplication.md)
- [func openPlayground(withContentIdentifier: String, toPageAtIndex: Int?)](playgroundpage/3239067-openplayground.md)
- [func showGlossaryEntry(named: String, at: CGRect?, in: UIView?)](playgroundpage/3239068-showglossaryentry.md)
### Enumerations
- [enum PlaygroundPage.PageNavigation](playgroundpage/pagenavigation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage)*