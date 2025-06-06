# macOS Catalina 10.15 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 10.15 SDK provides support for developing apps for Macs running macOS Catalina 10.15. The SDK comes bundled with Xcode 11 available from the Mac App Store. For information on the compatibility requirements for Xcode 11, see [`Xcode 11 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-11-release-notes).

##### General

###### Known Issues

- During installation of macOS 10.15 you might be prompted to enter your administrator password multiple times to allow installation to proceed. (51206649)

###### Deprecations

- macOS frameworks are now thinned for the x86-64 architecture. Apps that execute i386 code now fail with the [`EBADARCH`](https://developer.apple.com/documentation/foundation/posixerror/2293398-ebadarch) error code. The remaining stub frameworks are nonfunctional and exist only for compatibility purposes. (51236070)

##### Airdrop

###### Known Issues

- AirDrop doesn’t work when a VPN is connected with the [`includeAllNetworks`](https://developer.apple.com/documentation/NetworkExtension/NEVPNProtocol/includeAllNetworks) and [`excludeLocalNetworks`](https://developer.apple.com/documentation/NetworkExtension/NEVPNProtocol/excludeLocalNetworks) options enabled. (52618489)  Disconnect the VPN before using AirDrop.

##### Appleevents

###### New Features

- To enhance security, AppleEvents and AppleScripts that target an app on a remote system must authenticate as the same user on the remote system. An AppleEvent that targets an app running as a different user receives a `procNotFound` error.To allow remote AppleEvents to target apps in any user session, run the following command in Terminal on the server: `defaults write /Library/Preferences/com.apple.AEServer RestrictAccessToUserSession -bool false` Then disable and reenable Remote Apple Events in System Preferences > Sharing. (5353592)

##### Audio

###### New Features

- You can now enable voice processing mode on [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine). (50906329)
- You can use new [`AVAudioNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioNode) types to wrap a user-defined block for sending or receiving data in real-time.
- A new method is available for an [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) based app to retrieve a list of all nodes attached to an [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) instance.
- A new rendering mode in [`AVAudioEnvironmentNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode) selects the best spatial audio rendering algorithm automatically based on the output device.
- A new [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) property allows system sounds and haptics to play while the session is actively using audio input.
- A new property, [`AVAudioSession.PromptStyle`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/PromptStyle-swift.enum) informs apps which style of voice prompt they should play based on other audio activity in the system.
- The [`AVAudioSession.RouteSharingPolicy`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/RouteSharingPolicy-swift.enum) enumeration is extended to allow apps to specify route sharing policies so their audio and video is routed to the same location as AirPlay.
- Audio Unit Extensions now support user presets that are available across all host apps.

###### Deprecations

- The `OpenAL` framework is deprecated and remains present for compatibility purposes. Transition to [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) for spatial audio functionality.
- [`AUGraph`](https://developer.apple.com/documentation/AudioToolbox/AUGraph) is deprecated in favor of [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine).
- Inter-App audio is deprecated. Use Audio Units for this functionality.
- Carbon component-based Audio Units are deprecated and support will be removed in a future release.
- Legacy Core Audio HAL audio hardware plug-ins are no longer supported.  Use Audio Server plug-ins for audio drivers.

##### Avfoundation

###### New Features

- The [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) class includes two new properties, [`eligibleForHDRPlayback`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/eligibleForHDRPlayback) and [`eligibleForHDRPlaybackDidChangeNotification`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/eligibleForHDRPlaybackDidChangeNotification), which you can use to determine whether an HDR display is available and can play on the current device. (35938145)
- AVFoundation now supports encoding video with alpha channels using HEVC. Videos encoded in this manner are broadly supported in AVFoundation APIs and by Safari within web pages. Technical details of the format can be found in the Interoperability Profile specification. (8045917)

###### Deprecations

- The previously deprecated 32-bit QuickTime framework is no longer available in macOS 10.15.
- The symbols for QTKit, which relied on the QuickTime framework, are still present but the classes are non-functional.

##### Camera

###### Known Issues

- Apps using Picture Taker must specify the [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) key to access the FaceTime camera. (47916725)

##### Core Image

###### New Features

- The [`init(imageURL:options:)`](https://developer.apple.com/documentation/coreimage/cifilter/1438096-init) and [`init(imageData:options:)`](https://developer.apple.com/documentation/coreimage/cifilter/1437879-init) initializers no longer support RAW decoder versions earlier than 6. Version 6 and later remain supported. (50911303)
- Added new APIs for instantiating and modifying the built-in Core Image filters.
- The [`CICoreMLModel`](https://developer.apple.com/documentation/coreimage/cicoremlmodel) filter is enhanced to support models with an input or output of type [`MLFeatureType.multiArray`](https://developer.apple.com/documentation/CoreML/MLFeatureType/multiArray).
- Metal [`CIKernel`](https://developer.apple.com/documentation/coreimage/cikernel) instances now support arguments with arbitrarily structured data.
- Metal [`CIKernel`](https://developer.apple.com/documentation/coreimage/cikernel) instances now support returning a group of two by two pixels.
- The integer values of [`CIFormat`](https://developer.apple.com/documentation/coreimage/ciformat) symbols, such as [`ARGB8`](https://developer.apple.com/documentation/coreimage/ciformat/1437883-argb8), have changed to a new set of values which are consistent across platforms. The former values remain supported for backward compatibility; however, you should avoid dependancies on specific numerical values.

##### Endpointsecurity

###### Deprecations

- The `kauth` API has been deprecated. (50419013)

##### Icloud

###### Known Issues

- After updating to macOS Catalina 10.15 Beta 7 or later, iCloud Drive might synchronize for an extended period of time. If you notice any missing files, they can be found inside a Recovered Files folder in your home folder. (54046219)
- Even when Optimize Storage is switched off, iCloud Drive might fail to automatically download all files. (50667204)  Download files individually.
- When creating a new Pages, Numbers, or Keynote document in a shared folder, you might see the message “Couldn’t connect to iCloud”. (50827963)  Close and reopen the document.

##### Launch Daemons and Agents

###### New Features

- Launch daemons and launch agents introduce new user privacy protections. Specifying privacy-sensitive files and folders in a launchd property list might not work as expected and prevent the service from running. Having `Program` or `ProgramArguments` pointing to an executable in a privacy sensitive location is currently allowed, but may be restricted in a future release. (49702405) To comply with the new privacy protections, resources for a launchd service must be stored in locations that aren’t privacy sensitive. If necessary, the app can set up resources during its execution rather than using launchd property list keys, making it possible to grant the app access using System Preferences > Security & Privacy > Privacy. The following launchd property list keys are affected: `KeepAlive`, `PathState`, `QueueDirectories`, `Sockets`, `SockPathName`, `StandardErrorPath`, `StandardInPath`, `StandardOutPath`, and `WatchPaths`.

##### Mac Catalyst

###### Known Issues

- [`nativeScale`](https://developer.apple.com/documentation/UIKit/UIScreen/nativeScale) might be inaccurate. Instead, get the scale factor from the local trait collection. (54009624)
- [`MPMediaPickerController`](https://developer.apple.com/documentation/MediaPlayer/MPMediaPickerController) might not display the contents of your library. (51785735)
- AppKit and Mac Catalyst apps are currently view-only clients of [`PencilKit`](https://developer.apple.com/documentation/PencilKit). (51146823)
- The [`UIScreen`](https://developer.apple.com/documentation/UIKit/UIScreen) class’s [`isCaptured`](https://developer.apple.com/documentation/UIKit/UIScreen/isCaptured) API isn’t currently supported. (48360589)
- The [`current`](https://developer.apple.com/documentation/UIKit/UIDevice/current) property on [`UIDevice`](https://developer.apple.com/documentation/UIKit/UIDevice) and the OS Product Name is currently returned as iOS rather than macOS, which can affect diagnostic logs generated by your system. (49792004)
- When sending Mail attachments via [`Message UI`](https://developer.apple.com/documentation/MessageUI), each attachment might appear as two icons when viewed by the recipient. (50369995)
- Controls drawn with accent color incorrectly maintain their active color when the window is inactive. There is no need to work around this in your app. (50563638)
- For Mac Catalyst apps to save to Photos Library, explicitly linking the Photos framework is required. (50781430)
- Action and share extensions might exhibit visual anomalies. (51005363)
- All assets at 3x scale factor are currently ignored when compiling the asset catalog for Mac Catalyst apps. Because the search begins with the universal asset, assets for a specific memory or graphics class won’t be found. For example, if you provide an image and only give a 6GB and Metal 5v1 asset, it won’t be found at runtime. It’s recommended that you provide all images as vectors to allow generation of the correct scale factors, or at minimum provide 2x versions of the assets. If you’re classifying resources based on memory and graphics families then you should provide “Any Memory” and “Any Graphics”. (51033745)
- CallKit [`CXAction`](https://developer.apple.com/documentation/CallKit/CXAction) instances might return an error. (51074735)
- When creating a Mac Catalyst app from your iPad app, Xcode automatically generates a unique Mac bundle identifier. If you have an existing Mac bundle identifier you’d prefer to use, you can do so by using manual signing in Xcode. (51076014) Follow these steps to configure your project, AppID, and provisioning profile: 1. [`Sign in to Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account), then select Certificates, Identifiers, and Profiles.
2. In the Identifiers section, select your iOS app identifier to edit.
3. Check the Mac Catalyst capability to enable it, then click the Configure button.
4. Choose Use an existing macOS AppID and select the identifier you’d like to use from the popup menu. Click the Save button to finish editing your AppID.
5. In the Profiles section, click the  button to create a new profile, select ‘macOS App Development’, and click Continue.
6. Select your iOS AppID from the popup, click Continue, and complete the rest of the profile creation flow. When finished, click the Download button.
7. In Xcode, select your project to view the Project Editor and select your app’s target. Then select the Build Settings tab.
8. Set the Derive Mac Catalyst Product Bundle Identifier setting to No.
9. Expand the Product Bundle Identifier build setting to view its configurations.Next to the Debug configuration, click the  button to add a conditional value.
10. For the build setting condition, select Any macOS from the popup menu. Edit the value of the conditional build setting to match the macOS bundle identifier you want to use. Repeat this step for all  configurations in your project.
11. In the Signing & Capabilities tab, uncheck Automatically manage signing.
12. For your macOS app, select Import Profile from the Provisioning Profile popup and then select the profile you downloaded earlier.
- Catalyst apps using [`UIDocumentInteractionController`](https://developer.apple.com/documentation/UIKit/UIDocumentInteractionController) might quit unexpectedly. You can work around this issue by excluding [`UIDocumentInteractionController`](https://developer.apple.com/documentation/UIKit/UIDocumentInteractionController) functionality with target macros. (48878552)
- DOM keyboard events aren’t dispatched as expected in [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) when pressing or releasing keys. Web apps needing to track typed characters can instead listen for DOM input events. (54580414)

##### Mail

###### Known Issues

- If your Mac contains both macOS Mojave 10.14 and macOS 10.15 volumes, you might experience issues searching in Mail. (46611310)  While running macOS Mojave 10.14, open Terminal and execute the following command: `sudo touch /.metadata_never_index_unless_rootfs` Reboot into macOS 10.15, open Terminal and execute the following command: `sudo touch /System/Volumes/Data/.metadata_never_index_unless_rootfs` Reboot into macOS Mojave 10.14, open Terminal and execute the following command: `sudo mdutil -E /` Depending on the size of your Mail database, it might take many hours to reindex all content.

##### Networking

###### New Features

- [`NSURLRequest.CachePolicy.reloadRevalidatingCacheData`](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy/reloadrevalidatingcachedata) and [`NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData`](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy/reloadignoringlocalandremotecachedata) APIs are now available. (49660334)
- All [`URLSessionTask`](https://developer.apple.com/documentation/Foundation/URLSessionTask) instances with a GET HTTP method which contain a body will now produce the error [`NSURLErrorDataLengthExceedsMaximum`](https://developer.apple.com/documentation/foundation/nsurlerrordatalengthexceedsmaximum). (46025234)

###### Known Issues

- The [`NWEthernetChannel`](https://developer.apple.com/documentation/Network/NWEthernetChannel) API doesn’t currently support VLAN interfaces. [`NEPacketTunnelProvider`](https://developer.apple.com/documentation/NetworkExtension/NEPacketTunnelProvider) will see both tagged and untagged frames arriving on physical interfaces. Depending on the Ethernet driver, VLAN tags might be processed by hardware and thus stripped off the Ethernet frames thus [`NEPacketTunnelProvider`](https://developer.apple.com/documentation/NetworkExtension/NEPacketTunnelProvider) won’t see the VLAN tag. (51275655)

###### Deprecations

- Support for FTP and File URL schemes for Proxy Automatic Configuration (PAC) is removed. HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including but not limited to configurations set using Settings, System Preferences, profiles, URLSession APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411499-connectionproxydictionary), and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). (28578280)
- SPDY support is removed from the [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) APIs. Servers should use HTTP 2 or HTTP 1.1. (43391641)
- The Network Kernel Extension API is now deprecated. (49284108)

##### Privacy

###### Known Issues

- The behavior of `access(2)` on privacy-protected filesystem locations has been restored to that of macOS Mojave. (47309955)

##### Remote Desktop

###### Resolved Issues

- Fixed an issue where turning on Curtain Mode prevented you from being able to control a remote Mac. (52900397)

##### Quartz Composer

###### Deprecations

- Starting in macOS 10.15, the Quartz Composer framework is deprecated and remains present for compatibility purposes. Transition to frameworks such as Core Image, SceneKit, or Metal. (50911608)

##### Scripting Language Runtimes

###### Deprecations

- Scripting language runtimes such as Python, Ruby, and Perl are included in macOS for compatibility with legacy software. Future versions of macOS won’t include scripting language runtimes by default, and might require you to install additional packages. If your software depends on scripting languages, it’s recommended that you bundle the runtime within the app. (49764202)
- Use of Python 2.7 isn’t recommended as this version is included in macOS for compatibility with legacy software. Future versions of macOS won’t include Python 2.7. Instead, it’s recommended that you run `python3` from within Terminal. (51097165)

##### Swiftui

###### New Features

- You can now create a [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) from a [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) or [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor). (49833933)
- [`NSManagedObject`](https://developer.apple.com/documentation/CoreData/NSManagedObject) now conforms to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject). The new `@`[`FetchRequest`](https://developer.apple.com/documentation/SwiftUI/FetchRequest) property wrapper can drive views from the results of a fetch request, and [`managedObjectContext`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/managedObjectContext) is now included in the environment. (50280673)
- Gesture modifiers are renamed for consistency. For example, `tapAction(count:_:)` is renamed [`onTapGesture(count:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onTapGesture(count:perform:)), and `longPressAction(minimumDuration:maximumDistance:_:pressing:)` is renamed [`onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)). (50395282)
- [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) now has a default line limit of `nil` so that it wraps by default. (51147116)
- [`ContentSizeCategory`](https://developer.apple.com/documentation/SwiftUI/ContentSizeCategory) and several other enumerations are now [`CaseIterable`](https://developer.apple.com/documentation/Swift/CaseIterable). (51168712)
- `SegmentedControl` is now a style of [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker). (51769046)
- `BindableObject` is replaced by the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol from the Combine framework. (50800624) You can manually conform to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) by defining an [`objectWillChange`](https://developer.apple.com/documentation/Combine/ObservableObject/objectWillChange-5gopl) publisher that emits before the object changes. However, by default, [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) automatically synthesizes [`objectWillChange`](https://developer.apple.com/documentation/Combine/ObservableObject/objectWillChange-5gopl) and emits before any `@`[`Published`](https://developer.apple.com/documentation/Combine/Published) properties change. ```swift
// RoomStore.swift
import Foundation

class RoomStore: ObservableObject {
    @Published var rooms: [Room] = []
}

struct Room: Identifiable {
    var id: UUID
    var name: String
    var capacity: Int
    var hasVideo: Bool
}

// ContentView.swift
import SwiftUI

struct ContentView: View {
    @ObservedObject var store: RoomStore

    var body: some View {
        NavigationView {
            List(store.rooms) { room in
                RoomCell(room: room)
            }
            .navigationBarTitle("Rooms")
        }
    }
}
``` `@ObjectBinding` is replaced by `@`[`ObservedObject`](https://developer.apple.com/documentation/SwiftUI/ObservedObject).
- The [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol is now part of the Swift standard library. As a result, your model files no longer need to import the SwiftUI framework. ([`SE-0261`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0261-identifiable.md))
- The [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues) structure has four new properties for reading accessibility values from the environment: `accessibilityDifferentiateWithoutColor`, `accessibilityReduceTransparency`, `accessibilityReduceMotion`, and `accessibilityInvertColors`. (51712481)
- The `color(_:)` text modifier is renamed [`foregroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/Text/foregroundColor(_:)) for consistency with the more general [`foregroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/View/foregroundColor(_:)) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection) protocol is extended to include a [`remove(atOffsets:)`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection/remove(atOffsets:)) method and the [`MutableCollection`](https://developer.apple.com/documentation/Swift/MutableCollection) protocol is extended to include a [`move(fromOffsets:toOffset:)`](https://developer.apple.com/documentation/Swift/MutableCollection/move(fromOffsets:toOffset:)) method. Each new method takes [`IndexSet`](https://developer.apple.com/documentation/Foundation/IndexSet) instances that you use with the doc://com.apple.documentation/documentation/swiftui/foreach/onmove(perform:) and doc://com.apple.documentation/documentation/SwiftUI/foreach/ondelete(perform:) modifiers on [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/sheet(isPresented:onDismiss:content:)), [`actionSheet(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/actionSheet(isPresented:content:)), [`alert(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/alert(isPresented:content:)), and `isPresented` in the environment, to replace the previous `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The `basic` animations are now named after the curve type — such as [`linear`](https://developer.apple.com/documentation/SwiftUI/Animation/linear) and [`easeInOut`](https://developer.apple.com/documentation/SwiftUI/Animation/easeInOut). The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](https://developer.apple.com/documentation/SwiftUI/Animation/interpolatingSpring(mass:stiffness:damping:initialVelocity:)), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/spring(response:dampingFraction:blendDuration:)) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/interactiveSpring(response:dampingFraction:blendDuration:)), depending on whether or not the animation is driven interactively. (50280375)
- Added an initializer for creating a [`Font`](https://developer.apple.com/documentation/SwiftUI/Font) from a [`CTFont`](https://developer.apple.com/documentation/CoreText/CTFont). (51849885)
- You can style a [`NavigationView`](https://developer.apple.com/documentation/SwiftUI/NavigationView) using two new style properties: [`StackNavigationViewStyle`](https://developer.apple.com/documentation/SwiftUI/StackNavigationViewStyle) and [`DoubleColumnNavigationViewStyle`](https://developer.apple.com/documentation/SwiftUI/DoubleColumnNavigationViewStyle). By default, navigation views on iPhone and Apple TV visually reflect a navigation stack, while on iPad and Mac, a split-view styled navigation view displays. (51636729) When using the [`DoubleColumnNavigationViewStyle`](https://developer.apple.com/documentation/SwiftUI/DoubleColumnNavigationViewStyle) style, you can provide two views when creating a navigation view — the first is the primary and the second is the detail. For example: ```swift
NavigationView {
    MyPrimaryView()
    MyDetailView()
}
.navigationViewStyle(DoubleColumnNavigationViewStyle())
```

###### Known Issues

- Apps containing SwiftUI inside a Swift package might not run on versions of iOS earlier than iOS 13. (53706729) : When back-deploying to an OS which doesn’t contain the SwiftUI framework, add the `-weak_framework SwiftUI` flag to the Other Linker Flags setting in the Build Settings tab. See [`Frameworks and Weak Linking`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WeakLinking.html#//apple_ref/doc/uid/20002378) for more information on weak linking a framework. This workaround doesn’t apply when using dynamically linked Swift packages which import SwiftUI.

###### Deprecations

- The `Command` structure is replaced by passing selectors directly. (53187891)
- `NavigationDestinationLink` and `DynamicNavigationDestinationLink` are deprecated; their functionality is now included in [`NavigationLink`](https://developer.apple.com/documentation/SwiftUI/NavigationLink). (50630794)
- The `Length` type is replaced by [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct). (50654095)
- `TabbedView` is now named [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView). (51012120)
- `HAlignment` and `VAlignment` are now deprecated, use the more flexible [`HorizontalAlignment`](https://developer.apple.com/documentation/SwiftUI/HorizontalAlignment) or [`VerticalAlignment`](https://developer.apple.com/documentation/SwiftUI/VerticalAlignment) types instead and use [`TextAlignment`](https://developer.apple.com/documentation/SwiftUI/TextAlignment) for text. (51190531)
- The `SelectionManager` protocol is removed, use [`Optional`](https://developer.apple.com/documentation/Swift/Optional) and [`Set`](https://developer.apple.com/documentation/Swift/Set) instances directly for selection. (51557694)
- The `isPresented` environment value is deprecated and replaced with the more general [`presentationMode`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/presentationMode) value. (51641238)
- The `StaticMember` protocol is deprecated. Use protocol-conforming types directly instead. For example, use an instance of [`WheelPickerStyle`](https://developer.apple.com/documentation/SwiftUI/WheelPickerStyle) directly rather than the `wheel` static member.(52911961)
- Complex overloads for the [`background(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/background(_:alignment:)) and [`border(_:width:)`](https://developer.apple.com/documentation/SwiftUI/View/border(_:width:)) modifiers are deprecated.

Use shapes in a [`background(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/background(_:alignment:)) or [`overlay(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/overlay(_:alignment:)) to draw these instead. (53067530)

- SwiftUI APIs deprecated in previous betas are now removed. (52587863)
- The `identified(by:)` method on the [`Collection`](https://developer.apple.com/documentation/Swift/Collection) protocol is deprecated in favor of dedicated [`init(_:id:rowContent:)`](https://developer.apple.com/documentation/SwiftUI/List/init(_:id:rowContent:)-4s0aj) and [`init(_:id:content:)`](https://developer.apple.com/documentation/SwiftUI/ForEach/init(_:id:content:)-6p8p9) initializers. (52976883, 52029393) The retroactive conformance of [`Int`](https://developer.apple.com/documentation/Swift/Int) to the Identifiable protocol is removed. Change any code that relies on this conformance to pass .self to the id parameter of the relevant initializer. Constant ranges of Int continue to be accepted: ```swift
List(0..<5) {
  Text("Rooms")
}
``` However, you shouldn’t pass a range that changes at runtime. If you use a variable that changes at runtime to define the range, the list displays views according to the initial range and ignores any subsequent updates to the range.
- Several extensions to the [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) structure are removed. (51624798) If you have code such as the following: ```swift
struct LandmarkList: View {
    var landmark: [Landmark]
    @Binding var favorites: Set<Landmark>

    var body: some View {
        List(landmarks) { landmark in
            Toggle(landmark.name, isOn: self.$favorites.contains(landmarkID))
        }
    }
}
``` Define the following subscript on the Set structure: ```swift
extension Set {
    subscript(member: Element) -> Bool {
        get { contains(member) }
        set {
            if newValue {
                insert(member)
            } else {
                remove(member)
            }
        }
    }
}
``` Then, change `self.$favorites.contains(landmarkID)` to` self.$favorites[landmarkID]`.
- The [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) structure’s conditional conformance to the [`Collection`](https://developer.apple.com/documentation/Swift/Collection) protocol is removed. (51624798) If you have code such as the following: ```swift
struct LandmarkList: View {
    @Binding var landmark: [Landmark]

    var body: some View {
        List(landmarks) { landmark in
            Toggle(landmark.value.name, isOn: landmark[\.isFavorite])
        }
    }
}
``` Define the following collection type: ```swift
struct IndexedCollection<Base: RandomAccessCollection>: RandomAccessCollection {
    typealias Index = Base.Index
    typealias Element = (index: Index, element: Base.Element)

    let base: Base

    var startIndex: Index { base.startIndex }

    var endIndex: Index { base.endIndex }

    func index(after i: Index) -> Index {
        base.index(after: i)
    }

    func index(before i: Index) -> Index {
        base.index(before: i)
    }

    func index(_ i: Index, offsetBy distance: Int) -> Index {
        base.index(i, offsetBy: distance)
    }

    subscript(position: Index) -> Element {
        (index: position, element: base[position])
    }
}

extension RandomAccessCollection {
    func indexed() -> IndexedCollection<Self> {
        IndexedCollection(base: self)
    }
}
``` Then, update your code to: ```swift
struct LandmarkList: View {
    @Binding var landmarks: [Landmark]

    var body: some View {
        List(landmarks.indexed(), id: \.1.id) { (index, landmark) in
            Toggle(landmark.name, isOn: self.$landmarks[index].isFavorite)
        }
    }
}
```
- The `relativeWidth(_:)`, `relativeHeight(_:)`, and `relativeSize(width:height:)` modifiers are deprecated. Use other modifiers like [`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)) instead. (51494692)

##### Xcode

###### Deprecations

- Command line tool support for Subversion — including `svn`, `git-svn`, and related commands — is no longer provided by Xcode. (50266910)

## See Also

- [macOS Catalina 10.15.6 Release Notes](macos-catalina-10_15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.5 Release Notes](macos-catalina-10_15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.4 Release Notes](macos-catalina-10_15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.3 Release Notes](macos-catalina-10_15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.2 Release Notes](macos-catalina-10_15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.1 Release Notes](macos-catalina-10_15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-catalina-10_15-release-notes)*