# macOS Big Sur 11.0.1 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 11 SDK provides support to develop apps for Macs running macOS Big Sur 11. The SDK comes bundled with Xcode 12.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 12.2, see [`Xcode 12.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12_2-release-notes).

##### General

###### Known Issues

> ❗ **Important**: Updating to macOS Big Sur 11.0.1 from previous versions of macOS might take significantly longer than expected. Data loss could occur if the update is interrupted. (59101197)

Updating to macOS Big Sur 11.0.1 from previous versions of macOS might take significantly longer than expected. Data loss could occur if the update is interrupted. (59101197)

##### Accessibility

###### Known Issues

- You might be unable to pair certain braille displays using Bluetooth. (69794099)  Connect these devices using USB instead.

##### Appkit

- See [`AppKit Release Notes for macOS Big Sur 11`](appkit-release-notes-for-macos-11.md).

##### App Store

###### New Features

- [`SKStoreProductViewController`](https://developer.apple.com/documentation/StoreKit/SKStoreProductViewController) and [`SKProductStorePromotionController`](https://developer.apple.com/documentation/StoreKit/SKProductStorePromotionController) APIs are now available for both macOS and Mac Catalyst apps. (56300909)

##### Core Ml

###### Deprecations

- The default initializer on the auto-generated model interface has been deprecated in favor of `init(configuration:)`. Please use `init(configuration:)` or the newly introduced `.load()` method and handle model load errors as appropriate. (64432588)

##### Installer and Software Update

###### Known Issues

- When updating from macOS Big Sur 11 beta 2 to macOS Big Sur 11 beta 3 or later, you might be offered an unexpectedly large download rather than an incremental software update. (65753086)  Under the “Another update is available” text, click the “More info…” link. This reveals the incremental update where you can click the Install Now button.
- You might need to adjust Energy Saver settings so your Mac doesn’t go to sleep while preparing to install macOS Big Sur 11.0.1. (63166401)
- If macOS Big Sur 11.0.1 is installed into the same APFS container as previous versions of macOS Catalina 10.15, system software updates can no longer be installed on the previous versions of macOS. (64411484)  Update the previous version of macOS Catalina to 10.15.6 or later.

##### Kernel

###### Known Issues

- Installing a new kernel extension requires signing in as an Admin user. You must also restart your Mac to load the extension. Kernel extensions using certain deprecated KPIs won’t be loaded. For more information, see [`Deprecated Kernel Extensions and System Extension Alternatives`](https://developer.apple.comhttps://developer.apple.com/support/kernel-extensions/). (55068348)  During development, you can temporarily disable System Integrity Protection to allow these deprecated kernel extensions to load.
- New in macOS Big Sur 11.0.1, the system ships with a built-in dynamic linker cache of all system-provided libraries. As part of this change, copies of dynamic libraries are no longer present on the filesystem. Code that attempts to check for dynamic library presence by looking for a file at a path or enumerating a directory will fail. Instead, check for library presence by attempting to `dlopen()` the path, which will correctly check for the library in the cache. (62986286)
- Use only absolute paths with the `--volume-root` option of `kmutil`, and don’t use a trailing `/`. (63773848)
- Symbols exported by both xnu and Apple kernel extensions will change. Recompile your kernel extension with each update to macOS Big Sur 11.0.1 to ensure compatibility. (64262563)

###### New Features

- The `kern.argmax` limit has been increased, allowing programs to receive longer argument lists. (48661669)
- Darwin `kevent` now allows non-parent processes to register for `NOTE_EXITSTATUS`, which delivers the same values as the `wait()` family of functions in the event data. Refer to the `wait4()` man page for more information. This event is subject to the following security checks: - The requesting process is allowed to send signals by sandbox restrictions.
- The requesting process and the target process are running as the same user or the requesting process has root privileges. (58134463)

###### Deprecations

- Kernel extensions using certain deprecated KPIs no longer load. Refer to the [`support page`](https://developer.apple.comhttps://developer.apple.com/support/kernel-extensions). While macOS Big Sur remains in development, you can temporarily disable System Integrity Protection to allow these deprecated extensions to load. (55068348)

##### Key Value Observing

###### New Features

- Key-Value Observation removal facilities now employ deterministic bookkeeping methods. Cases that would have produced hard-to-diagnose crashes, especially those where KVO signals problems accessing deallocated observer pointers or observers associated with incorrect objects, now produce an exception pinpointing which observed object needs a missed [`removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1413994-removeobserver) call, and by which observers. This exception was previously thrown as ‘best effort’ when KVO could detect the problem; the new deterministic bookkeeping allows it to be thrown for all cases where `removeObserver(_:)` is needed. The improved determinism also allows improved Swift API handling. Instances of [`NSKeyValueObservation`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservation), produced by the Swift `NSObject.observe(_:changeHandler:)` method, take advantage of integration with this bookkeeping so they now invalidate automatically when the observed object is released,  regardless of how the object implements its KVO behavior. This applies to all usage of this API in macOS 11 Big Sur beta, including on processes built with previous versions of the SDK, and eliminates certain classes of crashes that sometimes required using the legacy API instead. (65051563)

##### Logging

###### New Features

- New APIs are available for using `os_log` from Swift as part of the [`os`](https://developer.apple.com/documentation/os) framework: - A new type [`Logger`](https://developer.apple.com/documentation/os/Logger) can be instantiated using a subsystem and category and provides methods for logging at different levels ([`debug(_:)`](https://developer.apple.com/documentation/os/Logger/debug(_:)), [`error(_:)`](https://developer.apple.com/documentation/os/Logger/error(_:)), [`fault(_:)`](https://developer.apple.com/documentation/os/Logger/fault(_:))).
- The `Logger` APIs support specifying most formatting and privacy options supported by legacy `os_log` APIs.
- The new APIs provide significant performance improvements over the legacy APIs.
- You can now pass Swift string interpolation to the `os_log` function.  The new APIs can’t be back deployed; however, the existing `os_log` API remains available for back deployment. (22539144)

##### Mac Catalyst

###### Known Issues

- `WebGL` content in [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) might experience reduced performance. (70587571)
- A [`ToolbarItem`](https://developer.apple.com/documentation/SwiftUI/ToolbarItem) with automatic placement isn’t placed in the window toolbar. (63690384)
- Select [`UIKit`](https://developer.apple.com/documentation/UIKit) controls, control customizations, and methods throw exceptions when used in the Mac idiom. Unsupported controls and behaviors on macOS Big Sur 11 throw exceptions as follows: - [`UIButton`](https://developer.apple.com/documentation/UIKit/UIButton). [`addGestureRecognizer(_:)`](https://developer.apple.com/documentation/UIKit/UIView/addGestureRecognizer(_:)) throws an exception if the button uses the macOS appearance. [`setTitle(_:for:)`](https://developer.apple.com/documentation/UIKit/UIButton/setTitle(_:for:)) and [`setImage(_:for:)`](https://developer.apple.com/documentation/UIKit/UIButton/setImage(_:for:)) throws an exception for any state except `UIControlStateNormal`.
- [`UISlider`](https://developer.apple.com/documentation/UIKit/UISlider). [`setThumbImage(_:for:)`](https://developer.apple.com/documentation/UIKit/UISlider/setThumbImage(_:for:)), [`thumbTintColor`](https://developer.apple.com/documentation/UIKit/UISlider/thumbTintColor), [`setMinimumTrackImage(_:for:)`](https://developer.apple.com/documentation/UIKit/UISlider/setMinimumTrackImage(_:for:)), [`minimumTrackTintColor`](https://developer.apple.com/documentation/UIKit/UISlider/minimumTrackTintColor), [`setMaximumTrackImage(_:for:)`](https://developer.apple.com/documentation/UIKit/UISlider/setMaximumTrackImage(_:for:)), [`maximumTrackTintColor`](https://developer.apple.com/documentation/UIKit/UISlider/maximumTrackTintColor), [`minimumValueImage`](https://developer.apple.com/documentation/UIKit/UISlider/minimumValueImage), and [`maximumValueImage`](https://developer.apple.com/documentation/UIKit/UISlider/maximumValueImage) all throw an exception.
- [`UISwitch`](https://developer.apple.com/documentation/UIKit/UISwitch) throws an exception when `title` is set in a non-Mac idiom view.
- [`UIStepper`](https://developer.apple.com/documentation/UIKit/UIStepper) throws an exception when this control is added to a Mac idiom view.
- [`UIRefreshControl`](https://developer.apple.com/documentation/UIKit/UIRefreshControl) throws an exception when this control is added to a Mac idiom view.
- [`UIPickerView`](https://developer.apple.com/documentation/UIKit/UIPickerView) throws an exception when this control is added to a Mac idiom view. Use conditional code that respects the targeted platforms to avoid these exceptions. For example, an iOS app with an Optimized for Mac version available on macOS Big Sur 11, and an iPad idiom version available on macOS Catalina could style a `UISlider` as follows: ```swift
func style(_ slider: UISlider) {
    if slider.traitCollection.userInterfaceIdiom != .mac {
        slider.setThumbImage(customThumb, for: .normal)
        slider.setThumbImage(customThumb, for: .disabled)
        slider.maximumTrackTintColor = .clear
    }
}
``` A Mac Catalyst app targeting solely iOS and Optimized for Mac versions could conditionally compile the code as follows: ```swift
func style(_ slider: UISlider) {
    #if !targetEnvironment(macCatalyst)
        if slider.traitCollection.userInterfaceIdiom != .mac {
            slider.setThumbImage(customThumb, for: .normal)
            slider.setThumbImage(customThumb, for: .disabled)
            slider.maximumTrackTintColor = .clear
        }
    #endif
}
``` This helps ensure that your app won’t see unexpected configurations or appearances, if these behaviors change. Use caution when reading the [`userInterfaceIdiom`](https://developer.apple.com/documentation/UIKit/UIDevice/userInterfaceIdiom) from a [`UIDevice`](https://developer.apple.com/documentation/UIKit/UIDevice) or [`UIScreen`](https://developer.apple.com/documentation/UIKit/UIScreen) to guard Mac idiom behaviors in case your app targets CarPlay or uses AirPlay to stream to another screen.
- The button configuration for the [`preferredAction`](https://developer.apple.com/documentation/UIKit/UIAlertController/preferredAction) is the default button with the key equivalent of return.
- The button configuration for the action with [`UIAlertAction.Style.cancel`](https://developer.apple.com/documentation/UIKit/UIAlertAction/Style-swift.enum/cancel) has the key equivalent of escape.
- Button configurations for actions with [`UIAlertAction.Style.destructive`](https://developer.apple.com/documentation/UIKit/UIAlertAction/Style-swift.enum/destructive) will be configured with [`hasDestructiveAction`](https://developer.apple.com/documentation/AppKit/NSButton/hasDestructiveAction).
- If you apply both `preferredAction` and `UIAlertActionStyleCancel` to the same action, `preferredAction` takes precedence. It’s not possible to have a default button with the escape key equivalent.
- The system adds an Open Recent menu automatically to applications that support opening files. The menu identifier is [`openRecent`](https://developer.apple.com/documentation/UIKit/UIMenu/Identifier-swift.struct/openRecent).
- [`UIScene.ActivationRequestOptions`](https://developer.apple.com/documentation/UIKit/UIScene/ActivationRequestOptions) has a new [`collectionJoinBehavior`](https://developer.apple.com/documentation/UIKit/UIScene/ActivationRequestOptions/collectionJoinBehavior) property. A scene collection is a group of scenes that display together. In Catalyst, this is used to add windows to an [`NSWindowTabGroup`](https://developer.apple.com/documentation/AppKit/NSWindowTabGroup). - The default placement is [`UISceneCollectionJoinBehavior.automatic`](https://developer.apple.com/documentation/UIKit/UISceneCollectionJoinBehavior/automatic) and the new scene will follow system preferences for joining collections.
- Set the placement value to [`UISceneCollectionJoinBehavior.preferred`](https://developer.apple.com/documentation/UIKit/UISceneCollectionJoinBehavior/preferred) to have the new scene attempt to join the collection that contains the [`requestingScene`](https://developer.apple.com/documentation/UIKit/UIScene/ActivationRequestOptions/requestingScene), or any compatible collection if `requestingScene` is not set.
- Set the value to [`UISceneCollectionJoinBehavior.disallowed`](https://developer.apple.com/documentation/UIKit/UISceneCollectionJoinBehavior/disallowed) to create a new collection for the scene, ignoring system preferences.
- Set the value to [`UISceneCollectionJoinBehavior.preferredWithoutActivating`](https://developer.apple.com/documentation/UIKit/UISceneCollectionJoinBehavior/preferredWithoutActivating) to add the new scene without deactivating the `requestingScene`. Otherwise this propery behaves the same as `preferred`.
- [`UISwitch`](https://developer.apple.com/documentation/UIKit/UISwitch) has a new [`preferredStyle`](https://developer.apple.com/documentation/UIKit/UISwitch/preferredStyle) property that can alter the appearance of the switch in Catalyst apps running in the Mac idiom, see [`Optimize the Interface of your Mac Catalyst App — WWDC20`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10056/) for more information.
- Set the `preferredstyle` value to [`UISwitch.Style.sliding`](https://developer.apple.com/documentation/UIKit/UISwitch/Style-swift.enum/sliding) to give the traditional iOS switch appearance; it will look like a native switch in Optimized Catalyst apps.
- Set the `preferredstyle` value to [`UISwitch.Style.checkbox`](https://developer.apple.com/documentation/UIKit/UISwitch/Style-swift.enum/checkbox) to give a traditional macOS checkbox in optimized Catalyst apps. When set to the `checkbox` style, the system displays the new [`title`](https://developer.apple.com/documentation/UIKit/UISwitch/title) property in a label within the clickable bounds of the checkbox. The `title` property is inert with the `sliding` style.
- The `UISwitch` `preferredstyle` property defaults to `automatic` and renders as a sliding switch in all idioms except the Mac idiom — the only idiom where the checkbox is available.
- A notable consequence of this default style of the sliding switch is that if you’re using the `checkbox` style `UISwitch`, you may need to call [`sizeToFit()`](https://developer.apple.com/documentation/AppKit/NSControl/sizeToFit()) or provide a `frame` through other means where the intrinsic size alone was sufficient.
- The default context menu presented from a [`UITextView`](https://developer.apple.com/documentation/UIKit/UITextView) or [`UITextField`](https://developer.apple.com/documentation/UIKit/UITextField) has missing items related to spelling and formatting.
- The text you use in a `UITextView` or `UITextField` to look up definitions may be out of sync with the visual selection.
- [`UITitlebar`](https://developer.apple.com/documentation/UIKit/UITitlebar) has a new [`UITitlebarSeparatorStyle`](https://developer.apple.com/documentation/UIKit/UITitlebarSeparatorStyle) property that gives control over the appearance of the hairline bar in between a macOS window’s titlebar and its content. This property is especially useful when designing interfaces in the style of the new macOS Big Sur full-height sidebar.

###### New Features

- Optimized for Mac is a new option for Catalyst apps. When optimized for Mac, Catalyst apps use Mac controls, appearances, spacing, and true font metrics, and content is no longer scaled by 77 percent. A new constant, [`UIUserInterfaceIdiom.mac`](https://developer.apple.com/documentation/UIKit/UIUserInterfaceIdiom/mac), has been introduced to support the new idiom. For more information on the new idiom and optimizing your Mac Catalyst app, see [`Choosing a user interface idiom for your Mac app`](https://developer.apple.com/documentation/UIKit/choosing-a-user-interface-idiom-for-your-mac-app), and [`Optimize the Interface of your Mac Catalyst App — WWDC20`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10056/).
- When you deliver your iPad app on the Mac via Catalyst, your existing users on iOS no longer need to purchase your app a second time. In addition, you can manage the capabilities and App Store metadata of your app in one place.
- Application preferences that include no items users can set are instead shown in the About box.

##### Networking

###### New Features

- Experimental HTTP/3 support can be enabled in Safari via Experimental Features in the Developer menu, and enabled system-wide using the Terminal command `defaults write -g CFNetworkHTTP3Override -int 3`. (62969220)

##### Realitykit

###### New Features

- The new `DebugModelComponent` struct has been renamed to [`ModelDebugOptionsComponent`](https://developer.apple.com/documentation/RealityKit/ModelDebugOptionsComponent), and its `shaderDebugMode` property has been renamed to [`visualizationMode`](https://developer.apple.com/documentation/RealityKit/ModelDebugOptionsComponent/visualizationMode-swift.property). (64275817)

##### Safari and Webkit

###### New Features

- Support for 4K HDR playback of YouTube videos. (64824895)
- Support for Web Extensions is now available. Existing Chrome and Firefox extensions can be converted for Safari using `xcrun safari-web-extension-converter` and distributed through the App Store for use in Safari 14. (55707949)
- Webpage Translation is now available in the U.S. and Canada. Supported languages include English, Spanish, Simplified Chinese, French, German, Russian, and Brazilian Portuguese. Safari will automatically detect if translation is available based on your Preferred Languages list. (64437861)

##### Security

###### New Features

- macOS Big Sur 11 beta improves system security by requiring an administrator password when a certificate trust settings change is made in the admin trust domain. Running as the root user alone is no longer sufficient to modify certificate trust. User trust domain settings continue to require confirmation by entering the password for the user’s account. This change may affect you if one of the following is true: - You have written scripts which call `/usr/bin/security add-trusted-cert -d ...` as root.
- Your process runs as root and calls the SecTrustSettingsSetTrustSettings function to trust a certificate.
- Workflows that add trust settings in the admin trust domain, such as for an enterprise root certificate, may require modification if the user can’t authenticate as an administrator at the time settings are changed. (21855995)  Use Apple Configurator 2 to create and install a configuration profile containing your root certificate.

##### Swiftui

###### Known Issues

- [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) generic type signature has changed, adding the [`currentValueLabel`](https://developer.apple.com/documentation/SwiftUI/GaugeStyleConfiguration/currentValueLabel-swift.property) generic parameter. This change doesn’t require any source changes, but it causes apps compiled using an earlier beta SDK to quit unexpectedly. (63580200)  Re-compile apps for macOS Big Sur 11 Beta 6 or later to resolve this issue.

###### New Features

- A [`ToolbarItem`](https://developer.apple.com/documentation/SwiftUI/ToolbarItem) attached to the content of a sheet will now display [`confirmationAction`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/confirmationAction), [`cancellationAction`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/cancellationAction), [`destructiveAction`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/destructiveAction) and [`automatic`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/automatic) placements below the the content of the sheet. (61180502)
- A [`ToolbarItem`](https://developer.apple.com/documentation/SwiftUI/ToolbarItem)  [`Label`](https://developer.apple.com/documentation/SwiftUI/Label) is now automatically used when the window’s toolbar is set to Icon and Text or Text Only. (67823018)
- Adding a [`Spacer`](https://developer.apple.com/documentation/SwiftUI/Spacer) to a [`toolbar`](https://developer.apple.com/documentation/SwiftUI/CommandGroupPlacement/toolbar) now creates flexible spaces. (64189289)
- A [`ToolbarItem`](https://developer.apple.com/documentation/SwiftUI/ToolbarItem) now automatically creates an overflow menu item. (60104785)
- Use the new `.fileImporter()` modifier to present a system interface for importing one or more files into your app, and the new `.fileMover()` modifier to move one or more existing files to a new location. The following is an example of a simple UI for importing and moving files: ```swift
struct FileMover : View {
    @Binding var selectedFiles: [URL]
    var includeDirectories: Bool = false
    
    @State private var isImporting: Bool = false
    @State private var isMovingSelection: Bool = false

    var body: some View {
        List(selectedFiles, id: \.self) { url in
            Text(url.absoluteString)
        }
        .toolbar {
            Button("Import", action: { isImporting = true })
            Button("Move", action: { isMovingSelection = true })
        }
        .fileImporter(
            isPresented: $isImporting,
            allowedContentTypes: includeDirectories ? [.item, .directory] : [.item],
            allowsMultipleSelection: true
        ) { result in
            do {
                selectedFiles = try result.get()
            } catch {
                // Handle failure.
            }
        }
        .fileMover(isPresented: $isMovingSelection, files: selectedFiles) {
            if case .success = $0 {
                selectedFiles = []
            } else {
                // Handle failure.
            }
        }
    }
}
```
- Use the new `.fileExporter()` modifier to present a system interface for exporting one or more documents from your app. In this example, an app provides a simple note-taking interface for quickly jotting down some text and then exporting it to disk: ```swift
struct QuickNote : View {
    @Binding var draft: QuickNoteDocument
    @State private var isExporting: Bool = false

    var body: some View {
        TextEditor(text: $draft.text)
            .toolbar {
                Button("Save", action: { isExporting = true })
            }
            .fileExporter(
                isPresented: $isExporting,
                document: draft,
                contentType: .plainText,
                defaultFilename: "MyNote"
            ) { result in
                // Clear the draft now that it's saved.
                if case .success = result {
                    draft.text = ""
                } else {
                    // Handle failure.
                }
            }
    }
}

struct QuickNoteDocument : FileDocument {
    static var readableContentTypes: [UTType] { [.plainText] }

    var text: String

    init(text: String) {
        self.text = text
    }

    init(configuration: ReadConfiguration) throws {
        // Deserialize the document.
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        // Serialize the document.
    }
}
```
- Use the new `.fileMover()` modifier to present a system interface for moving one or more existing files to a new location. (66182201)
- The `ImportFilesAction` and `ExportFilesAction` APIs have been replaced with a collection of new view modifiers.
- [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) can be converted to and from [`CGColor`](https://developer.apple.com/documentation/uikit/uicolor/1621943-cgcolor). The [`ColorPicker`](https://developer.apple.com/documentation/SwiftUI/ColorPicker) can also now be configured with a binding to a `CGColor`. (56939085)
- Introduced [`ToolbarItemGroup`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemGroup) as a convenient way to place multiple items in a specific location of non-customizable toolbars. (64178863)
- [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) now supports adding a secondary “current value label” that describes the current progress level of the task. Use the [`label`](https://developer.apple.com/documentation/SwiftUI/ProgressViewStyleConfiguration/label-swift.property) to describe the overall task, and the [`currentValueLabel`](https://developer.apple.com/documentation/SwiftUI/ProgressViewStyleConfiguration/currentValueLabel-swift.property) to provide more specific details about the progress of the task. (63580200)
- [`FileDocument`](https://developer.apple.com/documentation/SwiftUI/FileDocument) and  have updated protocol requirements: - Their initializer requirement now has a single `FileDocumentReadConfiguration` parameter that the `fileWrapper` and `contentType` can be read from.
- Their `write()` functions that were expected to write to an inout [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) parameter are now `fileWrapper()` functions that return a `FileWrapper` instead.
- The Document-based app templates in Xcode have been updated to reflect this change in API.
- Source compatibility with the previous requirements will eventually be removed. (65146043)
- [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) is now redacted when the doc://com.apple.documentation/documentation/swiftui/anyview/redacted(reason:) modifier is applied. (65047189)
- [`InlinePickerStyle`](https://developer.apple.com/documentation/SwiftUI/InlinePickerStyle) is now available and allows a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) to appear in-line with the rest of the content in its surrounding container. The style will adapt its appearance for different containers and platforms, such as individual menu items in a menu. (59868844)
- [`MenuPickerStyle`](https://developer.apple.com/documentation/SwiftUI/MenuPickerStyle) is now available and allows a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) to present its options within a menu. This style will display its options within a submenu when the `Picker` is nested within a [`Menu`](https://developer.apple.com/documentation/SwiftUI/Menu), [`ContextMenu`](https://developer.apple.com/documentation/SwiftUI/ContextMenu), or [`CommandMenu`](https://developer.apple.com/documentation/SwiftUI/CommandMenu). (65515392)
- Using a [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) in a [`Settings`](https://developer.apple.com/documentation/SwiftUI/Settings) scene will now use the correct style for macOS preference windows. The selected tab will be persisted if no selection binding is passed to the `TabView`. The window for a `Settings` scene will have an appropriate title by default. This will be either the name of the app followed by “Preferences”, or the label of the currently selected tab, if using `TabView`. (51558644) ```swift
Settings {
    TabView {
        Text("General Settings")
            .tabItem {
                Text("General")
                Image(systemName: "gearshape")
            }
        Text("Advanced Settings")
            .tabItem {
                Text("Advanced")
                Image(systemName: "gearshape.2")
            }
    }
    .frame(width: 400, height: 400)
}
```
- [`NavigationView`](https://developer.apple.com/documentation/SwiftUI/NavigationView) and [`HSplitView`](https://developer.apple.com/documentation/SwiftUI/HSplitView) will now automatically separate their child panes’ toolbar items, aligning them with their associated split pane. (60105046) ```swift
NavigationView {
    Sidebar()
        .toolbar {
            Button(action: {}) {
                Label("Sidebar Item", systemImage: "plus")
            }
        }
    Detail()
        .toolbar {
            Button(action: {}) {
                Label("Detail Item", systemImage: "square.and.pencil")
            }
        }
}
```
- [`SceneStorage`](https://developer.apple.com/documentation/SwiftUI/SceneStorage) is now supported. (63190637)
- [`NavigationView`](https://developer.apple.com/documentation/SwiftUI/NavigationView) panes are now automatically resizable and no longer require an explicit frame. (63941018)
- doc://com.apple.documentation/documentation/swiftui/form/useractivity(_:isactive:_:), doc://com.apple.documentation/documentation/swiftui/anyview/oncontinueuseractivity(_:perform:), `onURL` are now supported. (64513929)
- [`List`](https://developer.apple.com/documentation/SwiftUI/List) may now be used with [`ScrollViewReader`](https://developer.apple.com/documentation/SwiftUI/ScrollViewReader). (35471164)
- [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) gains a new initializer accepting a [`Formatter`](https://developer.apple.com/documentation/Foundation/Formatter). (63641785)
- doc://com.apple.documentation/documentation/swiftui/view/body-swift.property is now implicitly a [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) and [`body`](https://developer.apple.com/documentation/SwiftUI/App/body-swift.property) is now implicitly a [`SceneBuilder`](https://developer.apple.com/documentation/SwiftUI/SceneBuilder). (63606493)
- A new redaction reason API for applying placeholder [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) treatment is now available. (63288447)

##### Third Party Apps

###### Known Issues

- You might experience kernel panics when using earlier versions of Parallels Desktop 16. (67358596)  Upgrade to the most-recent version of Parallels Desktop 16.
- Some third-party scripts might produce unexpected results due to the change in macOS version from 10.x to 11. (62477208)  Set `SYSTEM_VERSION_COMPAT=1` in the calling environment, for example: `$ SYSTEM_VERSION_COMPAT=1 legacy_script.pl`

##### Time Machine

###### New Features

- APFS-formatted backup volumes are now supported for faster, more compact, and more reliable backups. New local and network Time Machine backup destinations are formatted as APFS by default. Time Machine will continue backing up to existing HFS backup volumes. (65155545)

##### Virtualization

###### New Features

- The [`Hypervisor`](https://developer.apple.com/documentation/Hypervisor) framework now requires the `com.apple.security.hypervisor` entitlement. (63960391)
- A new `Virtualization` framework provides high-level APIs to run Linux in a virtual machine. (64492914)

###### Deprecations

- The function [`hv_vcpu_run(_:)`](https://developer.apple.com/documentation/hypervisor/1441231-hv_vcpu_run) is deprecated.
- The `VNIdentifiedPointsObservation` class is deprecated. Use [`VNRecognizedPointsObservation`](https://developer.apple.com/documentation/Vision/VNRecognizedPointsObservation) instances instead. (63690311)

##### Wallet

###### Known Issues

- [`isPassLibraryAvailable()`](https://developer.apple.com/documentation/PassKit/PKPassLibrary/isPassLibraryAvailable()) doesn’t ensure uniform availability of pass library functionality between platforms and devices. (60697880)  Call a more specific API to check available functionality, such as [`canAddPasses()`](https://developer.apple.com/documentation/PassKit/PKAddPassesViewController/canAddPasses()).

###### New Features

- Apple Pay support is now available to Mac Catalyst apps. Two methods have been added to existing delegate protocols. No changes are required for iPad apps, but one or both of these methods must be implemented when building for Catalyst. (64187739) - The first method is an addition to the [`PKPaymentAuthorizationControllerDelegate`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationControllerDelegate) protocol: [`presentationWindow(for:)`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationControllerDelegate/presentationWindow(for:)). This method is required for Catalyst when using [`PKPaymentAuthorizationController`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationController), because `PKPaymentAuthorizationController`, unlike [`PKPaymentAuthorizationViewController`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationViewController), doesn’t have knowledge of the window requesting presentation of the payment sheet. Pass back the `UIWindow` instance displaying the UI requesting the payment, for example, `MyViewController.view.window`. This method is marked as required when building for Catalyst, but is otherwise optional.
- The second method depends on whether you’re using `PKPaymentAuthorizationController` or `PKPaymentAuthorizationViewController`. For `PKPaymentAuthorizationControllerDelegate`, use [`paymentAuthorizationController(_:didRequestMerchantSessionUpdate:)`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationControllerDelegate/paymentAuthorizationController(_:didRequestMerchantSessionUpdate:)). For `PKPaymentAuthorizationViewControllerDelegate`, use [`paymentAuthorizationViewController(_:didRequestMerchantSessionUpdate:)`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationViewControllerDelegate/paymentAuthorizationViewController(_:didRequestMerchantSessionUpdate:)).
- This method must be implemented to request a merchant session via your server, and return it via the handler. This mirrors the security model used in WebKit, and replaces listing merchant IDs in the app’s Apple Pay entitlements. This method in turn uses the following class to send back results: ```None
API_AVAILABLE(macos(10.16), ios(14.0), watchos(7.0))
@interface PKPaymentRequestMerchantSessionUpdate : NSObject

- (instancetype)initWithStatus:(PKPaymentAuthorizationStatus)status
               merchantSession:(nullable PKPaymentMerchantSession *)session;

@property (nonatomic, assign) PKPaymentAuthorizationStatus status;
@property (nullable, nonatomic, strong) PKPaymentMerchantSession *session;

@end
```

##### Xcode

###### Known Issues

- Legacy Xcode versions prior to 11.5 might unexpectedly quit when launched. (59991056)  Run the following command in Terminal: `defaults write com.apple.dt.Xcode DVTDisableMainThreadChecker 1`, then deselect Main Thread Checker in the Diagnostic tab of the Run and Test actions for each scheme in your project.

###### New Features

- [`hv_vcpu_run_until(_:_:)`](https://developer.apple.com/documentation/hypervisor/3181548-hv_vcpu_run_until) now supports the deadline [`HV_DEADLINE_FOREVER`](https://developer.apple.com/documentation/Hypervisor/HV_DEADLINE_FOREVER). (57025216)
- The new [`hv_vcpu_enable_managed_msr(_:_:_:)`](https://developer.apple.com/documentation/hypervisor/3567096-hv_vcpu_enable_managed_msr) and [`hv_vcpu_set_msr_access(_:_:_:)`](https://developer.apple.com/documentation/hypervisor/3567097-hv_vcpu_set_msr_access) enable direct MSR access from a guest. (50291076)

## Topics

### AppKit
- [AppKit Release Notes for macOS Big Sur 11](appkit-release-notes-for-macos-11.md)
  Update your apps to use new features, and test your apps against API changes.

## See Also

- [macOS Big Sur 11.5 Release Notes](macos-big-sur-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.4 Release Notes](macos-big-sur-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.3 Release Notes](macos-big-sur-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.2 Release Notes](macos-big-sur-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.1 Release Notes](macos-big-sur-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Universal Apps Release Notes](macos-big-sur-11_0_1-universal-apps-release-notes.md)
  Update your apps to support Macs with Apple silicon.
- [macOS Big Sur 11.0.1 iOS & iPadOS Apps on Mac Release Notes](macos-big-sur-11_0_1-ios-ipados-apps-on-mac-release-notes.md)
  Considerations for running iPhone and iPad apps on Macs with Apple silicon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-big-sur-11_0_1-release-notes)*