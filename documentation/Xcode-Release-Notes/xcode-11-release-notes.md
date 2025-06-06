# Xcode 11 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 11 is available in the Mac App Store and includes SDKs for iOS 13, macOS Catalina 10.15, watchOS 6, and tvOS 13. Xcode 11 supports development for devices running iOS 13.1. Xcode 11 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11 requires a Mac running macOS Mojave 10.14.4 or later.

> **Note**: Fixed an Asset Catalog bug that prevented named colors from being found at runtime when running on iOS 11. (54325712)

##### General

###### New Features

- Xcode 11 supports development with [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI). (22843503) > **Note**: SwiftUI previews and inspectors are only available when running on macOS Catalina 10.15.
- Xcode 11 adds support for Mac Catalyst to bring iPad apps to the Mac. (43577997) > **Note**: iPad apps can only be configured to build for Mac when running on macOS Catalina 10.15, and the My Mac run destination is unavailable on earlier versions of macOS.
- You can now change the appearance of Xcode independently of the system appearance setting. (41165587)
- Xcode supports uploading apps from the Organizer window or from the command line with `xcodebuild` or `xcrun altool`. Application Loader is no longer included with Xcode. (29008875)
- LaunchServices on macOS now respects the selected Xcode when launching Instruments, Simulator, and other developer tools embedded within Xcode. For example, when you double-click an Instruments trace in Finder, the version of Instruments for the selected Xcode launches. Change which Xcode is used with xcode-select from the command line. (6757601)
- Editors can be added to any window without needing the Assistant Editor. Editors are added using the “Add Editor” button in the jump bar or the File > New > Editor command. Each editor can independently show its own assistant or canvas via commands in the Editor or Editor Options menus. These two modes will automatically show relevant content when available. When using multiple editors, the View > Editor > Focus command can be used to temporarily expand the active editor to fill the entire window, hiding other editors. Additionally, “Show Editor Only” will reset a given editor, turning off any extra views that have been enabled in that editor. For source control support, the Code Review button in the Toolbar replaces the Comparison Editor. The “Show Authors” command is now available from the Source Editor’s Editor menu. The SCM Log is now in the Inspector Area. (43806898)

###### Known Issues

- When building an Objective-C iOS File Provider application extension that implements the `-URLForItemWithPersistentIdentifier:` method, Xcode emits a warning saying that this callback method is deprecated and won’t be called. This warning is incorrect; the method isn’t deprecated, and is called at the appropriate times. (54487300)

###### Resolved Issues

- Fixed an issue where issue text may appear light when using a light theme with a dark system appearance. (48230278)

##### Apple Clang Compiler

###### New Features

- Clang now provides a mechanism for controlling exit-time destructor registration. You can disable these globally with the flag `-fno-c++-static-destructors`, or apply the attribute `[[clang::no_destroy]]` to disable the destructors of specific variables. The attribute `[[clang::always_destroy]]` was also added to enable destructors of specific variables when `-fno-c++-static-destructors` is used. (21734598)
- As an extension, C++11 enums with fixed underlying types are now supported in all language modes. (43831380)
- Deprecation warnings will be issued when standard library facilities that were deprecated in the active Standard version are used. (46881474)
- Stack checking is on by default on all platforms to prevent memory corruptions. (25859140)
- The machine code outliner is on by default under `-Oz`. It reduces code size by identifying identical code sequences across functions. Such sequences are encapsulated (“outlined”) in a single compiler generated function. Each original code sequence is replaced with a call to that outlined function. (46385499)
- In order to improve performance and security the static linker (`ld`) now moves globals that are marked as constant into a new segment: `__DATA_CONST`. These globals may consist of compiler generated pointers that the dynamic linker (`dyld`) needs to fix up during load, but are otherwise constant such as vtables and explicitly declared constant pointers. Once `dyld` has finished loading the image it makes `__DATA_CONST` readonly. This change doesn’t impact well behaved code, but may break code that depends on undefined behavior such as using a type pun to write to a pointer that’s declared as `const`. (50898833) ```objc
static int value1 = 0;                  // Stored in __DATA
static int value2 = 0;                  // Stored in __DATA

const int * const valuePtr = &value1;   // Stored in __DATA_CONST

// ERROR: Attempting to store a value to a constant pointer
(int *)valuePtr = &value2;
```
- Clang now supports the C++17 `<filesystem>` library for iOS 13, macOS 10.15, watchOS 6, and tvOS 13. (50988273)

###### Resolved Issues

- The `<experimental/optional>` and `<experimental/variant>` headers are removed. Use `<optional>` and `<variant>` from C++17 instead. (50175894)
- Resolved a long compile-time issue in the loop-invariant code motion pass of the optimizer. (39648918)

##### Asset Catalog

###### New Features

- Xcode can find assets in your workspace/project using the Find navigator. The Asset Catalog Editor also supports Find and Replace, and you can rename assets using Replace. (14279237)
- Assets can now be cut, copied, pasted, and duplicated using the menu or keyboard shortcuts. (27107912)

###### Known Issues

- When an asset is localized in the asset catalog, another localized resource must exist in the corresponding `lproj` directory for the app to use that language at runtime. An empty strings file can serve this purpose. (49565973)

###### Resolved Issues

- Fixed an Asset Catalog bug that prevented named colors from being found at runtime when running on iOS 11. (54325712)

##### Build System

###### New Features

- Xcode uses response files by default to pass input files to the Swift compiler. To turn this behavior off, set `USE_SWIFT_RESPONSE_FILE` to `NO`. (50852028)
- Run script phases and custom build rules may declare and emit a dependencies file, in the Makefile-style `.d` format output used by some compilers and build tools. The build system checks the files listed for changes during subsequent builds when determining if the rule or phase should be executed. (49226986)
- Projects may now use custom build rules by setting the ‘Process Header Files’ (`APPLY_RULES_IN_COPY_HEADERS`) build setting to `YES`. (48185100)
- Custom build rules can now specify additional, static input files that are used during execution. These resolved input file paths are supplied to rule scripts using the `SCRIPT_INPUT_FILE_#` environment variables. (49645853)
- Xcode removes some entries from the `Info.plist` file of a product at build time if the entries are not appropriate for the platform being built for, which is useful for targets which are configured to build for multiple platforms. This behavior can be disabled by setting the build setting `DISABLE_INFOPLIST_PLATFORM_PROCESSING` to `YES`, in which case the target must assume the responsibility of managing these entries appropriately. (47797497)
- Custom build rules can now declare that they should run once per architecture (the default), or run only once across all architectures. This is useful for custom rules which are architecture-neutral, for example, code generation tools that generate files that don’t differ per architecture. (47716990)
- An XCFramework makes it possible to bundle a binary framework or library for multiple platforms —including iOS devices, iOS simulators, and Mac Catalyst — into a single distributable `.xcframework` bundle that your developers can use within their own applications. An `.xcframework` bundle can be added to an Xcode target’s Link Libraries phase and Xcode uses the right platform’s version of the included framework or library at build time. Creation of frameworks is supported from the command line using `xcodebuild -create-xcframework`. Frameworks or libraries bundled in an XCFramework should be built with the Build Libraries for Distribution build setting set to `YES`. (49948269)

###### Known Issues

- Incremental builds to may fail to `codesign` properly for non-source related changes to your project, such as resource file modifications, which can result in the app failing to launch. (41254808)  Change a source file within the same target to trigger the `codesign` process, or perform a clean build.
- Updating your iOS app for Mac Catalyst might show new error diagnostics stating that certain frameworks or functionality is not available on the Mac. If one of these diagnostics is shown erroneously, you can disable it by setting the `VALIDATE_WORKSPACE` build setting to `NO`. (50607174)
- The new build system doesn’t evaluate a leading tilde (`~`) in paths in build settings to the user’s home directory. (41339901)  Use `$(HOME)` instead.
- If a target enables `RUN_CLANG_STATIC_ANALYZER`, then single file processing commands — such as Compile, Preprocess, Show Assembly — won’t work correctly because they generate the static analyzer output file rather than the appropriate output. (43340227)  Disable RUN_CLANG_STATIC_ANALYZER in the target.
- If the build of an app-hosted test target — where `TEST_HOST` is defined — fails, subsequent builds may fail when signing the app product because the test target is incomplete and unsigned when the initial signing of the app occurs. (43402096)  Perform a clean build. Or, manually delete the unsigned test bundle from inside the app target’s product and rebuild.
- Targets which override the Architectures and Valid Architectures build settings for iOS may need to remove or conditionalize the overrides to build correctly for Mac Catalyst. (51074742)
- When using Xcode on macOS 10.15, some files — especially `.xib` files and storyboard files — might be copied rather than compiled, resulting in an incorrect build product. (49351105)  In the File Inspector for the file which is being copied, toggle the Type popup away from Default -  then back to Default. This resets the file type in the project file to the correct type and enables the build system to match it to the correct tool to process it.
- When building for the first time users may get a popup stating that SimulatorTrampoline would like access to Desktop Files because `ibtool` running in simulator needs access to these files to compile storyboards. (51114450)  Allow access to the files in the prompt.

###### Resolved Issues

- By default, Xcode’s new build system doesn’t detect changes in directories declared as inputs to shell script build phases. Enabling the build setting `USE_RECURSIVE_SCRIPT_INPUTS_IN_SCRIPT_PHASES` causes it to do so. However, if any of the files inside such a directory are generated by a task that depends on the output of the script phase, then a dependency cycle error is emitted and must be resolved by restructuring the target. (41126633)

##### Command Line Tools

###### Known Issues

- When using the Command Line Tools as the active Developer directory, some users may experience random crashes in the Swift compiler. (53582696)  Execute the command `sudo rm -f /Library/Developer/CommandLineTools/usr/lib/swift/macosx/libswift*.dylib` in Terminal.

###### Deprecations

- Xcode’s built-in `usdz_converter` tool is deprecated and will be removed. Use the updated tool suite located under Resources in [`Augmented Reality`](https://developer.apple.comhttps://developer.apple.com/augmented-reality/). (52922369)
- Command line support for Subversion will be removed in a future release. (50195246, 50231958, 50266910, 51740851, 52528748)

##### Core Data

###### New Features

- There is now a checkbox that makes it possible for you to distinguish whether the default value of a string attribute should be `nil` or the empty string. When set, the default value is the empty string if no other default is specified. (26534406)
- The Xcode 11 data model file format no longer writes out or preserves deprecated Sync Services information for entities or properties. (32524648)
- The Core Data data model editor has added support for derived attributes when using the Xcode 11 data model file format and an appropriate deployment target. (45567066)
- When creating an application using Core Data, there is a new checkbox to also enable CloudKit support for the data model’s default configuration. This can also be enabled for an existing data model using the new configuration inspector. When a data model configuration supports CloudKit, the data model editor performs additional validation to ensure the model conforms to the requirements for Core Data CloudKit support. (51126024)

###### Resolved Issues

- Using the UUID attribute type, the URI attribute type, or the persistent history feature properly generates an error when used with a data model file format prior to the format used in Xcode 9. (50188371)

##### Create Ml

###### New Features

- You can now classify sounds live directly from the microphone using Sound Classification preview. (52131594)
- A Tabular Regressor template is now available, joining Image Classification, Sound Classification, Activity Classification, Tabular Classification, Word Tagger and Text Classification. (54005628)

###### Known Issues

- Apps importing the Create ML framework may not launch if they are compiled by Xcode 11. This doesn’t impact existing apps. (53795065)  Add the file `libswiftCreateML.tbd` in the ‘Link Library with Libraries’ section.

###### Resolved Issues

- Non-ASCII characters can be used as training labels for Image Classification and Sound Classification. (53594243)

##### Debugging

###### New Features

- The view debugger now shows the names of [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) instances in the inspector. (35516797)
- The graphical filter in the Size inspector for debugging view hierarchies identifies which attributes on the selected view are constrained. Selecting attributes in the filter narrows the displayed constraints to ones matching that attribute. Standard modifier keys such as Shift and Command can be used to expand the selection showing the union of constraints matching those attributes. (44864394)
- You can now debug the view hierarchies of watchOS apps. (45173634)
- You can now simulate network conditions and thermal states for a connected device from the Devices and Simulators window. (44608479)
- The view debugger shows [`UIWindowScene`](https://developer.apple.com/documentation/UIKit/UIWindowScene) instances in the debug navigator and canvas. (45378799)
- View debugging can be disabled in the scheme options. (45928299)
- The Size inspector for debugging view hierarchies has more details about constraints including a filter, hover highlighting in the editor, and better descriptions. (16153188)
- The view debugger supports debugging Mac Catalyst apps. (37507479)
- The view debugger inspector shows [`contentTintColor`](https://developer.apple.com/documentation/AppKit/NSButton/contentTintColor) for [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView) and [`NSButton`](https://developer.apple.com/documentation/AppKit/NSButton). (49506123)
- The view debugger now shows the names of iOS named and system colors. (45162028)
- The view debugger shows trait collection information. (45161975)
- The view debugger shows the names of [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) instances. (45327089)
- The view debugger now shows symbol information, like baseline and midline. (49508874)
- The debug bar appearance switcher supports changing between dark and light modes on iOS. (45161907)
- The “Pause on issues” checkboxes in the Diagnostics tab of the Scheme Editor are replaced by regular breakpoints. You can use the Breakpoints Navigator to create a Runtime Issue Breakpoint. (31409112)
- Override system settings like appearance, dynamic type, and accessibility options for the debugged process using Environment Overrides, accessible from the debug bar. (45848655)
- The debugger supports working with crash logs (`.crash` files). (48408310)
- The debugger can debug tvOS Top Shelf extensions. (48869701)
- Xcode can prefer using Wi-Fi to connect to a Watch when installing or debugging an app. (50313856) > **Note**: The iPhone-Watch pair must be on the same 2.4 GHz network. Networks that block peer-to-peer connections cannot be used.
- The VoiceOver actions menu for breakpoints includes an action to jump to the corresponding line of code. (44941178)
- When debugging views with constraints, double clicking a constraint in the size inspector selects that constraint in the editor and show information for the constraint in the inspector. (18842905)
- LLDB’s Python scripting is now based on Python 3. If you are using Python extensions that aren’t compatible with Python 3, they will break. To help with the transition, you can run in Python 2 mode by setting a default: ```shell
defaults write com.apple.dt.lldb DefaultPythonVersion 2
``` Python 2 support will be removed in the future. (47806994)
- Swift [`Decimal`](https://developer.apple.com/documentation/Foundation/Decimal) values have a data formatter in LLDB, making them display in a readable way. (38983073)

###### Known Issues

- Console output for Previews is only shown when debugging Live Previews in the Simulator. (49891045)
- In watchOS 6, an `apns-push-type` key is required in the APNs request header. Specify `alert` or `background` for the type of notification being sent. The template APNs files in Xcode don’t contain this header by default. (50709418)
- Debugging symbols might be unavailable for Apple Watch. (26995636)  Verify that you have a working internet connection and that you’re signed into your Apple ID in Preferences > Accounts.
- Debugging a watch app in a watchOS simulator might fail the first time the simulator boots. (50263836)  Wait until the watch simulator finishes booting, then start debugging it again.

###### Resolved Issues

- Fixed an Xcode crash on macOS 10.15 when dragging the process item in the Debug Navigator. (48453949)
- Items in the view debugger can be revealed in the Debug navigator from the context menu. (18598643)
- Improved the formatting of Swift class names when debugging the view hierarchy. (39679411)
- Fixed an issue where the debug console would display a page column guide. (49693398)
- Breakpoints support the VoiceOver command to open the shortcut menu. (44940944)
- Redeclaring `self` in Swift code works properly with LLDB. (39611934)
- The Swift REPL and LLDB’s python scripting work properly when the python binary in `PATH` isn’t the system one. (40961425)
- Resolved an issue that prevented running a Watch App that has the ‘Supports Running Without iOS App Installation’ setting on a pre-watchOS 6.0 device or simulator. (54104164)

##### Deprecations

- The WatchKit framework is no longer included in the iOS SDK. If you’re using WatchKit APIs from iOS, you need to remove this use. The WatchKit framework remains available on watchOS. If you’re using WatchKit APIs from iOS to infer availability of features on the paired Apple Watch, include information about your use case when you submit feedback to [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com). (49707950)
- Scripting language runtimes such as Python, Ruby, and Perl are included in macOS for compatibility with legacy software. In future versions of macOS, scripting language runtimes won’t be available by default, and may require you to install an additional package. If your software depends on scripting languages, it’s recommended that you bundle the runtime within the app. (49764202)
- Use of Python 2.7 isn’t recommended. This version is included in macOS for compatibility with legacy software. Future versions of macOS won’t include Python 2.7. Instead, it’s recommended that you run `python3` in Terminal. (51097165)
- Starting in macOS 10.15, the Quartz Composer framework is marked as deprecated, but remains present for compatibility purposes. Transition to frameworks such as Core Image, SceneKit, or Metal if your app is using Quartz Composer. (50911608)

##### Devices

###### Resolved Issues

- Resolved an issue that prevented running a watch app built with the thread sanitizer enabled on older versions of watchOS. (49288795)

##### Instruments

###### New Features

- Tracks in Instruments can now be formed in hierarchies. They can now represent any engineering type and are created using Custom Instruments. (28615789)
- Instruments now allows for copying multiple rows from a table at one time. (39326522)
- Instruments allows for creating scopes for easier navigation within the trace document. (49022012)
- `<os-signpost-point-schema>` is available in the Custom Instruments to match point events coming from [`os_signpost(_:dso:log:name:signpostID:)`](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostID:)-2oz8u). (50586708)

###### Known Issues

- When profiling a standalone watchOS app, an iOS simulator is launched. (49788679)

##### Interface Builder

###### New Features

- Interface Builder supports iOS 13 [`UIVisualEffectView`](https://developer.apple.com/documentation/UIKit/UIVisualEffectView) blur and vibrancy visual effects. (48023286)
- Interface Builder supports iOS 13 [`UIActivityIndicatorView`](https://developer.apple.com/documentation/UIKit/UIActivityIndicatorView) styles. (48573772)
- The iOS home indicator color now adapts to light and dark canvas appearances. (48610782)
- Interface Builder supports customizing [`UIButton`](https://developer.apple.com/documentation/UIKit/UIButton) symbol configurations. (51323174)
- Interface Builder supports the new layout [`TVCollectionViewFullScreenLayout`](https://developer.apple.com/documentation/TVUIKit/TVCollectionViewFullScreenLayout) on Apple TV. (47598895)
- [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) instances now default to the Automatic modal presentation mode. Modal presentation segues can override this setting. (48129590)
- Interface Builder supports Dark Mode on iOS. (45314199)
- Interface Builder’s device bar lets you switch between the light and dark appearance for iOS apps. (45282451)
- You can add SwiftUI hosting controllers, such as [`UIHostingController`](https://developer.apple.com/documentation/SwiftUI/UIHostingController), to connect a storyboard controller flow to a hosting controller that manages a SwiftUI view hierarchy. You can populate the contents of a hosting controller in Interface Builder by providing a custom subclass that programmatically sets the [`rootView`](https://developer.apple.com/documentation/SwiftUI/UIHostingController/rootView) of the controller. (46039344) You can also set the root view of a [`UIHostingController`](https://developer.apple.com/documentation/SwiftUI/UIHostingController) or [`NSHostingController`](https://developer.apple.com/documentation/SwiftUI/NSHostingController) using a Segue Action.
- The object library now matches the selected system-wide appearance. (50874168)
- The [`NSStackView`](https://developer.apple.com/documentation/AppKit/NSStackView) inspector now allows configuring negative spacing. (49012055)
- [`NSSwitch`](https://developer.apple.com/documentation/AppKit/NSSwitch) is available when running on macOS 10.15. (47566686)
- Cells in a [`UITableView`](https://developer.apple.com/documentation/UIKit/UITableView) can now self size with Auto Layout constrained views in the canvas. To opt into the behavior for existing table views, enable “Automatic” for the table view estimated item size, and “Automatic” for cell’s height in the Size inspector. (35735970)
- [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) and [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) have a layout mode option in the Size inspector to explicitly opt into “translates autoresizing mask into constraints”. The default setting is “Automatic”, which is the existing behavior. “Automatic” implies that “translate autoresizing mask into constraints” is  when a view affect by constraints in the storyboard or `.xib` file, but  if unconstrained. (37352354)
- Improved the reliability of Auto Layout constraint generation with “Add Missing Constraints”. (43694622)
- The contents of a [`UIScrollView`](https://developer.apple.com/documentation/UIKit/UIScrollView) are scrollable within the canvas, once its subviews are fully constrained with Auto Layout constraints. (44727961)
- Cells in a [`UICollectionView`](https://developer.apple.com/documentation/UIKit/UICollectionView) can now self size with Auto Layout constrained views in the canvas. To opt into the behavior for existing collection views, enable “Automatic” for the collection view’s estimated size, and “Automatic” for cell’s size from the Size inspector. If deploying before iOS 13, you can activate self sizing collection view cells by calling [`performBatchUpdates(_:completion:)`](https://developer.apple.com/documentation/UIKit/UICollectionView/performBatchUpdates(_:completion:)) during [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()). (45617083)
- In inspector font popovers, the Family popup now renders menu items as a preview of the applicable font. (31484154)
- Update Frames can now be performed document-wide for misplaced frames, without selecting a view. (22076710)
- Content and Frame Layout guides are supported for [`UIScrollView`](https://developer.apple.com/documentation/UIKit/UIScrollView) and can be enabled in the Size inspector for more control over your scrollable content. (29711618)
- Interface Builder supports the new Apple TV tab bar style. (47598643)
- The new [`WKInterfaceTextField`](https://developer.apple.com/documentation/WatchKit/WKInterfaceTextField) interface element is available for watchOS. (45754186)
- The canvas supports customizing interfaces for Mac Catalyst apps. (37797710)
- SF Symbols are available in image inspector properties. (47532055)
- The [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView) inspector includes support for configuring symbols. (47797500)
- A view controller method annotated with the new `@IBSegueAction` attribute can be used to create a segue’s destination view controller in code, using a custom initializer with any required values. This makes it possible to use view controllers with non-optional initialization requirements in storyboards. Create a connection from a segue to an `@IBSegueAction` method on its source view controller. On new OS versions that support Segue Actions, that method will be called and the value it returns will be the `destinationViewController` of the segue object passed to [`prepare(for:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/prepare(for:sender:)). Multiple `@IBSegueAction` methods may be defined on a single source view controller, which can alleviate the need to check segue identifier strings in [`prepare(for:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/prepare(for:sender:)). (47091566) An `IBSegueAction` method takes up to three parameters: a coder, the sender, and the segue’s identifier. The first parameter is required, and the other parameters can be omitted from your method’s signature if desired. The [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) must be passed through to the destination view controller’s initializer, to ensure it’s customized with values configured in storyboard. The method returns a view controller that matches the destination controller type defined in the storyboard, or nil to cause a destination controller to be initialized with the standard init(coder:) method. If you know you don’t need to return `nil`, the return type can be non-optional. In Swift, add the `@IBSegueAction` attribute: ```swift
@IBSegueAction
func makeDogController(coder: NSCoder, sender: Any?, segueIdentifier: String?)
-> ViewController? {

  PetController(
      coder: coder,
      petName: self.selectedPetName,
      type: .dog
  )
}
``` In Objective-C, add `IBSegueAction` in front of the return type: ```objc
- (IBSegueAction ViewController *)makeDogController:(NSCoder *)coder
             sender:(id)sender
    segueIdentifier:(NSString *)segueIdentifier
{
 return [PetController initWithCoder:coder
                             petName:self.selectedPetName
                                type:@"dog"];
}
```

###### Known Issues

- A Segue Action on a relationship segue between a NSWindowController and a View Controller is currently not supported and ignored. (48252727)
- Older IB3 documents strings won’t be extracted during localization export, and won’t be included in the XLIFF. (47650747)
- When viewing an iPad storyboard with the Mac device selected in the device bar, custom fonts added by the project don’t render. (48528374)
- If a glyph has a light and dark mode representation, the dark mode representation won’t be picked up in the storyboard. (50354204)
- UIKit menus configured in Interface Builder are available at runtime on macOS, but not on iOS. (51077651)
- The iOS status bar is not displayed in the Interface Builder canvas. (48639919)
- There is an issue with [`UITabBarController`](https://developer.apple.com/documentation/UIKit/UITabBarController) where decoding an instance from a storyboard will create some extra views at the left end of the screen. Developers may remove these by applying a workaround. (55310448) : To remove the extraneous views from Storyboard, create a subclass of a [`UITabBarController`](https://developer.apple.com/documentation/UIKit/UITabBarController) and add the following snippet in the class’s [`init(coder:)`](https://developer.apple.com/documentation/UIKit/UIViewController/init(coder:)) method: ```swift
class WorkaroundTabBarController: UITabBarController {
  required init?(coder: NSCoder) {
      super.init(coder: coder)

      // This must be run immediately after the call to super.
      if (tabBar.subviews.count > 1) {
          tabBar.subviews[0].isHidden = true
      }
  }
}
```

##### Resolved Issues

- Connect-to-source popover fields support cut, copy, paste, and select all. (40899355)
- Corrected the alignment of [`UILabel`](https://developer.apple.com/documentation/UIKit/UILabel), [`UITextField`](https://developer.apple.com/documentation/UIKit/UITextField), and [`UITextView`](https://developer.apple.com/documentation/UIKit/UITextView) instances with alignment set to “center” or “right” in Interface Builder when designing for or running on macOS. (50062524)
- The inspector for [`UIDatePicker`](https://developer.apple.com/documentation/UIKit/UIDatePicker) now shows only the properties applicable to the selected mode. (26726319)
- The preview editor’s menu for adding iOS devices now matches the current canvas orientation. (48818470)
- Preview editor items now preserve the configured locale or pseudo-locale. (48303753)
- [`UIDatePicker`](https://developer.apple.com/documentation/UIKit/UIDatePicker) objects configured as Count Down in Interface Builder now use the specified duration at runtime. (23426425)
- The Embed In bar button is also visible in documents not using Auto Layout. (46855203)
- Subclasses of [`NSControl`](https://developer.apple.com/documentation/AppKit/NSControl) now have unique icons in the library and document outline. (24231920)
- Fixed an issue where system colors in XIB files set to deploy before iOS 13.0 wouldn’t adapt to the system appearance at runtime. (54362252)

##### Localization

###### New Features

- You can now localize assets in asset catalogs. Localization is enabled in the attribute inspector. (12948139)
- The settings bundle is now included in Xcode Localization Catalogs. (12495197)
- The manual page for `genstrings` documents its behavior in more detail. (19709369)
- The `genstrings` tool is enhanced and merged with the `extractLocStrings` tool. The previous version is deprecated, has been renamed to `ogenstrings`, and must now be invoked with `xcrun`. Any scripts that invoked `xcrun extractLocStrings` should be changed to use `genstrings`, but a compatibility symbolic link is currently provided that invokes `genstrings`. (19709395)
- The `genstrings` tool now takes an `-encoding` argument that allows specification of the file encoding for input files. (48224455)
- The updated version of `genstrings` has improved error reporting, and may report errors in scenarios that were previously silently accepted. As an example, `genstrings MyApp/*` will fail if the MyApp directory contains a subdirectory, because `genstrings` file arguments are required to be source files. (48304658)
- The `genstrings` tool can now take any number of `-s` arguments to specify additional macros similar to [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) or functions from which to extract strings. For example, `genstrings -s MyErrorSring -s MyUIString myfile.swift` treats both `MyErrorString` and `MyUIString` as equivalent to [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString). (48734596) > **Note**: Using `-s` arguments doesn’t suppress support for `NSLocalizedString` or `CFCopyLocalizedString`.
- The Export for Localization command and `genstrings` tool now support multiline Swift and Objective-C strings, and have relaxed whitespace requirements when recognizing arguments to `NSLocalizedString`. (50516442)
- The performance of the Export for Localization command is substantially improved. (40548416)

###### Resolved Issues

- The Export for Localization command and `genstrings` tool no longer crash on escaped, high Unicode code points such as `\U0001F603`. (18898240)
- Importing a localized string that contains embedded newlines now produces strings files with escaped `\n` sequences. (44649979)
- XLIFF files produced by Xcode localization export now add `xml:space="preserve"` to `<trans-unit />` elements to ensure that whitespace is preserved. (44928807)

##### Organizer

###### New Features

- The new [`Metrics organizer`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devb642b28ac) shows battery life and performance analytics for your app to help you drive optimizations. Metrics are reported for your app when distributed on the App Store and after sufficient field use. The available metrics are battery drain, launch time, hang rate, memory, and disk writes. You can filter data by device and usage characteristics. (43028903)

##### Playgrounds

###### New Features

- SwiftUI live views and inline results in playgrounds are supported. (42226387)

###### Known Issues

- Playgrounds in a workspace can’t import targets from a Swift package. (47668990)

###### Resolved Issues

- Playgrounds no longer crash if your code references a view off of the main thread. (46579594)

##### Project Navigator

###### New Features

- Xcode can find assets in your workspace or project using the Find navigator. The Asset catalog Editor also supports find and replace, and you can rename assets using Replace. (14279237)

##### Reality Composer

###### New Features

- Added support for object anchors in AR scenes. (48774003)

###### Known Issues

- A new project that contains a USDz file and was never manually saved will have missing USDz objects when opened after an autosave. (53565602)  Manually save and re-open the project.
- The [`RealityKit`](https://developer.apple.com/documentation/RealityKit) [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) class isn’t found at runtime when loading a storyboard if its module isn’t specified in Interface Builder. The following error message displays in the Xcode console: “Unknown class ARView in Interface Builder file.” (50840767)  [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) is a Swift view class, and requires both its class name ([`ARView`](https://developer.apple.com/documentation/RealityKit/ARView)) and module ([`RealityKit`](https://developer.apple.com/documentation/RealityKit)) to be specified in the Interface Builder inspector.
- RealityKit’s [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) class is not found at runtime when loading a storyboard if RealityKit isn’t otherwise used within the Xcode project. The following error message displays in the Xcode console: “Unknown class _TtC10RealityKit6ARView in Interface Builder file.” (50900969)  This issue occurs if you import RealityKit and define an `@IBOutlet` with a type of [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView), but don’t otherwise use RealityKit symbols in your project. To ensure that RealityKit is loaded at runtime with this configuration, manually add RealityKit to your target’s Link Binary with Libraries build phase.
- The Rename menu item isn’t enabled when scene, object, or behavior is selected. (54274819) : You can rename scenes and objects using the Name field in the Properties inspector. You can rename behaviors by right-clicking the behavior and selecting Rename from the contextual menu.

###### Resolved Issues

- Notification triggers and notify actions from other scenes no longer appear in scenes in which they weren’t authored. (51008577)

##### Server

###### New Features

- Xcode Server now supports Mac Catalyst apps. (50602873)

###### Known Issues

- When editing bots for a project that authenticates with SSH, Xcode Server may disable some project-specific settings. (51009722)  Either replace repositories in the Repositories tab when editing the bot or use HTTPS-based authentication with your Xcode Server integrations.
- Xcode Server can cause a crash when a bot is created from the context menu of any integration. (51082255)  Create bots from the context menu of the server or from the Product menu in Xcode.
- Build issues occurring in a source file built by multiple targets may be marked resolved and reintroduced on every integration. (46523551)

###### Resolved Issues

- Resolved an issue where Xcode Server failed to automatically sign projects that use the iCloud, Application Groups, Apple Pay, or Wallet capabilities. (41008156, 44704694)

##### Signing and Distribution

###### New Features

- Signing and capabilities settings are now combined within a new Signing & Capabilities tab in the Project Editor. The new tab enables using different app capabilities across multiple build configurations. The new capabilities library makes it possible to search for available capabilities. (35254597)
- Xcode 11 supports the new Apple Development and Apple Distribution certificate types. These certificates support building, running, and distributing apps on any Apple platform. Preexisting iOS and macOS development and distribution certificates continue to work, however, new certificates you create in Xcode 11 use the new types. Previous versions of Xcode don’t support these certificates. (45527608)

###### Known Issues

- If your iPad app uses private entitlements, those entitlements may not be available for use in your Mac Catalyst app. (51599125)  Generate a new entitlements file for your Mac Catalyst app and exclude the unavailable entitlements by following these steps:  Select your entitlements file in the project navigator then select File > Duplicate.  Give your Mac Catalyst entitlements file a unique name and save it.  Remove any unavailable private entitlements from your new Mac Catalyst entitlements file.  Navigate to your Mac Catalyst app’s build settings in the project editor and locate the Code Signing Entitlements build setting.  Expand the build setting so that you can view its value for all build configurations. For each of your build configurations, click the plus (+) button to add a conditional setting.  From the popup button in each conditional setting, select Any macOS, then edit the conditional setting’s value to refer to the name of your new Mac Catalyst entitlements file.
- The archive action does not code sign command-line executable products from Swift packages. (48717735)  Manually sign archived executables using the `codesign` tool before distributing them.
- Mac provisioning profiles that you have manually installed using the bot editor’s Signing tab will be installed using the wrong file extension, causing integrations to fail. (47636041)  Sign into your bot user’s account and rename the affected profiles in the `~/Library/MobileDevice/Provisioning Profiles` directory.

###### Resolved Issues

- Resolved an issue where Xcode incorrectly reported: “No iTunes Connect access for the team” when uploading to the App Store. (39292849)

##### Simulator

###### New Features

- Simulator can automatically select the macOS GPU based on the current power source. When your Mac is connected to AC power the discrete GPU is used. When your Mac is running on battery power the integrated GPU is used. You can change the policy in Simulator by navigating to File > GPU Selection. (53032365)
- `simctl` can now override status bar values for iOS devices. For example, to set the time and battery, use: ```shell
xcrun simctl status_bar <device> override --time "9:41" --batteryState charged --batteryLevel 100
``` See `xcrun simctl help status_bar` for the full range of options. (51697821)
- Metal is available in iOS 13 and tvOS 13 simulators when running on macOS 10.15. Metal code is executed on the host Mac GPU, and is significantly faster than simulated OpenGL code. (System APIs in watchOS 6.0 simulators are also GPU accelerated.) The APIs in SceneKit, CoreAnimation, and other system frameworks abstract many differences between GPUs, reducing the need for device-specific code. When running on earlier versions of macOS or in an environment where Metal is not available, simulators continue to use software rendered OpenGL. If your Mac has multiple GPUs, use the File menu in Simulator to select which GPU to use. If the GPU in use becomes unavailable, any simulators using it automatically shut down. (18430676)
- Xcode no longer creates every available iOS simulator device by default. Instead a set of the most commonly used devices are created. To create other devices — or multiple instances of a device — open the Devices window, select Simulators, click the  button, enter a name, and select the relevant device type and OS version. In Terminal, execute the `xcrun simctl create <name> <device type> <OS version>` command, for example `xcrun simctl create "My iPhone 7" "iPhone 7" iOS13.0`. (49428617)
- [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) is available in iOS 13 and tvOS 13 simulators. (45101325)
- iOS 13, watchOS 6, and tvOS 13 simulators now have a `dyld` shared cache. This improves simulator launch times and reduces the number of open file handles used by simulator processes. If you report an issue you believe is related to the shared cache, include a `simctl diagnose` and the output of launching your program with `DYLD_PRINT_LIBRARIES=1`. (13632739) > **Note**: A missing symbol crash may now mention the shared cache but this is not a shared cache bug. The message is merely informing you that the shared cache was consulted when searching for the symbol.
- `simctl` now accepts short aliases for runtime names. This means you can create a new iPhone X simulator with a command like `simctl create 'iPhone X' iOS13`. (41089607)
- For headless and continuous integration scenarios, you can configure CoreSimulator to skip compositing operations in the virtual frame buffer by setting `defaults write com.apple.CoreSimulator FramebufferServerRendererPolicy` to `none`. In this mode simulators can’t be viewed and `simctl io` is unable to take screenshots or record videos. (48264341)
- Bundles without a [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion) are invalid and can’t be properly installed on devices or simulators. CoreSimulator now checks and rejects such bundles earlier in the process with a clearer error message. (49892531)
- The Simulator dock icon now includes a menu to quickly boot a simulator. (43067512)
- Simulator’s File menu now includes a GPU selection menu to control which GPU is used by Metal support in simulators and for compositing by Simulator’s virtual frame buffer. If the Use External GPU When Available item is checked, any simulators booted after an external GPU is connected use the external GPU. If the external GPU is disconnected, any simulators using it automatically shut down. Changes to these settings only take effect when a simulator is booted. Simulators already booted when this setting is changed continue using the previously selected GPU until they’re restarted. (46134036)
- iOS 13 simulators now strictly simulate edge gestures. To perform an edge swipe in a simulator turn on bezel mode and begin your gesture in the bezel area. (55052127)

###### Known Issues

- Simulator doesn’t distribute the load if multiple GPUs in a system match the chosen GPU policy. Only the first matching GPU, as returned by [`MTLCopyAllDevices()`](https://developer.apple.com/documentation/Metal/MTLCopyAllDevices()), is used. (50608554)  You may see higher performance by locating the simulator window on the display directly connected to the GPU the simulator is using, which avoids copying across GPUs. > **Note**: As with any app that leverages the GPU, the performance behavior for an externally connected display varies depending on workload.
- Video recording of the iOS 13, tvOS 13, and watchOS 6 simulator through `xcrun simctl io `` recordVideo` returns an error instead of recording video. (50625716)
- watchOS simulators don’t honor a breakpoint on a cold boot. (51148192)  Completely boot the simulator before launching the app you’re debugging.
- iCould Drive isn’t supported in iOS 13.0 and earlier simulator runtimes when running on macOS Catalina 10.15. Logging into iCloud on impacted simulators will result in `bird` terminating and relaunching in a cycle. (51392951) : Log out of iCloud in impacted simulators to halt the crash cycle.
- Simulated devices running iOS 13 may fail to enable an external display or CarPlay display, instead displaying a black window. (53966664) : Close the window and try again. If that fails restart the affected simulator.
- When running UI tests in a simulated device on a macOS host with slow hardware the test runner process may get killed by the CPU watchdog. (54136015) : Free up resources so the simulated device has faster I/O. You can also extend the watchdog timeouts by setting a user default in the relevant simulator. Boot the simulator, then run: ```shell
xcrun simctl spawn <device> defaults write com.apple.springboard FBLaunchWatchdogScale
``` This must be set on each simulator. Erasing a simulator will reset this setting.
- Attempting to create an MIDINetworkSession in a simulated device running iOS 13 won’t succeed. (54484923)
- CarPlay does not work in iOS 13 simulators. (54492162)

###### Resolved Issues

- Simulator correctly displays the checkmark for Touch ID > Enrolled when it’s enrolled. (50553667)
- Automatic synchronization of pasteboards between a host and simulated devices behaves correctly. (46686100)
- [`IOSurface`](https://developer.apple.com/documentation/IOSurface/IOSurface) is now functional in iOS 13, watchOS 6, and tvOS 13 simulators. (11051639)
- Apps in a simulator that plays audio no longer automatically also open the microphone for input. (32406954)
- The previously deprecated `availability` field in `simctl` list’s JSON output is removed. Use the `isAvailable` Boolean field to determine availability. (45142676)
- Fixed an issue that could cause Simulator to crash or become unresponsive following clipboard-related actions in other applications if automatic pasteboard synchronization is enabled. (54011137)
- Changing the audio in a simulated device while a video is playing in Safari won’t mute the audio of the video. (51207286)

##### Source Control

###### New Features

- You can now cherry-pick changes from one branch to another. (18285039)
- When cloning a new repository, you can now select the branch to check out from the list of available branches. (41122122)
- Using the new source control file inspector, you can browse the full history of a file for the current branch. The log inspector is available for all file types, including Interface Builder documents. (45109443)
- You can now stash changes and manage stashes from the source control navigator. Additionally, Xcode offers to automatically stash and restore changes for source control operations like pulling from a repository. (8797804)
- Source control authors are now available on a per-editor basis. (45108927)

###### Known Issues

- When performing a Pull in Xcode on a branch that’s already up to date when rebase is enabled, the sheet doesn’t dismiss automatically. (50377240)
- Viewing the changes for a revision of a file from the source control log inspector may fail if that file has since been renamed. (49673170)
- Filtering packages in the Add Package assistant isn’t supported for Bitbucket Cloud or Bitbucket Server hosted accounts. (47290085)
- Filtering packages in the Add Package assistant isn’t supported for GitLab or GitLab Self-Managed hosted accounts. (47290125)
- When using `xcodebuild`, resolving packages may fail to verify SSH fingerprints unless that fingerprint is already in the `~/.ssh/known_hosts` file. (50686014)  SSH into the host and verify the fingerprint from the command line before using `xcodebuild`, or manually add the host fingerprint to the `~/.ssh/known_hosts` file.

###### Resolved Issues

- Source control status in the file navigator will reflect the same information as `git status` from the terminal. (14986450)
- Pulling with rebase no longer fails if author information isn’t yet configured for Git in Preferences > Source Control. (48680076)
- Resolved issues where hosted account providers like GitHub and BitBucket were unavailable in the add account sheet, and previously added accounts would be disabled. (47645098)
- Addresses an issue where source control operations in Xcode presented a “Couldn’t communicate with helper application” dialog. (47227781)
- Fixes a performance issue where Personal, organizational and Starred repositories took a long time to load. (48620126)
- Fixes a bug where some source editor menu options were unavailable in the Code Review Editor. (48774008)

##### Source Editor

###### New Features

- Semantic highlighting, code completion, live issues, symbol search, and jump-to-definition are now supported for the Metal shading language. (45144204)
- Introduces the ability to view inline code diffs for changes in the Source Editor by clicking on the Source Control Change Bar and choosing Show or Hide Change. (49073551)
- Added new High Contrast (Dark) theme and High Contrast (Light) theme. Also added new settings for Marks, Type Declarations and Other Declarations. (50036007)
- Added dedicated syntax coloring for declarations in Swift files, which can be customized in Preferences > Fonts & Colors under Type Declarations and Other Declarations. Declaration coloring for C-family languages isn’t supported. (10342935)
- Xcode’s source editor now supports spell checking. (32062963)
- Xcode 11’s source editor introduces a mini-map of the file. The mini-map includes legible text for `Mark:`, highlighted lines with errors and warnings, source control changes, breakpoints, and highlighted Find results. The mini-map is enabled by default and can be turned off per editor. (35939517, 46064742, 46064809, 46064921, 46064981, 47127500, 47208960, 47516881)
- Added syntax highlighting for markup in documentation comments and playground markup. You can customize the prose font in Preferences > Fonts & Colors under Documentation Markup, and customize delimiter appearance in Preferences > Text Editing > Display. (42941263)
- Toggle Comments supports multiple cursors. (44319433)
- When dragging and dropping text, space is opened up between lines to make it easier to see where text will be dropped. When dragging full lines, Xcode only allows drops to occur between other lines. (44735912)
- The editor allows hierarchical code folding. (47502128)
- Code folding supports square brackets, and parentheses. (50460404)
- `// MARK:` comments and `#pragma mark` directives now draw a separator line in the editor. The preference for showing mark separators is in Preferences > Text Editing > Display > Show Mark Separators. (7299224)
- Added options to control the indentation of case labels inside switch statements. This can be controlled separately for Swift and C-family languages under Preferences -> Text Editing -> Indentation. (9441571)
- Added an option for controlling indentation inside the C++ namespace and external C blocks in Preferences > Text Editing > Indentation. (20700010)
- Pasted text is no longer re-indented by default, though the initial whitespace is adjusted to match the surrounding text. This can be controlled with Preferences > Text Editing > Indentation. (16047992)
- Added support for syntax coloring YAML files. (19942196)

###### Resolved Issues

- [`NSProgressIndicator`](https://developer.apple.com/documentation/AppKit/NSProgressIndicator) objects now preserve the current value configured in the inspector when built and run. (43257511)
- Resolved an issue where Xcode erroneously opened an assistant editor when you ran Fix All Issues using a keyboard shortcut. (37995114)
- Added dedicated syntax coloring for `// MARK: `comments and `#pragma mark` directives, which you can customize in Preferences > Fonts & Colors > Mark. (22114159)
- You can command-click on Swift operators to use Quick Help and Jump to Definition. (32695862)
- Resolved an issue that could occur when editing an unclosed block in Objective-C. (48201424)
- Resolved an issue where code completion sorted deprecated symbols ahead of their nondeprecated counterparts. (38422586)
- Resolved an issue where code completion rows appeared empty when deleting text. (48621410)
- Resolved an issue where C++ functions weren’t parsed correctly when using `throw` or `noexcept` clauses. (37682611)
- Accessibility Zoom focus now follows the insertion point in the source editor while typing. (32775118)
- VoiceOver doesn’t repeat the previous line when moving by line in the source editor. (34334763)
- VoiceOver has rotors in the source editor for methods, errors, warnings, breakpoints, and marks which makes it easy to search for and move to the line of code corresponding to an error or other rotor item. (34493080)
- VoiceOver text attributes now include the number of spaces, number of tabs, indent level and line number for a line of code in the source editor. (34607795)
- VoiceOver no longer speaks extra characters around placeholder tokens when reading in the source editor, and says that they are placeholders. (44941610)
- Resolved an issue where C++ raw strings didn’t highlight correctly. (10770485)
- Resolved an issue of issues where C++ class declarations didn’t parse correctly when using qualified names, templates, or multiple inheritance. (11286215)
- Resolved an issue where local classes nested inside functions or methods weren’t shown in the jump bar. (13337638)
- Resolved an issue where C++11 trailing return types weren’t properly recognized. (13634062)
- Resolved an issue where C++ typed enums were not parsed correctly. (13693443)
- Improved the parsing of declarations that use availability macros and attributes. (14569168)
- Resolved an issue where C++ numeric literals with single quotes were not recognized. (18121031)
- Resolved an issue where struct member functions were not parsed correctly. (27946356)
- Resolved an issue where enum declarations were not displayed in the Jump Bar correctly. (32518576)
- Improved the recognition of classes and functions in JavaScript. (42537831)
- Resolved an issue where functions returning enum types were not parsed correctly. (46164630)
- Resolved an issue where unsigned and long integer literals were not syntax colored correctly. (47138177)
- Updated JavaScript syntax highlighting to include ECMAScript 6 keywords. (47354463)
- Fixed an issue where double clicking on a C++ destructor name would also select the tilde (`~`). (6368356)
- Makefiles are now correctly recognized, and are always indented using tab characters. (16975247)
- Fixed an issue where changing a file’s tab width would not update the display. (52026893)
- When full lines are selected, typing a delimiter now places the delimiters on separate lines, shifting the selection to the right. (52077437)
- Fixed a problem where double-clicking text containing words separated by periods in comments would select too much. (11541526)
- Double-clicking the quotes of a Swift string containing interpolations now selects the whole string. (24470374)
- Improved the recognition of functions in shell script files. (52478049)
- Improved performance and correctness when parsing XML and HTML files. (50672550)
- Improved the syntax coloring for `man` page files. (52035097)

##### Static Analyzer

###### New Features

- The static analyzer checks for violations of the MIG calling convention in mach server routines. These violations can lead to use-after-free vulnerabilities. (35380337)
- The static analyzer checks for violations of IOKit and libkern reference counting rules with respect to out-parameters. (46357478)
- The static analyzer checks for violations of DriverKit reference counting rules. These violations can lead to leaks and use-after-free issues. (50349513)

##### Swift

###### New Features

- The `@frozen` attribute for structures and enumerations is now available. ([`SE-0260`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0260-library-evolution.md), 36597490)
- The memberwise initializer for structures now provides default values for variables that hold default expressions. ([`SE-0242`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0242-default-values-memberwise.md), 47130624) ```swift
struct Dog {
    var name = "Generic dog name"
    var age = 0

    // The synthesized memberwise initializer
    init(name: String = "Generic dog name", age: Int = 0)
}

let sparky = Dog(name: "Sparky") // Dog(name: "Sparky", age: 0)
```
- An `@autoclosure` parameter can now be declared using a type alias. ([`SR-2688`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-2688), 50560849) ```swift
class Foo {
    typealias FooClosure = () -> String

    func fooFunction(closure: @autoclosure FooClosure) {}
}
```
- Methods declared using the `@objc` attribute inside a class can now return `Self`. ([`SR-7601`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-7601), 50560991) ```swift
class MyClass: NSObject {
    @objc func clone() -> Self { return self }
}
```
- Key path expressions can now include references to tuple elements. (50562288)
- Single-parameter functions that accept values of type `Any` are no longer preferred over other functions. (50562333)
- Conversions between tuple types are now fully implemented. Previously, the following would diagnose an error. ([`SR-2672`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-2672), 12340004) ```swift
let values: (Int, Int) = (10, 15)

let converted: (Int?, Any) = values
```
- You can now declare and use type subscripts, just like type properties and type methods. Declare one by applying the `static` or, in classes, `class` modifier to the subscript declaration. ([`SE-0254`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0254-static-subscripts.md), 16555559) ```swift
// Declare a type with a static subscript:
enum ProcessEnvironment {
    static subscript(name: String) -> String? {
        get { getenv(name) }
        set { setenv(name, to: newValue) }
    }
}

// Use it with any of these syntaxes:
ProcessEnvironment["PATH"]! += ":/usr/local/bin"
ProcessEnvironment["PATH"]! += ":/usr/local/bin"
someVarOfProcessEnvironmentDotType["PATH"]! += ":/usr/local/bin"Type subscripts can also be used with dynamic member lookup to create dynamic type properties.
// Declare a type with a static subscript:

@dynamicMemberLookup
enum ProcessEnvironment {
    // …As above…
    static subscript(dynamicMember name: String) -> String? {
        get { self[name] }
        set { self[name] = newValue }
    }
}

// Now you can use property syntax with ProcessEnvironment:
ProcessEnvironment.PATH! += ":/usr/local/bin"
ProcessEnvironment.self.PATH! += ":/usr/local/bin"
someVarOfProcessEnvironmentDotType.PATH! += ":/usr/local/bin"
```
- Assigning [`Optional.none`](https://developer.apple.com/documentation/Swift/Optional/none) to an enumeration that also has a `none` case, or comparing such an enumeration with [`Optional.none`](https://developer.apple.com/documentation/Swift/Optional/none) now produces a warning. Such expressions create an ambiguity because the compiler chooses [`Optional.none`](https://developer.apple.com/documentation/Swift/Optional/none) over the `none` case defined by your own enumeration. ([`SR-2176`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-2176), 26126801) ```swift
enum Foo { case none }

// Assigned Optional.none instead of Foo.none.
let foo: Foo? = .none

// Comparing with Optional.none instead of Foo.none.
let isEqual = foo == .none
``` The compiler provides a warning along with a fix-it to replace `.none` with `Optional.none` or `Foo.none` to resolve the ambiguity.
- Functions can now hide their concrete return type by declaring what protocols it conforms to, instead of specifying the exact return type: ```swift
func makeACollection() -> some Collection {
    return [1, 2, 3]
}
``` Code that calls the function can use the interface of the protocol, but doesn’t have visibility into the underlying type. ([`SE-0244`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0244-opaque-result-types.md), 40538331)
- Enum cases can now be matched against an optional enum without requiring a ‘?’ at the end of the pattern. ([`SR-7799`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-7799), 41494702) ```swift
enum Foo { case zero, one }

let foo: Foo? = .zero

switch foo {
    case .zero: break
    case .one: break
    case .none: break
}
```
- The existing `@dynamicMemberLookup` attribute now supports typed key path implementations. ([`SE-0252`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0252-keypath-dynamic-member-lookup.md), 49069813) ```swift
struct Point {
    var x, y: Int
}

@dynamicMemberLookup
struct Box<T> {
    var v: T

    init(_ v: T) {
        self.v = v
    }

    subscript<U>(dynamicMember member: KeyPath<T, U>) -> U {
        get { return v[keyPath: member] }
    }
}

var box = Box(Point(x: 0, y: 0))
_ = box.x
```
- You can now use the `Self` expression to refer to the innermost nominal type inside structure, enumeration and class declarations. For example, the two method declarations inside this structure are equivalent: ```swift
struct Box<Value> {
    func transform1() -> Self { return self }
    func transform2() -> Box<Value> { return self }
}
``` In classes, `Self` is the dynamic type of the `self` value, as before. Existing restrictions on `Self` in declaration types still apply; that is, `Self` can only appear as the return type of a method. However, `Self` can now be used inside the body of a method without limitation. ([`SE-0068`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0068-universal-self.md), 17892696)
- [`Array`](https://developer.apple.com/documentation/Swift/Array) and [`ContiguousArray`](https://developer.apple.com/documentation/Swift/ContiguousArray) now have the [`init(unsafeUninitializedCapacity:initializingWith:)`](https://developer.apple.com/documentation/Swift/Array/init(unsafeUninitializedCapacity:initializingWith:)) initializer, which provides access to the array’s uninitialized storage. (21880692)
- More thorough checking has been implemented for restrictions around escaping closures capturing in-out parameters or values of `noescape` type. While most code isn’t affected, there are edge cases where the Swift 5.0 compiler accepted code that violated these restrictions. ([`SR-8546`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-8546), [`SR-9043`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-9043), 43355341) An example of invalid code which was incorrectly accepted by the Swift 5.0 compiler is an `@escaping` closure that calls a local function that references an in-out parameter from an outer scope: ```swift
struct BadCaptureExample {
    var escapingClosure: () -> ()

    mutating func takesInOut(_ x: inout Int) {
        func localFunction() {
            x += 1
        }

        escapingClosure = { localFunction() }
    }
}
``` The compiler now correctly diagnoses the above code by pointing out that the capture of x by `localFunction()` is invalid, since `localFunction()` is referenced from an `@escaping` closure.This also addresses certain cases where the compiler incorrectly diagnosed certain code as invalid, when in fact no violation of restrictions had taken place. For example: ```swift
func takesNoEscape(_ fn: () -> ()) {
    func localFunction() {
      fn()
    }

    { localFunction() }()
}
```

###### Known Issues

- The `NEHotspotConfigurationError` enum from the [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) framework changed from `NS_ENUM` to `NS_ERROR_ENUM`, which can cause compiler errors in existing Swift code that uses the enum. For example, in code like this: ```swift
let code = NEHotspotConfigurationError(rawValue: errorCode)
``` You will see the error message: “error: incorrect argument label in call (have ‘rawValue:’, expected ‘_nsError:’).” (54134493) : Replace references of `NEHotspotConfigurationError` with [`NEHotspotConfigurationError`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfigurationError). For the above example, change the code to: ```swift
let code = NEHotspotConfigurationError.Code(rawValue: errorCode)
```

###### Resolved Issues

- Duplicate tuple element labels are no longer allowed, because it leads to incorrect behavior. ([`SR-8974`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-8974), 45218256) The following is now diagnosed as an error: ```swift
let dupLabels: (foo: Int, foo: Int) = (foo: 1, foo: 2)

enum Foo {
    case bar(x: Int, x: Int)
}

let f: Foo = .bar(x: 0, x: 1)
``` You can still use duplicate labels when declaring functions and subscripts, as long as the internal labels are different. For example: ```swift
func foo(bar x: Int, bar y: Int) {}

subscript(a x: Int, a y: Int) -> Int {}
```
- Static libraries are now always force-loaded in their entirety during linking, fixing most “unable to demangle” runtime errors. (47598583)
- `weak` and `unowned` stored properties no longer inhibit the automatic synthesis of [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable) or [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) conformance. (SR-9827, 50566123)
- If symbols in a crash log aren’t properly demangled, run the `swift-demangle` command and pass in the content of the crash log. (34920390)
- If a type has the same name as its containing module, importing that module from a module interface works properly. (19481048, 48445154)

##### Swiftui

###### Known Issues

- Deploying SwiftUI previews to a device in a project with a deployment prior to iOS 10 will fail, even if the device is running iOS 13. SwiftUI previews can only be deployed to devices when the deployment target of the project is iOS 10+, and the device is running iOS 13. (52121546)
- The software keyboard doesn’t appear in previews. (35615536)
- Code changes you make while running an on-device preview might display the Home screen briefly while the app relaunches. (48208765)
- Pinching to zoom is unavailable in live previews. (51183125)  Exit live mode or use the zoom controls in the canvas or editor menu.
- Static previews for iOS, tvOS, and watchOS don’t support SceneKit, MapKit, and Metal views, and experience a delay when rendering updates. (50965310)
- Previews in packages always perform a full build of the active scheme. (51030302)
- [`HStack`](https://developer.apple.com/documentation/SwiftUI/HStack) and [`VStack`](https://developer.apple.com/documentation/SwiftUI/VStack) inspectors don’t support custom layout guides. (49710501)  Use the source editor for custom layout guides.
- The attribute inspector doesn’t allow specifying flexible frames. (51310989) : Use the source editor to work with the frame inspector when specifying flexible size information.
- Entering live preview mode in the canvas might take several seconds the first time. (46505269)
- Previews may fail or update incorrectly when switching between files. (50841287)  Add a newline to the end of the active file, then click Resume in the banner that appears.
- The attributes inspector stays visible after the canvas closes, gets stuck on the last selected item, and doesn’t function. (50958316)  Reopen the canvas or switch to a different file.
- Previews don’t appear in the canvas for `private` and `fileprivate` structures that conform to [`PreviewProvider`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider). (47011316)  Remove the `private` or `fileprivate` access control from your conforming type.
- Previews might take several seconds to update when switching devices in the run destination selector the first time. (47562171)
- Previews might temporarily show the incorrect device chrome when switching devices using the run destination from the Scheme pop-up menu. (49496647)
- Undo is unavailable in the canvas. (49651153)  Bring the source editor into focus and perform the undo there.
- Text view doesn’t display properly in tvOS playgrounds. (54148259)
- SwiftUI has an API that lets you change the value type of [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) to [`AnyHashable`](https://developer.apple.com/documentation/Swift/AnyHashable): ```swift
let someBinding: Binding<String> = ...

let typeErasedBinding = Binding<AnyHashable>(someBinding)
``` Attempting to use this API fails at compile time with a linker error on watchOS 6. (53769896)
- Apps containing SwiftUI inside a Swift package crash on launch on devices running iOS versions earlier than iOS 13. (53706729) : When back-deploying to an OS that doesn’t contain the SwiftUI framework, add `-weak_framework SwiftUI` to the Other Linker Flags setting in the Build Settings tab. See [`Frameworks and Weak Linking`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WeakLinking.html#//apple_ref/doc/uid/20002378) for more information on weak linking a framework. Note that this workaround doesn’t apply when using dynamically-linked Swift packages which import SwiftUI.
- Xcode Previews fast turnaround may not work in some files. (48091832) : If you encounter issues using Xcode Previews, you can try disabling hot-swapping per file using the Editor > Previews menu. You will still be able to use previews, but without the faster turnaround that hot-swapping provides.

###### Resolved Issues

- The `#if`/`#endif` compiler conditionals surrounding PreviewProvider types have been removed from SwiftUI templates. PreviewProviders aren’t properly removed from built products when archived. (51539802)
- Xcode Previews work when your built products (derived data) are on a separate volume from your home directory. (54327360)
- Switching run destinations will show the correct device in Xcode Previews. (54006837)
- Fixed an issue preventing Xcode Previews from working for macOS apps with App Sandbox enabled. (51088926)

##### Swift Compiler

###### Known Issues

- Applying multiple property wrappers to a property could cause the compiler to synthesize accessors with the wrong ABI. This feature has been disabled to prevent incompatible ABI changes from occurring in the future. (53428736)

##### Swift Packages

###### New Features

- Xcode now supports creating and working with Swift packages, as well as adding, removing, and managing package dependencies. The package management support in Xcode is built on top of the open source Swift Package Manager project. (22427200)

###### Known Issues

- There is no explicit command-line option to build a Swift Package using `xcodebuild`. (45575820)  Run `xcodebuild -workspace .` in the directory containing the `Package.swift` file.
- Previews aren’t supported for standalone packages. (51072409)
- Swift packages don’t support adding resource files — such as images, storyboards, or audio — in a target. ([`SR-2866`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-2866), 33389529)
- Swift packages don’t support processing localized strings files. (48190792)
- Moving a local package in a project will convert it into a folder reference. (50320585)
- A package product that is linked into both app and its test target results in duplicated symbols. (50348625)  Link a package product only in the app or test target.
- The scheme that’s autogenerated for a Swift package isn’t automatically updated when the package adds or removes targets. (50586754)  Delete the scheme from the `swiftpm/xcode/xcshareddata/xcschemes` directory inside the package directory, then reopen the package to automatically generate a new scheme.
- Targets of a Swift package build with debug-conditional settings if the build configuration selected in the scheme is not named Debug or Release. (50696202)
- Removing a local package reference from a workspace removes its package products from all Xcode targets in the workspace, even when other references to that local package remain in the workspace. (50706448)  Add package product references back to the relevant targets.
- Previewing code in Swift packages which are not referenced by the active scheme and not being linked into an app target is not supported and shows an incorrect error message. (50909384)
- Test targets of newly-created Swift packages fail to build for watchOS because XCTest is unavailable on watchOS. (51054894)  Surround any code in watchOS test targets which references the XCTest framework or its APIs with conditional compilation statements. For example: ```swift
#if !os(watchOS)
// XCTest code
#endif
```
- WatchOS apps which are embedded in an iOS app will not build successfully if they depend on any system library targets from Swift packages. (54579347) : Add the watchOS app explicitly to the scheme being built, clean the build folder and build again.
- If an iOS, tvOS, or watchOS app uses a Swift Package that builds a dynamic library, it cannot be submitted to the App Store. (55564324) : Modify the Package manifest to build a static library.

###### Resolved Issues

- Code completion works for Swift package targets regardless if the name of the target declared in the `Package.swift` manifest file differs in casing with the directory name for that target. (49648458)
- Adding a new file in a C-family target of a Swift package doesn’t create the file with the `.swift` extension. (31395814)
- Swift packages that use `unsafeFlags` build settings can’t be used as a dependency. (50354068)

##### Testing

###### New Features

- The test plan editor now supports selecting a target to use when expanding build setting variables in command-line arguments and environment variable entries. (51841050)
- Support for writing [`XCTest`](https://developer.apple.com/documentation/XCTest) UI tests that interact with SwiftUI views. (35224680)
- Test Plans are a new way to manage which tests run, and how those tests run. Schemes can reference multiple test plans, and define a default test plan for automation. A new Test Plan editor supports defining test configurations, which can inherit shared settings from the plan itself. Running tests in Xcode now runs tests across all test configurations. The Source Editor test diamonds are updated to support running a test in a single configuration, and the Test Navigator is updated to allow choosing the active test plan. Test reports are updated to support displaying results generated by a test plan. (16138582)
- XCTest includes augmented performance testing capabilities with the new [`measure(metrics:options:block:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/measure(metrics:options:block:)) method and related methods. The metrics argument requires a list of objects conforming to the [`XCTMetric`](https://developer.apple.com/documentation/XCTest/XCTMetric) protocol. You can either implement your own custom metrics or use [`XCTClockMetric`](https://developer.apple.com/documentation/XCTest/XCTClockMetric), [`XCTOSSignpostMetric`](https://developer.apple.com/documentation/XCTest/XCTOSSignpostMetric), [`XCTCPUMetric`](https://developer.apple.com/documentation/XCTest/XCTCPUMetric), [`XCTMemoryMetric`](https://developer.apple.com/documentation/XCTest/XCTMemoryMetric), or [`XCTStorageMetric`](https://developer.apple.com/documentation/XCTest/XCTStorageMetric). (49430032) The following shows an example performance test that measures the CPU and Memory impact of sorting a list: ```swift
func testExample() {
    // Measures the CPU and memory impact of sorting the input list.
    measure(metrics: [XCTCPUMetric(), XCTMemoryMetric()]) {
        sortedList = qsort(list: self.fiftyNumbersFrom0to100)
    }
}
```
- Added an assertion function, `XCTUnwrap`, for use in Swift tests. `XCTUnwrap` asserts that an Optional variable’s value is not `nil`, returning its value if the assertion succeeds. This removes the need to combine [`XCTAssertNotNil(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTAssertNotNil(_:_:file:line:)) with either unwrapping the value or dealing with conditional chaining for the rest of the test. For example: ```swift
func testFirstNameNotEmpty() throws {
    let forenames: [String] = customer.forenames

    let firstName =  try XCTUnwrap(forenames.first)
    XCTAssertFalse(firstName.isEmpty)
}
``` `XCTUnwrap` is a throwing assertion, and is best used in a throwing test method as in the above example. (30667432)
- `xccov` now supports being passed result bundles directly, in addition to raw report and archive files. For example, to view the coverage report within a result bundle, invoke `xccov` as follows: `xccov view --report /path/to/result_bundle.xcresult`. (50500789)
- The format of result bundles changed in Xcode 11. A result bundle is an asset produced by Xcode 11 with the `xcresult` file extension that contains information about the build, tests, code coverage, and more. Any `xcresult` files produced with Xcode 10 or earlier cannot be read by Xcode 11. A result bundle can be produced by passing `-resultBundlePath ./Example.xcresult` to an `xcodebuild` invocation and the `Example.xcresult` can then be opened in Xcode. Xcode also creates result bundles in Derived Data. The current result bundle version number is 3, which can be specified by passing the `xcodebuild` flag `-resultBundleVersion 3`. Version 3 is the default in Xcode 11, but it is still recommended for automation to explicitly pass the flag, so that any potential future versions that become the default do not cause issues to existing tools. Result bundles can be inspected using `xcresulttool`. A JSON representation of the root object of the result bundle can be exported using `xcrun xcresulttool get --format json --path ./Example.xcresult` and any nested object, identified by its reference found in the JSON output, can be exported by adding the flag `--id REF`. `xcresulttool` also provides the description of its format using `xcrun xcresulttool formatDescription`. (41633595) - If a test runs on multiple destinations and fails on some but not others, the test report displays a summary describing the destinations on which the test failed, e.g. “Failed on iPad destinations running iOS 12.0”. (49164968)
- When running a test or test class via a source editor test diamond, option-clicking the diamond presents a popover that allows the test to be run under a specific configuration in the active test plan (if the test plan has multiple configurations). (46348663)
- When viewing a test report for tests that ran on multiple destinations (such as an Xcode Server integration, or a result bundle generated by an `xcodebuild` invocation with multiple destination specifiers), it’s now possible to filter the displayed results by destination. Clicking on the devices button in the scope bar will present a list of the destinations on which the tests ran, including the ability to hide or show only the destinations of interest. In addition, it’s now possible to filter to only those tests that failed on one destination but succeeded on another, via the “Mixed” button in the scope bar. (48981032)
- Result bundles produced by `xcodebuild` can now be shared, double-clicked, and opened in Xcode directly. (38620469)
- Introduces support for writing XCTest-based tests for Mac Catalyst apps. (41530313)
- Code Coverage is now enabled by default for newly created test plans. (48749597)
- In UI testing on macOS, mouse moves, including calls to the hover API as well as calls to click, scroll, and other APIs will move the cursor progressively across the screen, just as a user would in real interactions, rather than instantly moving the cursor to the final location. This may cause problems for tests involving UI that is heavily dependent on mouseover behavior. (49430331)
- The `.xctestrun` file format is modified for Test Plans to include information about how to perform each test configuration in the plan. When running `xcodebuild build-for-testing` for a scheme that uses test plans, the generated `.xctestrun` files use `FormatVersion 2` and have a revised property list structure. `.xctestrun` files generated for schemes which don’t use test plans continue to use `FormatVersion 1`, and `xcodebuild test-without-building` accepts either version. (46346053)
- The Code Coverage setting in the test plan editor doesn’t support selecting individual targets to gather code coverage for. If the test plan was created by converting a scheme to use test plans, and that scheme had individual code coverage targets selected at the time of conversion, those targets are preserved in the resulting test plan but aren’t editable within the plan. (50502861)
- `xcodebuild` is enhanced with new options supporting Test Plans. Use the new `-showTestPlans` option to list all test plans associated with a scheme. Use the new `-testPlan <name>` option to specify which test plans associated with a scheme to use for testing or building tests. If `-testPlan <name>` is not specified, `xcodebuild` test will use the scheme’s default test plan. (46346197)
- Xcode 11 introduces the option to automatically include screenshots from XCTest in Xcode Localization Catalogs. Enable Localization Screenshots in your test plan or in the scheme editor, then check “include screenshots” when exporting for localization. (28656175)
- When running tests using a test plan, it is now possible to configure which targets to include in code coverage results via the test plan’s code coverage setting. (53504451)

###### Known Issues

- The `XCTUnwrap` API is only available in primary test bundle targets and not in other libraries or frameworks. (51117167)  Move any library code that makes use of `XCTUnwrap` to your primary test bundle target or manually modify the following build settings in affected targets: ```text
SYSTEM_FRAMEWORK_SEARCH_PATHS = "$(inherited) $(PLATFORM_DIR)/Developer/Library/Frameworks"

LIBRARY_SEARCH_PATHS = "$(inherited) $(PLATFORM_DIR)/Developer/usr/lib"
SWIFT_INCLUDE_PATHS = "$(inherited) $(PLATFORM_DIR)/Developer/usr/lib"
```

###### Resolved Issues

- Schemes which have been converted to use test plans – and have test plan entries in the Build action enabled for actions other than Test (such as Run) – no longer crash with versions of Xcode before 11.0. (53645359)
- The structured build log in Xcode, and in standalone Result Bundles, shows durations for each step again. (48126238)
- The Execute in Parallel checkbox in the test action of a scheme is now enabled for test targets of a Swift package. (47564543)
- The [`exists`](https://developer.apple.com/documentation/XCTest/XCUIElement/exists) property on [`XCUIElement`](https://developer.apple.com/documentation/XCTest/XCUIElement) now produces test failures in situations where XCTest is unable to inspect the application’s UI — for example, due to the app’s main thread being unresponsive — instead of returning `false` in those situations. (37359653)
- The unit test discovery mechanism is more efficient for large projects. The test navigator gets populated faster after reopening a project. (32567980)

##### Watchos

###### Known Issues

- watchOS applications built with the watchOS 6 SDK and a deployment target of watchOS 5.3 will crash on launch. (55360395) : Set the `__WKEXTENSIONMAIN_LEGACY_TARGET_5_3` build setting to “legacy,” or use another deployment target instead of 5.3.

## See Also

- [Xcode 11.7 Release Notes](xcode-11_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.6 Release Notes](xcode-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.5 Release Notes](xcode-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4.1 Release Notes](xcode-11_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4 Release Notes](xcode-11_4-release-notes.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-11-release-notes)*