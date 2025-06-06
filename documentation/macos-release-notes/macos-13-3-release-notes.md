# macOS Ventura 13.3 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 13.3 SDK provides support to develop apps for Mac computers running Ventura 13.3. The SDK comes bundled with Xcode 14.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 14.3, see [`Xcode 14.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_3-release-notes).

##### Accelerate

###### New Features

- The BLAS and LAPACK libraries under the Accelerate framework are now inline with reference version 3.9.1. These new interfaces provide additional functionality and a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings. (105572917)

##### Accessory Security

###### New Features

- On Apple silicon portables, SD or SD extended capacity cards require user approval before the card can communicate with macOS. (102838867)

##### Core Ml

###### Deprecations

- Core ML Model Deployment is being deprecated. Consider using Background Assets or `NSURLSession` instead. (102993813)

##### Icloud Settings

###### Known Issues

- You might be unable to enter the upgrade page for iCloud+ from iCloud Settings. (104629261)  Click “Upgrade to iCloud+” from [`https://www.apple.com/icloud/`](https://developer.apple.comhttps://www.apple.com/icloud/) to trigger the upgrade page.
- Some apps which previously displayed sync toggles in iCloud Drive Settings aren’t currently displayed. (105239897)

##### Installation

###### Known Issues

- macOS Ventura 13.3 beta installer fails when upgrading from versions prior to macOS Big Sur. (106102320)  Upgrade to macOS Ventura 13.2.1 before upgrading to macOS Ventura 13.3.

##### Metal

###### Resolved Issues

- Fixed: [`MTLAccelerationStructureCommandEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder?language=objc) now supports `nil` for a refit scratch buffer if the required size of the buffer is zero bytes. (103192673)

##### Pages Numbers and Keynote

###### Known Issues

- When Advanced Data Protection for iCloud is turned on, Pages, Numbers, and Keynote might unexpectedly require collaborative documents to be closed. (103463223)  Close the affected document, spreadsheet, or presentation and reopen it after a few minutes.

##### Safari Web Extensions

###### New Features

- Added support for `modifyHeaders` action type for `declarativeNetRequest` rules. (71867709)
- Added support for `browser.storage.session` to store up to 10MB of data in-memory. (79283961)
- Added support for persistent content scripts via `browser.scripting.registerContentScript`, `browser.scripting.getRegisteredContentScripts`, `browser.scripting.unregisterContentScripts`, and `scripting.updateContentScripts`. (91261369)

###### Resolved Issues

- Fixed `browser.webNavigation` events firing for hosts where the extension didn’t have access. Extensions should request host permissions for sites to receive events. (100204850)

##### Storekit

###### Resolved Issues

- Fixed an issue causing iOS apps on Mac to fail while purchasing or restoring in-app content. (102123618)

##### Swiftui

###### Resolved Issues

- Fixed a regression where the `truncationMode` view modifier didn’t truncate `TextField` on macOS. (53647517)
- Fixed: Dragging an `Image` using `draggable` modifier no longer causes an app to freeze. (99157719)
- Fixed: An App defined with a `Window` scene will no longer cause the window tabbing menu items to be displayed, nor will it participate in any window tabbing behavior. (100982500)
- Fixed: Presentations in SwiftUI using the ‘sheet’ or ‘fullScreenCover’ modifier can now be dynamically presented again while a dismiss animation is in progress. Previously, attempting to present again in this case would do nothing. Note: A data race in app code that was previously ignored might cause a sheet to be presented again with this change. If this happens, check that your state isn’t triggering a new presentation. (101487810)
- Fixed an issue on macOS where columns in `Table` might not be able to be resized. (101936572)
- Fixed: When used as an auxiliary scene in a SwiftUI App, the `Window` scene will now behave as an auxiliary window with respect to Stage Manager and full screen mode. (102106455)
- Fixed: `List` in `.sidebar` style now supports swipe actions. (103910772)
- Fixed: `List` with `DisclosureGroup` now supports expand/collapse animations when `isExpanded` is set within a `withAnimation` block. (104923100)
- Fixed: `Table` on macOS will now properly respond to `scrollTo` requests with dynamcially added rows as target IDs. (105579236)

##### Swiftui Navigation

###### Resolved Issues

- Fixed: `.navigationSplitViewColumn` and `.layoutPriority` now control the widths of columns of a `NavigationSplitView` on macOS. Use the existing `.windowResizability(.contentSize)` scene modifier if needed to control the window’s size based off a root `NavigationSplitView`. ```None
struct MeasuredNavigationSplit: View {
   var body: some View {
      NavigationSplitView {
          Color.cyan
              .navigationSplitViewColumnWidth(min: 90, ideal: 100, max: 300)
              .layoutPriority(2)
       } content: {
          Color.pink
              .navigationSplitViewColumnWidth(ideal: 300, max: 400)
              .layoutPriority(3)
       } detail: {
          Color.yellow
              .navigationSplitViewColumnWidth(min: 200, ideal: 300)
              .layoutPriority(2)
       }
   }
}
``` (58333786)
- Fixed: Navigation destinations nested within `NavigationStack` and `NavigationSplitView` are detected more performantly and reliably, no longer logging update cycles. (97597634)
- Fixed: Navigation destinations that present a new view on top of a `NavigationSplitViewColumn` (rather than pushing a view onto a stack in that column) no longer cause an assertion failure on iOS or infinite loop on macOS when the destination view is itself a `NavigationStack`. For example, the below construction is functional ```swift
NavigationSplitView { 
    SidebarView()
    .navigationDestination(isPresented: $present) {
        NavigationStack { ... }
    }
} detail: { ... }
``` (103278180)
- Fixed: Navigation destinations with data dependencies captured from ancestor views update more reliably. ```swift
struct DataDependentNavigation: View {
  @State var changeColor: Bool = false
  @State var present: Bool = false

  var body: some View {
  NavigationSplitView {
    Color.blue
      .navigationDestination(isPresented: $present) {
           // This is a data dependency from an ancestor view
            changeColor ? Color.green : Color.yellow
      }
  } detail: {
    Color.teal
  }
}
``` (103429535)

##### Task Manager

###### Resolved Issues

- Fixed an issue introduced in macOS Ventura 13.1 that caused the system to post excessive “Background Items Added” notifications after toggling items in System Settings > General > Login Items. Toggling items in macOS Ventura 13.2 doesn’t cause excessive notifications, but that release doesn’t automatically correct the issue inherited from macOS Ventura 13.1. (102352141)

##### Virtualization

###### Resolved Issues

- Fixed: Installing macOS Ventura 13.3 beta on a virtual machine running on a Apple silicon Mac might result in a hang during setup. (105504504)

## See Also

- [macOS Ventura 13.5 Release Notes](macos-13_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.4 Release Notes](macos-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.2 Release Notes](macos-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.1 Release Notes](macos-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13 Release Notes](macos-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-13_3-release-notes)*