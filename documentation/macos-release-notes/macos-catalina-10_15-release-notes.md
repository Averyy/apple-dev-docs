# macOS Catalina 10.15 Release Notes

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 10.15 SDK provides support for developing apps for Macs running macOS Catalina 10.15. The SDK comes bundled with Xcode 11. For information on the compatibility requirements for Xcode 11, see [Xcode 11 Release Notes](../Xcode-Release-Notes/xcode-11-release-notes.md).

##### General

###### Known Issues

- During installation of macOS 10.15 you might be prompted to enter your administrator password multiple times to allow installation to proceed. (51206649)

###### Deprecations

- macOS frameworks are now thinned for the x86-64 architecture. Apps that execute i386 code now fail with the [`EBADARCH`](../Foundation/posixerror/ebadarch.md) error code. The remaining stub frameworks are nonfunctional and exist only for compatibility purposes. (51236070)

##### AirDrop

###### Known Issues

- AirDrop doesn’t work when a VPN is connected with the [`includeAllNetworks`](../NetworkExtension/nevpnprotocol/includeallnetworks.md) and [`excludeLocalNetworks`](../NetworkExtension/nevpnprotocol/excludelocalnetworks.md) options enabled. (52618489)

  **Workaround:** Disconnect the VPN before using AirDrop.

##### AppleEvents

###### New Features

- To enhance security, AppleEvents and AppleScripts that target an app on a remote system must authenticate as the same user on the remote system. An AppleEvent that targets an app running as a different user receives a `procNotFound` error.To allow remote AppleEvents to target apps in any user session, run the following command in Terminal on the server:

  `defaults write /Library/Preferences/com.apple.AEServer RestrictAccessToUserSession -bool false`

  Then disable and reenable Remote Apple Events in System Preferences > Sharing. (5353592)

##### Audio

###### New Features

- You can now enable voice processing mode on [`AVAudioEngine`](../AVFAudio/avaudioengine.md). (50906329)
- You can use new [`AVAudioNode`](../AVFAudio/avaudionode.md) types to wrap a user-defined block for sending or receiving data in real-time.
- A new method is available for an [`AVAudioEngine`](../AVFAudio/avaudioengine.md) based app to retrieve a list of all nodes attached to an [`AVAudioEngine`](../AVFAudio/avaudioengine.md) instance.
- A new rendering mode in [`AVAudioEnvironmentNode`](../AVFAudio/avaudioenvironmentnode.md) selects the best spatial audio rendering algorithm automatically based on the output device.
- A new [`AVAudioSession`](../AVFAudio/avaudiosession.md) property allows system sounds and haptics to play while the session is actively using audio input.
- A new property, [`AVAudioSession.PromptStyle`](../AVFAudio/avaudiosession/promptstyle-swift.enum.md) informs apps which style of voice prompt they should play based on other audio activity in the system.
- The [`AVAudioSession.RouteSharingPolicy`](../AVFAudio/avaudiosession/routesharingpolicy-swift.enum.md) enumeration is extended to allow apps to specify route sharing policies so their audio and video is routed to the same location as AirPlay.
- Audio Unit Extensions now support user presets that are available across all host apps.

###### Deprecations

- The `OpenAL` framework is deprecated and remains present for compatibility purposes. Transition to [`AVAudioEngine`](../AVFAudio/avaudioengine.md) for spatial audio functionality.
- [`AUGraph`](../AudioToolbox/augraph.md) is deprecated in favor of [`AVAudioEngine`](../AVFAudio/avaudioengine.md).
- Inter-App audio is deprecated. Use Audio Units for this functionality.
- Carbon component-based Audio Units are deprecated and support will be removed in a future release.
- Legacy Core Audio HAL audio hardware plug-ins are no longer supported.  Use Audio Server plug-ins for audio drivers.

##### AVFoundation

###### New Features

- The [`AVPlayer`](../AVFoundation/avplayer.md) class includes two new properties, [`eligibleForHDRPlayback`](../AVFoundation/avplayer/eligibleforhdrplayback.md) and [`eligibleForHDRPlaybackDidChangeNotification`](../AVFoundation/avplayer/eligibleforhdrplaybackdidchangenotification.md), which you can use to determine whether an HDR display is available and can play on the current device. (35938145)
- AVFoundation now supports encoding video with alpha channels using HEVC. Videos encoded in this manner are broadly supported in AVFoundation APIs and by Safari within web pages. Technical details of the format can be found in the Interoperability Profile specification. (8045917)

###### Deprecations

- The previously deprecated 32-bit QuickTime framework is no longer available in macOS 10.15.
- The symbols for QTKit, which relied on the QuickTime framework, are still present but the classes are non-functional.

##### Camera

###### Known Issues

- Apps using Picture Taker must specify the [`NSCameraUsageDescription`](../BundleResources/information-property-list/nscamerausagedescription.md) key to access the FaceTime camera. (47916725)

##### Core Image

###### New Features

- The [`init(imageURL:options:)`](../CoreImage/cifilter-swift.class/init%28imageurl,options%29.md) and [`init(imageData:options:)`](../CoreImage/cifilter-swift.class/init%28imagedata,options%29.md) initializers no longer support RAW decoder versions earlier than 6. Version 6 and later remain supported. (50911303)
- Added new APIs for instantiating and modifying the built-in Core Image filters.
- The [`CICoreMLModel`](../CoreImage/cicoremlmodel.md) filter is enhanced to support models with an input or output of type [`MLFeatureType.multiArray`](../CoreML/mlfeaturetype/multiarray.md).
- Metal [`CIKernel`](../CoreImage/cikernel.md) instances now support arguments with arbitrarily structured data.
- Metal [`CIKernel`](../CoreImage/cikernel.md) instances now support returning a group of two by two pixels.
- The integer values of [`CIFormat`](../CoreImage/ciformat.md) symbols, such as [`ARGB8`](../CoreImage/ciformat/argb8.md), have changed to a new set of values which are consistent across platforms. The former values remain supported for backward compatibility; however, you should avoid dependancies on specific numerical values.

##### EndpointSecurity

###### Deprecations

- The `kauth` API has been deprecated. (50419013)

##### iCloud

###### Known Issues

- After updating to macOS Catalina 10.15 Beta 7 or later, iCloud Drive might synchronize for an extended period of time. If you notice any missing files, they can be found inside a Recovered Files folder in your home folder. (54046219)
- Even when Optimize Storage is switched off, iCloud Drive might fail to automatically download all files. (50667204)

  **Workaround:** Download files individually.
- When creating a new Pages, Numbers, or Keynote document in a shared folder, you might see the message “Couldn’t connect to iCloud”. (50827963)

  **Workaround:** Close and reopen the document.

##### Launch Daemons and Agents

###### New Features

- Launch daemons and launch agents introduce new user privacy protections. Specifying privacy-sensitive files and folders in a launchd property list might not work as expected and prevent the service from running. Having `Program` or `ProgramArguments` pointing to an executable in a privacy sensitive location is currently allowed, but may be restricted in a future release. (49702405)

  To comply with the new privacy protections, resources for a launchd service must be stored in locations that aren’t privacy sensitive. If necessary, the app can set up resources during its execution rather than using launchd property list keys, making it possible to grant the app access using System Preferences > Security & Privacy > Privacy. The following launchd property list keys are affected: `KeepAlive`, `PathState`, `QueueDirectories`, `Sockets`, `SockPathName`, `StandardErrorPath`, `StandardInPath`, `StandardOutPath`, and `WatchPaths`.

##### Mac Catalyst

###### Known Issues

- [`nativeScale`](../UIKit/uiscreen/nativescale.md) might be inaccurate. Instead, get the scale factor from the local trait collection. (54009624)
- [`MPMediaPickerController`](../MediaPlayer/mpmediapickercontroller.md) might not display the contents of your library. (51785735)
- AppKit and Mac Catalyst apps are currently view-only clients of [PencilKit](../PencilKit/PencilKit.md). (51146823)
- The [`UIScreen`](../UIKit/uiscreen.md) class’s [`isCaptured`](../UIKit/uiscreen/iscaptured.md) API isn’t currently supported. (48360589)
- The [`current`](../UIKit/uidevice/current.md) property on [`UIDevice`](../UIKit/uidevice.md) and the OS Product Name is currently returned as iOS rather than macOS, which can affect diagnostic logs generated by your system. (49792004)
- When sending Mail attachments via [Message UI](../MessageUI/MessageUI.md), each attachment might appear as two icons when viewed by the recipient. (50369995)
- Controls drawn with accent color incorrectly maintain their active color when the window is inactive. There is no need to work around this in your app. (50563638)
- For Mac Catalyst apps to save to Photos Library, explicitly linking the Photos framework is required. (50781430)
- Action and share extensions might exhibit visual anomalies. (51005363)
- All assets at 3x scale factor are currently ignored when compiling the asset catalog for Mac Catalyst apps. Because the search begins with the universal asset, assets for a specific memory or graphics class won’t be found. For example, if you provide an image and only give a 6GB and Metal 5v1 asset, it won’t be found at runtime. It’s recommended that you provide all images as vectors to allow generation of the correct scale factors, or at minimum provide 2x versions of the assets. If you’re classifying resources based on memory and graphics families then you should provide “Any Memory” and “Any Graphics”. (51033745)
- CallKit [`CXAction`](../CallKit/cxaction.md) instances might return an error. (51074735)
- When creating a Mac Catalyst app from your iPad app, Xcode automatically generates a unique Mac bundle identifier. If you have an existing Mac bundle identifier you’d prefer to use, you can do so by using manual signing in Xcode. (51076014)

  Follow these steps to configure your project, AppID, and provisioning profile:

  1. [Sign in to Apple Developer](https://developer.apple.com/account), then select Certificates, Identifiers, and Profiles.
  2. In the Identifiers section, select your iOS app identifier to edit.
  3. Check the Mac Catalyst capability to enable it, then click the Configure button.
  4. Choose Use an existing macOS AppID and select the identifier you’d like to use from the popup menu. Click the Save button to finish editing your AppID.
  5. In the Profiles section, click the **+** button to create a new profile, select ‘macOS App Development’, and click Continue.
  6. Select your iOS AppID from the popup, click Continue, and complete the rest of the profile creation flow. When finished, click the Download button.
  7. In Xcode, select your project to view the Project Editor and select your app’s target. Then select the Build Settings tab.
  8. Set the Derive Mac Catalyst Product Bundle Identifier setting to No.
  9. Expand the Product Bundle Identifier build setting to view its configurations.Next to the Debug configuration, click the **+** button to add a conditional value.
  10. For the build setting condition, select Any macOS from the popup menu. Edit the value of the conditional build setting to match the macOS bundle identifier you want to use. Repeat this step for all  configurations in your project.
  11. In the Signing & Capabilities tab, uncheck Automatically manage signing.
  12. For your macOS app, select Import Profile from the Provisioning Profile popup and then select the profile you downloaded earlier.
- Catalyst apps using [`UIDocumentInteractionController`](../UIKit/uidocumentinteractioncontroller.md) might quit unexpectedly. You can work around this issue by excluding [`UIDocumentInteractionController`](../UIKit/uidocumentinteractioncontroller.md) functionality with target macros. (48878552)
- DOM keyboard events aren’t dispatched as expected in [`WKWebView`](../WebKit/wkwebview.md) when pressing or releasing keys. Web apps needing to track typed characters can instead listen for DOM input events. (54580414)

##### Mail

###### Known Issues

- If your Mac contains both macOS Mojave 10.14 and macOS 10.15 volumes, you might experience issues searching in Mail. (46611310)

  **Workaround:** While running macOS Mojave 10.14, open Terminal and execute the following command:

  `sudo touch /.metadata_never_index_unless_rootfs`

  Reboot into macOS 10.15, open Terminal and execute the following command:

  `sudo touch /System/Volumes/Data/.metadata_never_index_unless_rootfs`

  Reboot into macOS Mojave 10.14, open Terminal and execute the following command:

  `sudo mdutil -E /`

  Depending on the size of your Mail database, it might take many hours to reindex all content.

##### Networking

###### New Features

- [`NSURLRequest.CachePolicy.reloadRevalidatingCacheData`](../Foundation/nsurlrequest/cachepolicy-swift.enum/reloadrevalidatingcachedata.md) and [`NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData`](../Foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md) APIs are now available. (49660334)
- All [`URLSessionTask`](../Foundation/urlsessiontask.md) instances with a GET HTTP method which contain a body will now produce the error [`NSURLErrorDataLengthExceedsMaximum`](../Foundation/nsurlerrordatalengthexceedsmaximum-swift.var.md). (46025234)

###### Known Issues

- The [`NWEthernetChannel`](../Network/nwethernetchannel.md) API doesn’t currently support VLAN interfaces. [`NEPacketTunnelProvider`](../NetworkExtension/nepackettunnelprovider.md) will see both tagged and untagged frames arriving on physical interfaces. Depending on the Ethernet driver, VLAN tags might be processed by hardware and thus stripped off the Ethernet frames thus [`NEPacketTunnelProvider`](../NetworkExtension/nepackettunnelprovider.md) won’t see the VLAN tag. (51275655)

###### Deprecations

- Support for FTP and File URL schemes for Proxy Automatic Configuration (PAC) is removed. HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including but not limited to configurations set using Settings, System Preferences, profiles, URLSession APIs such as [`connectionProxyDictionary`](../Foundation/urlsessionconfiguration/connectionproxydictionary.md), and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](../CFNetwork/cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md). (28578280)
- SPDY support is removed from the [`URLSession`](../Foundation/urlsession.md) and [`NSURLConnection`](../Foundation/nsurlconnection.md) APIs. Servers should use HTTP 2 or HTTP 1.1. (43391641)
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

##### SwiftUI

###### New Features

- You can now create a [`Color`](../SwiftUI/color.md) from a [`UIColor`](../UIKit/uicolor.md) or [`NSColor`](../AppKit/nscolor.md). (49833933)
- [`NSManagedObject`](../CoreData/nsmanagedobject.md) now conforms to [`ObservableObject`](../Combine/observableobject.md). The new `@`[`FetchRequest`](../SwiftUI/fetchrequest.md) property wrapper can drive views from the results of a fetch request, and [`managedObjectContext`](../SwiftUI/environmentvalues/managedobjectcontext.md) is now included in the environment. (50280673)
- Gesture modifiers are renamed for consistency. For example, `tapAction(count:_:)` is renamed [`onTapGesture(count:perform:)`](../SwiftUI/view/ontapgesture%28count,perform%29.md), and `longPressAction(minimumDuration:maximumDistance:_:pressing:)` is renamed [`onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)`](../SwiftUI/view/onlongpressgesture%28minimumduration,maximumdistance,pressing,perform%29.md). (50395282)
- [`Text`](../SwiftUI/text.md) now has a default line limit of `nil` so that it wraps by default. (51147116)
- [`ContentSizeCategory`](../SwiftUI/contentsizecategory.md) and several other enumerations are now [`CaseIterable`](../Swift/caseiterable.md). (51168712)
- `SegmentedControl` is now a style of [`Picker`](../SwiftUI/picker.md). (51769046)
- `BindableObject` is replaced by the [`ObservableObject`](../Combine/observableobject.md) protocol from the Combine framework. (50800624)

  You can manually conform to [`ObservableObject`](../Combine/observableobject.md) by defining an [`objectWillChange`](../Combine/observableobject/objectwillchange-5gopl.md) publisher that emits before the object changes. However, by default, [`ObservableObject`](../Combine/observableobject.md) automatically synthesizes [`objectWillChange`](../Combine/observableobject/objectwillchange-5gopl.md) and emits before any `@`[`Published`](../Combine/published.md) properties change.

  ```swift
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
  ```

  `@ObjectBinding` is replaced by `@`[`ObservedObject`](../SwiftUI/observedobject.md).
- The [`Identifiable`](../Swift/identifiable.md) protocol is now part of the Swift standard library. As a result, your model files no longer need to import the SwiftUI framework. ([SE-0261](https://github.com/apple/swift-evolution/blob/master/proposals/0261-identifiable.md))
- The [`EnvironmentValues`](../SwiftUI/environmentvalues.md) structure has four new properties for reading accessibility values from the environment: `accessibilityDifferentiateWithoutColor`, `accessibilityReduceTransparency`, `accessibilityReduceMotion`, and `accessibilityInvertColors`. (51712481)
- The `color(_:)` text modifier is renamed [`foregroundColor(_:)`](../SwiftUI/text/foregroundcolor%28_%29.md) for consistency with the more general [`foregroundColor(_:)`](../SwiftUI/view/foregroundcolor%28_%29.md) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](../Swift/rangereplaceablecollection.md) protocol is extended to include a [`remove(atOffsets:)`](../Swift/rangereplaceablecollection/remove%28atoffsets%29.md) method and the [`MutableCollection`](../Swift/mutablecollection.md) protocol is extended to include a [`move(fromOffsets:toOffset:)`](../Swift/mutablecollection/move%28fromoffsets,tooffset%29.md) method. Each new method takes [`IndexSet`](../Foundation/indexset.md) instances that you use with the `onMove(perform:)` and `onDelete(perform:)` modifiers on [`ForEach`](../SwiftUI/foreach.md) views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](../SwiftUI/view/sheet%28ispresented,ondismiss,content%29.md), [`actionSheet(isPresented:content:)`](../SwiftUI/view/actionsheet%28ispresented,content%29.md), [`alert(isPresented:content:)`](../SwiftUI/view/alert%28ispresented,content%29.md), and `isPresented` in the environment, to replace the previous `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The `basic` animations are now named after the curve type — such as [`linear`](../SwiftUI/animation/linear.md) and [`easeInOut`](../SwiftUI/animation/easeinout.md). The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](../SwiftUI/animation/interpolatingspring%28mass,stiffness,damping,initialvelocity%29.md), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/spring%28response,dampingfraction,blendduration%29.md) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/interactivespring%28response,dampingfraction,blendduration%29.md), depending on whether or not the animation is driven interactively. (50280375)
- Added an initializer for creating a [`Font`](../SwiftUI/font.md) from a [`CTFont`](../CoreText/ctfont.md). (51849885)
- You can style a [`NavigationView`](../SwiftUI/navigationview.md) using two new style properties: [`StackNavigationViewStyle`](../SwiftUI/stacknavigationviewstyle.md) and [`DoubleColumnNavigationViewStyle`](../SwiftUI/doublecolumnnavigationviewstyle.md). By default, navigation views on iPhone and Apple TV visually reflect a navigation stack, while on iPad and Mac, a split-view styled navigation view displays. (51636729)

  When using the [`DoubleColumnNavigationViewStyle`](../SwiftUI/doublecolumnnavigationviewstyle.md) style, you can provide two views when creating a navigation view — the first is the primary and the second is the detail. For example:

  ```swift
  NavigationView {
      MyPrimaryView()
      MyDetailView()
  }
  .navigationViewStyle(DoubleColumnNavigationViewStyle())
  ```

###### Known Issues

- Apps containing SwiftUI inside a Swift package might not run on versions of iOS earlier than iOS 13. (53706729)

  **Workaround**: When back-deploying to an OS which doesn’t contain the SwiftUI framework, add the `-weak_framework SwiftUI` flag to the Other Linker Flags setting in the Build Settings tab. See [Frameworks and Weak Linking](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WeakLinking.html#//apple_ref/doc/uid/20002378) for more information on weak linking a framework. This workaround doesn’t apply when using dynamically linked Swift packages which import SwiftUI.

###### Deprecations

- The `Command` structure is replaced by passing selectors directly. (53187891)
- `NavigationDestinationLink` and `DynamicNavigationDestinationLink` are deprecated; their functionality is now included in [`NavigationLink`](../SwiftUI/navigationlink.md). (50630794)
- The `Length` type is replaced by [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md). (50654095)
- `TabbedView` is now named [`TabView`](../SwiftUI/tabview.md). (51012120)
- `HAlignment` and `VAlignment` are now deprecated, use the more flexible [`HorizontalAlignment`](../SwiftUI/horizontalalignment.md) or [`VerticalAlignment`](../SwiftUI/verticalalignment.md) types instead and use [`TextAlignment`](../SwiftUI/textalignment.md) for text. (51190531)
- The `SelectionManager` protocol is removed, use [`Optional`](../Swift/optional.md) and [`Set`](../Swift/set.md) instances directly for selection. (51557694)
- The `isPresented` environment value is deprecated and replaced with the more general [`presentationMode`](../SwiftUI/environmentvalues/presentationmode.md) value. (51641238)
- The `StaticMember` protocol is deprecated. Use protocol-conforming types directly instead. For example, use an instance of [`WheelPickerStyle`](../SwiftUI/wheelpickerstyle.md) directly rather than the `wheel` static member.(52911961)
- Complex overloads for the [`background(_:alignment:)`](../SwiftUI/view/background%28_,alignment%29.md) and [`border(_:width:)`](../SwiftUI/view/border%28_,width%29.md) modifiers are deprecated.

Use shapes in a [`background(_:alignment:)`](../SwiftUI/view/background%28_,alignment%29.md) or [`overlay(_:alignment:)`](../SwiftUI/view/overlay%28_,alignment%29.md) to draw these instead. (53067530)

- SwiftUI APIs deprecated in previous betas are now removed. (52587863)
- The `identified(by:)` method on the [`Collection`](../Swift/collection.md) protocol is deprecated in favor of dedicated [`init(_:id:rowContent:)`](../SwiftUI/list/init%28_,id,rowcontent%29-4s0aj.md) and [`init(_:id:content:)`](../SwiftUI/foreach/init%28_,id,content%29.md) initializers. (52976883, 52029393)

  The retroactive conformance of [`Int`](../Swift/int.md) to the Identifiable protocol is removed. Change any code that relies on this conformance to pass .self to the id parameter of the relevant initializer. Constant ranges of Int continue to be accepted:

  ```swift
  List(0..<5) {
    Text("Rooms")
  }
  ```

  However, you shouldn’t pass a range that changes at runtime. If you use a variable that changes at runtime to define the range, the list displays views according to the initial range and ignores any subsequent updates to the range.
- Several extensions to the [`Binding`](../SwiftUI/binding.md) structure are removed. (51624798)

  If you have code such as the following:

  ```swift
  struct LandmarkList: View {
      var landmark: [Landmark]
      @Binding var favorites: Set<Landmark>

      var body: some View {
          List(landmarks) { landmark in
              Toggle(landmark.name, isOn: self.$favorites.contains(landmarkID))
          }
      }
  }
  ```

  Define the following subscript on the Set structure:

  ```swift
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
  ```

  Then, change `self.$favorites.contains(landmarkID)` to` self.$favorites[landmarkID]`.
- The [`Binding`](../SwiftUI/binding.md) structure’s conditional conformance to the [`Collection`](../Swift/collection.md) protocol is removed. (51624798)

  If you have code such as the following:

  ```swift
  struct LandmarkList: View {
      @Binding var landmark: [Landmark]

      var body: some View {
          List(landmarks) { landmark in
              Toggle(landmark.value.name, isOn: landmark[\.isFavorite])
          }
      }
  }
  ```

  Define the following collection type:

  ```swift
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
  ```

  Then, update your code to:

  ```swift
  struct LandmarkList: View {
      @Binding var landmarks: [Landmark]

      var body: some View {
          List(landmarks.indexed(), id: \.1.id) { (index, landmark) in
              Toggle(landmark.name, isOn: self.$landmarks[index].isFavorite)
          }
      }
  }
  ```
- The `relativeWidth(_:)`, `relativeHeight(_:)`, and `relativeSize(width:height:)` modifiers are deprecated. Use other modifiers like [`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`](../SwiftUI/view/frame%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight,alignment%29.md) instead. (51494692)

##### Xcode

###### Deprecations

- Command line tool support for Subversion — including `svn`, `git-svn`, and related commands — is no longer provided by Xcode. (50266910)

## See Also

### macOS 10.15
- [macOS Catalina 10.15.6 Release Notes](./macos-catalina-10_15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.5 Release Notes](./macos-catalina-10_15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.4 Release Notes](./macos-catalina-10_15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.3 Release Notes](./macos-catalina-10_15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.2 Release Notes](./macos-catalina-10_15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.1 Release Notes](./macos-catalina-10_15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-catalina-10_15-release-notes)*