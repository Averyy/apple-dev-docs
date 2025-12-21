# init(hostingDelegateClass:id:value:)

**Framework**: UIKit  
**Kind**: init

Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier and presented value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init?<H, D>(hostingDelegateClass: H.Type, id: String, value: D) where H : UIHostingSceneDelegate, D : Decodable, D : Encodable, D : Hashable
```

#### Discussion

The specified scene must be declared in the `rootScene` property of your hosting delegate class. The initializer will fail if no scene with the specified identifier is defined.

```None
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "window", for: FavoriteNumber.self) { $value in
            ContentView(favoriteNumber: $value)
        }
    }
}

if let activationWithIDAndData = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "window", value: FavoriteNumber(13)
) {
    UIApplication.shared.activateSceneSession(for: activationWithIDAndData)
}
```

When a UIScene is activated using this request object, its configuration is managed by SwiftUI. You will not see a call to your app delegate’s `application(_:configurationForConnecting:)` method.

An instance of the provided hosting delegate class will be created by SwiftUI and receive lifecycle callbacks for the associated scene.

## Parameters

- `hostingDelegateClass`: A Class type that conforms to   .
- `id`: A string matching the   of one of the scenes declared in the   sceneRepresentation’s content.
- `value`: The data to be presented in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:id:value:))*