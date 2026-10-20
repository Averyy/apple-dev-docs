# init(nibName:bundle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized view controller with the nib file in the specified bundle.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

```objc
- (instancetype) initWithNibName:(NSString *) nibNameOrNil bundle:(NSBundle *) nibBundleOrNil;
```

## Parameters

- `nibNameOrNil`: The name of the nib file to associate with the view controller. The nib file name shouldn’t contain any leading path information. If you specify `nil`, the `nibName` property is set to `nil`.
- `nibBundleOrNil`: The bundle in which to search for the nib file. This method looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

## See Also

### Creating a search controller
- [init(searchResultsController: UIViewController?)](./init%28searchresultscontroller%29.md)
  Creates and returns a search controller with the specified view controller for displaying the results.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an initialized search controller from data in the specified unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/init(nibname:bundle:))*