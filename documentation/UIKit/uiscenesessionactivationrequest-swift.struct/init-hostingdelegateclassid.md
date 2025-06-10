# init(hostingDelegateClass:id:)

**Framework**: UIKit  
**Kind**: init

Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- visionOS 26.0+ (Beta)

## Declaration

```swift
init?<D>(hostingDelegateClass: D.Type, id: String) where D : UIHostingSceneDelegate
```

#### Discussion

The specified scene must be declared in the `rootScene` property of your hosting delegate class. The initializer will fail if no scene with the specified identifier is defined.

```None
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "swiftui-window") {
            ContentView()
        }
    }
}

if let requestWithID = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "swiftui-window"
) {
    UIApplication.shared.activateSceneSession(for: requestWithID)
}
```

When a UIScene is activated using this request object, its configuration is managed by SwiftUI. You will not see a call to your app delegate’s `application(_:configurationForConnecting:options:)` method.

An instance of the provided hosting delegate class will be created by SwiftUI and receive lifecycle callbacks for the associated scene.

## Parameters

- `hostingDelegateClass`: A Class type that conforms to   .
- `id`: A string matching the   of one of the scenes declared in the   sceneRepresentation’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:id:))*