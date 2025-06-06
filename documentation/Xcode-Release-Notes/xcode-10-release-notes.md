# Xcode 10 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 10 is available in the Mac App Store and includes SDKs for iOS 12, watchOS 5, macOS 10.14, and tvOS 12. Xcode 10 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 10 requires a Mac running macOS 10.13.6 or later.

##### General

###### New Features

- Added an export option to the Quick Look popover for data types such as [`NSData`](https://developer.apple.com/documentation/Foundation/NSData). (41370369)
- Newly created schemes now default to being shared by all users of an Xcode project. To create a personal scheme, uncheck the “Shared” checkbox in the “Manage Schemes” sheet. (40223696)
- Select Schemes and Run Destinations from the keyboard. Press “Ctrl+0” to open the Scheme popup and “Ctrl+Shift+0” to open the Run Destination popup. Once the popup appears, type enough characters to highlight the appropriate entry, use the arrow keys to highlight it, and press return to select it. (8999215)
- Holding the Option key when opening the Library will cause it to remain visible until it is manually dismissed, rather than automatically closing after each use. (40880961)
- Library content has moved from the bottom of the Inspector area to an overlay window, which can be moved and resized like Spotlight search. It dismisses once items are dragged, but holding the Option key before dragging will keep the library open for an additional drag. The library can be opened via a new toolbar button, the View > Libraries menu, or the ⇧⌘L keyboard shortcut. Content dynamically matches the active editor, so the same UI provides access to code snippets, Interface Builder, SpriteKit, or SceneKit items. The media library is available via a long press on the toolbar button, the View > Libraries menu, or the ⇧⌘M keyboard shortcut. (37318979, 39885726)
- The Capabilities tab in the Project Editor provides a new Hardened Runtime capability for macOS apps and app extensions. Enabling this capability will opt your app into new security protections provided by macOS 10.14 and will be required for your app to be notarized. (39674498)

###### Known Issues

- Opening Xcode projects and workspaces stored in iCloud Drive, or changing source control branches for an open workspace or project stored in iCloud Drive, might cause Xcode to hang. (34086758)

###### Resolved Issues

- The New File template for Objective-C header (`.h`) files includes the `NS_ASSUME_NONNULL_BEGIN` and `NS_ASSUME_NONNULL_END` macros. (22753521)
- Fixed an issue where the text range of a find result wouldn’t be highlighted when selecting from the Find Navigator. (37820835)
- Project settings validation understands build setting values set by reference to other build settings. (30549576)
- Schemes for which “Show” has been unchecked in the Manage Schemes sheet no longer appear in the Product > Scheme submenu. (24579413)
- Double Click Navigation now defaults to Same as Click. This can be changed in the Navigation pane of Preferences. (37294346)
- Fixed a crash when pressing the tab key in the code snippet editor. (41296805)

##### Apple Clang Compiler

###### New Features

- Xcode 10 adds support for the C++17 headers `<any>`, `<optional>`, and `<variant>`. (39271859)

###### Resolved Issues

- Clang now correctly handles invalid Objective-C properties that could affect code completion support. (33761186)

##### Asset Catalog

###### New Features

- Named colors can now symbolically reference system colors. (39196638)
- Support for ARKit 3D [`ARReferenceObject`](https://developer.apple.com/documentation/ARKit/ARReferenceObject) assets. (38086640)
- Support for CarPlay assets. (35543584)
- Support for varying image and color assets by Light, Dark, and High Contrast appearances on macOS 10.14 and above. (38735965)
- The background of the asset catalog and view debugger can be set explicitly to light or dark so foreground elements display with sufficient contrast. (39073926)

###### Resolved Issues

- Auto scaling is no longer turned on by default in asset catalogs for watchOS PDF assets, regardless of selection. (35788204)
- Fixed a hang that could happen when opening an asset catalog that’s part of an external project reference. (14235592)

##### Build System

See [`Build System Release Notes for Xcode 10`](build-system-release-notes-for-xcode-10.md).

##### Command Line Tools

###### New Features

- The Command Line Tools package installs the macOS system headers inside the macOS SDK. Software that compiles with the installed tools will search for headers within the macOS SDK provided by either Xcode at: `/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk` or the Command Line Tools at: `/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk` depending on which is selected using `xcode-select`. The command line tools will search the SDK for system headers by default. However, some software may fail to build correctly against the SDK and require macOS headers to be installed in the base system under `/usr/include`. If you are the maintainer of such software, we encourage you to update your project to work with the SDK or file a bug report for issues that are preventing you from doing so. As a workaround, an extra package is provided which will install the headers to the base system. In a future release, this package will no longer be provided. You can find this package at: `/Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg` To make sure that you’re using the intended version of the command line tools, run `xcode-select -s`  or `xcode select -s /Library/Developer/CommandLineTools` after installing.

##### Create Ml

###### New Features

- [`MLDataTable`](https://developer.apple.com/documentation/CreateML/MLDataTable), [`MLDataColumn`](https://developer.apple.com/documentation/CreateML/MLDataColumn), and [`MLUntypedColumn`](https://developer.apple.com/documentation/CreateML/MLUntypedColumn) support math operations, range-based slicing, multiple column sub-selection, type conversion and additional data preprocessing methods. (38199042)
- Augmentation supports the ability to crop images. (42077294)

###### Known Issues

- Create ML isn’t supported for use in Command Line Tools. (40637430)

###### Resolved Issues

- Changing the name of a model saves correctly when clicking off the field. (40437531)

##### Debugging

###### New Features

- You can change the appearance of your macOS app at runtime by using the Debug > View Debugging > Appearance menu, the Override Appearance menu in the debug bar, or the touch bar. (39448599)
- Xcode’s view debugger adds an option to choose between light and dark canvas background color. (39159102)
- [`NSVisualEffectView`](https://developer.apple.com/documentation/AppKit/NSVisualEffectView) properties are now presented in the view debugger inspector. (18124270)
- The files table in the Disk Gauge Report includes files that were closed so that developers are aware of their size. (39359014)
- The view debugger adds [`appearance`](https://developer.apple.com/documentation/AppKit/NSApplication/appearance) and [`effectiveAppearance`](https://developer.apple.com/documentation/AppKit/NSApplication/effectiveAppearance) properties to the view inspector. (38198002)
- The debugging Attach sheet allows developers to turn on Malloc Stack Logging (Live Allocations). (35447219)
- The Disk Gauge Report includes a new table that shows the total Read and Write sizes of the process across time. (39359147)
- Named colors shown in the inspector while view debugging now indicate their names and whether they are system colors. (38193961)
- The Metal Frame Debugger. (33194071)The Metal Frame Debugger lets you debug your Metal shaders. Capture a Metal workload, select a draw / dispatch call and click the new debug button on the debug bar to start debugging your shaders. Selecting command encoder items in Debug Navigator will bring up a graph showing how encoders depend on each other through resource usage. Zoom in to get more information about attachments and encoders.Every draw call has new “Geometry” item where you can see 3D visualization of your post transform vertex data alongside with your vertex inputs and outputs.

###### Resolved Issues

- The Memory Gauge Report now reports the physical footprint consistently across all the platforms. (20472364)
- The performance of the first Swift expression evaluation has been optimized when a large number of static Swift modules are present. (40905971)
- Xcode waits for a simulator to be available before attempting to run an app on that simulator. (39116182)
- Options in the Debug > View Debugging menu, like Show View Frames, now continue the target application as expected. (26649378)

##### Deprecation Notices

###### Deprecations

- Building with libstdc++ was deprecated with Xcode 8 and is not supported in Xcode 10 when targeting iOS. C++ projects must now migrate to libc++ and are recommended to set a deployment target of macOS 10.9 or later, or iOS 7 or later. Besides changing the C++ Standard Library build setting, developers should audit hard-coded linker flags and target dependencies to remove references to libstdc++ (including -lstdc++, -lstdc++.6.0.9, libstdc++.6.0.9.tbd, and libstdc++.6.0.9.dylib). Project dependencies such as static archives that were built against libstdc++ will also need to be rebuilt against libc++. (40885260)
- Libgcc is obsoleted. Xcode 10 can no longer build apps with deployment targets of macOS 10.4 and 10.5. (42818150, 38035243)
- Support for Subversion has been removed. (33361671)
- Custom dtrace-based instrumentation that was available for macOS and Simulator only is no longer supported in Instruments. The new Custom Instruments packages based on os_signpost allow for greater flexibility and control over presentation of data and support all platforms. (38812912)
- Xcode 10 is the last release that will support Swift 3. Migrate your projects from Swift 3 code to Swift 4.2 syntax by opening the project and choosing Edit > Convert > To Current Swift Syntax… (43101816)
- The macOS 10.14 SDK no longer contains support for compiling 32-bit applications. If developers need to compile for i386, Xcode 9.4 or earlier is required. (39858111)

##### Devices

###### Known Issues

- Devices running iOS 12 may fail to take screenshots requested from Xcode’s Devices window. (42873539)  Take the screenshot on the device.
- Running a WatchKit app with Xcode 10 that was built with a previous version of Xcode can give an installation error “The WatchKit app has an invalid stub executable.” (40567857)  Clean the build folder and run the app again.

##### Documentation Viewer

###### New Features

- Quick Help uses a single column layout, making better use of the available space that it’s presented in. (39518057)
- Code listings in the documentation viewer and Quick Help match the user’s currently selected theme colors. (39435799)

##### Instruments

###### New Features

- There is a new graph mode available for threads when using System Trace instrumentation in Instruments 10 – Thread States – which shows only the thread state lane. The previous OS Fundamentals graph style (system calls, VM faults, and thread state lanes) is still available as well. (37727022)
- The support for system trace instrumentation prior to Instruments 8 has been removed. Some trace files containing data from these instruments will no longer open in Instruments. A version of Xcode prior to Xcode 10 can be downloaded from developer.apple.com in order to view these older files. (38506479)
- You can now build and distribute your own custom instruments. (37987666)

###### Known Issues

- Instruments may fail to launch if Xcode has not finished preparing any attached devices for development. (43066159)  Wait for Xcode’s device setup phase to complete and then open Instruments.
- Instruments may not profile library or framework unit tests in iOS simulator. (39334812)
- When stopping a recording that includes signposts (e.g. [`pointsOfInterest`](https://developer.apple.com/documentation/os/OSLog/Category/pointsOfInterest), [`os_signpost(_:dso:log:name:signpostID:)`](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostID:)-2oz8u), or [`os_log(_:dso:log:_:_:)`](https://developer.apple.com/documentation/os/3019240-os_log) instruments), the recording button may not reactivate for an extended period of time. (43361649)  Launch Console on your Mac, select the target device, and leave Console running. This connection between Console and the target will be enough keep Instruments from hanging at the end of a recording.

###### Resolved Issues

- Most templates failed when profiling on iOS versions prior to iOS 11.3. (39759266)

##### Interface Builder

See [`Interface Builder Release Notes for Xcode 10`](interface-builder-release-notes-for-xcode-10.md).

##### Localization

###### New Features

- Xcode 10 supports a new Xcode Localization Catalog (`.xcloc`) export and import format for localization data that can contain both an XLIFF file and other localizable content such as image files. (28662326)
- Xcode offers to enable Base Internationalization for projects that don’t yet use it but support multiple localizations. (13178091)

###### Resolved Issues

- In an XLIFF produced by the Export For Localization command, content from a file outside the project directory will be referenced via a path relative to the project directory rather than an absolute path. (38680116)
- Xcode now extracts the appropriate values of the following `Info.plist` keys for localization: `UTExportedTypeDeclarations`, `UTImportedTypeDeclarations`, `UIApplicationShortcutItems`, `INAlternativeAppNames`. (40853982)

##### Metal

###### New Features

- When calling the metal compiler directly you must use the `-c` flag when building a `.metal` file. Not adding the option will result in an error when the resulting `.air` file is consumed by `metallib`. Calling the Metal compiler using Xcode’s build system will add the flag automatically. (40655432)

##### Playgrounds

###### New Features

- Playgrounds in Xcode now execute code incrementally, compiling new lines of code when you type Shift-Return or press the Run button next to the new line of code. This is especially useful for long tasks that you don’t want to run repeatedly, like training a machine learning model or setting up your live view’s state, and allows you to progressively iterate on your ideas without restarting the playground. (34313149)

###### Known Issues

- Switching to a non-default toolchain while in a playground may cause Xcode to crash. (43659135)  Switch back to the default toolchain and then open the playground.

###### Resolved Issues

- Fixed an issue where playgrounds would fail to run, presenting a “couldn’t lookup symbols” error message. (38505726)
- Fixed a crash that occurred in playgrounds with inline results. (38281379)
- Fixed a crash that sometimes occurred when creating a new playground page, especially if the playground was locked. (38281509)
- Fixed an issue that prevented the iOS Game playground template from working correctly. (38828600)
- Code completion is now supported in auxiliary source files in playgrounds. (34363732)

##### Refactoring

###### Resolved Issues

- Fixed an issue where the editing field of Refactor > Rename would not get keyboard focus if the “Reduce motion” Accessibility option was turned on. (40719848)

##### Server

###### Resolved Issues

- Certain Xcode Server logs, such as trigger logs, are now visible in the integration Logs report. (40462372)

##### Signing and Distribution

###### New Features

- Support for uploading apps to Apple via the command line. The `xcodebuild -exportArchive` command will perform an upload if the provided `ExportOptions.plist` contains a key named “destination” with value “upload”. In addition, an Apple ID account with the necessary App Store Connect role and provider membership must be added in Xcode’s Accounts preference pane. The “app-store”, “developer-id”, and “validation” distribution methods are supported for use from `xcodebuild`. (28555930)
- The Developer ID distribution option in Xcode’s Organizer now provides support for uploading apps to Apple to be notarized. After building an archive, this option can be selected in the Organizer by clicking the Distribute App button and then selecting the Developer ID method and the Upload destination. In order to upload an app to be notarized, you must enter an Apple ID in Xcode’s Accounts preferences pane with the necessary App Store Connect role and provider membership. In addition, apps uploaded to be notarized must be signed with a Developer ID certificate. The distribution workflow can create this certificate if necessary, but requires an Apple ID account with the Agent role in order to do so. After uploading an app to be notarized, you can view your app’s status in the Organizer window by selecting your archive and clicking the Show Status Log button. When you receive notification that your app has been notarized, you can export it from the Organizer window by selecting your archive and clicking the Export App button. The exported app contains a stapled ticket and is ready for distribution. (36409604)

##### Simulator

###### New Features

- The Copy and Paste items in Simulator’s Edit menu are no longer used for synchronization with a simulator devices’s pasteboard. The Edit menu now has explicit menu items to handle these actions. (38225290)
- When running tests from xcodebuild or Xcode Server with iOS Simulator destinations, test failures will result in the collection of log archives embedded in the test action result bundle. (42172805)

###### Known Issues

- Video output might stop playing on external displays if using keyboard commands for fast forward and rewind. (41917187)  Pull down the control panel from the top-right corner of the screen and then hide it again.
- Synchronization between the macOS pasteboard and pasteboards in simulated devices can sometimes fail. (36036706, 38052949, 41916640)
- The OS can take several minutes to boot for the first time in a simulator. (40535421)
- On macOS 10.14, Simulator might prompt for Microphone access at launch or when first interacting with the microphone in a simulator (for example, by using Siri). If you decline permissions, simulator audio sessions will not be able to use audio input of any kind, regardless of the permissions granted inside a simulator. Use the macOS System Preferences, Security & Privacy preference pane to change this setting. Your application must still be granted Microphone permission inside the simulator as well. macOS applies its permission policy to Simulator application as a whole, across all simulator runtime versions and all applications inside a simulator. Each simulator applies permission policies to individual applications just like devices. (40113388)

##### Source Control

###### New Features

- Improved source control authentication workflows provide more information and greater control to perform an authenticated operation. (33726987)
- Integration with Bitbucket Cloud and Bitbucket Server source control. (31156776)
- Tags can optionally be pushed from the push sheet. (40141815)
- Integration with GitLab.com and GitLab self-hosted source control. (37501192)
- With a source control-enabled project the source editor displays changes made by a developer in the gutter and shows changes made by other developers that haven’t yet been pulled into the project. (9794871)
- SSH keys can be easily managed using the new create, validate and upload workflows with GitHub, Bitbucket, and GitLab. (31798220)
- Rebase support when pulling source control changes. (8937399)

###### Known Issues

- Xcode doesn’t support ed25519 encrypted SSH keypairs. (40912136)  Use an SSH key pair that uses a different form of encryption.

###### Resolved Issues

- The source control authors editor submode performance is improved to load and scroll faster. (40179372)

##### Source Editor

See [`Source Editor Release Notes for Xcode 10`](source-editor-release-notes-for-xcode-10.md).

##### Static Analyzer

###### New Features

- The static analyzer checks for a common performance anti-pattern when using Grand Central Dispatch, which involves waiting on a callback using a semaphore: ```objc
+ (NSString *)requestCurrentTaskName {
    __block NSString *taskName = nil;
    dispatch_semaphore_t sema = dispatch_semaphore_create(0);
    NSXPCConnection *connection =
      [[NSXPCConnection alloc]
        initWithServiceName:@"MyConnection"];
    id remoteObjectProxy = connection.remoteObjectProxy;
    [remoteObjectProxy requestCurrentTaskName:^(NSString *task) {
        taskName = task;
        dispatch_semaphore_signal(sema);
    }];
    dispatch_semaphore_wait(sema,
        dispatch_time(DISPATCH_TIME_NOW, 100)
    );
    return taskName;
}
``` Such a pattern can degrade performance and cause hangs in your application. The check is currently disabled by default, but can be enabled using the build setting “Performance Anti-Patterns with Grand Central Dispatch”. (37312818)
- The static analyzer is more efficient and will report additional issues on most programs. (36672459)

##### Swift

See [`Swift 4.2 Release Notes for Xcode 10`](swift-4_2-release-notes-for-xcode-10.md).

##### Testing

###### New Features

- Schemes can now be configured to only run a fixed subset of tests in a test bundles and not automatically include new tests that are added to the bundle. This can be configured in the Test pane of the scheme editor as an option for each test bundle. (35050431)
- XCTest UI tests now capture the standard output and error streams from launched target apps to a file in the result bundle. (30929875)
- Xcode 10 supports running tests in parallel, which reduces the time it takes to run tests. Test parallelization is supported for macOS unit tests, as well as unit and UI tests on iOS and tvOS simulators. To enable parallelization, navigate to the scheme editor (Product > Scheme > Edit Scheme), select the Test action followed by the Info tab, and then next to your test target, click Options. Finally, select “Execute in parallel” (for macOS tests) or “Execute in parallel on Simulator” (for iOS and tvOS tests). Test parallelization occurs by distributing the test classes in a target across multiple runner processes. Use the test log to see how your test classes were parallelized. You will see an entry in the log for each runner process that was launched, and below each runner you will see the list of classes that it executed. When testing in parallel on Simulator, each runner process executes on a separate clone of the selected simulator. For a simulator named “iPhone X”, these clones will appear in Simulator as “Clone 1 of iPhone X”, “Clone 2 of iPhone X”, etc. (35224733)
- XCTest now enforces that [`XCTestExpectation`](https://developer.apple.com/documentation/XCTest/XCTestExpectation) instances must not be waited on more than once. This prevents accidental misuse and is especially important for inverted expectations because they cause waiting to take the full timeout duration which might cause tests to execute more slowly. (41641176)One way that an expectation might be accidentally waited on multiple times is if it’s created using [`expectation(description:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/expectation(description:)), is waited on using [`wait(for:timeout:)`](https://developer.apple.com/documentation/XCTest/XCTWaiter/wait(for:timeout:)-swift.method), and then [`waitForExpectations(timeout:handler:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/waitForExpectations(timeout:handler:)) is called. XCTest will now raise an exception when this occurs, listing the problematic expectations that should be adjusted.For example, the following code suffers from this problem: ```swift
func testFoo() {
    let expectation1 = self.expectation(description: "expectation1")
    doSomething { expectation1.fulfill() }
    XCTWaiter().wait(for: [expectation1], timeout: 1)
   
    let expectation2 = self.expectation(description: "expectation2")
    doSomething { expectation2.fulfill() }
   
    // API Violation exception because it waits on both expectations,
    // but expectation1 has already been waited on.
    self.waitForExpectations(timeout: 1)
}
``` Here are two possible fixes: ```swift
func testFoo_fix1() {
    let expectation1 = self.expectation(description: "expectation1")
    doSomething { expectation1.fulfill() }
    XCTWaiter().wait(for: [expectation1], timeout: 1)
  
    let expectation2 = self.expectation(description: "expectation2")
    doSomething { expectation2.fulfill() }
  
    // Only wait on expectation2, which has not yet been waited on.
    self.wait(for: [expectation2], timeout: 1)
}
   
func testFoo_fix2() {
    // Create an XCTestExpectation directly, not using XCTestCase convenience API.
    let expectation1 = XCTestExpectation(description: "expectation1")
    doSomething { expectation1.fulfill() }
    XCTWaiter().wait(for: [expectation1], timeout: 1)
  
    let expectation2 = self.expectation(description: "expectation2")
    doSomething { expectation2.fulfill() }
  
    self.waitForExpectations(timeout: 1) // Waits only for expectation2.
}
```
- Test bundles can now be configured to execute their contents in a random order each time the tests are run. This can be enabled in the Test pane of the scheme editor as an option for each test bundle. (11719679)
- xcodebuild has new command line options to control the behavior of parallel testing. Use `-parallel-testing-enabled` to override the per-target setting in the scheme for whether parallelization is enabled. If you want to control the number of runners that are launched, use `-parallel-testing-worker-count` or `-maximum-parallel-testing-workers`. (39648990)
- The General pane in Preferences now includes UI for controlling the degree of parallelism that Xcode should attempt while running tests in parallel. The “Mac Test Parallelization” slider can be used to adjust the number of runners to spawn when running macOS unit tests in parallel. The “Simulator Test Parallelization” slider can be used to adjust the number of simulator clones to spawn when running iOS or tvOS app/UI tests in parallel. Setting either of these sliders to “Auto” (the default) instructs Xcode to pick a default number. Note that when testing from `xcodebuild`, the `-parallel-testing-worker-count` and `-maximum-parallel-testing-workers` command line options take precedence over these values. (41779908)
- XCTest has added new API on [`XCUIElement`](https://developer.apple.com/documentation/XCTest/XCUIElement) for capturing the entire state of the UI, either for exporting to external systems or for inspecting locally. It includes a type representing a snapshot of the UI and API for exporting that snapshot to a dictionary of standard value types (strings and numbers). (35168151)

###### Resolved Issues

- Errors that may lead to missing or no coverage data are now displayed in the test log. If you notice any such errors, please file a bug using [`Apple Byg Reporter`](https://developer.apple.comhttps://bugreport.apple.com), and attach a zipped archive of your project’s folder in `DerivedData`. (39930570)
- Xcode no longer crashes during UI test recording when interacting with content inside of [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) and [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController). (33593609)
- Fixed an issue causing baseline measurement changes to be lost and future measurements to report as `%inf` when editing those measurements on a system with a locale that does not use dots as decimal separators. (31813795)
- In the destination configuration options for an Xcode Server bot, the “Run tests in parallel” option has been renamed “Test on the selected destinations concurrently”. This option causes the selected destinations to run the scheme’s tests simultaneously. It does not cause an individual destination to run tests in parallel. To allow each destination to run tests in parallel, deselect this checkbox and either enable parallel testing in the scheme or add `-parallel-testing-enabled YES` as an `xcodebuild` argument. (39985444)
- Xcode and `xcodebuild` now build all targets in the active scheme when clicking a test gem in the Test navigator or source editor (Xcode), or when using `-only-testing`: (`xcodebuild`). Previously, only the relevant test bundle target and its dependencies would be built. Xcode and `xcodebuild` will now also disallow you from running a test or test class whose test bundle is not part of the active (Xcode) or specified (xcodebuild) scheme. (38935442)

## Topics

### Release Notes
- [Build System Release Notes for Xcode 10](build-system-release-notes-for-xcode-10.md)
  Update your apps to use new features, and test your apps against changes.
- [Interface Builder Release Notes for Xcode 10](interface-builder-release-notes-for-xcode-10.md)
  Update your apps to use new features, and test your apps against changes.
- [Source Editor Release Notes for Xcode 10](source-editor-release-notes-for-xcode-10.md)
  Update your programming workflow to use new features, and test your workflow against changes.
- [Swift 4.2 Release Notes for Xcode 10](swift-4_2-release-notes-for-xcode-10.md)
  Update your code to use new language features and test your apps against changes.

## See Also

- [Xcode 10.3 Release Notes](xcode-10_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.2.1 Release Notes](xcode-10_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.2 Release Notes](xcode-10_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.1 Release Notes](xcode-10_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-10-release-notes)*