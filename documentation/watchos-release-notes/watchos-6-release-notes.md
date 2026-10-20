# watchOS 6 Release Notes

**Framework**: watchOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 6 SDK provides support for developing watchOS apps for Apple Watch devices running watchOS 6. The SDK comes bundled with Xcode 11 beta available from [Beta Software Downloads](https://developer.apple.com/download/). For information on the compatibility requirements for Xcode 11, see [Xcode 11 Release Notes](../Xcode-Release-Notes/xcode-11-release-notes.md).

> ⚠️ **Warning**: You must update your watch to watchOS 6 beta 2 or later before updating to iOS 13 beta 7 or later, otherwise your watch will no longer be able to connect to your phone. (52854192)

##### Networking

###### New Features

- To enhance security, [`URLSession`](../Foundation/urlsession.md) no longer sniffs the MIME type when the server sends `Content-Type: application/octet-stream`. (7820658)
- [`NSURLRequest.CachePolicy.reloadRevalidatingCacheData`](../Foundation/nsurlrequest/cachepolicy-swift.enum/reloadrevalidatingcachedata.md) and [`NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData`](../Foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md) APIs are now available. (49660334)
- [`URLSessionWebSocketTask`](../Foundation/urlsessionwebsockettask.md) and [`URLSessionStreamTask`](../Foundation/urlsessionstreamtask.md) are now available for use in watchOS apps. (49779789)

###### Known Issues

- The [`urlSession(_:taskIsWaitingForConnectivity:)`](../Foundation/urlsessiontaskdelegate/urlsession%28_,taskiswaitingforconnectivity%29.md) delegate callback might not function as expected. (54309264)

###### Deprecations

- The [`URLSession`](../Foundation/urlsession.md) and [`NSURLConnection`](../Foundation/nsurlconnection.md) APIs no longer support SPDY. Servers should use HTTP 2 or HTTP 1.1. (43391641)

##### Notifications

###### New Features

- To send a [User Notifications](../UserNotifications/UserNotifications.md) push to a watchOS device, a new `apns-push-type` key is now required as part of the APNs request header. Depending on the type of notification, this key can be set to `alert` or `background` and is supported across all Apple platforms. (47099534)

##### Podcasts

###### Known Issues

- Asking Siri to play a podcast on Apple Watch might result in an error message. (50392036)

##### SwiftUI

###### New Features

- You can now create a [`Color`](../SwiftUI/color.md) from a [`UIColor`](../UIKit/uicolor.md) or [`NSColor`](../AppKit/nscolor.md). (49833933)
- [`NSManagedObject`](../CoreData/nsmanagedobject.md) now conforms to [`ObservableObject`](../Combine/observableobject.md). The new `@`[`FetchRequest`](../SwiftUI/fetchrequest.md) property wrapper can drive views from the results of a fetch request, and [`managedObjectContext`](../SwiftUI/environmentvalues/managedobjectcontext.md) is now included in the environment. (50280673)
- Gesture modifiers are renamed for consistency. For example, `tapAction(count:_:)` is renamed [`onTapGesture(count:perform:)`](../SwiftUI/view/ontapgesture%28count,perform%29.md), and `longPressAction(minimumDuration:maximumDistance:_:pressing:)` is renamed [`onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)`](../SwiftUI/view/onlongpressgesture%28minimumduration,maximumdistance,pressing,perform%29.md). (50395282)
- [`Text`](../SwiftUI/text.md) now has a default line limit of `nil` so that it wraps by default. (51147116)
- [`ContentSizeCategory`](../SwiftUI/contentsizecategory.md) and several other enumerations are now [`CaseIterable`](../Swift/caseiterable.md). (51168712)
- `SegmentedControl` is now a style of [`Picker`](../SwiftUI/picker.md). (51769046)
- `BindableObject` is replaced by the [`ObservableObject`](../Combine/observableobject.md) protocol from the Combine framework. (50800624) You can manually conform to [`ObservableObject`](../Combine/observableobject.md) by defining an [`objectWillChange`](../Combine/observableobject/objectwillchange-5gopl.md) publisher that emits before the object changes. However, by default, [`ObservableObject`](../Combine/observableobject.md) automatically synthesizes [`objectWillChange`](../Combine/observableobject/objectwillchange-5gopl.md) and emits before any `@`[`Published`](../Combine/published.md) properties change.

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

  `@``ObjectBinding` is replaced by `@`[`ObservedObject`](../SwiftUI/observedobject.md).
- The [`EnvironmentValues`](../SwiftUI/environmentvalues.md) structure has four new properties for reading accessibility values from the environment: [`accessibilityDifferentiateWithoutColor`](../SwiftUI/environmentvalues/accessibilitydifferentiatewithoutcolor.md), [`accessibilityReduceTransparency`](../SwiftUI/environmentvalues/accessibilityreducetransparency.md), [`accessibilityReduceMotion`](../SwiftUI/environmentvalues/accessibilityreducemotion.md), and [`accessibilityInvertColors`](../SwiftUI/environmentvalues/accessibilityinvertcolors.md). (51712481)
- The `color(_:)` modifier for [`Text`](../SwiftUI/text.md) is renamed [`foregroundColor(_:)`](../SwiftUI/text/foregroundcolor%28_%29.md) for consistency with the more general [`foregroundColor(_:)`](../SwiftUI/view/foregroundcolor%28_%29.md) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](../Swift/rangereplaceablecollection.md) protocol is extended to include a [`remove(atOffsets:)`](../Swift/rangereplaceablecollection/remove%28atoffsets%29.md) method and the [`MutableCollection`](../Swift/mutablecollection.md) protocol is extended to include a [`move(fromOffsets:toOffset:)`](../Swift/mutablecollection/move%28fromoffsets,tooffset%29.md) method. Each new method takes [`IndexSet`](../Foundation/indexset.md) instances that you use with the `onMove(perform:)` and `onDelete(perform:)` modifiers on [`ForEach`](../SwiftUI/foreach.md) views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](../SwiftUI/view/sheet%28ispresented,ondismiss,content%29.md), [`actionSheet(isPresented:content:)`](../SwiftUI/view/actionsheet%28ispresented,content%29.md), and [`alert(isPresented:content:)`](../SwiftUI/view/alert%28ispresented,content%29.md) — along with `isPresented` in the environment — replace the existing `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The basic animations are now named after the curve type — such as [`linear`](../SwiftUI/animation/linear.md) and [`easeInOut`](../SwiftUI/animation/easeinout.md). The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](../SwiftUI/animation/interpolatingspring%28mass,stiffness,damping,initialvelocity%29.md), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/spring%28response,dampingfraction,blendduration%29.md) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](../SwiftUI/animation/interactivespring%28response,dampingfraction,blendduration%29.md), depending on whether or not the animation is driven interactively. (50280375)
- Added an initializer for creating a [`Font`](../SwiftUI/font.md) from a [`CTFont`](../CoreText/ctfont.md). (51849885)

###### Known Issues

- SwiftUI has an API that lets you change the value type of [`Binding`](../SwiftUI/binding.md) to [`AnyHashable`](../Swift/anyhashable.md):

  ```swift
  let someBinding: Binding<String> = ...
  let typeErasedBinding = Binding<AnyHashable>(someBinding)
  ```

  Attempting to use this API at compile time results in a linker error on watchOS 6. (53769896)
- A [`WKInterfaceObjectRepresentable`](../SwiftUI/wkinterfaceobjectrepresentable.md) instance with no explicit width might expand to the bounds of its container.

  **Workaround:** Wrap the [`WKInterfaceObjectRepresentable`](../SwiftUI/wkinterfaceobjectrepresentable.md) instance in a [`GeometryReader`](../SwiftUI/geometryreader.md) to get an explicit width for the view. (53512858)
- [`Image`](../SwiftUI/image.md) instances don’t use resizing information configured in asset catalogs. Configure the size of an image using the [`resizable(capInsets:resizingMode:)`](../SwiftUI/image/resizable%28capinsets,resizingmode%29.md) modifier instead. (49114577)

###### Deprecations

- SwiftUI APIs deprecated in previous betas are now removed. (52587863, 53310683)
- The `Length` type is replaced by [`CGFloat`](../CoreFoundation/cgfloat-swift.struct.md). (50654095)
- `TabbedView` is now named [`TabView`](../SwiftUI/tabview.md). (51012120)
- `HAlignment` and `VAlignment` are now deprecated, use the more flexible [`HorizontalAlignment`](../SwiftUI/horizontalalignment.md) or [`VerticalAlignment`](../SwiftUI/verticalalignment.md) types instead and use [`TextAlignment`](../SwiftUI/textalignment.md) for text. (51190531)
- The `SelectionManager` protocol is removed, use [`Optional`](../Swift/optional.md) and [`Set`](../Swift/set.md) instances directly for selection. (51557694)
- The `isPresented` environment value is deprecated and replaced with the more general [`presentationMode`](../SwiftUI/environmentvalues/presentationmode.md) value. (51641238)
- The `StaticMember` protocol is deprecated. Use protocol-conforming types directly instead. For example, use an instance of [`WheelPickerStyle`](../SwiftUI/wheelpickerstyle.md) directly rather than the `wheel` static member.(52911961)
- Complex overloads for the [`background(_:alignment:)`](../SwiftUI/view/background%28_,alignment%29.md) and [`border(_:width:)`](../SwiftUI/view/border%28_,width%29.md) modifiers are deprecated. Use shapes in a [`background(_:alignment:)`](../SwiftUI/view/background%28_,alignment%29.md) or [`overlay(_:alignment:)`](../SwiftUI/view/overlay%28_,alignment%29.md) to draw these instead. (53067530)
- The `identified(by:)` method on the [`Collection`](../Swift/collection.md) protocol is deprecated in favor of dedicated `init(_:id:selection:rowContent:)` and `init(_:id:content:)` initializers. (52976883, 52029393)

  The retroactive conformance of Int to the [`Identifiable`](../Swift/identifiable.md) protocol is removed. Change any code that relies on this conformance to pass `\.self` to the `id` parameter of the relevant initializer. Constant ranges of [`Int`](../Swift/int.md) continue to be accepted:

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

  Then, change `self.$favorites.contains(landmarkID)` to `self.$favorites[landmarkID]`.
- The [`Binding`](../SwiftUI/binding.md) structure’s conditional conformance to the Collection protocol is removed. (51624798)

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

##### Xcode

###### Known Issues

- If your watch debugging session continuously times out, you might need to quit and relaunch Xcode after connecting to the internet in order to download the appropriate DeviceSupport files. (50554987)
- The watchOS Mail app and related processes might quit unexpectedly when used within the Simulator. (53799899)

## See Also

### watchOS 6
- [watchOS 6.2.8 Release Notes](./watchos-6_2_8-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.2.5 Release Notes](./watchos-6_2_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.2 Release Notes](./watchos-6_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1.2 Release Notes](./watchos-6_1_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1.1 Release Notes](./watchos-6_1_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1 Release Notes](./watchos-6_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-6-release-notes)*