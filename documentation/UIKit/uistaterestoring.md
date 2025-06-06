# UIStateRestoring

**Framework**: UIKit  
**Kind**: protocol

Methods for adding objects to your state restoration archives.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIStateRestoring : NSObjectProtocol
```

## Mentions

- [About the UI preservation process](about-the-ui-preservation-process.md)

#### Overview

You can add state restoring objects to an archive directly or by referencing them from another object that’s preserved, such as a view controller. The methods of the protocol let you save enough information about the object to find or recreate it during the next launch cycle.

When adopting this protocol in your custom objects, you must also remember to register those objects using the [`registerObject(forStateRestoration:restorationIdentifier:)`](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md) method of the [`UIApplication`](uiapplication.md) class. You don’t need to register views or view controllers explicitly because UIKit registers those objects automatically. View controllers adopt this protocol so that they may be used as the restoration parent of one of your custom objects.

## Topics

### Accessing the object information
- [var restorationParent: (any UIStateRestoring)?](uistaterestoring/restorationparent.md)
  The parent object used to scope the current object.
- [var objectRestorationClass: (any UIObjectRestoration.Type)?](uistaterestoring/objectrestorationclass.md)
  The class responsible for creating this object when restoring the app’s state.
### Encoding and decoding the object
- [func encodeRestorableState(with: NSCoder)](uistaterestoring/encoderestorablestate(with:).md)
  Encodes state-related information for the object.
- [func decodeRestorableState(with: NSCoder)](uistaterestoring/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the object.
- [func applicationFinishedRestoringState()](uistaterestoring/applicationfinishedrestoringstate.md)
  Called after all objects have had a chance to decode their state.
### Constants
- [State restoration keys](state-restoration-keys.md)
  Keys that are available in restoration archives.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActivityViewController](uiactivityviewcontroller.md)
- [UIAlertController](uialertcontroller.md)
- [UICloudSharingController](uicloudsharingcontroller.md)
- [UICollectionViewController](uicollectionviewcontroller.md)
- [UIColorPickerViewController](uicolorpickerviewcontroller.md)
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](uidocumentviewcontroller.md)
- [UIFontPickerViewController](uifontpickerviewcontroller.md)
- [UIImagePickerController](uiimagepickercontroller.md)
- [UIInputViewController](uiinputviewcontroller.md)
- [UINavigationController](uinavigationcontroller.md)
- [UIPageViewController](uipageviewcontroller.md)
- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)
- [UISearchContainerViewController](uisearchcontainerviewcontroller.md)
- [UISearchController](uisearchcontroller.md)
- [UISplitViewController](uisplitviewcontroller.md)
- [UITabBarController](uitabbarcontroller.md)
- [UITableViewController](uitableviewcontroller.md)
- [UITextFormattingViewController](uitextformattingviewcontroller.md)
- [UIVideoEditorController](uivideoeditorcontroller.md)
- [UIViewController](uiviewcontroller.md)

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [Restoring Your App’s State with SwiftUI](../swiftui/restoring_your_app_s_state_with_swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.
- [protocol UIViewControllerRestoration](uiviewcontrollerrestoration.md)
  The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.
- [protocol UIObjectRestoration](uiobjectrestoration.md)
  The interface that restoration classes use to restore preserved objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring)*