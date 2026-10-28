# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized search controller from data in the specified unarchiver.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Return Value

An initialized search controller, or `nil` if the coder doesn’t define a search controller.

## Parameters

- `coder`: An unarchiver object.

## See Also

### Creating a search controller
- [init(searchResultsController: UIViewController?)](./init%28searchresultscontroller%29.md)
  Creates and returns a search controller with the specified view controller for displaying the results.
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Returns an initialized view controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/init(coder:))*