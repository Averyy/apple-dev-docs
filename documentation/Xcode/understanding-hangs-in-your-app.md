# Understanding hangs in your app

**Framework**: Xcode

Determine the cause for delays in user interactions by examining the main thread and the main run loop.

#### Overview

A discrete user interaction occurs when a person performs a single well-contained interaction and the screen then updates. An example is when someone presses a key on the keyboard and the corresponding letter then appears onscreen. Although the software running on the device needs time to process the incoming user input event and compute the corresponding screen update, it’s usually so quick that a human can’t perceive it and the screen update seems instantaneous.

When the delay in handling a discrete user interaction becomes noticeable, that period of unresponsiveness is known as a . Other common terms for this behavior are  because the app stops updating, and  based on the spinning wait cursor that appears in macOS when an app is unresponsive.

Although discrete interactions are less sensitive to delays than continuous interactions, it doesn’t take long for a person to perceive a gap between an action and its reaction as a pause, which breaks their immersive experience. A delay of less than 100 ms in a discrete user interaction is rarely noticeable, but even a few hundred milliseconds can make people feel that an app is unresponsive.

A hang is almost always the result of long-running work on the main thread. This article explains what causes a hang, why the main thread and the main run loop are essential to understanding hangs, and how various tools can detect hangs on Apple devices.

> **Note**:  This article assumes a basic understanding of the event-handling and rendering loop, as well as a basic understanding of hangs and hitches, and how they differ. If you’re unfamiliar with hangs and hitches, see [`Understanding user interface responsiveness`](understanding-user-interface-responsiveness.md) for more information about them, as well as the event-handling and rendering loop.

##### Understand Work on the Main Thread

Processing incoming events and updating the UI accordingly is the responsibility of an app’s main thread. As part of handling an event, the main thread performs the following work:

1. Delivers the event to the right place and calls the right handler.
2. Makes any state changes, fetches data, updates the UI, and so on.
3. Performs a Core Animation (CA) commit, which submits all the changes of the view hierarchy to the render server. The UI framework usually performs the CA commit automatically when your code finishes handling the event.

![A timeline illustration consisting of a horizontal block between two dashed vertical lines. The dashed vertical line on the left has a callout that says Begin time, the dashed vertical line on the right has a callout that says Commit deadline. The horizontal block in the center contains the title Main Thread Work and three smaller rectangular boxes. It is slightly offset to the left and doesn’t align with either of the two dashed lines directly. The first box inside the Main Thread Work box says Dispatch Event, the second says Your Code, and the third says CA Commit. ](https://docs-assets.developer.apple.com/published/aef125312e584e43c3de0448ce027513/understanding-hangs-in-our-app-1%402x.png)

Your code is involved in each of these stages, but most of it typically deals with the second stage.

Consider the Send button in a messaging app using SwiftUI. Your implementation might look like the following:

```swift
import SwiftUI 

struct MessengerView: View {
    @State var messageText: String

    var body: someView {
        // [...] other UI
        Button("Send", action: {
            messageSender.send(message: messageText)
        })
        // [...] other UI
    }
}
```

When someone taps the Send button, they touch the screen where the button appears. The operating system registers this as a  event. Similar events exist for other input methods, like mouse-down on macOS.

As soon as the finger comes in contact with the screen, the touch-down event is sent. Your app’s main thread then determines which view is responsible for handling the event. It compares the event’s location on the screen to the frames of all the views in the view hierarchy to find the one that’s frontmost at that location. Because the user touched the location of your Send button, the view representing that button receives the touch-down event.

When they lift their finger from the screen, the touchscreen registers the finger leaving the screen, and the OS creates a  event and delivers it to your app. The touch-up event goes to the same view that received the corresponding touch-down event, even if the finger has moved to a different position by then. In response to the touch-up event, if the location of the finger is still inside its bounds when the touch-up event occurs, a `Button` calls its `action` closure.

At this point, the first stage, , or , is complete. The event reaches its destination and the UI framework calls the appropriate event-handling method, which is usually your code, on the selected view. Your design also contributes to how quickly the system delivers events, as you set up the view hierarchy, decide where to place the button, and add any other UI elements, which might include custom views. All of this can have an impact on the speed of event delivery. However, most of the time, this step is fast and not something you need to worry about.

During the second stage, SwiftUI calls your `send(message:)` method as part of calling the Button’s `action` closure, where your app likely starts some asynchronous work to serialize the message string into a data packet, send it to a backend server, and so on. Your app also needs to add the new message to the list of messages in the current conversation, so it can store it, even if sending the message fails. Additionally, your app needs to update the UI to show the user the result of their action. For instance, you might want to display a message bubble onscreen and clear the text field to prepare it for the next message. For more information on responding asynchronously to UI events, see [`Improving app responsiveness`](improving-app-responsiveness.md).

In the third stage, the UI framework takes over again and commits the changes to the UI so the render server can start rendering the new frame. Your code usually isn’t directly involved in the CA commit, but your code does influence how many changes the UI framework needs to commit and how expensive the commit is.

Handling this event isn’t the only thing your app needs the main thread for. Maybe you set a timer to check whether the user is still typing and then update a typing indicator, or your app’s request to the backend server to check for new messages finishes and returns a new message that the app needs to display onscreen.

In each of these situations, your app needs to make updates to the user interface, but doing so isn’t thread-safe, meaning the system can’t modify the UI from multiple threads at the same time. Instead, it needs to serialize and execute the updates to the UI one after the other. For this reason, there’s only one thread that can make UI updates: the main thread. In Swift, using the [`MainActor`](https://developer.apple.com/documentation/Swift/MainActor) ensures that your code executes on the main thread. It also helps the compiler prevent any code outside the main thread from making changes to the user interface.

Because there’s only one thread that can make changes to the UI, you don’t want to block it waiting for someone to press the Send button. So, the system needs need a way to schedule work to execute on the main thread, and then check for that work and execute it whenever it comes in — whether it’s handling an event, processing the result of a network request, or reacting to a timer firing. This scheduling and sequential processing of various work items is the responsibility of the main thread’s [`RunLoop`](https://developer.apple.com/documentation/Foundation/RunLoop).

##### Understand the Main Run Loop

Run loops provide a mechanism for threads to wait on input sources and fire input handlers when any of those sources has data or events to process. Any thread can have a run loop. The main thread starts a run loop, the , as soon as an app finishes launching. This is the run loop that processes all incoming user interaction events.

A very simplified implementation of a run loop might resemble the following:

```swift
class RunLoop {
    var stopped = false
    
    func run() {
        repeat {
            if let work = workSet.fetchNextWorkItem() {
                processWork(work)
            } else {
                sleepUntilNewWorkArrives()
            }
        } while(!stopped)
    }
}
```

After calling `run`, the run loop keeps running in an infinite loop, checking for new work to process. If there’s work to do, the run loop processes it by calling an appropriate handler. If there isn’t any work, it goes to sleep, which means the main thread also sleeps, so it isn’t running. If a new work item comes in, the operating system wakes up the main thread, and its run loop processes the incoming work before going back to sleep.

Any work that the system needs to execute on the main thread, like updating the UI, becomes a work item that it submits to the run loop, and the run loop then processes it as soon as possible. Work items may include:

- Incoming user events
- A callback of a timer scheduled on the run loop (when a timer fires, it submits its callback to run on the run loop.)
- Work on the main [`DispatchQueue`](https://developer.apple.com/documentation/Dispatch/DispatchQueue), the main [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue), or the main actor

Although the run loop performs work items that the system submits to it on the main thread, it isn’t the same as the main dispatch queue. The main dispatch queue, the main `NSOperationQueue`, the main actor, and the main run loop are all ways to submit work to run on the main thread, but for the main thread specifically, the run loop is the foundation of everything.

The main dispatch queue, the main `NSOperationQueue`, and the main actor are clients of the run loop, and the run loop executes work you submit to any of them, but it can also execute work from other sources. As such, a long-running item that you submit to the main dispatch queue becomes a long-running item on the main run loop, and prevents other work from executing. And a long-running item on the main run loop prevents it from executing any work of other run-loop clients, whether it’s the main dispatch queue, a timer, or some other work.

Ideally, the run loop only wakes up briefly to process an incoming event, goes to sleep again, and spends most of the time asleep waiting for new work.

If the run loop is already processing work, it can’t handle a new incoming event until processing of the previous work item is complete. So, it’s important to finish any work on the main thread as quickly as possible so the run loop can go back to sleep and wait for the next incoming event.

In the case of an incoming user input event, the run loop simply processes the event by calling the corresponding UI framework, such as UIKit or AppKit, which handles the event, likely calling some of your code in the process. To handle an event promptly, the run loop needs to be asleep or just finishing a work item when the event comes in.

No matter why your code runs on the main run loop, whether its due to handling an event or any of the other ways described above: If code running on the main runloop takes too long to complete, it prevents the run loop from processing other work, including incoming events, and may cause a hang.

##### Understand Hangs

Although the relevant delay for the user is the time between interacting with the physical device and the physical screen updating, most of the stages in the event-handling and rendering loop take a short amount of time and are fairly consistent in timing.

![A timeline illustration entitled Delay Perceived by User that consists of six horizontal blocks labeled: Input, Event delivery, Wait for main thread availability, Main thread work, Rendering, and Update display. The Main Thread Work and Wait for main thread availability blocks are significantly wider than the others. The Wait for block has a dashed outline. A line beneath the Input and Event delivery blocks says <10 ms. A line beneath Rendering says: 8 ms to 33 ms, and a line beneath Update display says: 8 ms to 16 ms. A line below the six blocks spans the entire width and says: Goal: <100 ms.](https://docs-assets.developer.apple.com/published/78b6e2f0f0a0ba2ff794e9d1edc57b28/understanding-hangs-in-our-app-2%402x.png)

It usually takes just a few milliseconds for the hardware device to recognize user input, send it to the OS, and have the OS forward it to the correct process. Although the output side of rendering the new frame and updating pixels on the display can add a delay of 16 ms to 50 ms, it’s rare that these steps take longer when everything else in your app works well.

Because the other stages have fairly consistent timing, it’s almost always main thread work that takes too long when the system doesn’t meet this threshold. This can be due to the event handling itself taking too long, or due to the main thread being busy with other work and not being available to handle the event. Observing the main runloop’s behavior is a good way to tell whether the main thread is too busy.

A healthy run loop spends most of its time asleep and waiting for events, as in the following example:

![An Instruments screenshot showing a healthy main run loop. All busy periods are very short, and most of the overall run-loop time consists of waiting for events.](https://docs-assets.developer.apple.com/published/012f48b9b3f38a4599bec69430e1bdb9/understanding-hangs-in-our-app-3a.png)

In the screenshot above, the run loop is waiting for events (the gray areas) most of the time, and the periods where it’s busy (the light blue areas) are very short.

For this reason, the hang reporting feature on Apple platforms focuses on the main run loop being unresponsive for an extended period of time as a proxy for hangs that the user experiences. More specifically, hang reporting looks at the duration between two  periods of the run loop, also known as the  portion. During a busy period, the run loop can’t process other incoming events, so if it gets too long, the system reports it as a potential hang.

![An Instruments screenshot showing a main run loop during a hang. The run loop is busy for a period of over 600 ms.](https://docs-assets.developer.apple.com/published/2d823296beb839509b72c42372ea527d/understanding-hangs-in-our-app-3b.png)

Most of Apple’s developer tools start reporting issues when the period of unresponsiveness for the main run loop exceeds 250 ms. Some of them, like the Hangs instrument in the Instruments app, allow you to choose lower thresholds for reporting an unresponsive main run loop.

Hang reporting only measures the time on the main run loop. The time necessary for event delivery, before handing the event to the main run loop, and the time to render the new screen after the main thread finishes updating the UI can add 10 ms to 50 ms to the overall delay that the user experiences, even under normal operation. For more details about what happens after the main thread finishes updating the UI, see [`Understand frame lifetime and hitch duration`](understanding-hitches-in-your-app#Understand-frame-lifetime-and-hitch-duration.md).

## See Also

- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md)
  Make your app more responsive by examining the event-handling and rendering loop.
- [Understanding and improving SwiftUI performance](understanding-and-improving-swiftui-performance.md)
  Identify and address long-running view updates, and reduce the frequency of updates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/understanding-hangs-in-your-app)*