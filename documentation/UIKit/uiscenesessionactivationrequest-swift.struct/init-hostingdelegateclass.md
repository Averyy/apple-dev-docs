# init(hostingDelegateClass:)

**Framework**: UIKit  
**Kind**: init

Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init?<D>(hostingDelegateClass: D.Type) where D : UIHostingSceneDelegate
```

#### Discussion

The first scene declared in the `rootScene` property of your hosting delegate class will be activated by this request.

```None
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup() {
            ContentView()
        }
    }
}

let request = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self
)
UIApplication.shared.activateSceneSession(for: request)
```

When a UIScene is activated using this request object, its configuration is managed by SwiftUI. You will not see a call to your app delegate’s `application(_:configurationForConnecting:options:)` method.

An instance of the provided hosting delegate class will be created by SwiftUI and receive lifecycle callbacks for the associated scene.

## Parameters

- `hostingDelegateClass`: A Class type that conforms to   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:))*