# iOS & iPadOS 13.1 Release Notes

**Framework**: iOS & iPadOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 13.1 SDK provides support for developing apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 13.1. The SDK comes bundled with Xcode 11. For information on the compatibility requirements for Xcode 11, see [Xcode 11 Release Notes](../Xcode-Release-Notes/xcode-11-release-notes.md).

##### General

###### Known Issues

- Snapshots for apps that use Metal might have an unexpected appearance in the App Switcher. (53121694)

###### Deprecations

- The [`UIApplicationExitsOnSuspend`](../BundleResources/information-property-list/uiapplicationexitsonsuspend.md) key is no longer supported in iOS & iPadOS 13. Update your apps to handle modern multitasking. (43958234)

##### Audio

###### New Features

- Voice Processing mode can now be enabled on [`AVAudioEngine`](../AVFAudio/avaudioengine.md). (50906329)
- New [`AVAudioNode`](../AVFAudio/avaudionode.md) types can be used to wrap a user-defined block for sending or receiving data in real time.
- A new method is available for an [`AVAudioEngine`](../AVFAudio/avaudioengine.md)-based app to retrieve a list of all nodes attached to an [`AVAudioEngine`](../AVFAudio/avaudioengine.md) instance.
- A new rendering mode in [`AVAudioEnvironmentNode`](../AVFAudio/avaudioenvironmentnode.md) selects the best spatial audio rendering algorithm automatically based on the output device.
- A new [`AVAudioSession`](../AVFAudio/avaudiosession.md) property allows system sounds and haptics to play while the session actively uses audio input.
- A new enumeration, [`AVAudioSession.PromptStyle`](../AVFAudio/avaudiosession/promptstyle-swift.enum.md), informs apps which style of voice prompt they should play based on other audio activity in the system.
- [`AVAudioSession.RouteSharingPolicy`](../AVFAudio/avaudiosession/routesharingpolicy-swift.enum.md) now permits apps to specify route-sharing policies so their audio and video routes to the same location as AirPlay.
- Audio Unit Extensions now support user presets that are available across all host applications.

###### Deprecations

- The OpenAL framework is deprecated and remains present for compatibility purposes. Transition to [`AVAudioEngine`](../AVFAudio/avaudioengine.md) for spatial audio functionality.
- [`AUGraph`](../AudioToolbox/augraph.md) is deprecated in favor of [`AVAudioEngine`](../AVFAudio/avaudioengine.md).
- Inter-App audio is deprecated. Use Audio Units for this functionality moving forward.
- Carbon component-based Audio Units are deprecated and support will be removed in a future release.
- Legacy Core Audio HAL audio hardware plug-ins are no longer supported.  Use audio server plug-ins for audio drivers moving forward.

##### Audio Sharing

###### New Features

- Audio sharing is compatible with AirPods (1st generation or later) and PowerBeats Pro. iPhone 8 or later, iPad Pro 12.9-inch (2nd generation or later), iPad Pro 11-inch, iPad Pro 10.5-inch, iPad (5th generation or later), iPad Air (3rd generation), iPad mini (5th generation), or iPod touch (7th generation or later) is required. (51331268)

##### AVFoundation

###### New Features

- [AVFoundation](../AVFoundation/AVFoundation.md) now supports encoding video with alpha channels using HEVC.  Videos encoded in this manner are broadly supported in AVFoundation APIs, and by Safari within web pages. Technical details of the format can be found in the Interoperability Profile specification. (8045917)

##### Core Haptics

###### Known Issues

- By default, haptics are disabled when microphone recording begins. You can override this by setting the [`AVAudioSession`](../AVFAudio/avaudiosession.md) property [`allowHapticsAndSystemSoundsDuringRecording`](../AVFAudio/avaudiosession/allowhapticsandsystemsoundsduringrecording.md) to `true` before activating its audio session. (25811898)
- Events — such as [`audioContinuous`](../CoreHaptics/chhapticevent/eventtype/audiocontinuous.md), [`hapticContinuous`](../CoreHaptics/chhapticevent/eventtype/hapticcontinuous.md), and [`audioCustom`](../CoreHaptics/chhapticevent/eventtype/audiocustom.md) — can’t be resumed during the event; no output occurs for that event, only for subsequent events. This applies to playback at a specific time offset, seeking, and resuming. (29274583)
- [`CHHapticDynamicParameter`](../CoreHaptics/chhapticdynamicparameter.md) instances with nonzero relative times that are sent as part of a [`sendParameters(_:atTime:)`](../CoreHaptics/chhapticpatternplayer/sendparameters%28_,attime%29.md) call on a [`CHHapticAdvancedPatternPlayer`](../CoreHaptics/chhapticadvancedpatternplayer.md) with the `atTime` parameter set to `0.0` are incorrectly applied at the beginning of the [`CHHapticPattern`](../CoreHaptics/chhapticpattern.md), instead of the expected nonzero relative time. This doesn’t occur on a [`CHHapticPatternPlayer`](../CoreHaptics/chhapticpatternplayer.md). (46316890)
- Both vibrations generated through [`AudioServicesPlaySystemSound(_:)`](../AudioToolbox/audioservicesplaysystemsound%28_%29.md) and vibration patterns generated through the user-created tap-to-vibrate UI are attenuated when compared to prior versions of iOS. (47448156)
- Parameter Curves are not supported with a [`CHHapticAdvancedPatternPlayer`](../CoreHaptics/chhapticadvancedpatternplayer.md), only a [`CHHapticPatternPlayer`](../CoreHaptics/chhapticpatternplayer.md). No error is generated when a [`CHHapticPattern`](../CoreHaptics/chhapticpattern.md) containing a Parameter Curve is passed to a [`CHHapticAdvancedPatternPlayer`](../CoreHaptics/chhapticadvancedpatternplayer.md). (47891515)
- Brief audio distortion occurs when starting a Playback category app such as Music in the background. For example, brief distortion occurs if you start the app from Control Center while Core Haptics audio playback using a [`playAndRecord`](../AVFAudio/avaudiosession/category-swift.struct/playandrecord.md) audio session is already underway. (48121467)
- Following any decompression to uncompressed floating-point samples, the total limit on all [`audioCustom`](../CoreHaptics/chhapticevent/eventtype/audiocustom.md) resources per process is eight megabytes. (48659023)
- Multiple overlapping Parameter Curves for the same [`CHHapticDynamicParameter.ID`](../CoreHaptics/chhapticdynamicparameter/id.md) might result in playback artifacts. (50026384)
- The maximum duration for a [`hapticContinuous`](../CoreHaptics/chhapticevent/eventtype/hapticcontinuous.md) haptic event is 30 seconds. Events exceeding this limit can be constructed and accepted by [`CHHapticPatternPlayer`](../CoreHaptics/chhapticpatternplayer.md), but haptic playback will fade out after 30 seconds. (51322525)
- There is a limit of 16 control points for any type of Parameter Curve. If more control points are desired, create additional parameter curves for consecutive windows of time for the same parameter. (49486454)

##### Core Image

###### New Features

- The [`init(imageURL:options:)`](../CoreImage/cifilter-swift.class/init%28imageurl,options%29.md) and [`init(imageData:options:)`](../CoreImage/cifilter-swift.class/init%28imagedata,options%29.md) initializers no longer support RAW version 5 and earlier. Version 6 and later remain supported. (50911303)
- Added new APIs for instantiating and modifying the built-in Core Image filters.
- The [`CICoreMLModel`](../CoreImage/cicoremlmodel.md) filter is enhanced to support models with an input or output of type [`MLFeatureType.multiArray`](../CoreML/mlfeaturetype/multiarray.md).
- Metal [`CIKernel`](../CoreImage/cikernel.md) instances support arguments with arbitrarily structured data.
- Metal [`CIKernel`](../CoreImage/cikernel.md) instances support returning a group of 2 × 2 pixels.
- The integer values of [`CIFormat`](../CoreImage/ciformat.md) symbols, such as [`ARGB8`](../CoreImage/ciformat/argb8.md), have changed to a new set of values that are consistent across platforms. The former values remain supported for backward compatibility; however, you should avoid dependancies on specific numerical values.

##### Find My

###### Known Issues

- When performing an action in Find My that generates an email, you might see references to the Find My Friends and Find My iPhone apps. (51123613)

##### iCloud

###### Known Issues

- You might be unable to delete the Recovered Files folder in On My iPad/iPhone. (54785368)

  **Workaround**: Back up your device, erase it, restore from backup, then try again.
- After updating to iOS 13 beta 6 or later, iCloud Drive might synchronize for an extended period of time. If you notice any missing files, they can be found in a Recovered Files folder under On My iPhone/iPad within the Files app. (53772753)
- When creating a new Pages, Numbers, or Keynote document in a shared folder, you might see the message: “Couldn’t connect to iCloud.” (50827963)

  **Workaround:** Close and reopen the document.

##### Mail

###### New Features

- Ignore Blocked Senders can now be enabled in Settings > Mail. The blocked contacts list is shared with Messages, FaceTime, and Phone. (50775961)

##### Metal

###### Known Issues

- In iOS 13, if you refer to a sparse texture in an argument buffer you must explicitly call [`useResource(_:usage:stages:)`](../Metal/mtlrendercommandencoder/useresource%28_,usage,stages%29.md) on the texture rather than calling [`useHeap(_:)`](../Metal/mtlrendercommandencoder/useheap%28_%29.md) on the heap. (54605833)

##### Networking

###### New Features

- To enhance security, [`URLSession`](../Foundation/urlsession.md) no longer sniffs the MIME type when the server sends `Content-Type: application/octet-stream`. (7820658)
- [`NSURLRequest.CachePolicy.reloadRevalidatingCacheData`](../Foundation/nsurlrequest/cachepolicy-swift.enum/reloadrevalidatingcachedata.md) and [`NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData`](../Foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md) APIs are now available. (49660334)
- Starting with iOS 13 beta 4, the copy attribute of the [`httpBodyStream`](../Foundation/nsmutableurlrequest/httpbodystream.md) property of [`NSMutableURLRequest`](../Foundation/nsmutableurlrequest.md) is enforced. If the body data is mutated after the property setter has been called, data sent in the HTTP request won’t include that mutation. Invoking the property getter no longer returns a [`NSMutableData`](../Foundation/nsmutabledata.md) reference, even when the setter was invoked with data of that type. As of iOS 13 beta 5, apps built using the iOS 12 SDK or previous SDKs use the legacy behavior. (53427882)
- The [`CNCopyCurrentNetworkInfo`](../SystemConfiguration/cncopycurrentnetworkinfo.md) API has changed to address privacy. Please refer to the updated API documentation and headers for more details. (52707167)
- All [`URLSessionTask`](../Foundation/urlsessiontask.md) instances with a `GET` HTTP method that contain a body now produce the error [`NSURLErrorDataLengthExceedsMaximum`](../Foundation/nsurlerrordatalengthexceedsmaximum-swift.var.md). (46025234)

###### Deprecations

- Removed support for FTP and File URL schemes for Proxy Automatic Configuration (PAC). HTTP and HTTPS are the only supported URL schemes for PAC. This affects all PAC configurations including, but not limited to, configurations set using Settings, System Preferences, Profiles, and [`URLSession`](../Foundation/urlsession.md) APIs such as [`connectionProxyDictionary`](../Foundation/urlsessionconfiguration/connectionproxydictionary.md) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](../CFNetwork/cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md). (28578280)
- The [`URLSession`](../Foundation/urlsession.md) and [`NSURLConnection`](../Foundation/nsurlconnection.md) APIs no longer support SPDY. Servers should use HTTP 2 or HTTP 1.1. (43391641)

##### RealityKit

###### Known Issues

- The camera feed will remain visible at the base of objects loaded from a Reality File when [`ARView.Environment.Background`](../RealityKit/arview/environment-swift.struct/background-swift.struct.md) is set to `ARView.Environment.Background.skybox(_:)` (53715030)

  **Workaround**: Turn off grounding shadows when setting the background to `ARView.Environment.Background.skybox(_:)` by setting [`ARView.RenderOptions`](../RealityKit/arview/renderoptions-swift.struct.md) to [`disableGroundingShadows`](../RealityKit/arview/renderoptions-swift.struct/disablegroundingshadows.md).

##### Screen Time

###### Known Issues

- If you enable Share Across Devices, Screen Time settings don’t sync with iCloud until your iOS device is restarted. Any edits you make to your Screen Time settings on that device before restarting are lost. (50194586)

##### Sidecar

###### Known Issues

- To use Sidecar with iPadOS 13.1 beta 2 or later, macOS Catalina Beta 8 or later is required. (54903543)

##### Siri

###### Known Issues

- The [`supportsOnDeviceRecognition`](../Speech/sfspeechrecognizer/supportsondevicerecognition.md) property always returns `false` the first time it’s accessed. After a few seconds, accessing it again returns the correct value. (47822242)
- Shortcuts opened on iOS & iPadOS 13 beta are automatically upgraded and can no longer be opened on iOS 12. If a device with iOS 12 and a device with iOS 13 share an iCloud account, shortcuts might become unusable on the device running iOS 12. (50873839)

  **Workaround:** Disable iCloud Sync between devices running iOS & iPadOS 13 beta and devices running iOS 12.
- Currently, the only supported response for `INSearchForMediaIntent` is `continueInApp`. (51010311)

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
  // RoomStore.Swift

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

  // ContentView.Swift
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
- The [`Identifiable`](../Swift/identifiable.md) protocol is now part of the Swift standard library. As a result, your model files no longer need to import the SwiftUI framework. ([SE-0261](https://github.com/apple/Swift-evolution/blob/master/proposals/0261-identifiable.md))
- The [`EnvironmentValues`](../SwiftUI/environmentvalues.md) structure has four new properties for reading accessibility values from the environment: [`accessibilityDifferentiateWithoutColor`](../SwiftUI/environmentvalues/accessibilitydifferentiatewithoutcolor.md), [`accessibilityReduceTransparency`](../SwiftUI/environmentvalues/accessibilityreducetransparency.md), [`accessibilityReduceMotion`](../SwiftUI/environmentvalues/accessibilityreducemotion.md), and [`accessibilityInvertColors`](../SwiftUI/environmentvalues/accessibilityinvertcolors.md). (51712481)
- The `color(_:)` modifier for [`Text`](../SwiftUI/text.md) is renamed [`foregroundColor(_:)`](../SwiftUI/text/foregroundcolor%28_%29.md) for consistency with the more general [`foregroundColor(_:)`](../SwiftUI/view/foregroundcolor%28_%29.md) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](../Swift/rangereplaceablecollection.md) protocol is extended to include a [`remove(atOffsets:)`](../Swift/rangereplaceablecollection/remove%28atoffsets%29.md) method and the [`MutableCollection`](../Swift/mutablecollection.md) protocol is extended to include a [`move(fromOffsets:toOffset:)`](../Swift/mutablecollection/move%28fromoffsets,tooffset%29.md) method. Each new method takes [`IndexSet`](../Foundation/indexset.md) instances that you use with the `onMove(perform:)` and `onDelete(perform:)` modifiers on `ForEach` views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](../SwiftUI/view/sheet%28ispresented,ondismiss,content%29.md), [`actionSheet(isPresented:content:)`](../SwiftUI/view/actionsheet%28ispresented,content%29.md), and [`alert(isPresented:content:)`](../SwiftUI/view/alert%28ispresented,content%29.md) — along with `isPresented` in the environment — replace the existing `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The basic animations are now named after the curve type — such as linear and easeInOut. The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](../SwiftUI/animation/interpolatingspring%28mass,stiffness,damping,initialvelocity%29.md), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/spring%28response,dampingfraction,blendduration%29.md) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/interactivespring%28response,dampingfraction,blendduration%29.md), depending on whether or not the animation is driven interactively. (50280375)
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

- SwiftUI APIs deprecated in previous betas are now removed. (52587863, 53310683)
- `NavigationDestinationLink` and `DynamicNavigationDestinationLink` are deprecated; their functionality is now included in [`NavigationLink`](../SwiftUI/navigationlink.md). (50630794)
- The `Length` type is replaced by [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md). (50654095)
- `TabbedView` is now named [`TabView`](../SwiftUI/tabview.md). (51012120)
- `HAlignment` and `VAlignment` are now deprecated, use the more flexible [`HorizontalAlignment`](../SwiftUI/horizontalalignment.md) or [`VerticalAlignment`](../SwiftUI/verticalalignment.md) types instead and use [`TextAlignment`](../SwiftUI/textalignment.md) for text. (51190531)
- The `SelectionManager` protocol is removed, use [`Optional`](../Swift/optional.md) and [`Set`](../Swift/set.md) instances directly for selection. (51557694)
- The `isPresented` environment value is deprecated and replaced with the more general [`presentationMode`](../SwiftUI/environmentvalues/presentationmode.md) value. (51641238)
- The `StaticMember` protocol is deprecated. Use protocol-conforming types directly instead. For example, use an instance of [`WheelPickerStyle`](../SwiftUI/wheelpickerstyle.md) directly rather than the `wheel` static member.(52911961)
- Complex overloads for the [`background(_:alignment:)`](../SwiftUI/view/background%28_,alignment%29.md) and [`border(_:width:)`](../SwiftUI/view/border%28_,width%29.md) modifiers are deprecated. Use shapes in a [`background(_:alignment:)`](../SwiftUI/view/background%28_,alignment%29.md) or [`overlay(_:alignment:)`](../SwiftUI/view/overlay%28_,alignment%29.md) to draw these instead. (53067530)
- The `identified(by:)` method on the [`Collection`](../Swift/collection.md) protocol is deprecated in favor of dedicated [`init(_:id:rowContent:)`](../SwiftUI/list/init%28_,id,rowcontent%29-4s0aj.md) and [`init(_:id:content:)`](../SwiftUI/foreach/init%28_,id,content%29.md) initializers. (52976883, 52029393)

  The retroactive conformance of [`Int`](../Swift/int.md) to the Identifiable protocol is removed. Change any code that relies on this conformance to pass `\.self` to the `id` parameter of the relevant initializer. Constant ranges of `Int` continue to be accepted:

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

  Define the following subscript on the [`Set`](../Swift/set.md) structure:

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

  Then, change `self.$favorites.contains(landmarkID)` to `self.$favorites[landmarkID]`.
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

      var endIndex: Index { base.startIndex }

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

##### Third-Party Apps

###### Known Issues

- You might be unable to stream to a Chromecast device. (51334673)

##### UIKit

###### New Features

- The [`UITableViewCell`](../UIKit/uitableviewcell.md) class no longer changes the [`backgroundColor`](../UIKit/uiview/backgroundcolor.md) or [`isOpaque`](../UIKit/uiview/isopaque.md) properties of the [`contentView`](../UIKit/uitableviewcell/contentview.md) and any of its subviews when cells become highlighted or selected. If you are setting an opaque `backgroundColor` on any subviews of the cell inside (and including) the `contentView`, the appearance when the cell becomes highlighted or selected might be affected. The simplest way to resolve any issues with your subviews is to ensure their `backgroundColor` is set to `nil` or [`clear`](../UIKit/uicolor/clear.md), and their `opaque` property is `false`. However, if needed you can override the [`setHighlighted(_:animated:)`](../UIKit/uitableviewcell/sethighlighted%28_,animated%29.md) and [`setSelected(_:animated:)`](../UIKit/uitableviewcell/setselected%28_,animated%29.md) methods to manually change these properties on your subviews when moving to or from the highlighted and selected states. (13955336)
- Since iOS 8, using [`UISearchController`](../UIKit/uisearchcontroller.md) with [`UINavigationController`](../UIKit/uinavigationcontroller.md) has required setting the [`definesPresentationContext`](../UIKit/uiviewcontroller/definespresentationcontext.md) property of the top view controller to `true`. Failure to do so leads to subtle bugs that can be hard to detect and debug. Starting in iOS & iPadOS 13 beta, if a view controller’s [`navigationItem`](../UIKit/uiviewcontroller/navigationitem.md) has a non-`nil` [`searchController`](../UIKit/uinavigationitem/searchcontroller.md), when the view controller is shown in a navigation controller, [`UINavigationController`](../UIKit/uinavigationcontroller.md) automatically sets that view controller’s [`definesPresentationContext`](../UIKit/uiviewcontroller/definespresentationcontext.md) property to `true`. If you are targeting earlier versions of iOS, set this property before your search controller becomes active. (31338934)
- The [`UIRefreshControl`](../UIKit/uirefreshcontrol.md) class no longer directly modifies the [`contentInset`](../UIKit/uiscrollview/contentinset.md) of its scroll view. Instead, its adjustments to the content inset will be incorporated into the scroll view’s [`adjustedContentInset`](../UIKit/uiscrollview/adjustedcontentinset.md). The only exception is when the scroll view’s [`contentInsetAdjustmentBehavior`](../UIKit/uiscrollview/contentinsetadjustmentbehavior-swift.property.md) is set to [`UIScrollView.ContentInsetAdjustmentBehavior.never`](../UIKit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/never.md), in which case the [`UIRefreshControl`](../UIKit/uirefreshcontrol.md) instance will modify the `contentInset` directly as it did in previous releases. (35866834)
- If you implement self-sizing cells in a [`UITableView`](../UIKit/uitableview.md) by overriding [`sizeThatFits(_:)`](../UIKit/uiview/sizethatfits%28_%29.md) without using Auto Layout, the height you return is interpreted as the desired height for the `contentView` of the cell, and [`UITableViewCell`](../UIKit/uitableviewcell.md) automatically adds any additional height needed to allow room for the cell separator. If you implement manual self-sizing this way, the cell’s `contentView` width is guaranteed to be accurate for you to use in manual layout calculations when [`sizeThatFits(_:)`](../UIKit/uiview/sizethatfits%28_%29.md) is called on the [`UITableViewCell`](../UIKit/uitableviewcell.md). (39742612)
- Trait environments, such as views and view controllers, now have their `traitCollection` property populated with traits during initialization. These initial traits represent a prediction of the ultimate traits that the trait environment will receive when it gets added to the hierarchy. Because the traits that are populated during initialization are just a prediction, they might differ from the traits that are received once actually in the hierarchy. Therefore, when possible you should wait to perform work that uses the `traitCollection` until the view, or view controller’s view, has moved into the hierarchy — meaning [`window`](../UIKit/uiview/window.md) returns a non-`nil` value — so that you don’t have to throw away any work done using the predicted traits if the actual traits are different. The best time to use the `traitCollection` is during layout, such as inside [`layoutSubviews()`](../UIKit/uiview/layoutsubviews%28%29.md), [`viewWillLayoutSubviews()`](../UIKit/uiviewcontroller/viewwilllayoutsubviews%28%29.md), or [`viewDidLayoutSubviews()`](../UIKit/uiviewcontroller/viewdidlayoutsubviews%28%29.md).
- The [`traitCollectionDidChange(_:)`](../UIKit/uitraitenvironment/traitcollectiondidchange%28_%29.md) method is only called when the value of a trait changes. Importantly, because the trait collection is now initialized to a prediction of the ultimate traits in the destination hierarchy, when the initial predicted traits match the ultimate traits in the hierarchy, [`traitCollectionDidChange(_:)`](../UIKit/uitraitenvironment/traitcollectiondidchange%28_%29.md) will not be called when the trait environment is added to the hierarchy.  Because [`traitCollectionDidChange(_:)`](../UIKit/uitraitenvironment/traitcollectiondidchange%28_%29.md) is intended to be an invalidation callback to notify you that one or more traits changed, audit your existing implementations of this method, as well as the [`UIContentContainer`](../UIKit/uicontentcontainer.md) method [`willTransition(to:with:)`](../UIKit/uicontentcontainer/willtransition%28to,with%29.md), for places where you might have been relying on it to trigger initial setup. The best place to lazily perform work that uses the `traitCollection` is inside one of the `layoutSubviews` methods discussed above, but remember that these layout methods are called any time layout occurs so be sure to avoid repeating work when you don’t need to. (46818941)
- You can now enable debug logging to easily see when [`traitCollectionDidChange(_:)`](../UIKit/uitraitenvironment/traitcollectiondidchange%28_%29.md) or [`willTransition(to:with:)`](../UIKit/uicontentcontainer/willtransition%28to,with%29.md) is called on your own classes. Turn on the logging by using the following launch argument: `-UITraitCollectionChangeLoggingEnabled YES`. You might want to temporarily disable the Main Thread Checker while using this launch argument and running your app from Xcode to avoid extra log messages for unrelated classes. (47858564)
- The [`UITableViewCell`](../UIKit/uitableviewcell.md) class’s [`contentView`](../UIKit/uitableviewcell/contentview.md) property is always laid out edge-to-edge with adjacent accessories, both on the leading and the trailing side. This streamlines the layout code so developers who want the correct default offset no longer have to align their content with the content view border or the layout margin depending on whether there is an accessory on the trailing side or not. You should now always lay out their code on the layout margins of the cell’s content view to get the default system insets. These insets will be adjusted automatically based on the accessories visible in the cell to match the system’s default spacing. (48214114)
- You can now invoke a custom initializer from a creation block that’s passed through [`instantiateInitialViewController(creator:)`](../UIKit/uistoryboard/instantiateinitialviewcontroller%28creator%29.md) or [`instantiateViewController(identifier:creator:)`](../UIKit/uistoryboard/instantiateviewcontroller%28identifier,creator%29.md). This makes it possible for you to initialize view controllers with additional context and arguments, while taking advantage of defining them in a storyboard through Interface Builder. A custom controller initializer must call its `super.init(coder:)` method and pass the coder argument that it receives through the creation block. (48313869)

###### Known Issues

- Specifying `UIWindowScene.DestructionRequestOptions` in Swift is currently unavailable. (51036709)

##### Voice Analytics

###### Known Issues

- Voice Analytics is currently available only when using server based speech recognition. (53604093)

##### Watch

###### Known Issues

- Complications might disappear from Apple Watch after updating to iOS 13 beta or later if your watch isn’t running watchOS 6 beta or later. (50507942)

##### Xcode

###### New Features

- [`CAMetalLayer`](../QuartzCore/cametallayer.md) is now available in Simulator. (45101325)

## See Also

### iOS & iPadOS 13
- [iOS & iPadOS 13.7 Release Notes](./ios-ipados-13_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.6 Release Notes](./ios-ipados-13_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.5 Release Notes](./ios-ipados-13_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.4 Release Notes](./ios-ipados-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.3.1 Release Notes](./ios-ipados-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.3 Release Notes](./ios-ipados-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.2 Release Notes](./ios-ipados-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 13 Release Notes](./ios-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-13_1-release-notes)*