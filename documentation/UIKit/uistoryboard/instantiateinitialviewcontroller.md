# instantiateInitialViewController()

**Framework**: UIKit  
**Kind**: method

Creates the initial view controller and initializes it with the data from the storyboard.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func instantiateInitialViewController() -> UIViewController?
```

#### Return Value

The initial view controller in the storyboard.

#### Discussion

Every storyboard file has an initial view controller that represents the default view controller to create. Typically, you use the initial view controller as the root view controller for a window. However, you can also instantiate the initial view controller when transitioning to content in a new storyboard file. This method creates a new instance of the initial view controller using its doc://com.apple.documentation/documentation/oslog/oslogentry/init(coder:) method.

When you specify a storyboard in the [`UISceneStoryboardFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication/UISceneStoryboardFile) or [`UIMainStoryboardFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIMainStoryboardFile) key of your app’s `Info.plist` file, UIKit loads the initial view controller from that storyboard.

## See Also

- [func instantiateInitialViewController<ViewController>(creator: ((NSCoder) -> ViewController?)?) -> ViewController?](uistoryboard/instantiateinitialviewcontroller(creator:).md)
  Creates the initial view controller from the storyboard and initializes it using your custom initialization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard/instantiateinitialviewcontroller())*