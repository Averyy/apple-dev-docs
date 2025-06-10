# encodeRestorableState(with:)

**Framework**: UIKit  
**Kind**: method

Encodes state-related information for the view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func encodeRestorableState(with coder: NSCoder)
```

#### Discussion

Do not call this method directly. The system calls this method during the state preservation process to give your view controller or view-controller subclass a chance to save state-related information.

When deciding what data to save, write the smallest amount of data needed to restore the view controller to its current configuration. The information you save should be data that you could not easily recreate, such as the user’s current selection. You might also save references to any data objects that the view controller was using, but never write the data objects themselves to the coder. Instead, store enough information so that you can retrieve the data objects from your app’s main data structures again.

> ❗ **Important**:  This method is not a substitute for saving your app’s data structures persistently to disk. You should continue to save your app’s actual data to iCloud or the local file system using existing techniques. This method is intended only for saving configuration state or other information related to your app’s user interface. You should consider any data you write to the coder as purgeable and be prepared for it to be unavailable during subsequent launches.

It is strongly recommended that you call `super` at some point during your implementation to give parent classes an opportunity to save information. A [`UIViewController`](uiviewcontroller.md) object saves a reference to the presented view controller and to the storyboard (if any) that was used to create the view controller. The view controller also asks the views in its view hierarchy to save any relevant information. However, a view controller does not automatically save references to contained child view controllers. If you are implementing a custom container view controller, you must encode the child view controller objects yourself if you want them to be preserved.

Your implementation of this method can encode other restorable objects views, view controllers, and objects that adopt the [`UIStateRestoring`](uistaterestoring.md) protocol, using the [`encode(_:forKey:)`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver/encode(_:forKey:)-9f4n9) method of the provided coder object. Encoding a restorable object writes that object’s restoration identifier to the coder. That identifier is then used during the decode process to locate the new version of the object. If the view or view controller defines its own version of this method, that method is also called at some point so that the object can encode its own state.

For objects that are not restorable, encoding the object writes its data (and not a restoration identifier) to the archive. Such objects must adopt the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol. During decoding, the system creates a new object that is initialized with the data from the archive.

## Parameters

- `coder`: The coder object to use to encode the state of the view controller.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [var restorationIdentifier: String?](uiviewcontroller/restorationidentifier.md)
  The identifier that determines whether the view controller supports state restoration.
- [var restorationClass: (any UIViewControllerRestoration.Type)?](uiviewcontroller/restorationclass.md)
  The class responsible for recreating this view controller when restoring the app’s state.
- [func decodeRestorableState(with: NSCoder)](uiviewcontroller/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view controller.
- [func applicationFinishedRestoringState()](uiviewcontroller/applicationfinishedrestoringstate.md)
  Called on restored view controllers after other object decoding is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/encoderestorablestate(with:))*