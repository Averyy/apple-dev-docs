# watchOS 6 Release Notes

**Framework**: Watchos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 6 SDK provides support for developing watchOS apps for Apple Watch devices running watchOS 6. The SDK comes bundled with Xcode 11 beta available from [`Beta Software Downloads`](https://developer.apple.comhttps://developer.apple.com/download/). For information on the compatibility requirements for Xcode 11, see [`Xcode 11 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-11-release-notes).

> ⚠️ **Warning**: You must update your watch to watchOS 6 beta 2 or later before updating to iOS 13 beta 7 or later, otherwise your watch will no longer be able to connect to your phone. (52854192)

You must update your watch to watchOS 6 beta 2 or later before updating to iOS 13 beta 7 or later, otherwise your watch will no longer be able to connect to your phone. (52854192)

##### Networking

###### New Features

- To enhance security, [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) no longer sniffs the MIME type when the server sends `Content-Type: application/octet-stream`. (7820658)
- [`NSURLRequest.CachePolicy.reloadRevalidatingCacheData`](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy/reloadrevalidatingcachedata) and [`NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData`](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy/reloadignoringlocalandremotecachedata) APIs are now available. (49660334)
- [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/Foundation/URLSessionWebSocketTask) and [`URLSessionStreamTask`](https://developer.apple.com/documentation/Foundation/URLSessionStreamTask) are now available for use in watchOS apps. (49779789)

###### Known Issues

- The [`urlSession(_:taskIsWaitingForConnectivity:)`](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/2908819-urlsession) delegate callback might not function as expected. (54309264)

###### Deprecations

- The [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) APIs no longer support SPDY. Servers should use HTTP 2 or HTTP 1.1. (43391641)

##### Notifications

###### New Features

- To send a [`User Notifications`](https://developer.apple.com/documentation/UserNotifications) push to a watchOS device, a new `apns-push-type` key is now required as part of the APNs request header. Depending on the type of notification, this key can be set to `alert` or `background` and is supported across all Apple platforms. (47099534)

##### Podcasts

###### Known Issues

- Asking Siri to play a podcast on Apple Watch might result in an error message. (50392036)

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
``` `@``ObjectBinding` is replaced by `@`[`ObservedObject`](https://developer.apple.com/documentation/SwiftUI/ObservedObject).
- The [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues) structure has four new properties for reading accessibility values from the environment: [`accessibilityDifferentiateWithoutColor`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityDifferentiateWithoutColor), [`accessibilityReduceTransparency`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityReduceTransparency), [`accessibilityReduceMotion`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityReduceMotion), and [`accessibilityInvertColors`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityInvertColors). (51712481)
- The `color(_:)` modifier for [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) is renamed [`foregroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/Text/foregroundColor(_:)) for consistency with the more general [`foregroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/View/foregroundColor(_:)) view modifier. (50391847)
- The `BindableObject` protocol’s requirement is now `willChange` instead of `didChange`, and should now be sent before the object changes rather than after it changes. This change allows for improved coalescing of change notifications. (51580731)
- The [`RangeReplaceableCollection`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection) protocol is extended to include a [`remove(atOffsets:)`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection/remove(atOffsets:)) method and the [`MutableCollection`](https://developer.apple.com/documentation/Swift/MutableCollection) protocol is extended to include a [`move(fromOffsets:toOffset:)`](https://developer.apple.com/documentation/Swift/MutableCollection/move(fromOffsets:toOffset:)) method. Each new method takes [`IndexSet`](https://developer.apple.com/documentation/Foundation/IndexSet) instances that you use with the doc://com.apple.documentation/documentation/SwiftUI/ForEach/onmove(perform:) and doc://com.apple.documentation/documentation/SwiftUI/ForEach/ondelete(perform:) modifiers on [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) views. (51991601)
- Added improved presentation modifiers: [`sheet(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/sheet(isPresented:onDismiss:content:)), [`actionSheet(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/actionSheet(isPresented:content:)), and [`alert(isPresented:content:)`](https://developer.apple.com/documentation/SwiftUI/View/alert(isPresented:content:)) — along with `isPresented` in the environment — replace the existing `presentation(_:)`, `Sheet`, `Modal`, and `PresentationLink` types. (52075730)
- Updated the APIs for creating animations. The basic animations are now named after the curve type — such as [`linear`](https://developer.apple.com/documentation/SwiftUI/Animation/linear) and [`easeInOut`](https://developer.apple.com/documentation/SwiftUI/Animation/easeInOut). The interpolation-based `spring(mass:stiffness:damping:initialVelocity:)` animation is now [`interpolatingSpring(mass:stiffness:damping:initialVelocity:)`](https://developer.apple.com/documentation/SwiftUI/Animation/interpolatingSpring(mass:stiffness:damping:initialVelocity:)), and `fluidSpring(stiffness:dampingFraction:blendDuration:timestep:idleThreshold:)` is now [`spring(response:dampingFraction:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/spring(response:dampingFraction:blendDuration:)) or [`interactiveSpring(response:dampingFraction:blendDuration:)`](https://developer.apple.com/documentation/SwiftUI/Animation/interactiveSpring(response:dampingFraction:blendDuration:)), depending on whether or not the animation is driven interactively. (50280375)
- Added an initializer for creating a [`Font`](https://developer.apple.com/documentation/SwiftUI/Font) from a [`CTFont`](https://developer.apple.com/documentation/CoreText/CTFont). (51849885)

###### Known Issues

- SwiftUI has an API that lets you change the value type of [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) to [`AnyHashable`](https://developer.apple.com/documentation/Swift/AnyHashable): ```swift
let someBinding: Binding<String> = ...
let typeErasedBinding = Binding<AnyHashable>(someBinding)
``` Attempting to use this API at compile time results in a linker error on watchOS 6. (53769896)
- A [`WKInterfaceObjectRepresentable`](https://developer.apple.com/documentation/SwiftUI/WKInterfaceObjectRepresentable) instance with no explicit width might expand to the bounds of its container.  Wrap the [`WKInterfaceObjectRepresentable`](https://developer.apple.com/documentation/SwiftUI/WKInterfaceObjectRepresentable) instance in a [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader) to get an explicit width for the view. (53512858)
- [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) instances don’t use resizing information configured in asset catalogs. Configure the size of an image using the [`resizable(capInsets:resizingMode:)`](https://developer.apple.com/documentation/SwiftUI/Image/resizable(capInsets:resizingMode:)) modifier instead. (49114577)

###### Deprecations

- SwiftUI APIs deprecated in previous betas are now removed. (52587863, 53310683)
- The `Length` type is replaced by [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct). (50654095)
- `TabbedView` is now named [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView). (51012120)
- `HAlignment` and `VAlignment` are now deprecated, use the more flexible [`HorizontalAlignment`](https://developer.apple.com/documentation/SwiftUI/HorizontalAlignment) or [`VerticalAlignment`](https://developer.apple.com/documentation/SwiftUI/VerticalAlignment) types instead and use [`TextAlignment`](https://developer.apple.com/documentation/SwiftUI/TextAlignment) for text. (51190531)
- The `SelectionManager` protocol is removed, use [`Optional`](https://developer.apple.com/documentation/Swift/Optional) and [`Set`](https://developer.apple.com/documentation/Swift/Set) instances directly for selection. (51557694)
- The `isPresented` environment value is deprecated and replaced with the more general [`presentationMode`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/presentationMode) value. (51641238)
- The `StaticMember` protocol is deprecated. Use protocol-conforming types directly instead. For example, use an instance of [`WheelPickerStyle`](https://developer.apple.com/documentation/SwiftUI/WheelPickerStyle) directly rather than the `wheel` static member.(52911961)
- Complex overloads for the [`background(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/background(_:alignment:)) and [`border(_:width:)`](https://developer.apple.com/documentation/SwiftUI/View/border(_:width:)) modifiers are deprecated. Use shapes in a [`background(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/background(_:alignment:)) or [`overlay(_:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/overlay(_:alignment:)) to draw these instead. (53067530)
- The `identified(by:)` method on the [`Collection`](https://developer.apple.com/documentation/Swift/Collection) protocol is deprecated in favor of dedicated `init(_:id:selection:rowContent:)` and `init(_:id:content:)` initializers. (52976883, 52029393) The retroactive conformance of Int to the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol is removed. Change any code that relies on this conformance to pass `\.self` to the `id` parameter of the relevant initializer. Constant ranges of [`Int`](https://developer.apple.com/documentation/Swift/Int) continue to be accepted: ```swift
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
``` Then, change `self.$favorites.contains(landmarkID)` to `self.$favorites[landmarkID]`.
- The [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) structure’s conditional conformance to the Collection protocol is removed. (51624798) If you have code such as the following: ```swift
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

###### Known Issues

- If your watch debugging session continuously times out, you might need to quit and relaunch Xcode after connecting to the internet in order to download the appropriate DeviceSupport files. (50554987)
- The watchOS Mail app and related processes might quit unexpectedly when used within the Simulator. (53799899)

## See Also

- [watchOS 6.2.8 Release Notes](watchos-6_2_8-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.2.5 Release Notes](watchos-6_2_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.2 Release Notes](watchos-6_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1.2 Release Notes](watchos-6_1_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1.1 Release Notes](watchos-6_1_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1 Release Notes](watchos-6_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-6-release-notes)*