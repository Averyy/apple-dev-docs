# Making changes to reduce memory use

**Framework**: Xcode

Decrease your app’s use of memory by addressing common causes of excessive use.

#### Overview

Once you’ve localized the growth in your app’s memory use to a specific feature or action, you can make changes to reduce memory use. Common causes of excessive memory use and the actions you can take to reduce their impact are described below.

##### Optimize Image Assets

Large images, especially at high color depths, use a lot of memory. Optimize assets bundled with the app for the size at which the app displays them. Transform images loaded from other sources—for example, from network services or the user’s photo library—to an appropriate scale and color depth. Use [`Image I/O`](https://developer.apple.com/documentation/ImageIO) for these transforms to minimize memory impact. WWDC 2018 Session 416, [`iOS Memory Deep Dive`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/416), gives advice on choosing appropriate Image I/O transforms.

##### Reduce the Size of Core Data Transactions

[`Core Data`](https://developer.apple.com/documentation/CoreData) stores changes to [`NSManagedObject`](https://developer.apple.com/documentation/CoreData/NSManagedObject) instances in memory until their associated [`NSManagedObjectContext`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext) is saved, at which time it writes changes to the parent `NSManagedObjectContext` or to the persistent store. Until the changes make their way into the persistent store, they’re resident in memory, so the longer your app goes between saves, the bigger Core Data’s working set can grow. Conversely, the more frequently your app saves, the more writes it makes to the device’s solid-state drive, which impacts performance and increases wear on the drive. Design your app’s persistence model to strike a balance between these two resource constraints.

##### Discard Unused View Objects

The user isn’t looking at your app’s views when they lock the screen or when the app is in the background. There’s no need to keep images, video, SceneKit scenes, and other view-related objects in memory during those times. Release view-related content when your app enters the background, and prepare views again when it re-enters the foreground. For information about preparing your app for background use, see [`Managing your app’s life cycle`](https://developer.apple.com/documentation/UIKit/managing-your-app-s-life-cycle).

##### Eliminate Memory Leaks

A memory leak occurs when allocated memory becomes unreachable and the app can’t deallocate it. Allowing an allocated-memory pointer to go out of scope without freeing the memory can cause a memory leak. A retain cycle in your app’s object graph can also cause a memory leak. When the app removes its reference to any of the objects in a retain cycle, strong references remain within the cycle, and the objects aren’t released.

Use the [`Leaks profiling template`](https://developer.apple.comhttps://help.apple.com/instruments/mac/10.0/#/dev022f987b) to detect memory leaks. Instruments periodically scans the memory your app is using to report allocated but unreachable regions of memory. The Leaks instrument shows the address and size of the leaked memory, along with a stack trace showing the code responsible for allocating the memory.

##### Remove References to Unused Objects

It’s possible for an app to accumulate memory that it has allocated and has access to but doesn’t use. This unused memory increases the app’s memory use without contributing to its functionality, and without showing up in leak-detection tools like the Leaks instrument.

For example, a social media app might load a list of messages from a service and store them in a dictionary by message identifier. As the user scrolls through their timeline, the app loads more messages into the dictionary so that it can quickly display more information when the user taps a message. Without a strategy to purge earlier messages from this dictionary, it can grow without bounds as the user scrolls further along the list.

Make sure your app only keeps references to objects it needs to support the features that the user is currently working with. Discard old content, or write it to disk for later retrieval. For example, the social media app can discard messages from its dictionary when the user scrolls away from those messages.

## See Also

- [Gathering information about memory use](gathering-information-about-memory-use.md)
  Identify memory-use inefficiencies by measuring and profiling your app.
- [Preventing memory-use regressions](preventing-memory-use-regressions.md)
  Measure the memory that your app’s features use, and detect increases by using XCTest performance tests.
- [Responding to low-memory warnings](responding-to-low-memory-warnings.md)
  Detect when your app is using excessive memory, and bring memory use under control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/making-changes-to-reduce-memory-use)*