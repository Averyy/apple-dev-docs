# searchableObject

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object to search, responsible for performing the search operation and decorating the results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var searchableObject: (any __UITextSearching)? { get }
```

```objc
@property (nonatomic, weak, readonly) id<UITextSearching> searchableObject;
```

#### Discussion

Use the methods this object implements from the [`UITextSearching`](../uitextsearching-53wjq.md) protocol to search text in your app and decorate the found results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchingfindsession/searchableobject)*