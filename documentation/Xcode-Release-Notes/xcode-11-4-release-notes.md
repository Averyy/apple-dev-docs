# Xcode 11.4 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 11.4 includes SDKs for iOS 13.4, iPadOS 13.4, tvOS 13.4, watchOS 6.2, and macOS Catalina 10.15.4. The Xcode 11.4 release supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11.4 requires a Mac running macOS Catalina 10.15.2 or later.

##### General

###### New Features

- Xcode 11.4 supports building and distributing macOS apps as a universal purchase. To distribute your macOS app as a universal purchase, specify the same bundle identifier as your iOS app in the Xcode template assistant when creating a new project. If you have an existing project, edit its bundle identifier in the Project Editor.
- Universal purchase is enabled by default for new Mac Catalyst apps created in Xcode 11.4. When you create a new Mac Catalyst app, it will use the same bundle identifier as your iOS app.
- Automatic signing in Xcode 11.4 supports building Mac Catalyst apps with a custom bundle identifier. You can edit the bundle identifier of your app using the Signing & Capabilities tab in the Project Editor. If you choose to build your Mac Catalyst app with a custom bundle identifier that doesn’t match your iOS app, you won’t be able to distribute the app as a universal purchase.

###### Known Issues

- When targeting devices running iOS 13.3.1, tvOS 13.3.1, watchOS 6.1, or later using a free Apple Developer account, app extensions incorrectly count against the limit of three apps installed simultaneously. When this happens, Xcode reports an error: “The maximum number of apps for free development profiles has been reached.” (59264389) (FB7568073) : Delete apps signed with your free account from your device and also remove any associated provisioning profiles from the device using Xcode’s Devices window. If your app contains more than two app extensions, remove them to remain under the three app limit.

###### Resolved Issues

- Creating an Objective-C category file by choosing File > New > File no longer creates a file that includes an import of the AppKit framework. (55977950) (FB7346800)

##### Apple Clang Compiler

###### New Features

- Xcode 11.4 turns the `-Watimport-in-framework-header` warning on by default. Using `@import` in framework headers is discouraged, because doing so requires all importers to use modules. (59222634) (FB7566046) To temporarily silence this warning, use: ```objc
#if __has_feature(modules)

#if __has_warning("-Watimport-in-framework-header")
#pragma clang diagnostic ignored "-Watimport-in-framework-header"
#endif
@import NameOfFramework;
#endif
```

##### Asset Catalogs

###### Known Issues

- Assets localized in the asset catalog are now used at runtime, regardless of whether an associated `.lproj` directory exists. (49565973)

###### Resolved Issues

- Fixed an issue where previews of symbol images in the asset catalog had flipped baselines. (57540017) (FB7473079)
- Asset Catalog `Contents.json` files ending in a newline will retain that newline when saved. (50630207) (FB6058998)

##### Build System

###### New Features

- Build settings have a new evaluation operator, `default`, which you can use to specify the default value of a build setting if it evaluates to `empty` in the context of the evaluation. For example: ```text
$(SETTING:default=something)
``` If `$(SETTING)` is empty, this expression evaluates to ‘something’. The default value may itself be an expression that contains build setting evaluations. (57402718)
- Building codeless kernel extensions with the new build system now requires you to set the `GENERATE_KERNEL_MODULE_INFO_FILE` build setting to `NO`. (57247534)

###### Resolved Issues

- Fixed a link failure that could occur when building for testing while using bitcode. (57857082)

##### Debugging

###### New Features

- Xcode 11.4 adds support to copy and paste breakpoints in the Breakpoint Navigator. (11723352)
- The view debugger now presents layout guides ([`UILayoutGuide`](https://developer.apple.com/documentation/UIKit/UILayoutGuide), [`NSLayoutGuide`](https://developer.apple.com/documentation/AppKit/NSLayoutGuide)) and their referencing constraints. (20387325)
- View debugging supports showing layers using the Show Layers menu item in the Editor menu. (15775898)
- The exception reason now surfaces as an editor annotation. You can inspect the Exception object in Variables View and find the backtrace of the original uncaught exception, if any, in the Debug Navigator. (8045587)
- You can now use the Terminal for standard I/O, instead of Xcode’s Console. Make this choice using the Scheme Editor’s Options tab. (33552211)

###### Known Issues

- The Build & Run action may fail to launch a watchOS app on series 2 and series 3 watch simulators when attempting to deploy soon after booting the simulator. (60281738) : Build and run again on the simulator after the simulated device finishes booting.
- Xcode may not persist changes made to diagnostics in the Scheme Editor within the first few minutes of opening a project for the first time. For example, if you enable the Malloc Stack Logging checkbox soon after creating a new project from a template, the checkbox may be spontaneously unchecked before you build and run the target, thus preventing the diagnostics from being enabled. (59154142) : If you find that diagnostics you enabled, such as Malloc Stack Logging, aren’t working, please check the scheme editor because the relevant checkboxes may have spontaneously become unchecked. Re-enable the desired preference. Xcode will recover in a few minutes and save the selections you’ve made.

###### Resolved Issues

- View outlines in the view debugger are now more visible. (44861893) (FB5361403)

##### Devices

###### Known Issues

- Xcode 11.4 doesn’t work with devices running iOS 13.4 beta 1 and beta 2. (60055806)

###### Resolved Issues

- Icons and names for devices running iOS 13.0 reflect the correct OS version in the Devices and Simulators window. (55044395)

##### Instruments

###### Resolved Issues

- State restoration in Instruments now depends on the scope selection. As a result, you may need to reconfigure and re-save custom templates in Instruments 11.4. (37746235)
- Fixed an issue where removing one run from Instruments removed all of them. (53451989)
- Fixed an issue in the iOS 13.4 Simulator runtime where applications wouldn’t launch using the Allocations and Leaks templates. (56543962) (FB7403237)
- Fixed a crash that occured when double-clicking a symbol in extended detail view. (58058064)
- Importing a file into an Instruments template now creates trace scopes according to the template specification. (58100654)
- Instruments now properly tracks processes that exited during “All Processes” recordings. (59072482)
- Fixed an issue where the Allocations instrument wouldn’t record on watchOS devices. (59268958) (FB7568204)

##### Interface Builder

###### New Features

- Added Pointer Button property to [`UITapGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UITapGestureRecognizer) to control which mouse events trigger the gesture recognizer to succeed. (59330235)
- Added new Pointer Interaction property on [`UIButton`](https://developer.apple.com/documentation/UIKit/UIButton). (59337826)
- [`UIDatePicker`](https://developer.apple.com/documentation/UIKit/UIDatePicker) has a new Style property, and will use a new compact style by default in Mac Catalyst apps on macOS 10.15.4. (56384950)
- Added dynamic system gray colors to inspector color pickers. (55403376) (FB7281404)

###### Resolved Issues

- Fixed an issue that prevented the color picker panel from having any effect when a text field in the inspector was focused. (56067005) (FB7358220)
- Added Scroll Types property to [`UIPanGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UIPanGestureRecognizer) to control which mouse events trigger the gesture recognizer to succeed. (59330150)
- Resolved an issue where `NSSwitch` did not correctly update in the canvas when the control size was set to Small or Mini. (56520376)
- Resolved an issue where Xcode could hang when working with [`UITableViewCell`](https://developer.apple.com/documentation/UIKit/UITableViewCell) in a tvOS storyboard. (56353682)
- Resolved a crash that could occur when switching the style of a [`UITableViewCell`](https://developer.apple.com/documentation/UIKit/UITableViewCell) from basic to custom. (56079081)
- Removed a large tooltip that obscured the list of constraints. (55938862) (FB7343268)
- Fixed a bug where [`NSMenuItem`](https://developer.apple.com/documentation/AppKit/NSMenuItem) images no longer displayed on the canvas. (55838210) (FB7336326)
- Resolved a crash when editing attributed string values of [`UILabel`](https://developer.apple.com/documentation/UIKit/UILabel) and [`UIButton`](https://developer.apple.com/documentation/UIKit/UIButton) controls. (55737956) (FB7326816)
- Resolved a hang when using [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) in tvOS storyboards. (55645930) (FB7318427)
- Fixed a bug where using named colors in `IBInspectable` properties would use a fixed color at runtime, instead of the dynamic color from the asset catalog. (55248109) (FB7248211)
- Resolved an Xcode crash that occurred when editing [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) items in Mac documents. (55172989) (FB7212782)
- Improved the rendering of images in iOS, macOS, tvOS and watchOS documents. PDF images render their vector representations. The scale factor is better preserved when image filenames end with a scale (`@2x`). Use a more pleasant placeholder when an image is missing. (53887572)
- Improved performance working with Mac XIBs and storyboards containing a large number of controls. (52603889) (FB6472772)
- Fixed duplicate keyboard shortcuts used for inspector categories. (52388396) (FB6366331)
- Fixed an issue where Interface Builder canvas and previews did not always display the correct image content for the selected languages when localizing images in the asset catalog. (48353744)
- Fixed a compilation bug with the label on an [`NSTabViewItem`](https://developer.apple.com/documentation/AppKit/NSTabViewItem) not getting localized. (46290566)
- Removed [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) from the Apple TV object library because it isn’t supported on the platform. (45957591)
- Resolved an issue where drag images of view controllers would sometimes render upside-down when both 1x and 2x displays were connected. (45464632) (FB5704168)
- Fixed an issue where `NSResponder.h` would incorrectly show up in the Assistant Editor for XIB/Storyboard files. (37259359)
- Fixed an issue where some Xcode editors, often Interface Builder, would be misaligned from the Xcode window that contains them. (39655724)
- Objects are automatically labeled based on connections, sometimes resulting in view controllers called “Delegate”. This behavior has been changed to only apply from parents to children. Additionally, accessibility connections (“link” and “title”) no longer affect automatic labeling. (22972580) (FB5806917)
- Resolved a crash when selecting a container view controller and opening the Preview editor. (23099319)
- Fixed an issue where the inspector section for [`NumberFormatter`](https://developer.apple.com/documentation/Foundation/NumberFormatter) Symbols had a light background in dark mode. (57393302) (FB7459536)
- Fixed an issue where several [`NSResponder`](https://developer.apple.com/documentation/AppKit/NSResponder) actions were missing from the Connections Inspector. (56546759) (FB7403346)
- Fixed a crash that could occur when moving duplicate [`NSComboBox`](https://developer.apple.com/documentation/AppKit/NSComboBox) items in the Inspector. (55796760)
- Fixed an issue where the Interface Style Simulated Metrics setting wouldn’t apply to objects being dragged. (55207867)
- Fixed an issue where named Global Tint colors weren’t properly unarchived during Interface Builder document loading, resulting in incorrect Global Tint colors on subsequent document saves. (55158004) (FB7232333)
- Fixed an issue where unrecognized system colors wouldn’t have their fallback colors preserved after loading and saving Interface Builder documents. (54623340)
- Fixed a bug that prevented entering a `0` constant in the constraint popup editors. (54076090)
- Fixed an issue where `XIB` template files didn’t have dynamic background colors. (53907727) (FB6918296)
- Fixed a crash that occurred if an [`NSLevelIndicator`](https://developer.apple.com/documentation/AppKit/NSLevelIndicator) Minimum inspector value was higher than its Maximum. (53302326) (FB6740368)
- Fixed an issue where Interface Builder documents that contain [`UINavigationBar`](https://developer.apple.com/documentation/UIKit/UINavigationBar) titles configured with named colors could be archived with duplicate-named color resources. (52162293) (FB6253352)
- Fixed an issue where Apple TV [`UITableViewCell`](https://developer.apple.com/documentation/UIKit/UITableViewCell) safe area frames displayed incorrectly in `XIB` files. (51679086)
- Fixed an issue where Xcode could crash after configuring text to be non-attributed. (46228389) (FB5673720)
- Fixed an issue where creating a Swift outlet with drag-to-source could result in a class-not-found error. (57883610) (FB7491401)
- [`UIDatePicker`](https://developer.apple.com/documentation/UIKit/UIDatePicker) compact style is available. (58963416)
- Removed inspector support for configuring [`NSTableColumn`](https://developer.apple.com/documentation/AppKit/NSTableColumn) header cell fonts to match the API. You can configure header cell fonts by subclassing [`NSTableHeaderCell`](https://developer.apple.com/documentation/AppKit/NSTableHeaderCell) and overriding the `font` property in code. (23664679) (FB5630174)

##### Metal

###### New Features

- The Metal Frame Debugger now supports iOS and tvOS simulators. (54273848)

###### Resolved Issues

- The SIMD-group functions (see section 6.8.2 of the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)) compile for iOS. (59338106)

##### Organizer

###### New Features

- The Crashes Organizer now shows crash logs for universal purchase macOS apps. (57607495)

##### Playgrounds

###### Known Issues

- SwiftUI views aren’t rendered by Quick Look previews or inline result views. (59908350)

###### Resolved Issues

- Inline results no longer obscure lines below them. (35682773) (FB5729414)
- Automatic code suggestions are more reliable for Playgrounds embedded within projects. (59411425)
- Single line doc comments no longer cause the following line to be rendered as documentation. (55861744)
- iOS live views now use the system background color by default. (54516552)
- Improved reliability of issue annotations in Playground source code. (43793952) (FB5423160)

##### Previews

###### New Features

- Xcode Previews now saves the zoom and pin state of the canvas. (49168788)
- You can now turn off the device bezels in Xcode Previews using the Editor > Previews menu. (48676867)
- Xcode Previews now shows UI for quickly adding a new [`PreviewProvider`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider) when the open file contains no [`PreviewProvider`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider). (45471721)
- You can now copy, cut, paste, duplicate, and delete views directly within the Xcode Previews canvas. (56134191)
- Selecting a SwiftUI preview in code now highlights the corresponding preview in the canvas, and vice versa. (56412209)
- Xcode Previews now supports previewing iPad applications brought to the Mac. (41416222)

###### Known Issues

- On-device debugging of SwiftUI Previews may not work for Series 2 and Series 3 watches because the preview is built for the wrong architecture. (59909746) : Use the Build & Run action with the watch selected as the destination. The application will be built for the correct architecture.
- Previews may fail for Mac Catalyst applications or sandboxed macOS applications when Xcode isn’t in the Applications folder. (57096274) : Move Xcode to the Applications folder
- Using [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) to set Preview properties may result in preview failure. (58985849) : Use [`Group`](https://developer.apple.com/documentation/SwiftUI/Group) to set Preview properties.

###### Resolved Issues

- The Xcode Previews canvas now surfaces better accessibility information for selectable views. (55538520)
- Fixed an issue where the popover SwiftUI inspector could open empty. (58064269)
- Fixed a crash when working with certain user types in Xcode Previews. (56057560)
- Fixed an issue where SwiftUI previews display pixelated on 1x displays. (55227670)
- Fixed a crash when using the Xcode Previews inspector. (54991451)
- Fixed an issue where some Xcode Previews would spin forever when first updating. (55560302)
- Xcode Previews now correctly builds previews in frameworks that depend on other frameworks in the project. (56956786) (FB7431181)
- Fixed a crash in Xcode Previews that could occur when using the inspectors. (55933725)

##### Project Navigator

###### Known Issues

- When restoring a workspace, the Canvas and Assistant checkboxes are sometimes unexpectedly disabled in the Editor Options menu. (59962740) : Use the Canvas and Assistant items in the Editor menu, or their respective keyboard shortcuts, to toggle the visibility of these views.

##### Server

###### Known Issues

- An Xcode Server bot loses authentication when a user clicks the “Replace Repositories” button under the Repositories tab. (59066142) : Either don’t click “Replace Repositories”, or reauthenticate after doing so.
- Users can no longer select which branch to use for integrations under the Repositories tab of an Xcode Server bot. (59068222, 58615215)

##### Simulator

###### New Features

- Simulator supports pointer capture for iPadOS. When pointer capture is enabled, any events for connected mice or trackpads are sent to the simulator instead of to macOS. (55401573)
- Dragging and dropping an SSL certificate (CER or PEM file) will now install the certificate into the simulated device’s trusted root store. (56225826)
- `simctl` supports a keychain subcommand. This command can add certificates to the trusted root store or the keychain. It can also reset the keychain, deleting all saved items. For example, to install “my-selfsigned.cer” to the trusted root store: ```shell
xcrun simctl keychain <device> add-root-cert my-selfsigned.cer
``` Adding a certificate to the trusted root store causes `TLS` / `SSL` connections to trust the certificate. (56213319)
- `simctl` now supports modifying privacy permissions. You can modify privacy permissions to create known states for testing purposes. For example, to allow an example app to access the photo library without any prompts: ```shell
xcrun simctl privacy <device> grant photos com.example.appTo
``` reset all permissions to defaults, as if the app had never been installed before: ```shell
xcrun simctl privacy <device> reset all com.example.appAlways
``` test your application after resetting permissions to ensure you have the correct usage description keys in your `Info.plist` and you are properly requesting and handling different authorization states. See `simctl help privacy` for more information. (55155981)
- Simulator supports toggling appearance for iOS simulators (13.0 and later). From within the app select Debug > Toggle Appearance. From the command line use the `simctl ui` subcommand, e.g. to set dark appearance (54556446) (FB7093020): ```shell
xcrun simctl ui <device> appearance dark
```
- Simulator now has a menu item and keyboard shortcut to bring up the app switcher in iOS Simulators. (54252732) (FB7014782)
- `simctl status_bar` now allows changing the operator (carrier) name. (54162823) (FB6985308)
- Simulator now has a menu item to trigger screenshots in iOS simulators. This saves a screenshot to the simulated device’s camera roll. The existing screenshot feature has been renamed “Save Screen” for clarity and continues to save the device’s framebuffer to your Mac’s desktop by default. Hold Option when saving the screen to change the default location. (52852628)
- tvOS simulators no longer capture the Touch Bar as if it were a Siri Remote paired with your Mac. (48547948)
- Simulator supports simulating remote push notifications, including background content fetch notifications. In Simulator, drag and drop an APNs file onto the target simulator. The file must be a JSON file with a valid Apple Push Notification Service payload, including the “aps” key. It must also contain a top-level “Simulator Target Bundle” with a string value that matches the target application’s bundle identifier.`simctl` also supports sending simulated push notifications. If the file contains “Simulator Target Bundle” the bundle identifier is not required, otherwise you must provide it as an argument (8164566): ```shell
xcrun simctl push <device> com.example.my-app ExamplePush.apns
```
- Simulator has a new UI that streamlines working with simulated devices. Simulated device windows have a standard title bar, with buttons for common tasks. App-level settings are now available in the Preferences window. (57715023, 57380865, 58013098)

###### Known Issues

- Pointer capture isn’t supported over a Screen Sharing session. If you enable pointer capture all input will be blocked and you will be unable to exit capturing mode. Capture mode monitors for HID events, so any system that injects CGEvents directly isn’t usable with Simulator’s capturing support. (59411574) : Disconnect and reconnect Screen Sharing. This will automatically cancel pointer capturing.
- Notification Service Extensions do not work in simulated push notifications. The `mutable-content` key is not honored. (55822721)
- Third-party “endpoint security” software may cause slow simulators, system freezes, or prevent debug processes from running in simulators reliably. This sometimes manifests as `debugserver` disconnections, or sends simulator applications a `SIGKILL` signal. (55853555) : Uninstall the third-party software.

###### Resolved Issues

- CoreSimulator now cleans up temporary files generated by Interface Builder during the build process. (53568836)
- When multiple GPUs are installed, Simulator assigns each booted simulator to one of the available GPUs. (50608554)
- Fixed an issue that could cause certain kinds of IOSurfaces in simulators to corrupt memory or be created with the wrong memory protection. (52899754)

##### Siri Intents

###### Known Issues

- Xcode 11.4 fails to generate source files from your intent definition files when using the Legacy Build System. (60591035) : First, add a Run Script phase before the Compile Sources phase of your target: ```shell
xcrun intentbuilderc generate -input ${SRCROOT}/PATH/TO/Intents.intentdefinition -output ${SRCROOT}/Intents -classPrefix "" -language Swift -swiftVersion 5.0
``` Then, add all of the generated files from the output path specified in the command above to all required targets in your project. You can find more information about arguments of `intentbuilderc` by running this command: ```shell
xcrun intentbuilderc help
```

##### Source Control

###### New Features

- Improved stability of core source-control functionality, and reduced memory footprint related issues. (54765574)
- Split functionality of “Fetch and Refresh Status” menu item into two separate menu items to separate fetching and refreshing status. (54326241)

###### Resolved Issues

- Fixed an issue that prevented adding a GitHub account. (59205637)

###### Deprecations

- Personal access tokens are now the default method of authentication for GitHub.com Source Control accounts in Xcode. Newly added accounts will require a personal access token and you may need to update existing accounts with a personal access token after July 1, 2020.  For more information, see [`Deprecated APIs and authentication`](https://developer.apple.comhttps://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api). (59388185)

##### Source Editor

###### Resolved Issues

- A rename refactor of a Swift or Objective-C object correctly renames the file that contains the object. (32408445)

##### Swift Packages

###### New Features

- Remote Swift packages with tools version 5.2 and above no longer resolve package dependencies that are only used in their test targets, improving performance and reducing the chance of dependency version conflicts. (56925017)
- Swift Package Manager uses a new strategy to resolve package dependencies that significantly improves the quality of error messages and performance in complex package graphs. (45371461)

###### Resolved Issues

- iOS, tvOS, or watchOS apps with a Swift Package that builds a dynamic library can be submitted to the App Store. (55564324) (FB7303066)
- You can now use Swift-only [`XCTest`](https://developer.apple.com/documentation/XCTest) APIs (such as [`XCTUnwrap(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTUnwrap(_:_:file:line:))) when building a package using command-line SwiftPM. (51959291)
- You can import `libxml2`, `libxslt`, and `libexslt` modules in both Swift package targets and regular Xcode targets, without any additional search paths. (52043828)

##### Swift

###### New Features

- Type checking is now more precise.  In many situations, this precision allows code completion to be 1.2 to 1.6 times faster for large files in Xcode 11.4, compared to Xcode 11.3.1.
- Code completion of implicit members is now available for incomplete dictionary literals and incomplete ternary expressions.
- Code completion results have improved type information. Results will display opaque result types (for example `some View)` when possible, and preserve typealiases. Results will no longer show unnecessary parent types. For example: ```swift
import SwiftUI

struct MyModifier: ViewModifier {
    body
}
``` When completing `body` inside `MyModifier`, Xcode 11.4 will offer `body(content: Content) -> some View`.
- The compiler now supports local functions whose default arguments capture values from outer scopes. ([`SR-2189`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-2189)) (20796451) ```swift
func outer(x: Int) -> (Int, Int) {
    func inner(y: Int = x) -> Int {
        return y
    }

    return (inner(), inner(y: 0))
}
```
- The compiler will now emit a warning when attempting to pass a temporary pointer argument produced from an array, string, or `inout` argument to a parameter which is known to escape it. This includes the various initializers for the [`UnsafePointer`](https://developer.apple.com/documentation/Swift/UnsafePointer)/[`UnsafeBufferPointer`](https://developer.apple.com/documentation/Swift/UnsafeBufferPointer) family of types, as well as memberwise initializers. For example, the compiler will emit warnings compiling the following code: ```swift
struct S {
    var ptr: UnsafePointer<Int8>
}

func foo() {
    var i: Int8 = 0
    let ptr = UnsafePointer(&i)
    // warning: initialization of 'UnsafePointer<Int8>' results in a
    // dangling pointer

    let s1 = S(ptr: [1, 2, 3])
    // warning: passing '[Int8]' to parameter, but argument 'ptr' should be a
    // pointer that outlives the call to 'init(ptr:)'

    let s2 = S(ptr: "hello")
    // warning: passing 'String' to parameter, but argument 'ptr' should be a
    // pointer that outlives the call to 'init(ptr:)'

}
``` All 3 of the above examples are unsound because each argument produces a temporary pointer only valid for the duration of the call to which they are passed. Therefore the returned value in each case references a dangling pointer. ([`SR-2790`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-2790)) (31232450)
- You can call values of types that declare `func callAsFunction` methods like functions. The call syntax is shorthand for applying `func callAsFunction` methods: ```swift
struct Adder {
    var base: Int

    func callAsFunction(_ x: Int) -> Int {
      return x + base
    }
}

var adder = Adder(base: 3)
adder(10) // returns 13, same as adder.callAsFunction(10)
``` You must include `func callAsFunction` argument labels at call sites. You can add multiple `func callAsFunction` methods on a single type, and you can mark them as `mutating`. `func callAsFunction` works with `throws` and `rethrows`, and with trailing closures. (59014791)
- Subscripts can now declare default arguments. (59012048) ```swift
struct Subscriptable {
    subscript(x: Int, y: Int = 0) {
        ...
    }
}

let s = Subscriptable()
print(s[0])
```
- A class-constrained protocol extension, where the extended protocol does not impose a class constraint, now infers the constraint implicitly. (59011997) ```swift
protocol Foo {}

class Bar: Foo {
    var someProperty: Int = 0
}

// Even though 'Foo' does not impose a class constraint, it is automatically
// inferred due to the Self: Bar constraint.

extension Foo where Self: Bar {
    var anotherProperty: Int {
        get { return someProperty }
        // As a result, the setter is now implicitly nonmutating, just like
        // it would be if 'Foo' had a class constraint.
        set { someProperty = newValue }
    }
}
```
- Convenience initializer inheritance for subclasses defined outside the module that defines the base class now comes with additional restrictions. When these subclasses have a base class with non-public designated initializers, they no longer automatically inherit convenience initializers from their superclasses. To restore this automatic inheritance behavior, the base class must ensure that all of its designated initializers are `public` or `open`. (51249311)
- Xcode and the corresponding Command Line Tools package include the SourceKit-LSP language server for Swift and C-based languages. The language server is in early development, and this is a great time to experiment with it. SourceKit-LSP can be used with third-party tools that support the Language Server Protocol (LSP), and it supports Swift Packages built from the command-line. For information about using SourceKit-LSP see [`Getting Started with SourceKit-LSP`](https://developer.apple.comhttps://github.com/apple/sourcekit-lsp/#getting-started). (48004600)
- The Swift compiler uses a new strategy to produce diagnostics that drastically improves the quality and precision of error messages. Details about this new strategy can be found on the post [`New Diagnostic Architecture Overview`](https://developer.apple.comhttps://swift.org/blog/new-diagnostic-arch-overview/) on the Swift blog. (36854046)
- A method override can no longer have a generic signature with requirements not imposed by the base method. For example, the below code produces an error. (23626260) (FB5382462) ```swift
protocol P {}

class Base {
    func foo<T>(arg: T) {}
}

class Derived: Base {
    // generates an error because of the added requirement
    override func foo<T: P>(arg: T) {}
}
```

##### Known Issues

- If an Objective-C class is defined with the `objc_runtime_name` attribute and imported into Swift, Swift code may crash when trying to access the class. (60888835) : Instead of using `objc_runtime_name`, define the class with its runtime name as the class name, and use a `typedef` to establish the desired source-level name: ```swift
// This may cause a crash.

__attribute__((objc_runtime_name("Bar")))
@interface Foo: NSObject
@end

// Workaround
@interface Bar: NSObject
@end
typedef Bar Foo;
```
- Code that relies on the compiler automatically tupling a pattern may lead to a compiler error when upgrading to Xcode 11.4, even though the code compiled before. (58425942) For example, leaving out parentheses when switching on an Optional of a tuple type causes a compiler error: ```swift
switch x { // error: switch must be exhaustive
  case .some((let a, let b), let c): // warning: the enum case has a
       // single tuple as an associated value, but there are several
       // patterns here, implicitly tupling the patterns and trying
       // to match that instead
  ...
}
``` : Add extra parentheses to explicitly tuple the pattern: ```swift
switch x {
    case .some(((let a, let b), let c)): // Notice the extra pair of parentheses.
    ...
}
```

##### Resolved Issues

- The compiler now correctly strips argument labels from function references used with the `as` operator in a function call. As a result, you can now use the `as` operator to disambiguate a call to a function with argument labels: ```swift
func foo(x: Int) {}

func foo(x: UInt) {}

(foo as (Int) -> Void)(5)  // Calls foo(x: Int)
(foo as (UInt) -> Void)(5) // Calls foo(x: UInt)
``` Previously, this was only possible for functions without argument labels. This change also means that you can no longer use a generic type alias to preserve the argument labels of a function reference through the `as` operator. The following is now rejected: ```swift
typealias Magic<T> = T

func foo(x: Int) {}
(foo as Magic)(x: 5) // error: Extraneous argument label 'x:' in call
``` You must instead call the function value without argument labels. (59011892) ```swift
(foo as Magic)(5)
```

##### Testing

###### New Features

- To enable test timeout behavior from `xcodebuild`, or to override the corresponding setting in the test plan, pass the `-test-timeouts-enabled` option. To configure the default execution time allowance for an individual test when timeouts are enabled, pass the `-default-test-execution-time-allowance` option. To enforce an absolute cap on the amount of time a test can run (if it requests additional time via the [`executionTimeAllowance`](https://developer.apple.com/documentation/XCTest/XCTestCase/executionTimeAllowance) API), pass the `-maximum-test-execution-time-allowance` option. Refer to the `xcodebuild` man page (`man xcodebuild`) for more information. (58413928)
- You can enable test timeouts through the “Test Timeouts” option in the test plan. You can override this value from the command-line through the `-test-timeouts-enabled` option to `xcodebuild`. (58125818)
- The [`XCTAssertEqualWithAccuracy`](https://developer.apple.com/documentation/XCTest/XCTAssertEqualWithAccuracy) and [`XCTAssertNotEqualWithAccuracy`](https://developer.apple.com/documentation/XCTest/XCTAssertNotEqualWithAccuracy) APIs now support all FloatingPoint types. (57523034)
- When building a scheme which has been converted to use test plans and whose active test plan has code coverage enabled, Xcode now includes code coverage instrumentation when building for the ‘Run’ action, in addition to the ‘Test’ action. This matches the behavior of building schemes which don’t use test plans and have code coverage enabled, and avoids unnecessary rebuilds when alternating between running and testing actions. (57367856)
- Resetting the authorization status of a protected resource (e.g. Contacts, Bluetooth or Location) is now supported in UI testing contexts. [`XCUIApplication`](https://developer.apple.com/documentation/XCTest/XCUIApplication) gains a new method, [`resetAuthorizationStatus(for:)`](https://developer.apple.com/documentation/XCTest/XCUIApplication/resetAuthorizationStatus(for:)), that accepts an [`XCUIProtectedResource`](https://developer.apple.com/documentation/XCTest/XCUIProtectedResource). This allows test authors to easily set the the authorization status of apps to their initial state, providing a convenient way to test first-launch and first-access flows of their resources. (56628656)
- Xcode’s New File templates for [`XCTest`](https://developer.apple.com/documentation/XCTest) in Swift now include the `throws` keyword for all test methods. Errors thrown by test methods are recorded as test failures. (56619497)
- If you enable parallel testing for a test target in the active scheme/test plan, and you pass the `-parallelize-tests-among-destinations` flag to `xcodebuild` along with multiple destination specifiers, Xcode distributes test classes within that target among the destinations to speed up test execution. (56585597)
- UI testing and recording on macOS support the `Fn` key modifier. (56178883)
- When you run `xcodebuild build-for-testing` for a scheme that uses test plans, its generated `.xctestrun` file now includes metadata about each test plan, including the name of the test plan and whether it’s the scheme’s default plan. (53997527)
- Xcode introduced an “Enable Testing Search Paths” build setting to improve support for test support frameworks and libraries. This build setting is on by default for test bundle targets, as well as for targets which explicitly include `XCTest.framework` in their “Link Binary With Libraries” list. Source files in such targets can now import [`XCTest`](https://developer.apple.com/documentation/XCTest) without setting any custom search paths. (51117167)
- [`XCTest`](https://developer.apple.com/documentation/XCTest) has improved error handling and logging for the case where a custom [`XCTestObservation`](https://developer.apple.com/documentation/XCTest/XCTestObservation) implementation throws an exception. (44291078)
- `xcodebuild` now validates the deployment target and architecture of built products when running `xcodebuild test-without-building` with the `-xctestrun` flag. Targets that aren’t compatible with the requested run destination are skipped. (43107996)
- [`XCTest`](https://developer.apple.com/documentation/XCTest) now includes throwing variants of the [`setUp()`](https://developer.apple.com/documentation/XCTest/XCTest/setUp()) and [`tearDown()`](https://developer.apple.com/documentation/XCTest/XCTest/tearDown()) instance methods, allowing tests to throw errors in Swift during set up or tear down. Override the [`setUpWithError()`](https://developer.apple.com/documentation/XCTest/XCTest/setUpWithError()) or [`tearDownWithError()`](https://developer.apple.com/documentation/XCTest/XCTest/tearDownWithError()) methods instead of [`setUp()`](https://developer.apple.com/documentation/XCTest/XCTest/setUp()) or [`tearDown()`](https://developer.apple.com/documentation/XCTest/XCTest/tearDown()), respectively. If an error is thrown by [`setUpWithError()`](https://developer.apple.com/documentation/XCTest/XCTest/setUpWithError()), the test method is not executed, and if the error was due to calling an `XCTSkip*` API, the test is marked as skipped instead of failed. (42069831)
- Xcode now validates the deployment target of test bundle targets, and skips running any tests that are incompatible with the selected run destination. Some targets may require a change to their minimum deployment target build setting to continue to run on older run destinations. (39775813)
- Errors thrown by Swift test methods now record the source location where the error was thrown. Xcode highlights these lines in the source editor and allows jumping to those locations from the Issue Navigator. (26370684)
- Xcode now opens files in the source editor after they are created by clicking the ‘+’ button in the Test Navigator. (17088680)
- [`XCTest`](https://developer.apple.com/documentation/XCTest) now supports dynamically skipping tests based on runtime conditions, such as only executing some tests when running on certain device types or when a remote server is accessible. When a test is skipped, Xcode displays it differently in the Test Navigator and Test Report, and highlights the line of code where the skip occurred, along with an optional user description. Information about skipped tests is also included in the `.xcresult` for programmatic access. To skip a test, call one of the new `XCTSkip*` functions from within a test method or [`setUp()`](https://developer.apple.com/documentation/XCTest/XCTest/setUp()). For example: ```swift
func test_canAuthenticate() throws {
    try XCTSkipIf(AuthManager.canAccessServer == false, "Can't access server")

    // Perform test…
}
``` The [`XCTSkipUnless(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTSkipUnless(_:_:file:line:)) API is similar to [`XCTSkipIf(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTSkipIf(_:_:file:line:)) but skips if the provided expression is false instead of true, and the [`XCTSkip`](https://developer.apple.com/documentation/XCTest/XCTSkip-swift.struct) API can be used to skip unconditionally. (13696693)
- [`XCTest`](https://developer.apple.com/documentation/XCTest) now allows individual tests to time out if they exceed a configurable duration of time. If timeouts are enabled, either via a test-plan option or via an `xcodebuild` command-line option, a test will be given a default allowance within which it must complete. Tests that exceed this length of time will fail, and a spindump of the test process will be attached to the test in the test report. If the test needs additional time to run, it can request that time via the [`executionTimeAllowance`](https://developer.apple.com/documentation/XCTest/XCTestCase/executionTimeAllowance) property on [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase). For more information, refer to the documentation in `XCTestCase.h`. (12584283)

###### Resolved Issues

- [`XCTest`](https://developer.apple.com/documentation/XCTest) now correctly handles large wait-timeout values passed to [`XCTWaiter`](https://developer.apple.com/documentation/XCTest/XCTWaiter) “wait” APIs, such as `DBL_MAX`. (56503613)
- Source editor test diamonds for tests in Swift packages now appear automatically upon opening the package in Xcode. (51105554)
- Previously, when running UI tests, the target under test was reinstalled before each test started. Starting in Xcode 11.4, the target under test is installed once per test session and device, speeding up UI tests considerably. (24776269)
- When hit testing a target, macOS hit testing accepts descendants with frames equivalent to the target as hit test matches. (59275386)

## See Also

- [Xcode 11.7 Release Notes](xcode-11_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.6 Release Notes](xcode-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.5 Release Notes](xcode-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4.1 Release Notes](xcode-11_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.3.1 Release Notes](xcode-11_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.3 Release Notes](xcode-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.2.1 Release Notes](xcode-11_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.2 Release Notes](xcode-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.1 Release Notes](xcode-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11 Release Notes](xcode-11-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_4-release-notes)*